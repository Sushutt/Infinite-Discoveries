from noise import pnoise3
from PIL import Image

width, height = 512, 256
scale = 100.0
octaves = 6
persistence = 0.5
lacunarity = 2.0
seed = 12345

z = 10

# Generate noise values
noise_values = [[pnoise3(x / scale, y / scale, z / scale, octaves=octaves,
                          persistence=persistence, lacunarity=lacunarity,
                          repeatx=width, repeaty=height, repeatz=width, base=seed)
                 for y in range(height)]
                for x in range(width)]

# Normalize noise values to range [-1, 1]
min_val, max_val = min(map(min, noise_values)), max(map(max, noise_values))
noise_values = [[(val - min_val) / (max_val - min_val) * 2 - 1
                 for val in row]
                for row in noise_values]

# Create spherical texture with ice caps
center_x, center_y = width / 2, height / 2
radius = min(center_x, center_y) * 0.9
ice_cap_radius = radius * 0.2
ice_cap_strength = 5.0
texture = Image.new('L', (width, height))
for x in range(width):
    for y in range(height):
        dx = x - center_x
        dy = y - center_y
        dist = (dx ** 2 + dy ** 2) ** 0.5
        if dist <= radius:
            phi = (dist / radius) * 3.141592653589793
            if y < center_y:
                phi = -phi
            if phi > 1.2:
                texture.putpixel((x, y), 0)
            else:
                ice_cap_strength_factor = (1 - phi / 1.2) ** 3 * ice_cap_strength
                noise_val = noise_values[x][y] + ice_cap_strength_factor
                noise_val = max(-1, min(1, noise_val))
                pixel_val = int((noise_val + 1) / 2 * 255)
                texture.putpixel((x, y), pixel_val)

# Save image as PNG
texture.save('icecaps.png')
