# Infinite-Discoveries
Infinite Discoveries aims to create fully functional star systems with as little human input as possible.

## How to install Infinite Discoveries:

1. Find a place to put it (anywhere works, except for the KSP directory.)

2. Move the "InfiniteDiscoveries" folder to the aforementioned place you found to put it in.

3. Install ImageMagick (optional, best if you can though) https://imagemagick.org/script/download.php
(ImageMagick is NOT a ksp mod, it is a standalone program! Install it like any other program.)

3.1 (The right version is "ImageMagick-7.1.1-15-Q16-HDRI-x64-dll.exe" which takes some time to scroll down to.)

4. Install Kopernicus into KSP.

## How to use:

1. Run the "InfiniteDiscoveries" shortcut inside the InfiniteDiscoveries folder, you can also make a shortcut to access it easily.

2. Set your target KSP GameData folder in the folder browser.

3. Adjust whatever settings you want.

4. Press the big "Start Generator" button.

5. Wait until the panel on the right says that the generator is finished.

6. Start KSP and enjoy!


## Okay, so you don't trust the exe. You want to use this with more control... How to install this THE HARD WAY!

### Make sure you have the following prerequisites:
1. Visual Studio Code
2. ImageMagick
3. Python 3.whatever

### Then install the following libraries via pip:
1. pip install pillow (https://pillow.readthedocs.io/en/stable/installation.html)
2. pip install wand (https://imagemagick.org/index.php)
3. pip install colour
4. pip install noise
5. pip install scipy

### Install the actual program:
1. Find the main branch on github, and click the green "Code" button, then click "Download ZIP."
2. Put the InfiniteDiscoveries folder in your KSP GameData as you normally would.
3. Open the .py file in the "GenerateSystem" folder via Visual Studio Code.
4. Run the file in Visual Studio, I'm not really sure why it doesn't run outside it but that's how it works.
5. Use the program as usual.
