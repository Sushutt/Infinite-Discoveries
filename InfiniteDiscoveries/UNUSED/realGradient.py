from colour import Color

red = Color("#eb0000")
colors1 = list(red.range_to(Color("#f7e297"),8))
yellow = Color("#f7e297")
colors2 = list(yellow.range_to(Color("#f7f9fa"),14))
white = Color("#f7f9fa")
colors3 = list(white.range_to(Color("#0051ff"),85))
finalColors = colors1 + colors2 + colors3

starRadius = 161600000

Mult = starRadius*10 / 261600000
multRound = round(Mult)
starColor = Color.get_rgb(finalColors[multRound-1])
RGBfinal = str(starColor)[1:][:-1]
Lum = 1360 * starRadius / 261600000

theNum = multRound

print(finalColors[multRound-1])
print(starColor)

if theNum > 0 and theNum <= 3:
    color = "Red"
elif theNum > 3 and theNum <= 8:
    color = "Orange"
elif theNum > 8 and theNum <= 11:
    color = "Yellow"
elif theNum > 11 and theNum <= 30:
    color = "White"
elif theNum > 30 and theNum <= 100:
    color = "Blue"

print(color)

#num = random.choices(range(261,2616000), weights=range(261,2616000))
##print(num[0]*200)
#print(finalColors)
#atmClrR = random.randint(0,150)
#atmClrG = random.randint(0,150)
#atmClrB = random.randint(0,150)
#sctrClrR = (atmClrR*-1)+255
#sctrClrG = (atmClrG*-1)+255
#sctrClrB = (atmClrB*-1)+255
#print(str(atmClrR) + " " + str(atmClrG) + " " + str(atmClrB))
#print(str(sctrClrR) + " " + str(sctrClrG) + " " + str(sctrClrB))
#starRadius = random.randint(2616000,1616000000)
#print(starRadius)
#Mult = starRadius*10 / 261600000
#print(Mult)
#multRound = round(Mult)
#print(multRound)
#print(finalColors[multRound])
#print(Color.get_rgb(finalColors[multRound]))
# colors is now a list of length 10
# Containing: 
# [<Color red>, <Color #f13600>, <Color #e36500>, <Color #d58e00>, <Color #c7b000>, <Color #a4b800>, <Color #72aa00>, <Color #459c00>, <Color #208e00>, <Color green>]