import logging
import traceback
import os
filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
logging.basicConfig(filename=filepath+'/InfiniteDiscoveries.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

try:
    from PIL import Image, ImageEnhance, ImageFilter, ImageChops, ImageOps
    import numpy as np
    from scipy.signal import convolve2d
    import noise
    import math
    import time
    from colour import Color
    from wand import image as wImage
    import sys
    import random
    #from dds_sys import DDSFile

    #random.seed(69)

    generatorSeed = random.randint(0,353535) # Seed if you want less randomness

    terrainRNG = random.Random()
    terrainRNG_NP = np.random.RandomState()

    terrainRNG.seed(generatorSeed)
    terrainRNG_NP.seed(generatorSeed)

    #if terrainRNG.randint(0,3) == 0:
    #    oceanFac = terrainRNG.randint(16,255)
    #else:
    #    oceanFac = terrainRNG.randint(16,128)

    oceanFac = 200

    print(wImage.COMPRESSION_TYPES)

    # Star Colors
    black = Color("#000000")
    red = Color("#eb2700")
    colors1 = list(black.range_to(Color("#eb2700"),7))
    colors2 = list(red.range_to(Color("#ebac00"),10))
    lavaSpectrum = colors1 + colors2
    print(lavaSpectrum)

    oceanR = terrainRNG.randint(5,30)
    oceanG = terrainRNG.randint(5,50)
    oceanB = terrainRNG.randint(10,75)

    anomaly = "fltStrc"
    anLatLon = [23,-0]

    atmASL = 1
    vacuum = False
    geoActive = False
    ocean = True
    life = True
    temp = 290
    PstarRadius = 261600000
    planetRadius = 600000
    activeVolcano = True
    lava = False
    tidallyLocked = False
    eyeballType = "Temperate" # Temperate" is where the terminator is temperate. "Cold" is where the terminator is cold. "Hot" is where the terminator is hot.
    if planetRadius < 30000:
        isAsteroid = True
    else:
        isAsteroid = False
    icy = False

    if temp >= 700:
        eyeballType = "Hot"
        print("hot fuck you")
    elif temp < 700 and temp >= 210:
        eyeballType == "Temperate"
        print("temperate fucking cunt")
    elif temp < 210:
        eyeballType == "Cold"
        print("stupid cold bitch")

    if round(temp/100) < 17:
        lavaClr = (lavaSpectrum[round(temp/100)])
        lavaClr2 = (lavaSpectrum[round(temp/100)-7])
    else:
        lavaClr =  Color('#ff2100')  #lavaSpectrum[11]
        lavaClr2 = (lavaSpectrum[11])


    print(lavaClr)
    print(lavaClr2)
    
    lavaClrRGB = Color.get_rgb(lavaClr)
    lavaClr2RGB = Color.get_rgb(lavaClr2)


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

    albedoMap = Image.new("RGBA", (4096,2048), (0,0,0,0))

    def convertToBiomeFeature(featureMap, colour, brighten1):
        biomeFeature = Image.new("RGBA", (4096,2048), colour)
        biomeFeature.putalpha(ImageEnhance.Brightness(ImageOps.posterize(ImageEnhance.Brightness((featureMap.getchannel("A"))).enhance(brighten1), 1)).enhance(2))
        biomeMap.paste(biomeFeature, (0,0), mask=biomeFeature)

    def add_Surface_Features(noiseImg, type, amount, alphaAdd, minMax, types, mean, std_dev, albedo=None):
        featureMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
        minSize = minMax[0]
        maxSize = minMax[1]
        for i in range(0,amount):
            feature = Image.open(filepath + "/Presets/" + type + str(terrainRNG.randint(1,types)) + ".png")
            featureSizeInt = int(terrainRNG_NP.normal(mean, std_dev))
            featureSize = max(minSize, min(maxSize, featureSizeInt))
            featurePreRes = feature.resize((featureSize,featureSize))
            featureA = featurePreRes.getchannel("A")
            #print(int(alphaAdd*(featureSize/minMax[1])))
            alpha1 = Image.new("L", (featureSize, featureSize), (int(alphaAdd*(featureSize/minMax[1])))*2)
            featureA2 = ImageChops.multiply(alpha1,featureA)
            featurePreRes.putalpha(featureA2)

            print("Generating " + type + " " + str(i) + "...", end="\r")

            offs1 = terrainRNG.randint(0,4096-featureSize)
            offs2 = terrainRNG.randint(0,2048)
            #print(str(offs1) + " " + str(offs2))
            dist = (((offs2/2048)*2)*90)-90
            distCos = math.cos(math.radians(dist))
            featureRot = featurePreRes.rotate(terrainRNG.randint(0,360))
            featureRes = featureRot.resize((featureSize,math.ceil(featureSize*distCos)))
            
            featureMap.paste(featureRes, (int(offs1),int(offs2-featureSize//4)), mask=featureRes)

            if not albedo == None:
                albFeature = Image.open(filepath + "/Presets/" + albedo + str(terrainRNG.randint(1,types)) + ".png")
                albFeaturePreRes = albFeature.resize((featureSize,featureSize))
                albFeatureA = albFeaturePreRes.getchannel("A")
                albAlpha1 = Image.new("L", (featureSize, featureSize), (200))
                albFeatureA2 = ImageChops.multiply(albAlpha1,albFeatureA)
                albFeaturePreRes.putalpha(albFeatureA2)
                albFeatureRot = albFeaturePreRes.rotate(terrainRNG.randint(0,360))
                albFeatureRes = albFeatureRot.resize((featureSize,math.ceil(featureSize*distCos)))
                albedoMap.paste(albFeatureRes, (int(offs1),int(offs2-featureSize//4)), mask=albFeatureRes)
        noiseImg.paste(featureMap, (0,0), featureMap)
        #featureMap.show()
        #albedoMap.show()
        if not albedo == None:
            return featureMap, albedoMap
        else:
            return featureMap

    print("Generating noise...")
    texStartTime = time.time()
    seed = terrainRNG.randint(0,1000)
    size = 1024
    radius = 1.0
    #lacunarity = 2.6
    octaves = 5
    persistence = 0.5
    heightmap = np.zeros((size, size))
    if isAsteroid == True:
        freq_random = terrainRNG.randint(2,8)/10
        lacunarity = 5
    else:
        freq_random = terrainRNG.randint(10,20)/10
        lacunarity = 2.6
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

    #if lava == True:
    #    lavaNoise = np.zeros((size, size))
    #    for i in range(size):
    #        print("Generating for " + str(time.time()-texStartTime) + " seconds...", end="\r")
    #        for j in range(size):
    #            # Convert the pixel coordinates to spherical coordinates
    #            theta = 2 * math.pi * i / size
    #            phi = math.pi * j / size
    #            x = radius * math.sin(phi) * math.cos(theta)
    #            y = radius * math.sin(phi) * math.sin(theta)
    #            z = radius * math.cos(phi)
#
    #            # Sample the noise function at the current point using multiple octaves
    #            noise_value = 0.0
    #            frequency = 1
    #            amplitude = 1.0
    #            for k in range(octaves):
    #                noise_value += amplitude * noise.snoise4(x * frequency, y * frequency, z * frequency, seed)
    #                frequency *= 10
    #                amplitude *= 0.5
#
    #            # Store the noise value in the heightmap
    #            lavaNoise[i, j] = noise_value
#
    #    lavaNoise = (lavaNoise - lavaNoise.min()) / (lavaNoise.max() - lavaNoise.min())
    #    lavaNoiseImage = Image.fromarray((lavaNoise * 255).astype(np.uint8), mode='L')
    #    lavaImage90 = lavaNoiseImage.rotate(90)
    #    lavaImageRes = lavaImage90.resize((4096,2048), resample=Image.Resampling.BICUBIC)
    #    #lavaImageRes.show()

    heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
    image = Image.fromarray((heightmap * 255).astype(np.uint8), mode='L')
    image90 = image.rotate(90)
    imageRes = image90.resize((4096,2048), resample=Image.Resampling.BICUBIC)
    brtAmount = 1
    contrAmount = 1/brtAmount
    imageContr = ImageEnhance.Contrast(ImageEnhance.Brightness(imageRes).enhance(brtAmount)).enhance(contrAmount)
    texEndTime = time.time()
    noiseEndTime = texEndTime-texStartTime

    smallNoise = Image.new("L", [2048,1024], (0))

    for w in range(1024):
        for h in range(2048):
            randomValue = terrainRNG.randint(0,255)
            smallNoise.putpixel((h,w),randomValue)

    smallNoiseRes = smallNoise.resize((4096,2048)).convert("RGBA")
    smallNoiseRes.putalpha(terrainRNG.randint(2,8))

    imageContr.paste(smallNoiseRes,(0,0),mask=smallNoiseRes)

    print("Finished generating noise. Time elapsed: " + str(noiseEndTime) + " seconds.")

    # For future me. The function (in order) takes the Original Image, decal name, amount, alpha, min/max size, variants, mean, standard deviation, and an optional albedo feature.
    if atmASL < 0.35:
        if icy == False:
            if planetRadius < 30000 and planetRadius > 5000:
                large_craterMap = add_Surface_Features(imageContr, "crater", 50, 100, [500,1024], 2, 500, 750)
            elif planetRadius > 30000:
                craterMap = add_Surface_Features(imageContr, "crater", 250, 225, [200,800], 3, 250, 200)
                craterClusterMap = add_Surface_Features(imageContr, "craterCluster", 100, 255, [200,800], 1, 250, 200)
                small_craterMap = add_Surface_Features(imageContr, "crater", 250, 100, [25,250], 2, 100, 100)
            if planetRadius > 75000 and ocean == False:
                ray_craterMap, ray_albedoMap = add_Surface_Features(imageContr, "rayCrater", 200, 50, [100,700], 1, 100, 200, "rayCrater_alb")
        else:
            if atmASL < 0.35:
                craterMap = add_Surface_Features(imageContr, "crater", 50, 225, [200,800], 3, 250, 200)
            icy_Crack_Map = add_Surface_Features(imageContr, "crack", 300, 255, [400,600], 2, 50, 500)
    if geoActive == True and planetRadius > 80000:
        volcanoMap = add_Surface_Features(imageContr, "volcano", 200, 100, [50,200], 1, 50, 100)
        if activeVolcano == True:
            activeVolcanoMap, lavaAlbedoMap = add_Surface_Features(imageContr, "volcano", 200, 100, [50,200], 1, 50, 100, "volcano_Lava")
        canyonMap = add_Surface_Features(imageContr, "canyon", 400, 125, [50,400], 2, 50, 100)
    if vacuum == False and planetRadius > 30000:
        mountainMap = add_Surface_Features(imageContr, "mountain", 400, 175, [50,600], 3, 50, 300)
        plateauMap = add_Surface_Features(imageContr, "plateau", 400, 175, [50,600], 4, 50, 300)
    if lava == True and planetRadius > 80000:
        crackMap = add_Surface_Features(imageContr, "canyon", 200, 255, [100,500], 2, 50, 500)

    if icecaps == True and tidallyLocked == False:
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
        #icecap_drk = ImageEnhance.Brightness(icecap_img).enhance(0.6)

        if ocean == True and tidallyLocked == False: # Icecaps for the fucking thing
            heightmapFiltered = imageContr.point( lambda p: 255 if p > oceanFac else 0 )
            heightmapFilteredButAlsoInverted = ImageOps.invert(heightmapFiltered)
            icecap_foroceans = Image.new("RGBA", (4096,2048), (oceanFac+8,oceanFac+8,oceanFac+8,255))
            #icecap_foroceans.putalpha(heightmapFilteredButAlsoInverted)
            anotherFUCKINGBLACKBOX = Image.new("L", (4096,2048), (0))
            anotherFUCKINGBLACKBOX.putalpha(heightmapFiltered)
            blackFuckingBoxWhyTheFuckDoINeedToDoThis = Image.new("L", (4096,2048), (0))
            blackFuckingBoxWhyTheFuckDoINeedToDoThis.paste(icecap_img, (0,0), mask=icecap_img)
            blackFuckingBoxWhyTheFuckDoINeedToDoThis.paste(anotherFUCKINGBLACKBOX, (0,0), mask=anotherFUCKINGBLACKBOX)
            icecap_foroceans.putalpha(blackFuckingBoxWhyTheFuckDoINeedToDoThis)
            #heightmapFilteredButAlsoInverted.show()
            #icecap_foroceans.show()
            #icecap_img.show()
            imageContr.paste(icecap_foroceans, (0,0), mask=icecap_foroceans)

    if tidallyLocked == True:
        eyeball = Image.new("RGBA", (4096,2048), (255,255,255,255))
        blackCircle = Image.open(filepath + "/Presets/blackcircle.png")

        if eyeballType == "Temperate":
            circleSize = 1500
            backCircleSize = 2048
        elif eyeballType == "Cold":
            circleSize = temp * 7
            backCircleSize = 2500
        elif eyeballType == "Hot":
            circleSize = temp * 2
            backCircleSize = 2500

        blackCircleResized = blackCircle.resize((circleSize,circleSize))

        backBlackCircleResized = blackCircle.resize((backCircleSize,backCircleSize))

        circlePosX = int(2048 - (circleSize / 2))
        circlePosY = int(1024 - (circleSize / 2))

        backCirclePosX = int(2048 - (backCircleSize / 2))
        backCirclePosY = int(1024 - (backCircleSize / 2))

        Thingamabob = Image.new("RGBA", (4096,2048), (0,0,0,0))
        Thingamabob.paste(blackCircleResized, (circlePosX,circlePosY), mask=blackCircleResized)

        backThingamabob = Image.new("RGBA", (4096,2048), (0,0,0,0))
        backThingamabob.paste(backBlackCircleResized, (backCirclePosX,backCirclePosY), mask=backBlackCircleResized)

        blackCircle = Thingamabob
        backBlackCircleMoved = ImageChops.offset(backThingamabob, 2048,0)

        #backBlackCircleMoved.show()

        if eyeballType == "Temperate":
            eyeball.paste(blackCircle, (0,0), mask=blackCircle)

            eyeball.paste(backBlackCircleMoved, (0,0), mask=backBlackCircleMoved)
        elif eyeballType == "Cold":
            eyeball.paste(blackCircle, (0,0), mask=blackCircle)
        elif eyeballType == "Hot":
            eyeball.paste(blackCircle, (0,0), mask=blackCircle)

        map_img = imageRes.convert("RGBA")
        #Height = temp * 6
        #backg_black = Image.new("L", (4096,2048), (0))
        #img_black = Image.new("L", (4096,Height), (255))
        #center_y = icecap_img.size[1] // 2
        #top_left_y = center_y - img_black.size[1] // 2
        #backg_black.paste(img_black, (0,top_left_y+(int(top_left_y/((280/temp)*(280/temp))))), mask=img_black)
        #icecap_img.putalpha(ImageOps.invert(backg_black))

        #eyeball.show()

        #blurred_map_img = map_img.filter(ImageFilter.GaussianBlur(radius=2))
        # Get the pixel access objects for both images
        img_pixels = eyeball.load()
        map_pixels = map_img.load()
        # Define the displacement amount (in pixels)
        displacement = 25
        # Loop through each pixel in the image
        for y in range(eyeball.size[1]):
            #print("Calculating icecap deformity for pixel row " + str(y), end="\r")
            for x in range(eyeball.size[0]):
                # Get the displacement value from the map image
                map_value = map_pixels[x, y][0]  # Use the first channel of the map image

                # Calculate the new x-coordinate with the displacement value
                new_x = x + (map_value - 16) * displacement / 16

                # Get the pixel value from the original image at the new coordinates
                try:
                    pixel = img_pixels[new_x, y]
                except IndexError:
                    pixel = img_pixels[x, y]

                # Set the pixel value in the displaced image
                img_pixels[x, y] = pixel
        #print("Finished generating icecaps!")
        eyeballMoved = ImageChops.offset(eyeball, 150,0)
        eyeballDist = eyeballMoved.convert("L")
        #eyeballDist.show()

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
        randomM_R = terrainRNG.randint(125,200)
        randomM_G = terrainRNG.randint(125,150)
        randomM_B = terrainRNG.randint(100,105)
        randomW_R = terrainRNG.randint(65,100)
        randomW_G = terrainRNG.randint(65,100)
        randomW_B = terrainRNG.randint(65,100)
    elif life == False and ocean == True and icy == False:
        randomB_R = terrainRNG.randint(25,75)
        randomB_G = terrainRNG.randint(25,25)
        randomB_B = terrainRNG.randint(25,25)
        randomM_R = terrainRNG.randint(100,175)
        randomM_G = terrainRNG.randint(75,100)
        randomM_B = terrainRNG.randint(50,55)
        randomW_R = terrainRNG.randint(65,100)
        randomW_G = terrainRNG.randint(65,100)
        randomW_B = terrainRNG.randint(65,100)
    elif icy == True:
        randomB_R = terrainRNG.randint(100,125)
        randomB_G = terrainRNG.randint(100,125)
        randomB_B = terrainRNG.randint(100,200)
        randomM_R = terrainRNG.randint(100,125)
        randomM_G = terrainRNG.randint(100,125)
        randomM_B = terrainRNG.randint(100,200)
        randomW_R = terrainRNG.randint(25,125)
        randomW_G = terrainRNG.randint(25,125)
        randomW_B = terrainRNG.randint(25,200)
    else:
        randomB_R = terrainRNG.randint(25,75)
        randomB_G = terrainRNG.randint(25,75)
        randomB_B = terrainRNG.randint(25,75)
        randomM_R = terrainRNG.randint(100,175)
        randomM_G = terrainRNG.randint(75,100)
        randomM_B = terrainRNG.randint(50,55)
        randomW_R = terrainRNG.randint(50,200)
        randomW_G = terrainRNG.randint(50,200)
        randomW_B = terrainRNG.randint(50,200)
    print(str(randomB_R) + " " + str(randomB_G) + " " + str(randomB_B))
    print(str(randomM_R) + " " + str(randomM_G) + " " + str(randomM_B))
    print(str(randomW_R) + " " + str(randomW_G) + " " + str(randomW_B))
    if life == False:
        blackP = terrainRNG.randint(0,85)
        midP = terrainRNG.randint(85,150)
        whiteP = terrainRNG.randint(150,200)
    else:
        blackP = terrainRNG.randint(0,74)
        midP = terrainRNG.randint(150,200)
        whiteP = terrainRNG.randint(200,255)
        
    colorMap = ImageOps.colorize(grayMap, (randomB_R,randomB_G,randomB_B), (randomW_R,randomW_G,randomW_B), (randomM_R,randomM_G,randomM_B), blackpoint=blackP, midpoint=midP, whitepoint=whiteP)

    if tidallyLocked == True:
        if eyeballType == "Temperate":
            blackCircleA = blackCircle.getchannel("A")
            desertColor = ImageOps.colorize(blackCircle.convert("L"), (randomM_R, randomM_G, randomM_B), (0,0,0))
            desertColor.putalpha(blackCircleA)
            colorNoGrass = ImageOps.colorize(grayMap, (randomM_R,randomM_R,randomM_R), (randomW_R,randomW_G,randomW_B), (randomM_R,randomM_G,randomM_B), blackpoint=blackP, midpoint=midP, whitepoint=whiteP)
            #colorNoGrass.show()
            desertColorBlur = desertColor.filter(ImageFilter.GaussianBlur(radius=50))
            #desertColorBlur.show()
            colorMap.paste(colorNoGrass, (0,0), mask=desertColorBlur)
            iceSize = 2048
            iceColorBackg = Image.new("RGBA", (4096,2048), (0,0,0,0))
            iceColor = Image.new("RGBA", (iceSize,iceSize), (255,255,255,255))
            icePosX = int(2048 - (iceSize / 2))
            icePosY = int(1024 - (iceSize / 2))
            iceColorBackg.paste(iceColor, (icePosX,icePosY), mask=iceColor)
            iceColorMoved = ImageChops.offset(iceColorBackg, 2048,0)
            #iceColorMoved.show()
            iceColorBlur = iceColorMoved.filter(ImageFilter.GaussianBlur(radius=50))
            #iceColorBlur.show()
            colorMap.paste(iceColorBlur, (0,0), mask=iceColorBlur)
        elif eyeballType == "Cold":
            #iceSize = 2500
            iceColor = (eyeballDist)
            #iceColor.show()
            #icePosX = int(2048 - (iceSize / 2))
            #icePosY = int(1024 - (iceSize / 2))
            #iceColorBackg.paste(iceColor, (icePosX,icePosY), mask=iceColor)
            #iceColorMoved = ImageChops.offset(iceColorBackg, 2048,0)
            #iceColorMoved.show()
            
            if ocean == True:
                iceColorBlur = iceColor.filter(ImageFilter.GaussianBlur(radius=0))
            else:
                iceColorBlur = iceColor.filter(ImageFilter.GaussianBlur(radius=200))
            
            #iceColorBlur.show()

            colorMap.paste(iceColorBlur, (0,0), mask=iceColorBlur)

    if ocean == True:
        if tidallyLocked == True: # TIDALLY LOCKED OCEANS <----------------------------------------------------------------
            if eyeballType == "Temperate":
                brightFac = int(terrainRNG.randint(1,300)/100)
            elif eyeballType == "Cold":
                brightFac = int(terrainRNG.randint(1,50)/1000)

            print("Ocean exists! Dryness factor is " + str(brightFac))

            brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
            contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
            posted = ImageOps.posterize(contrHeight.convert("RGB"),2).convert("L")

            #posted.show()

            eyeball = Image.open(filepath + "/Presets/eyeball.png").convert("L")

            brightFinal = ImageEnhance.Brightness(posted).enhance(100)
            
            oceanRGBA = brightFinal.convert("RGBA")

            if eyeballType == "Temperate":
                eyeballInvPosterized = ImageEnhance.Brightness(ImageEnhance.Contrast(ImageOps.invert(eyeballDist)).enhance(100)).enhance(100)
            elif eyeballType == "Cold":
                eyeballInvPosterized = ImageEnhance.Brightness(ImageEnhance.Contrast((eyeballDist)).enhance(100)).enhance(100)

            eyeballInvPosterizedA = eyeballInvPosterized.convert("L")

            eyeballInvPosterized.putalpha(eyeballInvPosterizedA)

            brightFinal.paste(eyeballInvPosterized, (0,0), mask=eyeballInvPosterized)

            #oceanRGBA = brightFinal.convert("RGBA")

            #eyeballInvPosterized.show()
            #oceanRGBA.show()

            oceanInv = ImageOps.invert(brightFinal).convert("RGBA")

            ocInvL = oceanInv.convert("L")
            maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
            maxHeightMask.putalpha(posted)
            heightWithinThresh = ImageResFilter.convert("L")
            heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
            min_value, max_value = heightWithinThresh.getextrema()
            oceanGray = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
            #oceanGray.show()
            colorOcean = ImageOps.colorize(oceanGray, (oceanR,oceanG,oceanB), (oceanR,oceanG*2,oceanB), blackpoint=int(brightFac/2))
            colorOcean.putalpha(ocInvL)
            #colorOcean.show()
            
            #oceanInv.show()

            # Brighten the non-ocean parts to avoid invisible lakes from appearing
            eyeballInvPosterizedADrknd = ImageEnhance.Brightness(eyeballInvPosterizedA).enhance(0.5)
            eyeballInvPosterizedDrknd = Image.new("RGBA", (4096,2048), (255,255,255,255))
            eyeballInvPosterizedDrknd.putalpha(eyeballInvPosterizedADrknd)
            eyeballInvPosterizedBlur = eyeballInvPosterizedDrknd.filter(ImageFilter.GaussianBlur(5))
            ImageResFilter.paste(eyeballInvPosterizedBlur, (0,0), mask=eyeballInvPosterizedBlur)

            #oceanRGBA.putalpha(ocInvL)
            oceanBlurA = oceanInv.filter(ImageFilter.GaussianBlur(5)).convert("L")
            heightOcean = Image.new("RGBA", (4096,2048), (0,0,0))
            heightOcean.putalpha(oceanBlurA)
            
            ImageResFilter.paste(heightOcean, (0,0), mask=heightOcean)

            #ImageResFilter.show()

            normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
            normalOcean.putalpha(ocInvL)
            img_normalFilter.paste(normalOcean, (0,0), mask=ocInvL)

            #beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
            #beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
            #beachColor.putalpha(beachMask)
            #colorMap.paste(beachColor, (0,0), mask=beachColor)
            #colorOcean = Image.new("RGBA", (4096,2048), (oceanR+60,oceanG+60,oceanB+60))
            #colorOcean2 = Image.new("RGBA", (4096,2048), (oceanR, oceanG, oceanB))
            #ocInvL_Blur = ocInvL.filter(ImageFilter.GaussianBlur(15))
            #colorOcean2.putalpha(ocInvL_Blur)
            #colorOcean.paste(colorOcean2, (0,0), mask=colorOcean2)
            #colorOcean.putalpha(ocInvL)

            colorMap.putalpha(ocInvL)
        else: # NOT TIDALLY LOCKED OCEANS <----------------------------------------------------------------
            #brightFac = float(random.randint(1,500)/100)
            brightFac = oceanFac

            print("Ocean exists! Dryness factor is " + str(brightFac))

            #brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
            #contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
            #posted = ImageOps.posterize(contrHeight.convert("RGB"),2)

            imageThreshold = ImageResFilter.point( lambda p: 255 if p > brightFac else 0 )
            # To mono
            imageThreshold = imageThreshold.convert('RGB')
            #imageThreshold.show()
            posted = imageThreshold.convert("L")

            ocInvL = ImageOps.invert(posted)
            maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
            maxHeightMask.putalpha(posted)
            heightWithinThresh = ImageResFilter.convert("L")
            heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
            min_value, max_value = heightWithinThresh.getextrema()
            print("you fucking bitch")
            print(max_value)
            print(min_value)
            print((max_value - min_value))
            oceanGray = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
            colorOcean = ImageOps.colorize(oceanGray, (oceanR,oceanG,oceanB), (oceanR,oceanG*2,oceanB), blackpoint=int(brightFac/2))
            colorOcean.putalpha(ocInvL)
            #colorOcean.show()
            
            #ImageResFilter.paste(heightOcean, (0,0), mask=heightOcean)

            #ImageResFilter.show()

            normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
            normalOcean.putalpha(ocInvL)
            img_normalFilter.paste(normalOcean, (0,0), mask=ocInvL)
#
            #beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
            #beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
            #beachColor.putalpha(beachMask)
            #colorMap.paste(beachColor, (0,0), mask=beachColor)
            #colorOcean = Image.new("RGBA", (4096,2048), (oceanR+60,oceanG+60,oceanB+60))
            #colorOcean2 = Image.new("RGBA", (4096,2048), (oceanR, oceanG, oceanB))
            #ocInvL_Blur = ocInvL.filter(ImageFilter.GaussianBlur(15))
            #colorOcean2.putalpha(ocInvL_Blur)
            #colorOcean.paste(colorOcean2, (0,0), mask=colorOcean2)
            #colorOcean.putalpha(ocInvL)

            if icecaps == True:
                #icecap_alph = icecap_img.getchannel("A")
                #icecap_alph_blur = icecap_alph.filter(ImageFilter.GaussianBlur(10))
                #icecap_inv = ImageOps.invert(icecap_img.convert("RGB"))
                #icecap_inv.putalpha(icecap_alph_blur)
                #ocInvL.paste(icecap_inv, (0,0), mask=icecap_inv)
                icecapBlur = icecap_img.filter(ImageFilter.GaussianBlur(5))
                colorMap.paste(icecapBlur, (0,0), mask=icecapBlur)
                colorMap.putalpha(ocInvL)
                #icecap_img.show()
            else:
                colorMap.putalpha(ocInvL)
    elif icecaps == True and ocean == False and tidallyLocked == False:
        icecapBlur = icecap_img.filter(ImageFilter.GaussianBlur(5))
        colorMap.paste(icecapBlur, (0,0), mask=icecapBlur)

    if lava == True:
        if tidallyLocked == True:
            lavaFactor = np.interp(temp, [700, 2000], [32, 255])
            brightFac = int(lavaFactor*(terrainRNG.randint(80,120)/100))

            print("Lava exists! Dryness factor is " + str(brightFac))

            imageThreshold = ImageResFilter.point( lambda p: 255 if p > brightFac else 0 )
            # To mono
            imageThreshold = imageThreshold.convert('RGB')
            posted = imageThreshold.convert("L")

            eyeballInvPosterized = ImageEnhance.Brightness(ImageEnhance.Contrast((eyeballDist)).enhance(100)).enhance(100)

            eyeballInvPosterizedA = eyeballInvPosterized.convert("L")

            eyeballInvPosterized.putalpha(eyeballInvPosterizedA)

            posted.paste(eyeballInvPosterized, (0,0), mask=eyeballInvPosterized)

            #brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
            #contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
            #posted = ImageOps.posterize(contrHeight.convert("RGB"),2)

            lvInvL = ImageOps.invert(posted)
            maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
            maxHeightMask.putalpha(posted)
            heightWithinThresh = ImageResFilter.convert("L")
            heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
            min_value, max_value = heightWithinThresh.getextrema()
            lavaGray = image_stretched = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
            colorLava = ImageOps.colorize(lavaGray, (255, 204, 0), (255, 0, 0))
            colorLava.putalpha(lvInvL)
            colorLava.show()

            normalLava = Image.new("RGBA", (4096,2048), (128,128,255))
            normalLava.putalpha(lvInvL)
            img_normalFilter.paste(normalLava, (0,0), mask=lvInvL)
            
            heightLava = Image.new("RGBA", (4096,2048), (0,0,0))
            lvInvLBLUR = lvInvL.filter(ImageFilter.GaussianBlur(10))
            heightLava.putalpha(lvInvLBLUR)
            ImageResFilter.paste(heightLava, (0,0), mask=lvInvLBLUR)
            
            #colorLava = Image.new("RGBA", (4096,2048), (int(lavaClrRGB[0]*255),int(lavaClrRGB[1]*255),int(lavaClrRGB[2]*255)))
            #colorLava.show()
            #colorLava2 = ImageOps.colorize(lavaImageRes, (0,0,0), (lavaClrRGB[0]*255,lavaClrRGB[1]*255,lavaClrRGB[2]*255))
            #colorLava2.show()
            #lvInvL_Blur = lvInvL.filter(ImageFilter.GaussianBlur(10))
            #colorLava2.putalpha(lvInvL_Blur)
            #colorLava.paste(colorLava2, (0,0), mask=colorLava2)
            #colorLavaContr = ImageEnhance.Contrast(ImageEnhance.Brightness(colorLava).enhance(2)).enhance(2)
            #colorLava.putalpha(lvInvL)
        else:
            lavaFactor = np.interp(temp, [700, 2000], [32, 255])
            brightFac = int(lavaFactor*(terrainRNG.randint(80,120)/100))

            print("Lava exists! Dryness factor is " + str(brightFac))

            #brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
            #contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
            #posted = ImageOps.posterize(contrHeight.convert("RGB"),2)

            imageThreshold = ImageResFilter.point( lambda p: 255 if p > brightFac else 0 )
            # To mono
            imageThreshold = imageThreshold.convert('RGB')
            posted = imageThreshold.convert("L")
            lvInvL = ImageOps.invert(posted)
            maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
            maxHeightMask.putalpha(posted)
            heightWithinThresh = ImageResFilter.convert("L")
            heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
            min_value, max_value = heightWithinThresh.getextrema()
            lavaGray = image_stretched = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
            colorLava = ImageOps.colorize(lavaGray, (255, 204, 0), (255, 0, 0))
            colorLava.putalpha(lvInvL)
            colorLava.show()

            normalLava = Image.new("RGBA", (4096,2048), (128,128,255))
            normalLava.putalpha(lvInvL)
            img_normalFilter.paste(normalLava, (0,0), mask=lvInvL)
            
            heightLava = Image.new("RGBA", (4096,2048), (0,0,0))
            lvInvLBLUR = lvInvL.filter(ImageFilter.GaussianBlur(10))
            heightLava.putalpha(lvInvLBLUR)
            ImageResFilter.paste(heightLava, (0,0), mask=lvInvLBLUR)

            #colorLava = Image.new("RGBA", (4096,2048), (int(lavaClrRGB[0]*255),int(lavaClrRGB[1]*255),int(lavaClrRGB[2]*255)))
            #colorLava.show()
            #colorLava2 = ImageOps.colorize(lavaImageRes, (0,0,0), (lavaClrRGB[0]*255,lavaClrRGB[1]*255,lavaClrRGB[2]*255))
            #colorLava2.show()
            #lvInvL_Blur = lvInvL.filter(ImageFilter.GaussianBlur(10))
            #colorLava2.putalpha(lvInvL_Blur)
            #colorLava.paste(colorLava2, (0,0), mask=colorLava2)
            #colorLavaContr = ImageEnhance.Contrast(ImageEnhance.Brightness(colorLava).enhance(2)).enhance(2)
            #colorLava.putalpha(lvInvL)

    print("Generating biome maps...")
    texStartTime = time.time()

    biomeMap = ImageOps.posterize(imageContr, 2).convert("RGBA")

    try:
        convertToBiomeFeature(canyonMap, (255,0,255), 10)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(mountainMap, (255,255,0), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(craterMap, (0, 255, 150), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(large_craterMap, (0, 255, 150), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(small_craterMap, (0, 255, 150), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(ray_craterMap, (0, 255, 150), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(ray_albedoMap, (150, 255, 150), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(volcanoMap, (255,0,0), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(activeVolcanoMap, (255,0,0), 1.75)
    except NameError:
        print("Ignoring")

    try:
        convertToBiomeFeature(lavaAlbedoMap, (255, 98, 0), 1.75)
    except NameError:
        print("Ignoring")

    if ocean == True:
        ocean_colored = Image.new("RGBA", (4096,2048), (0, 0, 50))
        ocean_colored.putalpha(ocInvL)
        biomeMap.paste(ocean_colored, (0,0), mask=ocean_colored)

    if lava == True:
        ocean_colored = Image.new("RGBA", (4096,2048), (255, 98, 0))
        ocean_colored.putalpha(lvInvL)
        biomeMap.paste(ocean_colored, (0,0), mask=ocean_colored)

    if icecaps == True and tidallyLocked == False:
        icecap_colored = Image.new("RGBA", (4096,2048), (150, 200, 255))
        icecap_colored.putalpha(icecap_img.getchannel("A"))
        biomeMap.paste(icecap_colored, (0,0), mask=icecap_colored)

    if anomaly == "fltStrc":
        anomalyMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
        anomalyDot = Image.new("RGBA", (2,2), (119, 198, 247))
        x_pixel = round((anLatLon[1] + 180) * (4096 / 360))
        y_pixel = round((90 - anLatLon[0]) * (2048 / 180))
        print(x_pixel)
        print(y_pixel)
        anomalyMap.paste(anomalyDot, (int(x_pixel+(anomalyDot.size[0])/2), int(y_pixel+(anomalyDot.size[1])/2)), mask=anomalyDot)
        anomalyMapOffs = ImageChops.offset(anomalyMap,-1024,0)
        #anomalyMapOffs.show()
        biomeMap.paste(anomalyMapOffs, (0,0), mask=anomalyMapOffs)
    if anomaly == "crshShp":
        anomalyMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
        anomalyDot = Image.new("RGBA", (2,2), (82, 96, 105))
        x_pixel = round((anLatLon[1] + 180) * (4096 / 360) - 1024)
        y_pixel = round((90 - anLatLon[0]) * (2048 / 180))
        print(x_pixel)
        print(y_pixel)
        anomalyMap.paste(anomalyDot, (int(x_pixel+(anomalyDot.size[0])/2), int(y_pixel+(anomalyDot.size[1])/2)), mask=anomalyDot)
        anomalyMapOffs = ImageChops.offset(anomalyMap,-1024,0)
        #anomalyMapOffs.show()
        biomeMap.paste(anomalyMapOffs, (0,0), mask=anomalyMapOffs)

    texEndTime = time.time()
    biomeEndTime = texEndTime-texStartTime
    print("Finished generating biomes! Time elapsed: " + str(biomeEndTime) + " seconds.")

    nR,nG,nB,nA = img_normalFilter.convert("RGBA").split()
    nRinv = ImageOps.invert(nR)
    nRbl = Image.new("L", (4096,2048), (255))
    img_normal_Final = Image.merge("RGBA", (nRbl,nG,nB,nRinv))

    if life == True:
        colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.75)).enhance(0.75)
    elif lava == True:
        colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.3)).enhance(0.4)
    else:
        colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.25)).enhance(1.2)

    if ocean == True:
        vertColorMap = Image.new("RGB", (4096,2048), (0,0,0))
        vertColorMap.paste(colorMap_Filter)

    colorMap_Filter.paste(albedoMap, (0,0), mask=albedoMap)
    if lava == True:
        colorMap_Filter.paste(colorLava, (0,0), mask=colorLava)
    if ocean == True:
        colorMap_Filter.paste(colorOcean, (0,0), mask=colorOcean)

    #img_normal_FinalFlip = img_normal_Final.transpose(Image.FLIP_TOP_BOTTOM)
    #ImageResFilterFlip = ImageResFilter.transpose(Image.FLIP_TOP_BOTTOM)
    #colorMap_FilterFlip = colorMap_Filter.transpose(Image.FLIP_TOP_BOTTOM)

    print("Saving...")

    biomeMap.save(filepath + "/Textures/Misc/" + "biomeMapTest.png", compress_level=1)
    img_normal_Final.save(filepath + "/Textures/Misc/" + "normalMapTest.png", compress_level=1)
    if isAsteroid == True:
        #heightBlur = ImageResFilter.filter(ImageFilter.GaussianBlur(15))
        ImageResFilter.save(filepath + "/Textures/Misc/" + "heightMapTest.png", compress_level=1)
    else:
        ImageResFilter.save(filepath + "/Textures/Misc/" + "heightMapTest.png", compress_level=1)
    colorMap_Filter.save(filepath + "/Textures/Misc/" + "colorMapTest.png", compress_level=1)
    if ocean == True:
        vertColorMap.save(filepath + "/Textures/Misc/" + "vertColorMapTest.png", compress_level=1)
    texEndTime = time.time()
    clrEndTime = texEndTime-texStartTime

    ddsimg = wImage.Image(filename= filepath + "/Textures/Misc/" + "heightMapTest.png", )
    ddsimg.gaussian_blur(5, 1)
    ddsimg.compression = 'losslessjpeg'
    ddsimg.save(filename=filepath + "/Textures/Misc/ddstest.dds")

    print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime + biomeEndTime) + " seconds.")
except Exception as e:
    logging.error(traceback.format_exc())
    print(traceback.format_exc())
    input("Type anything or press enter to close: ")