initTemp = 287

starLum = 1360
starLumMult = starLum/1360

sma = 13599840256
smaMult = 13599840256/sma

finalTemp = round(initTemp*starLumMult*smaMult)
print(finalTemp)