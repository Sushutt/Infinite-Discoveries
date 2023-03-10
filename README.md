# Infinite-Discoveries
Kerbal Possibilites aims to create fully functional star systems with as little human input as possible.

How to install:
Simply put the folder named "ProcedualPlanets" in the zip file provided in the releases page into your KSP GameData folder.

How to use:
Make sure you have ImageMagick installed, as this mod requires it to convert PNG textures to DDS.
Run the shortcut inside the "ProcedualPlanets" folder, if windows complains about it, just let it run.
Input the numbers it asks you to input (the amount of stars to generate, max amount of planets and moons...)
Let it run!
Once you're done, start KSP! If you installed it correctly, it should work perfectly fine!


Okay, so you don't trust the exe. You want to use this with more control...
How to install this THE HARD WAY!

Make sure you have the following prerequisites:
Visual Studio Code
ImageMagick
Python 3.whatever

Then install the following libraries via pip:
pip install pillow (https://pillow.readthedocs.io/en/stable/installation.html)
pip install wand (unsure if this is actually necessary)
pip install colour

Install the actual program:
Find the main branch on github, and click the green "Code" button, then click "Download ZIP."
Put the ProcedualPlanets folder in your KSP GameData as you normally would.
Open the .py file in the "GenerateSystem" folder via Visual Studio Code.
Run the file in Visual Studio, I'm not really sure why it doesn't run outside it but that's how it works.
Use the program as usual.
