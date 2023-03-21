import time

startTime = time.time()

initTemp = 287

starLum = 1360
starLumMult = starLum/1360

sma = 13599840256
smaMult = 13599840256/sma

finalTemp = round(initTemp*starLumMult*smaMult)
print(finalTemp)

time.sleep(2)

endTime = time.time()
#elapsed = end - start
elapsedTime = endTime - startTime
if elapsedTime > 60:
    print(round(elapsedTime/60,2))
elif elapsedTime < 60:
    print(round(elapsedTime,2))