import os
filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

textureDir = filepath + "/Textures/PluginData"
configDir = filepath + "/Configs"
cacheDir = filepath + "/Cache"
visual_ScattererDir = filepath + "/Visuals/Scatterer"
visual_EveConfigDir = filepath + "/Visuals/Eve/Configs"
visual_ParallaxDir = filepath + "/Visuals/Parallax/Configs"
visual_CloudMapDir = filepath + "/Textures/Clouds"

allDirs = [textureDir, configDir, cacheDir, visual_ScattererDir, visual_EveConfigDir, visual_ParallaxDir, visual_CloudMapDir]

for e in range(0,len(allDirs)):
    currentDir = allDirs[e]
    for f in os.listdir(currentDir):
        if "_noDelete" in os.path.join(currentDir, f):
            print("No.")
        else:
            print(os.path.join(currentDir, f))

input("Confirm? ")

for e in range(0,len(allDirs)):
    currentDir = allDirs[e]
    for f in os.listdir(currentDir):
        if "_noDelete" in os.path.join(currentDir, f):
            print("Directory deleted, empty file ignored.")
        else:
            os.remove(os.path.join(currentDir, f))