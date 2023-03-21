from PIL import Image, ImageEnhance, ImageFilter, ImageChops, ImageOps
import numpy as np
from scipy.signal import convolve2d
import noise
import math
import random
import time
import os
from colour import Color

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

oceanR = random.randint(5,50)
oceanG = random.randint(5,50)
oceanB = random.randint(10,75)

atmASL = 0.5
vacuum = False
geoActive = True
ocean = True
life = False
temp = 280
PstarRadius = 214512000

if temp >= 50 and temp <= 300 and vacuum == False:
    icecaps = True
else:
    icecaps = False

black = Color("#000000")
Pcolors1 = list(black.range_to(Color("#700000"),5))
red = Color("#700000")
Pcolors2 = list(red.range_to(Color("#9e008c"),90))
pink = Color("#9e008c")
Pcolors3 = list(pink.range_to(Color("#fcf2fa"),5))
PfinalColors = Pcolors1 + Pcolors2 + Pcolors3

PMult = PstarRadius*30 / 261600000
if PMult > len(PfinalColors):
    PMult = len(PfinalColors)
PmultRound = round(PMult)
plantColor = Color.get_rgb(PfinalColors[PmultRound-1])
PRGBfinal = str(plantColor)[1:][:-1]

def add_Surface_Features(noiseImg, type, amount, alphaAdd, minMax, types):
    featureMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
    min = minMax[0]
    max = minMax[1]
    for i in range(0,amount):
        feature = Image.open(filepath + "/Presets/" + type + str(random.randint(1,types)) + ".png")
        featureSize = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
        featurePreRes = feature.resize((featureSize,featureSize))
        featureA = featurePreRes.getchannel("A")
        alpha1 = Image.new("L", (featureSize, featureSize), (alphaAdd))
        featureA2 = ImageChops.multiply(alpha1,featureA)
        featurePreRes.putalpha(featureA2)

        print("Generating " + type + " " + str(i) + "...", end="\r")

        offs1 = random.randint(0,4096-featureSize)
        offs2 = random.randint(0,2048-featureSize)
        #print(str(offs1) + " " + str(offs2))
        dist = (((offs2/2048)*2)*90)-90
        distCos = math.cos(math.radians(dist))
        featureRot = featurePreRes.rotate(random.randint(0,360))
        featureRes = featureRot.resize((featureSize,math.ceil(featureSize*distCos)))
        
        featureMap.paste(featureRes, (int(offs1),int(offs2)), mask=featureRes)
    noiseImg.paste(featureMap, (0,0), featureMap)
    featureMap.show()

print("Generating noise...")
texStartTime = time.time()
seed = random.randint(0,1000)
size = 1024
radius = 1.0
octaves = 10
lacunarity = 2.0
persistence = 0.5
heightmap = np.zeros((size, size))
freq_random = random.randint(10,20)/10
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
        frequency = freq_random
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
brtAmount = random.randint(50,100)/100
contrAmount = 1/brtAmount
imageContr = ImageEnhance.Contrast(ImageEnhance.Brightness(imageRes).enhance(brtAmount)).enhance(contrAmount)
texEndTime = time.time()
noiseEndTime = texEndTime-texStartTime
print("Finished generating noise. Time elapsed: " + str(noiseEndTime) + " seconds.")

if atmASL < 0.25:
    add_Surface_Features(imageContr, "crater", 400, 128, [50,400], 3)
if geoActive == True:
    add_Surface_Features(imageContr, "volcano", 200, 200, [50,200], 1)
    add_Surface_Features(imageContr, "canyon", 400, 125, [50,400], 2)
if vacuum == False:
    add_Surface_Features(imageContr, "mountain", 400, 175, [50,600], 3)

if icecaps == True:
    # Open the original image and the displacement map image
    icecap_img = Image.new("RGBA", (4096,2048), (255,255,255,255))
    map_img = imageRes.convert("RGBA")
    Height = temp * 6
    backg_black = Image.new("L", (4096,2048), (0))
    img_black = Image.new("L", (4096,Height), (255))
    center_y = icecap_img.size[1] // 2
    top_left_y = center_y - img_black.size[1] // 2
    backg_black.paste(img_black, (0,top_left_y+(int(top_left_y/((280/temp)*(280/temp))))), mask=img_black)
    icecap_img.putalpha(ImageOps.invert(backg_black))

    blurred_map_img = map_img.filter(ImageFilter.GaussianBlur(radius=5))
    # Get the pixel access objects for both images
    img_pixels = icecap_img.load()
    map_pixels = blurred_map_img.load()
    # Define the displacement amount (in pixels)
    displacement = 25
    # Loop through each pixel in the image
    for y in range(icecap_img.size[1]):
        print("Calculating icecap deformity for pixel row " + str(y), end="\r")
        for x in range(icecap_img.size[0]):
            # Get the displacement value from the map image
            map_value = map_pixels[x, y][0]  # Use the first channel of the map image

            # Calculate the new x-coordinate with the displacement value
            new_y = y + (map_value - 16) * displacement / 16

            # Get the pixel value from the original image at the new coordinates
            try:
                pixel = img_pixels[x, new_y]
            except IndexError:
                pixel = (255, 255, 255)

            # Set the pixel value in the displaced image
            img_pixels[x, y] = pixel
    print("Finished generating icecaps!")
    icecap_drk = ImageEnhance.Brightness(icecap_img).enhance(0.6)
    imageContr.paste(icecap_drk, (0,0), mask=icecap_drk)

print("Finished overlaying surface features!")

print("Generating normals...")
texStartTime = time.time()
# Load the grayscale image and normalize to [0, 1]
img_gray = imageContr.convert("L")
img_gray_data = np.array(img_gray) / 64.0
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


