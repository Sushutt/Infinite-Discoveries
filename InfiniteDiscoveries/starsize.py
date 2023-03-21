import random
import math

list1 = []
min = 56160000
max = 1316000000


for i in range(0,100):
    starRadius = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
    print(starRadius)
    #print(starRadius[0]*random.randint(50,1000))
    #print((starRadius[0]*175)/261600000)
    randomMult = 1
    finalStr = ""
    for i in range(0,round((starRadius/261600000))):
        finalStr = finalStr + "-"
    finalfinalStr = finalStr + "   " + str(starRadius)
    list1.append(finalfinalStr)
finalList = sorted(list1)
for o in range(0,len(finalList)):
    print(finalList[o])