# General settings, will change a lot.

useMultithreading = True # Will use multithreading, this will drastically increase generator efficiency and thus result in faster generation, but may increase CPU usage.

deleteUnnecessarFolders = False # (DEPRECATED, DOES NOTHING!!) Enabled on default, will delete the "GenerateSystem" folder once it's done. This is so that people stop complaining that their game won't start.

convertTexturesToDDS = True # Will remove the requirement for ImageMagick and reduce generator time if false. Will also increase KSP loading time so setting to false is not recommended.

minPlanets = 3 # Minimum number of planets per star.
minMoons = 0 # Minimum number of moons per star.

fantasyNames = True # Generate a fantasy name for bodies. Will not affect internal names!

showConsole = True # Whether or not to show the console.

# Star shenanigans, override if you want a specific type of star to spawn.

binaryOverride = None # Will override whether or not stars ONLY generate as binaries.
# A value of "None" (no quotation marks) will let the generator choose.
# "True" will make every star a binary.
# "False" will make every star NOT a binary.

# These must either be "None" OR a number!

binaryTypeOverride = None # Will override
# "None" will be random.
# "True" will make every binary system distant. (Planets divided to orbit both stars seperately.)
# "False" will make every binary system near. (All planets orbit both stars.)

starTypeOverride = None # Will override the type of non-binary stars.

starTypeOverrideBinary1 = None # Will override the type of the first binary star.
starTypeOverrideBinary2 = None # Will override the type of the second binary star.

# Star type guide:
# A value between any of these will generate the corresponding star ONLY.
# 0 - 18: Red Giant
# 19 - 28: White Dwarf
# 29 - 39: Neutron Star
# 40 - 50: Brown Dwarf
# 51 - 55: Wolf Rayet
# 55 and over: Main Sequence
# "None" will result in a random star (value from 0 to 150)
# For example, "starTypeOverride = 42" will generate ONLY brown dwarf stars!!

# Generator settings. These settings will greatly affect the generator speed.
# These values MUST be whole numbers!

# Distance between both stars in meters, average radius of both stars is added to the distance. 
binaryMinSMA = 0
binaryMaxSMA = 1500000000
                      #100000000000
distantBinaryMinSMA = 95000000000
distantBinaryMaxSMA = 150000000000

# More star stuff...
minStarSize = 66160000 # minStarSize and maxStarSize is DEPRECATED!
maxStarSize = 2092800000 # 784800000 is default

minStarDistance = 100000000000000
maxStarDistance = 500000000000000

# Generator settings.
noiseOctaves = 5 # This one greatly affects generator time, higher octaves = more noise detail but also longer time to generate.
noiseFrequencyMin = 10
noiseFrequencyMax = 20
noiseLacunarity = 2.6 # This one doesn't have to be a whole number lol.
icecapDisplacement = 25 # Not recommended to change this value. Changes the amount of pixels that the icecaps are displaced relative to the heightmap.

# Color settings, in the off chance that you want every planet to be a certain color.
# B means black, which is the black, or "bottom" of the heightmap.
# M means middle, which is the middle point of the heightmap.
# W means white, which is the white, or "peak" of the heightmap.
# Some settings may be missing because those certain parameters are controlled by external conditions.

# Color settings for worlds with life.

# Black settings handled by plant color calculation.

LIFE_M_RedMin = 100
LIFE_M_GreenMin = 75
LIFE_M_BlueMin = 50
LIFE_M_RedMax = 175
LIFE_M_GreenMax = 100
LIFE_M_BlueMax = 55

LIFE_W_RedMin = 65
LIFE_W_GreenMin = 65
LIFE_W_BlueMin = 65
LIFE_W_RedMax = 100
LIFE_W_GreenMax = 100
LIFE_W_BlueMax = 100

# Color settings for worlds without life but with oceans
OCEAN_B_RedMin = 25
OCEAN_B_GreenMin = 25
OCEAN_B_BlueMin = 25
OCEAN_B_RedMax = 75
OCEAN_B_GreenMax = 25
OCEAN_B_BlueMax = 25

OCEAN_M_RedMin = 100
OCEAN_M_GreenMin = 75
OCEAN_M_BlueMin = 50
OCEAN_M_RedMax = 175
OCEAN_M_GreenMax = 100
OCEAN_M_BlueMax = 55

OCEAN_W_RedMin = 65
OCEAN_W_GreenMin = 65
OCEAN_W_BlueMin = 65
OCEAN_W_RedMax = 100
OCEAN_W_GreenMax = 100
OCEAN_W_BlueMax = 100

# Color settings for icy worlds.
ICY_B_RedMin = 100
ICY_B_GreenMin = 100
ICY_B_BlueMin = 100
ICY_B_RedMax = 125
ICY_B_GreenMax = 125
ICY_B_BlueMax = 200

ICY_M_RedMin = 100
ICY_M_GreenMin = 100
ICY_M_BlueMin = 100
ICY_M_RedMax = 125
ICY_M_GreenMax = 125
ICY_M_BlueMax = 200

ICY_W_RedMin = 25
ICY_W_GreenMin = 25
ICY_W_BlueMin = 25
ICY_W_RedMax = 125
ICY_W_GreenMax = 125
ICY_W_BlueMax = 200

# Color settings for everything else. Deserts, vacuum worlds, etc... NOT STARS!
OTHER_B_RedMin = 25
OTHER_B_GreenMin = 25
OTHER_B_BlueMin = 25
OTHER_B_RedMax = 75
OTHER_B_GreenMax = 75
OTHER_B_BlueMax = 75

# Middle color settings handled by outside influence.

OTHER_W_RedMin = 50
OTHER_W_GreenMin = 50
OTHER_W_BlueMin = 50
OTHER_W_RedMax = 200
OTHER_W_GreenMax = 200
OTHER_W_BlueMax = 200

print("Yup, no problems here.")
print("---------------------------------------------------------------")
#import colorsys
#clrHSL = colorsys.rgb_to_hsv(0.5,1,0.5)
#clrRGB = colorsys.hsv_to_rgb(clrHSL[0], (clrHSL[1]/2), clrHSL[2])
#print(clrRGB)
#print("babababba.lalalla".split("."))
#print(len("52200"))
#radius = 300000 / 1000
#radiusDiv = 600 / radius
#print(radiusDiv)
#print(str((50/radiusDiv)/radiusDiv))
#import random
#def generastePieceOfShit(shid):
#    fuckershithead = random.Random()
#    fuckershithead.seed(random.randint(0,194935))
#    bitchhead = fuckershithead.randint(0,1)
#    print(bitchhead)
#for i in range(100):
#    shid = random.randint(0,1)
#    generastePieceOfShit(shid)
#import numpy as np
#print(np.interp(1200, [700, 2000], [32, 255]))