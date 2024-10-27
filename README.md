# Infinite-Discoveries
Infinite Discoveries is a randomized star system generator for KSP.

## How to install Infinite Discoveries (compiled version):

1. Find a place to put it (anywhere works, except for the KSP directory.)

2. Move the "InfiniteDiscoveries" folder to the aforementioned place you found to put it in.

3. Install ImageMagick (optional, best if you can though) https://imagemagick.org/script/download.php
(ImageMagick is NOT a ksp mod, it is a standalone program! Install it like any other program.)

4. Install Kopernicus to KSP.

## How to use:

1. Run the "InfiniteDiscoveries" shortcut inside the InfiniteDiscoveries folder, you can also make a shortcut to access it easily.

2. Set your target KSP GameData folder in the folder browser.

3. Adjust whatever settings you want.

4. Press the big "Start Generator" button.

5. Wait until the panel on the right says that the generator is finished.

6. Start KSP and enjoy!


## Running Infinite Discoveries from Source (OUTDATED, meant for commits prior to 1.0.0):

### Make sure you have the following prerequisites:
1. Visual Studio Code
2. ImageMagick
3. Python 3.whatever

### Then install the following libraries:
1. pip install pillow (https://pillow.readthedocs.io/en/stable/installation.html)
2. pip install wand (https://imagemagick.org/index.php)
3. pip install colour
4. pip install noise
5. pip install scipy

### Running the program:
1. Find the main branch on github, and click the green "Code" button, then click "Download ZIP."
2. Put the InfiniteDiscoveries folder in your KSP GameData as you normally would.
3. Open the .py file in the "GenerateSystem" folder via Visual Studio Code.
4. Run the file in Visual Studio, I'm not really sure why it doesn't run outside it but that's how it works.
5. Use the program as usual.

# For people wanting to contribute (only applies to version 1.0.0 and over):

Download the source code, add whatever change you need, and push to a new branch. Make sure to thouroughly explain your changes and why you deem them necessary.

General guidelines / things to note:

1. Do not make changes to files in the "UNUSED" folder.
2. The "GenerateSystem" file is obsolete. All functionality is split in to its own file and/or class.
3. "Infinite_DeflateStars" and "Infinite_GalaxyMode" are both obsolete and are handled in the main Infinite Discoveries folder.
