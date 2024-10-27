from PIL import Image, ImageFilter, ImageChops, ImageEnhance, ImageOps
import random
import os
from functools import lru_cache
filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

random.seed(42)

types = ["Jupiter", "Saturn"]
type = "Jupiter" #types[random.randint(0,len(types)-1)]

print(type)
ggClr = (120,170,200) #(random.randint(64,255),random.randint(64,255),random.randint(64,255))
ggMap = Image.new("RGBA", (8192,4096), (ggClr[0],ggClr[1],ggClr[2],255))
#ggMap.show()
#stormMap = Image.new("RGBA", (8192,4096), (0,0,0,0))

@lru_cache(maxsize=128)
def putBand():
    #print("aoch")
    if type == "Jupiter":
        randomNum = random.randint(1,3)
        randomBand = Image.open(filepath + "/Presets/jupiterBand" + str(randomNum) + ".png")
    else:
        randomNum = random.randint(1,1)
        randomBand = Image.open(filepath + "/Presets/saturnBand" + str(randomNum) + ".png")
    randomPos = random.randint(0,4096)
    randomBandOffs = ImageChops.offset(randomBand, xoffset=random.randint(0,4096), yoffset=0)
    bandHeight = randomBandOffs.height
    bandA = randomBand.getchannel("A")
    bandR = int(ggClr[0]*(random.randint(90,110)/100))
    bandG = int(ggClr[1]*(random.randint(90,110)/100))
    bandB = int(ggClr[2]*(random.randint(90,110)/100))
    bandClrd = ImageOps.colorize(randomBandOffs.convert("L"), (0,0,0), (0,0,0), (bandR,bandG,bandB))
    bandClrd.putalpha(bandA)
    if type == "Jupiter":
        ggMap.paste(bandClrd, (0,int(randomPos-bandHeight/2)), mask=bandClrd)
    else:
        ggMap.paste(bandClrd, (0,int(randomPos-bandHeight/1.5)), mask=bandClrd)
    return ggMap

for i in range(1,100):
    print(i, end="\r")
    ggMap = putBand()
    #if type == "Jupiter": #random.randint(0,20)
    #    for i in range(0,random.randint(0,1)):
    #        randomStormNum = random.randint(1,1)
    #        randomStorm = Image.open(filepath + "/Presets/jupiterStorm" + str(randomStormNum) + ".png")
    #        stormSizeMult = random.randint(50,200)/100
    #        randomStormSize = randomStorm.size
    #        randomStorm.resize((int(randomStormSize[0]*stormSizeMult),int(randomStormSize[1]*stormSizeMult)))
    #        randomPosX = random.randint(0,4096-int(randomStormSize[0]*stormSizeMult))
    #        randomPosY = randomPos
    #        stormA = randomStorm.getchannel("A")
    #        stormADrk = ImageEnhance.Brightness(stormA).enhance(0.5)
    #        stormClrd = ImageOps.colorize(randomStorm.convert("L"), (0,0,0), (0,0,0), (bandR,bandG,bandB))
    #        stormClrd.putalpha(stormADrk)
    #        
    #        stormMap.paste(stormClrd, (randomPosX,randomPosY), mask=stormClrd)

#ggMap.show()
if type == "Jupiter":
    ggMap.save(filepath + "/Textures/Misc/gasGiantTest.png")
else:
    ggMap.save(filepath + "/Textures/Misc/gasGiantTest.png")