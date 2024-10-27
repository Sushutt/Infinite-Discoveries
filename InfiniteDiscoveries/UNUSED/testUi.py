import random
import numpy as np
import os
import math

list1 = []

lat = -11.9500003918895
lon = 33.7400045176262

X = math.cos(lat)*math.cos(lon)
Y = math.sin(lat)
Z = math.cos(lat)*math.sin(lon)

print(str(X) + "," + str(Y) + "," + str(Z))

real = math.pi
for i in range(0,len(str(real)[:-1])):
    print(round(real, i))

gunbga = "h"
lobng = "a"
huh = [gunbga, lobng]
print(huh[0])

def test(guna):
    print(guna)
    wunga = "ooga"
    return wunga

guna = "a"

test2 = test(guna)
print(test2)

minVal = 1
maxVal = 100

print(1/(5.2*10**-116))

lam = 0.05 # set the lambda parameter for the exponential distribution

list = []
for i in range(0,100):
    # generate a random integer using an exponential distribution with lambda = 0.05
    num = int(np.random.exponential(scale=1/lam))

    # make sure the generated number is between 1 and 100
    num = max(1, min(100, num))

    #print(num)
    str1 = ""
    for i in range(0,int(num/10)):
        str1 = str1 + "#"
    str1 = str1 + " " + str(num/10)
    list.append(str1)

finalList = sorted(list)
for o in range(0,len(finalList)):
    print(finalList[o])