import random

from PIL import Image, ImageFilter
import numpy as np
import noise
import math

from scipy.signal import convolve2d
# Define the size of the heightmap
size = 2048

# Define the radius of the sphere
radius = 0.3

seed = (random.random())
def GenerateColorHeight():
    # Calculate the color temperature in Kelvin
    StarSurfaceTemp = int(input("enter temp of parent star: "))
    red = 0
    green = 0
    blue = 0

    if StarSurfaceTemp > 7500:
        red = 255
        green = 200
        blue = 200
    elif 6000 < StarSurfaceTemp and StarSurfaceTemp < 7500:
        red = 150
        green = 10
        blue = 10
    elif 5000 < StarSurfaceTemp and StarSurfaceTemp < 6000:
        red = 50
        green = 150
        blue = 50
    elif 3000 < StarSurfaceTemp and StarSurfaceTemp < 5000:
        red = 20
        green = 50
        blue = 100
    elif 2000 < StarSurfaceTemp and StarSurfaceTemp < 3000:
        red = 10
        green = 10
        blue = 10
    if StarSurfaceTemp < 2000:
        red = 0
        green = 0
        blue = 0




    # Define the parameters for the fractal noise
    octaves = 10
    lacunarity = 2.0
    persistence = 0.5

    # Create a 2D array to store the heightmap
    heightmap = np.zeros((size, size))

    # Generate the heightmap using fractal noise
    for i in range(size):
        for j in range(size):
            # Convert the pixel coordinates to spherical coordinates
            theta = 2 * math.pi * i / size
            phi = math.pi * j / size
            x = radius * math.sin(phi) * math.cos(theta)
            y = radius * math.sin(phi) * math.sin(theta)
            z = radius * math.cos(phi)

            # Sample the noise function at the current point using multiple octaves
            noise_value = (6)
            frequency = 4.0
            amplitude = 1.0
            for k in range(octaves):
                noise_value += amplitude * noise.snoise4(x * frequency, y * frequency, z * frequency, seed)
                frequency *= lacunarity
                amplitude *= persistence

            # Store the noise value in the heightmap
            heightmap[i, j] = noise_value

    # Normalize the heightmap to the range [0, 1]
    heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())

    # Create a color map for the land
    land_shade = 0.5
    land_color = (red, green, blue)
    # Create a color map for the ocean
    ocean_color = (27, 79, 114)
    ocean_shade = 0
    #Ice Color
    IceColor = (250, 250, 255)
    IceShade = 0.05
    #SandColor
    SandColor = (210, 180, 160)
    SandShade = 0.4
    # Convert the heightmap to an RGB image with land and ocean colors
    image = Image.new('RGB', (size, size))
    for i in range(size):
        for j in range(size):
            height = heightmap[i, j]
            if height < 0.5:
                # Ocean
                shade = int((1 - 2 * height) * 255 * ocean_shade)
                color = tuple(max(0, c - shade) for c in ocean_color)
            elif height > 0.50 and 0.51 > height:
                # Land
                shade = int((2 * height - 1) * 255 * SandShade)
                color = tuple(min(255, c + shade) for c in SandColor)
            elif height > 0.51 and 0.9 > height:
                # Land
                shade = int((2 * height - 1) * 255 * land_shade)
                color = tuple(min(255, c + shade) for c in land_color)
            else:
                shade = int((2 * height - 1) * 255 * IceShade)
                color = tuple(min(255, c + shade) for c in IceColor)
            image.putpixel((i, j), color)
    # Rotate and resize the image to the desired aspect ratio
    image90 = image.rotate(0)
    imageRes = image90.resize((2028, 1024))

    # Save the image to disk

    imageRes.save("PlanetTex.png")

def GenerateNormal():
    imageRes = Image.open("PlanetTex.png")
    img_gray = imageRes.convert("L")
    img_gray_data = np.array(img_gray) / 128.0

    # Compute the height map by subtracting from 1.0
    height_map = 1.0 - img_gray_data

    # Compute the partial derivatives using Sobel operator
    dx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    dy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
    height_dx = convolve2d(height_map, dx, mode="same")
    height_dy = convolve2d(height_map, dy, mode="same")

    # Compute the normal vectors at each pixel
    normal_vectors = np.dstack((-height_dx, -height_dy, np.ones_like(height_dx)))
    norm = np.linalg.norm(normal_vectors, axis=-1, keepdims=True)
    normal_vectors = normal_vectors / norm

    # Scale the normal vectors to [0, 255]
    normal_vectors = ((normal_vectors + 1) / 2) * 255

    # Create a new image from the normal vectors
    img_normal = Image.fromarray(normal_vectors.astype(np.uint8))
    img_normal.save("PlanetNormal.png")


GenerateColorHeight()
GenerateNormal()