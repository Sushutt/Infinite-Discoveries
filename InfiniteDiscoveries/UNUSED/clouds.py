import random
import time
from PIL import Image, ImageChops, ImageFilter
import math
import os
import numpy as np

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
#filepath = filepath1.replace("/GenerateSystem", "")

# What the fuck is this shit?
def place_image(map_image, small_image, position):
    map_width, map_height = map_image.size
    img_width, img_height = small_image.size
    x, y = position

    # Create a new image that will hold the final map with all images placed
    #final_map = map_image.copy()

    # Place the image at the specified position
    map_image.paste(small_image, (x % map_width, y % map_height), mask=small_image)

    # Handle wrapping to the opposite edges
    if x + img_width > map_width:
        # Wrap around to the left edge
        map_image.paste(small_image, ((x + img_width) % map_width - img_width, y % map_height), mask=small_image)

    return map_image


def addClouds(theThing, types, coverage, density, venusyness):
    featureMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
    for i in range(1,coverage):
        feature = Image.open(filepath + "/Presets/" + theThing + str(random.randint(1,types)) + ".png")
        feature.putalpha(feature.convert("L"))

        resizedFeature = feature.resize((density,density))

        featureSize = (resizedFeature.size[0],resizedFeature.size[1])
        position = (random.randint(0,4096), random.randint(-featureSize[1],2048+int(featureSize[1]/2)))

        #featureMap.paste(feature.rotate(random.randint(0,180)), position, mask=feature)
        place_image(featureMap, resizedFeature.rotate(random.randint(0,180)), position)


    width, height = featureMap.size

    pixels = np.array(featureMap)

    new_pixels = np.zeros_like(pixels)

    center = height // 2

    if venusyness > 0:
        for y in range(height):
            for x in range(width):
                distance_from_center = abs(y - center)
                displacement = int(venusyness * (1 - distance_from_center / center))
                
                new_x = (x + displacement) % width

                new_pixels[y, new_x] = pixels[y, x]

        distorted_image = Image.fromarray(new_pixels)
    else:
        distorted_image = Image.fromarray(pixels)

    distorted_image.save(filepath + "/Textures/Clouds/" + "cloudMapTest.png", compress_level=1)

addClouds("Cloud", 6, 200, 500, 512)