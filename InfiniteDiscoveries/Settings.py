# General settings, will change a lot.

convertTexturesToDDS = True # Will remove the requirement for ImageMagick and reduce generator time if false. Will also increase KSP loading time so setting to false is not recommended.

minPlanets = 3 # Minimum number of planets per star.
minMoons = 0 # Minimum number of moons per planet.

# Generator settings. These settings will greatly affect the generator speed.
# These values MUST be whole numbers!

minStarSize = 66160000
maxStarSize = 784800000
minStarDistance = 10000000000000
maxStarDistance = 50000000000000
noiseOctaves = 10
noiseFrequencyMin = 10
noiseFrequencyMax = 20
noiseLacunarity = 2.0 # This one doesn't have to be a whole number lol.
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