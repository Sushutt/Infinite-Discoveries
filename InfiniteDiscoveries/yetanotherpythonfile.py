from colour import Color
import os

starRadius = 214512000

black = Color("#000000")
Pcolors1 = list(black.range_to(Color("#700000"),5))
red = Color("#700000")
Pcolors2 = list(red.range_to(Color("#9e008c"),90))
pink = Color("#9e008c")
Pcolors3 = list(pink.range_to(Color("#fcf2fa"),5))
PfinalColors = Pcolors1 + Pcolors2 + Pcolors3
PMult = starRadius*30 / 261600000
if PMult > len(PfinalColors):
    PMult = len(PfinalColors)
PmultRound = round(PMult)
plantColor = Color.get_rgb(PfinalColors[PmultRound-1])
PmultRound = round(PMult)
print(PmultRound)
PstarColor = Color.get_rgb(PfinalColors[PmultRound-1])
PRGBfinal = str(PstarColor)[1:][:-1]
print(PfinalColors[PmultRound-1])
print(PRGBfinal)
print(PstarColor[1])