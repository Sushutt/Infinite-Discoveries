import random
ClrR = 0
ClrG = 0
ClrB = 0
starRadius = random.randint(26160000,1616000000)
print(starRadius)
Mult = 0.09
print(Mult)
if Mult < 0.12:
    ClrR = 255*Mult*8
    ClrG = 255*Mult*7
    ClrB = 255*Mult*6
else:
    ClrR = 255*Mult*1.01
    ClrG = 255*Mult*1.01
    ClrB = 255*Mult*1.02

print(str(round(ClrR)) + " " + str(round(ClrG)) + " " + str(round(ClrB)))
print(round(0.6823529411764706,3))