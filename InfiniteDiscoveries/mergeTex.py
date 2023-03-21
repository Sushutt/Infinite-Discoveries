from PIL import Image, ImageEnhance, ImageChops, ImageOps, ImageFilter
import random
import os
import time
from colour import Color
from wand import image as wImage
filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

vacuum = False
ocean = True
chosenImgs = []

def GeneratePlanetMaps():
    for i in range(0,3):
        randomNum = random.randint(1,6)
        if vacuum == True:
            chosenImgs.append("Vacuum" + str(randomNum))
        else:
            chosenImgs.append("Atmo" + str(randomNum))


    print(chosenImgs)

    srcBase = Image.open(filepath + "/Presets/GeneralNoise1.png")

    src1 = Image.open(filepath + "/Presets/" + chosenImgs[0] + ".png")
    src2 = Image.open(filepath + "/Presets/" + chosenImgs[1] + ".png")
    src3 = Image.open(filepath + "/Presets/" + chosenImgs[2] + ".png")

    #src1.show()
    #src2.show()
    #src3.show()

    print("Generating height map...")
    srcBase.putalpha(64)
    src1.putalpha(128)
    src2.putalpha(128)
    src3.putalpha(64)

    baseContr = ImageEnhance.Contrast(srcBase)
    baseFinl = baseContr.enhance(1)

    OffsetB = random.randint(0,4096)
    Offset1 = random.randint(0,4096)
    Offset2 = random.randint(0,4096)
    Offset3 = random.randint(0,4096)

    finalImg = Image.new("RGBA", (4096,2048), (128,128,128))
    baseOff = ImageChops.offset(baseFinl, OffsetB,0)
    imOff1 = ImageChops.offset(src1, Offset1,0)
    imOff2 = ImageChops.offset(src2, Offset2,0)
    imOff3 = ImageChops.offset(src3, Offset3,0)
    finalImg.paste(imOff1, (0,0), mask=imOff1)
    finalImg.paste(imOff2, (0,0), mask=imOff2)
    finalImg.paste(imOff3, (0,0), mask=imOff3)
    finalImg.paste(baseOff, (0,0), mask=baseOff)
    contraster = ImageEnhance.Contrast(finalImg)
    contrasted = contraster.enhance(2)
    brightener = ImageEnhance.Brightness(contrasted)
    brightened = brightener.enhance(1.5)
    finalHeight = brightened

    #finalHeight.show()

    print("Height map generated!")
    #time.sleep(1)
    print("Generating normals...")
    srcNRMBase = Image.open(filepath + "/Presets/GeneralNoise1NRM.png")

    srcNRM1 = Image.open(filepath + "/Presets/" + chosenImgs[0] + "NRM" + ".png")
    srcNRM2 = Image.open(filepath + "/Presets/" + chosenImgs[1] + "NRM" + ".png")
    srcNRM3 = Image.open(filepath + "/Presets/" + chosenImgs[2] + "NRM" + ".png")


    srcNRMBase.putalpha(64)
    srcNRM1.putalpha(128)
    srcNRM2.putalpha(128)
    srcNRM3.putalpha(64)

    finalImgNRM = Image.new("RGBA", (4096,2048), (255,255,255))
    baseNrmOff = ImageChops.offset(srcNRMBase, OffsetB,0)
    nrOff1 = ImageChops.offset(srcNRM1, Offset1,0)
    nrOff2 = ImageChops.offset(srcNRM2, Offset2,0)
    nrOff3 = ImageChops.offset(srcNRM3, Offset3,0)
    finalImgNRM.paste(nrOff1, (0,0), mask=nrOff1)
    finalImgNRM.paste(nrOff2, (0,0), mask=nrOff2)
    finalImgNRM.paste(nrOff3, (0,0), mask=nrOff3)
    finalImgNRM.paste(baseNrmOff, (0,0), mask=baseNrmOff)

    if ocean == True:
        ocMap = Image.open(filepath + "/Presets/" + "Ocean1" + ".png")
        ocNRM = Image.open(filepath + "/Presets/" + "Ocean1NRM" + ".png")

        Offs = random.randint(0,4096)

        ocMapOffs = ImageChops.offset(ocMap, Offs,0)
        ocMapOffs2 = ocMapOffs.transpose(Image.FLIP_TOP_BOTTOM)

        ocNRMOffs = ImageChops.offset(ocNRM, Offs,0)
        ocNRMOffs2 = ocNRMOffs.transpose(Image.FLIP_TOP_BOTTOM)

        #finalImgNRM.paste(ocNRMOffs2, (0,0), mask=ocNRMOffs2)
        #finalHeight.paste(ocMapOffs2, (0,0), mask=ocMapOffs2)

    
    #nrmFINAL = ImageOps.grayscale(nrmBrted)
    #nrmFINAL.show()
    print("Normal map generated!")

    print("Generating colors...")
    terrainR = random.randint(100,255)
    terrainG = random.randint(100,255)
    terrainB = random.randint(100,255)

    gray = ImageOps.grayscale(finalHeight)

    #clrCnt1 = ImageEnhance.Contrast(ImageEnhance.Brightness(imOff1).enhance(1)).enhance(5)
    #clrCnt2 = ImageEnhance.Contrast(ImageEnhance.Brightness(imOff2).enhance(1)).enhance(5)
    #clrCnt3 = ImageEnhance.Contrast(ImageEnhance.Brightness(imOff3).enhance(1)).enhance(5)
    #
    #colorFinal = Image.new("RGBA", (4096,2048), (255,255,255))
    #clrL1 = ImageOps.colorize(ImageOps.grayscale(clrCnt1), (128,128,128), (0,0,255)).convert("RGBA")
    #clrL2 = ImageOps.colorize(ImageOps.grayscale(clrCnt2), (128,128,128), (0,255,0)).convert("RGBA")
    #clrL3 = ImageOps.colorize(ImageOps.grayscale(clrCnt3), (128,128,128), (terrainR,terrainG,terrainB)).convert("RGBA")
    #colorFinal.paste(clrL1, (0,0), mask=clrL1)
    #colorFinal.paste(clrL2, (0,0), mask=clrL2)
    #colorFinal.paste(clrL3, (0,0), mask=clrL3)
    heightColor = ImageEnhance.Contrast(ImageEnhance.Brightness(finalHeight).enhance(0.5)).enhance(2)
    colorMap = ImageOps.colorize(ImageOps.grayscale(heightColor), ((random.randint(0,32)),(random.randint(0,32)),(random.randint(0,32))), (terrainR,terrainG,terrainB))

    if ocean == True:
        r,g,b,a = ocMapOffs2.split()
        ocMapInv = ImageOps.invert(ocMapOffs2.convert("RGB"))
        ocMapClr = ImageOps.colorize(ImageOps.grayscale(ocMapInv), (25,25,25), ((random.randint(10,50)),(random.randint(10,50)),(random.randint(10,50))))
        ocMapClr.putalpha(a)
        #colorMap.paste(ocMapClr, (0,0), mask=ocMapClr)
        colorMap.putalpha(a)
        
        brightFac = float(random.randint(100,200)/100)

        print(brightFac)

        brghtHeight = ImageEnhance.Brightness(finalHeight).enhance(brightFac)
        contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
        posted = ImageOps.posterize(contrHeight.convert("RGB"),2)
        brightFinal = ImageEnhance.Brightness(posted).enhance(100)
        oceanRGBA = brightFinal.convert("RGBA")
        oceanInv = ImageOps.invert(brightFinal).convert("RGBA")
        ocInvL = oceanInv.convert("L")
        oceanRGBA.putalpha(ocInvL)
        oceanBlurA = oceanInv.filter(ImageFilter.GaussianBlur(1)).convert("L")

        heightOcean = Image.new("RGBA", (4096,2048), (0,0,0))
        heightOcean.putalpha(oceanBlurA)
        finalHeight.paste(heightOcean, (0,0), mask=heightOcean)

        normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
        normalOcean.putalpha(ocInvL)
        finalImgNRM.paste(normalOcean, (0,0), mask=normalOcean)


        beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
        beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
        beachColor.putalpha(beachMask)
        colorMap.paste(beachColor, (0,0), mask=beachColor)
        colorOcean = Image.new("RGBA", (4096,2048), ((random.randint(50,100)),(random.randint(50,100)),(random.randint(50,100))))
        colorOcean.putalpha(ocInvL)
        colorMap.paste(colorOcean, (0,0), mask=colorOcean)
        colorMap.putalpha(ocInvL)

    nrmContr = ImageEnhance.Contrast(finalImgNRM)
    nrmContred = nrmContr.enhance(1)
    nrmBrt = ImageEnhance.Contrast(nrmContred)
    nrmBrted = nrmBrt.enhance(1)

    #colorMap.show()

    finalHeight.save(filepath + "/Textures/PluginData/" + "TestHeight.png")
    nR,nG,nB,nA = nrmBrted.convert("RGBA").split()
    nrmBrted.putalpha(nR)
    nrmBrted.save(filepath + "/Textures/PluginData/" + "TestNRM.png")
    #nrmConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + "TestNRM.png")
    #nrmConv.options['dds:mipmaps'] = '0'
    #nrmConv.compression = 'dxt5'
    #nrmConv.save(filename= filepath + "/Textures/PluginData/" + "TestNRM.dds")
    #os.remove(filepath + "/Textures/PluginData/" + "TestNRM.png")
    colorMap.save(filepath + "/Textures/PluginData/" + "TestColor.png")
    print("Colors generated!")
GeneratePlanetMaps()