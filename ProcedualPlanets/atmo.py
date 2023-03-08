import os

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

testAtmo = open(filepath + "/Configs/" + "TestAtmo" + ".cfg","x")

atmoHeight = 70000
kPa = 100

testAtmo.write(
    "            pressureCurve\n"
    "            {\n"
    "                key = " + str(round(0)) + " " +                 str(round(kPa))        + " -9.40053885714286E-03 -9.40053885714286E-03\n"
    "                key = " + str(round(atmoHeight/20.0)) + " " + str(round(kPa/1.289))  + " -9.06132071428572E-03 -9.06132071428572E-03\n"
    "                key = " + str(round(atmoHeight/10.0)) + " " + str(round(kPa/1.762))  + " -7.66193321571429E-03 -7.66193321571429E-03\n"
    "                key = " + str(round(atmoHeight/6.66)) + " " + str(round(kPa/2.440))  + " -5.75651121285714E-03 -5.75651121285714E-03\n"
    "                key = " + str(round(atmoHeight/5.00)) + " " + str(round(kPa/3.418))  + " -4.16994392857143E-03 -4.16994392857143E-03\n"
    "                key = " + str(round(atmoHeight/4.00)) + " " + str(round(kPa/4.746))  + " -2.90616120814286E-03 -2.90616100142857E-03\n"
    "                key = " + str(round(atmoHeight/3.33)) + " " + str(round(kPa/6.502))  + " -2.14383385714286E-03 -2.14383385714286E-03\n"
    "                key = " + str(round(atmoHeight/2.85)) + " " + str(round(kPa/9.229))  + " -1.57375037842857E-03 -1.57375037842857E-03\n"
    "                key = " + str(round(atmoHeight/2.50)) + " " + str(round(kPa/12.71))  + " -1.03374362157143E-03 -1.03374362157143E-03\n"
    "                key = " + str(round(atmoHeight/2.22)) + " " + str(round(kPa/16.95))  + " -7.27255171714286E-04 -7.27255171714286E-04\n"
    "                key = " + str(round(atmoHeight/2.00)) + " " + str(round(kPa/22.75))  + " -5.39731265282876E-04 -5.39731625876128E-04\n"
    "                key = " + str(round(atmoHeight/1.81)) + " " + str(round(kPa/30.09))  + " -4.01197907285714E-04 -4.01197907285714E-04\n"
    "                key = " + str(round(atmoHeight/1.66)) + " " + str(round(kPa/40.34))  + " -3.32120814571429E-04 -3.32120814571429E-04\n"
    "                key = " + str(round(atmoHeight/1.53)) + " " + str(round(kPa/57.58))  + " -2.57703878428571E-04 -2.57703878428571E-04\n"
    "                key = " + str(round(atmoHeight/1.42)) + " " + str(round(kPa/80.11))  + " -1.74466857142857E-04 -1.74466857142857E-04\n"
    "                key = " + str(round(atmoHeight/1.33)) + " " + str(round(kPa/110.6))  + " -1.36190255014286E-04 -1.36190255014286E-04\n"
    "                key = " + str(round(atmoHeight/1.25)) + " " + str(round(kPa/167.0))  + " -1.16655755014286E-04 -1.16655755014286E-04\n"
    "                key = " + str(round(atmoHeight/1.17)) + " " + str(round(kPa/288.0))  + " -9.19878571428571E-05 -9.19878571428571E-05\n"
    "                key = " + str(round(atmoHeight/1.11)) + " " + str(round(kPa/629.0))  + " -6.40814285714286E-05 -6.40814285714286E-05\n"
    "                key = " + str(round(atmoHeight/1.05)) + " " + str(round(kPa/2451))   + " -3.32465407285714E-05 -3.32465407285714E-05\n"
    "                key = " + str(round(atmoHeight/1.00)) + " " + str(round(0))          + " -1.70883816414286E-05 -1.70883816414286E-05\n"
    "            }\n"
)