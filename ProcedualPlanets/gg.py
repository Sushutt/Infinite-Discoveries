from PIL import Image, ImageEnhance, ImageChops, ImageOps
import random
import os
import time
from colour import Color
import numpy
import sys
filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")


def generateGasGiantMaps():
    gg1 = Image.open(filepath + "/Presets/" + "GasGiant" + str(random.randint(1,3)) + ".png")
    gg2 = Image.open(filepath + "/Presets/" + "GasGiant" + str(random.randint(1,3)) + ".png")
    gg3 = Image.open(filepath + "/Presets/" + "GasGiant" + str(random.randint(1,3)) + ".png")


    ggClr1 = ImageOps.colorize(ImageOps.grayscale(gg1),(128,128,128),(random.randint(0,255),random.randint(0,255),random.randint(0,255))).convert("RGBA")
    ggClr2 = ImageOps.colorize(ImageOps.grayscale(gg2),(128,128,128),(random.randint(0,255),random.randint(0,255),random.randint(0,255))).convert("RGBA")
    ggClr3 = ImageOps.colorize(ImageOps.grayscale(gg3),(128,128,128),(random.randint(0,255),random.randint(0,255),random.randint(0,255))).convert("RGBA")

    ggCnt1 = ImageEnhance.Contrast(ggClr1).enhance(random.randint(0,10))
    ggCnt2 = ImageEnhance.Contrast(ggClr2).enhance(random.randint(0,10))
    ggCnt3 = ImageEnhance.Contrast(ggClr3).enhance(random.randint(0,10))

    ggCnt1.putalpha(128)
    ggCnt2.putalpha(64)
    ggCnt3.putalpha(32)

    Offset1 = random.randint(0,2048)
    Offset2 = random.randint(0,2048)
    Offset3 = random.randint(0,2048)

    #gg1.show()
    #gg2.show()
    #gg3.show()

    ggOffs1 = ImageChops.offset(ggCnt1, 0,Offset1)
    ggOffs2 = ImageChops.offset(ggCnt2, 0,Offset2)
    ggOffs3 = ImageChops.offset(ggCnt3, 0,Offset3)

    finalImg = Image.new("RGBA", (4096,2048), (128,128,128))
    finalImg.paste(ggOffs1, (0,0), mask=ggOffs1)
    finalImg.paste(ggOffs2, (0,0), mask=ggOffs2)
    finalImg.paste(ggOffs3, (0,0), mask=ggOffs3)

    finalImg.show()

    finalNRM = ImageOps.grayscale(finalImg)
    finalNRM.putalpha(128)
    finalNRM.show()

    finalImg.save(filepath + "/Textures/PluginData/" + "GasGiantC" + ".png")
    finalNRM.save(filepath + "/Textures/PluginData/" + "GasGiantN" + ".png")

#generateGasGiantMaps()

def triangle(upper_bound):
    return int(random.triangular(0.0, float(upper_bound + 1) - sys.float_info.epsilon, 0.0))

def genRing():
    ring1 = Image.open(filepath + "/Presets/" + "Ring" + str(1) + ".png")
    ringOffs1 = ImageChops.offset(ring1, random.randint(0,1024),0)
    bands = ringOffs1.split()
    randomMult = random.randint(1,10)/10
    print(randomMult)
    adj_alpha = bands[3].point(lambda x: int(x * randomMult))
    ringAlph = Image.merge('RGBA', [*bands[:3], adj_alpha])
    ringAlph.save(filepath + "/Textures/PluginData/" + "RingTest" + str(1) + ".png")

genRing()

#print(triangle(100))