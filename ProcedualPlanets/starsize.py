import random
import math

list1 = []
min = 26160000
max = 2616000000


for i in range(0,100):
    starRadius = round(abs(random.random() - random.random()) * (10 + max - min) + min)
    #print(starRadius[0]*random.randint(50,1000))
    #print((starRadius[0]*175)/261600000)
    randomMult = 1
    finalStr = ""
    for i in range(0,round((starRadius*randomMult/261600000))):
        finalStr = finalStr + "-"
    finalfinalStr = finalStr + "   " + str(round(starRadius*randomMult/261600000))
    list1.append(finalfinalStr)
finalList = sorted(list1)
for o in range(0,len(finalList)):
    print(finalList[o])