# Infinite-Discoveries
Infinite Discoveries aims to create fully functional star systems with as little human input as possible.

## How to install:
Simply put the folder named "ProcedualPlanets" in the zip file provided in the releases page into your KSP GameData folder.

## How to use:
1. Make sure you have ImageMagick (https://imagemagick.org/index.php) installed, as this mod requires it to convert PNG textures to DDS.
2. Run the shortcut inside the "ProcedualPlanets" folder, if windows complains about it, just let it run.
3. Input the numbers it asks you to input (the amount of stars to generate, max amount of planets and moons...)
3. Let it run!
4. Once the planets generate, you HAVE TO delete the "GenerateSystem" folder due to the game freaking out over DLLs inside it.
5. Once you're done, start KSP! If you installed it correctly, it should work perfectly fine!


## Okay, so you don't trust the exe. You want to use this with more control... How to install this THE HARD WAY!

### Make sure you have the following prerequisites:
1. Visual Studio Code
2. ImageMagick
3. Python 3.whatever

### Then install the following libraries via pip:
1. pip install pillow (https://pillow.readthedocs.io/en/stable/installation.html)
2. pip install wand (https://imagemagick.org/index.php)
3. pip install colour

### Install the actual program:
1. Find the main branch on github, and click the green "Code" button, then click "Download ZIP."
2. Put the ProcedualPlanets folder in your KSP GameData as you normally would.
3. Open the .py file in the "GenerateSystem" folder via Visual Studio Code.
4. Run the file in Visual Studio, I'm not really sure why it doesn't run outside it but that's how it works.
5. Use the program as usual.
