from PIL import Image, ImageEnhance, ImageFilter, ImageChops, ImageOps
import numpy as np
from scipy.signal import convolve2d
import noise
import math
import random
import time
import os

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

vacuum = False
geoActive = True

def add_Surface_Features(noiseImg, type, amount, alphaAdd, minMax):
    featureMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
    min = minMax[0]
    max = minMax[1]
    feature = Image.open(filepath + "/Presets/" + type + "1" + ".png")
    for i in range(0,amount):
        featureSize = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
        featurePreRes = feature.resize((featureSize,featureSize))
        featureA = featurePreRes.getchannel("A")
        alpha1 = Image.new("L", (featureSize, featureSize), (alphaAdd))
        featureA2 = ImageChops.multiply(alpha1,featureA)
        featurePreRes.putalpha(featureA2)

        print("Generating " + type + " " + str(i), end="\r")

        offs1 = random.randint(0,4096-featureSize)
        offs2 = random.randint(0,2048)
        #print(str(offs1) + " " + str(offs2))
        dist = (((offs2/2048)*2)*90)-90
        distCos = math.cos(math.radians(dist))
        featureRot = featurePreRes.rotate(random.randint(0,360))
        featureRes = featureRot.resize((featureSize,math.ceil(featureSize*distCos)))
        
        featureMap.paste(featureRes, (int(offs1),int(offs2)), mask=featureRes)
        #CraterMap.save("C:/test _normals/cratermap.png")
    noiseImg.paste(featureMap, (0,0), featureMap)

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
imageContr = ImageEnhance.Contrast(ImageEnhance.Brightness(imageRes).enhance(0.5)).enhance(3)
texEndTime = time.time()
noiseEndTime = texEndTime-texStartTime
print("Finished generating noise. Time elapsed: " + str(noiseEndTime) + " seconds.")

if vacuum == True:
    add_Surface_Features(imageContr, "crater", 400, 128, [50,400])
if geoActive == True:
    add_Surface_Features(imageContr, "volcano", 200, 150, [50,200])
if vacuum == False:
    add_Surface_Features(imageContr, "mountain", 400, 175, [50,600])

print("Finished overlaying surface features!")

print("Generating normals...")
texStartTime = time.time()
# Load the grayscale image and normalize to [0, 1]
img_gray = imageContr.convert("L")
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

img_normalFilter = img_normal.filter(ImageFilter.GaussianBlur(1))
nrm_Patch = Image.open(filepath + "/Presets/" + "normalPatch.png")
img_normalFilter.paste(nrm_Patch, (0,0), mask=nrm_Patch)
img_normalFilter.save(filepath + "/Textures/PluginData/" + "normalMapTest.png")
texEndTime = time.time()
nrmEndTime = texEndTime-texStartTime
print("Finished generating normals. Time elapsed: " + str(nrmEndTime) + " seconds.")

ImageResFilter = imageContr.filter(ImageFilter.SMOOTH_MORE)
ImageResFilter.save(filepath + "/Textures/PluginData/" + "heightMapTest.png")

print("Generating color...")
texStartTime = time.time()

grayMap = ImageOps.grayscale(ImageResFilter)
randomB_R = random.randint(0,75)
randomB_G = random.randint(0,75)
randomB_B = random.randint(0,75)
randomW_R = random.randint(0,255)
randomW_G = random.randint(0,255)
randomW_B = random.randint(0,255)
colorMap = ImageOps.colorize(grayMap, (randomB_R,randomB_G,randomB_B), (randomW_R,randomW_G,randomW_B))

colorMap.save(filepath + "/Textures/PluginData/" + "colorMapTest.png")
texEndTime = time.time()
clrEndTime = texEndTime-texStartTime
print("Finished generating colors. Time elapsed: " + str(clrEndTime) + " seconds.")

print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime) + " seconds.")