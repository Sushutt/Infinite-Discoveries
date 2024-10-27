import random
import Settings
import numpy as np
from colour import Color
import string

red = Color("#eb0000")
colors1 = list(red.range_to(Color("#f7e297"),10))
yellow = Color("#f7e297")
colors2 = list(yellow.range_to(Color("#f7f9fa"),25))
white = Color("#f7f9fa")
colors3 = list(white.range_to(Color("#0051ff"),65))
finalColors = colors1 + colors2 + colors3
alphabet = list(string.ascii_uppercase)

print(random.randint(1,0))

print(finalColors[1+2])

# mainSeqCount = 0
# redGiantCount = 0
# whiteDwarfCount = 0
# neutronCount = 0
 
# def generateStar(mainSeqCount, redGiantCount, whiteDwarfCount, neutronCount):

mean = 66160000
std_dev = 784800000

print(int(np.random.normal(mean, std_dev)))

def generateStar(AmountOfPlanetsToGenerate, systemName, parentBarycenter=None, binarySMA=None, binaryP=None, binaryRad=None, maaoD=None, baryOrder=None):
    if random.randint(1,7) == 1:
        redGiant = True
        redGiantCount = redGiantCount + 1
    elif random.randint(1,8) == 1:
        whiteDwarf = True
        whiteDwarfCount = whiteDwarfCount + 1
    elif random.randint(1,10) == 1:
        neutron = True
        neutronCount = neutronCount + 1
    else:
        mainSeq = True
        mainSeqCount = mainSeqCount + 1
        
    if parentBarycenter == None:
        starName = str(alphabet[random.randint(0,len(alphabet)-1)]) + str(alphabet[random.randint(0,len(alphabet)-1)]) + "-" + str(random.randint(0,99999))
    else:
        starName = systemName + "-" + str(baryOrder)

    try:
        if mainSeq:
            print("Main sequence")
            mean = 66160000
            std_dev = 784800000
            starRadius = int(np.random.normal(mean, std_dev))
            starMass = starRadius * 6.7146251e+19

            Mult = starRadius*10 / 261600000
            multRound = round(Mult)
            starColor = Color.get_rgb(finalColors[multRound-1])
            RGBfinal = str(starColor)[1:][:-1]
            Lum = 1360 * starRadius / 261600000
    except UnboundLocalError:
        pass
    try:
        if redGiant:
            print("Red Giant")
    except UnboundLocalError:
        pass
    try:
        if whiteDwarf:
            print("White Dwarf")
    except UnboundLocalError:
        pass
    try:
        if neutron:
            print("Neutron Star")
    except UnboundLocalError:
        pass

    # Not type-specific settings.
    starDist = random.randint(Settings.minStarDistance,Settings.maxStarDistance)
    starDistG = random.randint(Settings.minStarDistance/5,Settings.maxStarDistance)
    
    return mainSeqCount, redGiantCount, whiteDwarfCount, neutronCount

amountOfStars = 25

for i in range(0,amountOfStars):
    mainSeqCount, redGiantCount, whiteDwarfCount, neutronCount = generateStar(mainSeqCount, redGiantCount, whiteDwarfCount, neutronCount)

print(mainSeqCount)
print(redGiantCount)
print(whiteDwarfCount)
print(neutronCount)

print("Main Sequence: " + str(mainSeqCount/amountOfStars*100)+"%")
print("Red Giant: " + str(redGiantCount/amountOfStars*100)+"%")
print("White Dwarf: " + str(whiteDwarfCount/amountOfStars*100)+"%")
print("Neutron Star: " + str(neutronCount/amountOfStars*100)+"%")