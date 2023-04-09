from PIL import Image, ImageFilter, ImageChops, ImageEnhance, ImageOps
import random
import os
import math
import numpy as np
from scipy.signal import convolve2d
import time
import noise

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

print("Generating noise...")
texStartTime = time.time()
seed = random.randint(0,1000)
size = 1024
radius = 1.0
octaves = 1
lacunarity = 2.0
persistence = 0.5
heightmap = np.zeros((size, size))
for i in range(size):
    print("Generating for " + str(time.time()-texStartTime) + " seconds...", end="\r")
    for j in range(size):
        # Convert the pixel coordinates to spherical coordinates
        theta = 2 * math.pi * i / size
        phi = math.pi * j / size
        x = radius * math.sin(phi) * math.cos(theta)
        y = radius * math.sin(phi) * math.sin(theta)
        z = radius * math.cos(phi)

        # Sample the noise function at the current point using multiple octaves
        noise_value = 0.0
        frequency = 10
        amplitude = 1.0
        for k in range(octaves):
            noise_value += amplitude * noise.snoise4(x * frequency, y * frequency, z * frequency, seed)
            frequency *= lacunarity
            amplitude *= persistence

        # Store the noise value in the heightmap
        heightmap[i, j] = noise_value

heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
image = Image.fromarray((heightmap * 255).astype(np.uint8), mode='L')
image90 = image.rotate(90)
imageRes = image90.resize((4096,2048), resample=Image.Resampling.BICUBIC)
noiseFinal = imageRes.convert("RGBA")

print("Finished generating noise!                          ")

mainImg = Image.new("RGBA", (4096,2048), (0,0,0,255))
color = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
for i in range(0,1500):
    print("Adding band " + str(i), end="\r")
    mult = random.randint(66,133)/100
    bandSizeInt = int(np.random.normal(5, 25))
    rand = max(5, min(50, bandSizeInt))
    bar = Image.new("RGBA", (4096,rand), (int(color[0]*mult),int(color[1]*mult),int(color[2]*mult),255))
    mainImg.paste(bar, (0,random.randint(0,2048)), mask=bar)

mainImgPreBlur = mainImg.filter(ImageFilter.SMOOTH_MORE())

blurred_map_img = noiseFinal.filter(ImageFilter.GaussianBlur(radius=5))
# Get the pixel access objects for both images
img_pixels = mainImgPreBlur.load()
map_pixels = blurred_map_img.load()
# Define the displacement amount (in pixels)
displacement = 1
# Loop through each pixel in the image
for y in range(mainImgPreBlur.size[1]):
    print("Calculating deformity for pixel row " + str(y), end="\r")
    for x in range(mainImg.size[0]):
        # Get the displacement value from the map image
        map_value = map_pixels[x, y][0]  # Use the first channel of the map image
        # Calculate the new x-coordinate with the displacement value
        new_y = y + (map_value - 16) * displacement / 16
        # Get the pixel value from the original image at the new coordinates
        try:
            pixel = img_pixels[x, new_y]
        except IndexError:
            pixel = (color[0], color[1], color[2])
        # Set the pixel value in the displaced image
        img_pixels[x, y] = pixel

print("Finished generating gas giant textures!             ")
mainImgEnh = ImageEnhance.Sharpness(mainImgPreBlur).enhance(10)
mainImgBlur = mainImgEnh.filter(ImageFilter.GaussianBlur(3))
mainImgBlur.save(filepath + "/Textures/PluginData/gg.png")