img_normalFilter = img_normal.filter(ImageFilter.SMOOTH)
nrm_Patch = Image.open(filepath + "/Presets/" + "normalPatch.png")
img_normalFilter.paste(nrm_Patch, (0,0), mask=nrm_Patch)
texEndTime = time.time()
nrmEndTime = texEndTime-texStartTime

print("Finished generating normals. Time elapsed: " + str(nrmEndTime) + " seconds.")

ImageResFilter = imageContr.filter(ImageFilter.SMOOTH_MORE)

print("Generating color...")
texStartTime = time.time()

grayMap = ImageOps.grayscale(ImageResFilter)
if life == True:
    randomB_R = plantColor[0]*255
    randomB_G = plantColor[1]*255
    randomB_B = plantColor[2]*255
    randomM_R = random.randint(100,175)
    randomM_G = random.randint(75,100)
    randomM_B = random.randint(50,55)
    randomW_R = random.randint(65,100)
    randomW_G = random.randint(65,100)
    randomW_B = random.randint(65,100)
elif life == False and ocean == True:
    randomB_R = random.randint(25,75)
    randomB_G = random.randint(25,25)
    randomB_B = random.randint(25,25)
    randomM_R = random.randint(100,175)
    randomM_G = random.randint(75,100)
    randomM_B = random.randint(50,55)
    randomW_R = random.randint(65,100)
    randomW_G = random.randint(65,100)
    randomW_B = random.randint(65,100)
else:
    randomB_R = random.randint(25,75)
    randomB_G = random.randint(25,75)
    randomB_B = random.randint(25,75)
    randomM_R = random.randint(100,175)
    randomM_G = random.randint(75,100)
    randomM_B = random.randint(50,55)
    randomW_R = random.randint(50,200)
    randomW_G = random.randint(50,200)
    randomW_B = random.randint(50,200)
print(str(randomB_R) + " " + str(randomB_G) + " " + str(randomB_B))
print(str(randomM_R) + " " + str(randomM_G) + " " + str(randomM_B))
print(str(randomW_R) + " " + str(randomW_G) + " " + str(randomW_B))
if life == False:
    blackP = random.randint(0,85)
    midP = random.randint(85,150)
    whiteP = random.randint(150,200)
else:
    blackP = random.randint(0,74)
    midP = random.randint(150,200)
    whiteP = random.randint(200,255)
colorMap = ImageOps.colorize(grayMap, (randomB_R,randomB_G,randomB_B), (randomW_R,randomW_G,randomW_B), (randomM_R,randomM_G,randomM_B), blackpoint=blackP, midpoint=midP, whitepoint=whiteP)

if ocean == True:
    brightFac = float(random.randint(1,500)/100)

    print("Ocean exists! Dryness factor is " + str(brightFac))

    brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
    contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
    posted = ImageOps.posterize(contrHeight.convert("RGB"),2)
    brightFinal = ImageEnhance.Brightness(posted).enhance(100)
    oceanRGBA = brightFinal.convert("RGBA")
    oceanInv = ImageOps.invert(brightFinal).convert("RGBA")
    ocInvL = oceanInv.convert("L")
    oceanRGBA.putalpha(ocInvL)
    oceanBlurA = oceanInv.filter(ImageFilter.GaussianBlur(5)).convert("L")
    heightOcean = Image.new("RGBA", (4096,2048), (0,0,0))
    heightOcean.putalpha(oceanBlurA)
    ImageResFilter.paste(heightOcean, (0,0), mask=heightOcean)

    normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
    normalOcean.putalpha(ocInvL)
    img_normalFilter.paste(normalOcean, (0,0), mask=ocInvL)

    beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
    beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
    beachColor.putalpha(beachMask)
    colorMap.paste(beachColor, (0,0), mask=beachColor)
    colorOcean = Image.new("RGBA", (4096,2048), (oceanR,oceanG,oceanB))
    colorOcean.putalpha(ocInvL)
    colorMap.paste(colorOcean, (0,0), mask=colorOcean)
    if icecaps == True:
        icecap_alph = icecap_img.getchannel("A")
        icecap_inv = ImageOps.invert(icecap_img.convert("RGB"))
        icecap_inv.putalpha(icecap_alph)
        ocInvL.paste(icecap_inv, (0,0), mask=icecap_inv)
        colorMap.paste(icecap_img, (0,0), mask=icecap_img)
        colorMap.putalpha(ocInvL)
    else:
        colorMap.putalpha(ocInvL)
elif icecaps == True and ocean == False:
    colorMap.paste(icecap_img, (0,0), mask=icecap_img)

nR,nG,nB,nA = img_normalFilter.convert("RGBA").split()
nRinv = ImageOps.invert(nR)
nRbl = Image.new("L", (4096,2048), (255))
img_normal_Final = Image.merge("RGBA", (nRbl,nG,nB,nRinv))

if life == False:
    colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.25)).enhance(1.2)
else:
    colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.75)).enhance(0.75)

img_normal_FinalFlip = img_normal_Final.transpose(Image.FLIP_TOP_BOTTOM)
ImageResFilterFlip = ImageResFilter.transpose(Image.FLIP_TOP_BOTTOM)
colorMap_FilterFlip = colorMap_Filter.transpose(Image.FLIP_TOP_BOTTOM)

img_normal_FinalFlip.save(filepath + "/Textures/PluginData/" + "normalMapTest.png")
ImageResFilterFlip.save(filepath + "/Textures/PluginData/" + "heightMapTest.png")
colorMap_FilterFlip.save(filepath + "/Textures/PluginData/" + "colorMapTest.png")
texEndTime = time.time()
clrEndTime = texEndTime-texStartTime

print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime) + " seconds.")