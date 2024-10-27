#"          			key = " + str((1200000000000*(brightnessThing / 261600000))) + " " + str((brightnessThing / 261600000)/1.5) + " -1.8E-12 -1.8E-12\n"
#"         			key = " + str((1800000000*(brightnessThing / 261600000))) + " " + str((brightnessThing / 261600000)/1.5) + " -1.2E-08 -1.2E-08\n"
# ^ Old middle star intensity key, if ever needed lmfao

import logging
import traceback
import os
filepath1 = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
filepath = filepath1.replace("/GenerateSystem", "")
#logging.basicConfig(filename=filepath +'/InfiniteDiscoveries.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
#logger=logging.getLogger(__name__)

try:
    import multiprocessing
    import threading
    currentProcess = threading.current_thread()
    allThreads = []
    allActions = []
    mainThreadFinished = False
    allActionArrayUpdated = False
    everythingEnded = False
    print(currentProcess.name)

    amountOfThingsToDo = 0
    amountOfThingsDone = 0

    if currentProcess.name == "MainThread":
        print(
            "■■■■■■■■■■■■■  ■■        ■■  ■■■■■■■■  ■■■■■■■■■■■■■  ■■        ■■  ■■■■■■■■■■■■■  ■■■■■■■■■■■■■  ■■■■■■■■■\n"
            "     ■■        ■■■■      ■■  ■■             ■■        ■■■■      ■■       ■■             ■■        ■      \n"
            "     ■■        ■■  ■■    ■■  ■■■■■■         ■■        ■■  ■■    ■■       ■■             ■■        ■■■■■  \n"
            "     ■■        ■■    ■■  ■■  ■■             ■■        ■■    ■■  ■■       ■■             ■■        ■      \n"
            "     ■■        ■■      ■■■■  ■■             ■■        ■■      ■■■■       ■■             ■■        ■      \n"
            "■■■■■■■■■■■■■  ■■        ■■  ■■        ■■■■■■■■■■■■■  ■■        ■■  ■■■■■■■■■■■■■       ■■        ■■■■■■■■■\n"
        )
        
        print(
            "■■■     ■■■■■     ■■■■       ■■■■       ■■       ■     ■      ■■■■■     ■■■■■    ■■■■■    ■■■■■     ■■■■\n"
            "■  ■      ■      ■          ■          ■  ■       ■   ■       ■         ■   ■      ■      ■        ■\n"
            "■  ■      ■       ■■■       ■          ■  ■       ■   ■       ■■■       ■■■        ■      ■■■       ■■■■\n"
            "■  ■      ■          ■      ■          ■  ■        ■ ■        ■         ■ ■        ■      ■             ■\n"
            "■■■     ■■■■■    ■■■■        ■■■■       ■■          ■         ■■■■■     ■  ■■    ■■■■■    ■■■■■     ■■■■\n"
        )
        
        print("---------------------------------------------------------------------------------------------------------")
        queue = []
    import random
    import string
    from PIL import Image, ImageEnhance, ImageChops, ImageOps, ImageFilter
    from colour import Color
    import sys
    import time
    import math
    import numpy as np
    from scipy.signal import convolve2d
    import noise
    import sys
    import shutil
    import subprocess
    #from flask import Flask, render_template
    import PySimpleGUI as sg
    import textwrap
    #import queue
    #app = Flask(__name__)
    import importlib
    import colorsys
    import matplotlib.pyplot as plt
    from matplotlib.colors import to_hex

    targetPath = ""

    def build_transition_table(tokens):
        transition_table = {}
        for i in range(len(tokens) - 1):
            current_char = tokens[i]
            next_char = tokens[i + 1]
            if current_char not in transition_table:
                transition_table[current_char] = []
            transition_table[current_char].append(next_char)
        return transition_table

    starNameCorpus = "Sun Galaxy Nebula Constellation Supernova Comet Meteor Astronomy Celestial Stellar Twinkle Cosmic Interstellar Astronomer Black Gravity Solar Space Meteorite Nebular Satellite Planetarium Radiant Hubble Luminous"
    starNameTokens = list(starNameCorpus)
    starTransisionTable = build_transition_table(starNameTokens)

    vacuumNameCorpus = "Earth Mercury Venus Mars Terrestrial Rocky Crust Mantle Core Atmosphere Geology Tectonics Volcanism Erosion Plateaus Mountains Canyons Valleys Deserts Plains"
    vacuumNameTokens = list(vacuumNameCorpus)
    vacuumTransisionTable = build_transition_table(vacuumNameTokens)

    oceanicNameCorpus = "Abyssal Tidal Submersible Aquatic Hydrothermal Coral Mariner Nautical Seafloor Plankton Tsunami Neptune Voyager Liquid Maritime Seafaring Atlantis Marine Abyss Voyager"
    oceanicNameTokens = list(oceanicNameCorpus)
    oceanicTransisionTable = build_transition_table(oceanicNameTokens)

    gaseousNameCorpus = "Cumulus Stratosphere Vapor Cirrus Nebula Condensation Haze Atmosphere Evaporation Methane Ozone Aerosol Fog Ammonia Carbon Dioxide Nitrogen Helium Vaporization Fogbank"
    gaseousNameTokens = list(gaseousNameCorpus)
    gaseousTransisionTable = build_transition_table(gaseousNameTokens)

    lifeNameCorpus = "Organism Evolution Biology Planet Respiration Reproduction Diversity Ecosystem Genetics Metabolism Microbes Adaptation Ecology Species Sustainability Biotechnology Biodiversity Survival Physiology Genetics"
    lifeNameTokens = list(lifeNameCorpus)
    lifeTransisionTable = build_transition_table(lifeNameTokens)

    rockyNameCorpus = "Barren Desolate Airless Vacant Lifeless Sterile Vacuum Harsh Inhospitable Rocky Surface Barren Wasteland No Atmosphere Rugged Desolation Uninhabitable"
    rockyNameTokens = list(rockyNameCorpus)
    rockyTransisionTable = build_transition_table(rockyNameTokens)

    lavaNameCorpus = "Magma Molten Flowing Volcanic Eruption Lava Lake Pyroclastic Viscosity Hot Molten Rock Igneous Crater Obsidian Glowing Vents Geological Ejecta Eruption Incandescent Lava Tube Pahoehoe Scoria"
    lavaNameTokens = list(lavaNameCorpus)
    lavaTransisionTable = build_transition_table(lavaNameTokens)

    icyNameCorpus = "Cryosphere Glacial Permafrost Frozen Tundra Ice Cap Frigid Glaciology Polar Icicle Frosty Snowy Frozen Wasteland Cryovolcano Hailstorm Blizzard Hibernation Subzero Crystalline Icy Surface Icebergs"
    icyNameTokens = list(icyNameCorpus)
    icyTransisionTable = build_transition_table(icyNameTokens)
    # Step 4: Generate words
    def generateName2(transition_table, word_length, seed):
        nameRNG = random.Random()
        nameRNG.seed(seed)
        current_char = ' '  # Start with a space character
        word = ""
        for _ in range(word_length):
            if current_char in transition_table:
                next_char = nameRNG.choice(transition_table[current_char])
                word += next_char
                current_char = next_char
            else:
                break
        return word

    # Variables lamo
    templates = ["Dres", "Duna", "Laythe", "Mun", "Jool"] # Laythe and Mun are unused lmao lol oops.
    planetsGenerated = 0
    alphabet = list(string.ascii_uppercase)

    # Star Colors
    cmap = plt.get_cmap('coolwarm')  # 'coolwarm' is a colormap that goes from red to blue
    gradient = np.linspace(0, 1, 100)
    colors = [to_hex(cmap(x)) for x in gradient]
    colorsReversed = list(reversed(colors))
    print(filepath)

    black = Color("#000000")
    lavaRed = Color("#eb2700")
    lavaColors1 = list(black.range_to(Color("#eb2700"),7))
    lavaColors2 = list(lavaRed.range_to(Color("#ebac00"),10))
    lavaSpectrum = lavaColors1 + lavaColors2

    sys.path.insert(0, filepath)
    import Settings # Ignore the warning, it still works.

    if Settings.convertTexturesToDDS == True:
        try:
            from wand import image as wImage
            canConvertToDDS = True
        except:
            print("ImageMagick is not installed, install it from: https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows")
            canConvertToDDS = False
    else:
        canConvertToDDS = False

    if Settings.showConsole == False:
        import win32gui, win32con

        the_program_to_hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

    #if Settings.fantasyNames == True:
    #    try:
    #        synonymCache = open(filepath + "/synonymCache.py", "x", encoding='utf-8')
    #        from wordhoard import Synonyms
    #        print("Loading synonyms (1/7).", end="\r")
    #        synonym = Synonyms(search_string='hot')
    #        synonym_results_hot = synonym.find_synonyms()
    #        print("Loading synonyms (2/7).", end="\r")
    #        synonym = Synonyms(search_string='cold')
    #        synonym_results_cold = synonym.find_synonyms()
    #        print("Loading synonyms (3/7).", end="\r")
    #        synonym = Synonyms(search_string='oceanic')
    #        synonym_results_oceanic = synonym.find_synonyms()
    #        print("Loading synonyms (4/7).", end="\r")
    #        synonym = Synonyms(search_string='rocky')
    #        synonym_results_rocky = synonym.find_synonyms()
    #        print("Loading synonyms (5/7).", end="\r")
    #        synonym = Synonyms(search_string='life')
    #        synonym_results_life = synonym.find_synonyms()
    #        print("Loading synonyms (6/7).", end="\r")
    #        synonym = Synonyms(search_string='dry')
    #        synonym_results_dry = synonym.find_synonyms()
    #        print("Loading synonyms (7/7).", end="\r")
    #        synonym = Synonyms(search_string='bright')
    #        synonym_results_light = synonym.find_synonyms()
    #        print("Finished loading synonyms!")
    #        synonymList = [synonym_results_hot, synonym_results_cold, synonym_results_oceanic, synonym_results_rocky, synonym_results_life, synonym_results_dry, synonym_results_light]
    #        synonymCache.write("synonyms = " + str(synonymList))
    #        synonymCache.flush()
    #    except FileExistsError:
    #        import synonymCache # Imports the file so that it can be read xdd
    #        synonymList = synonymCache.synonyms

    # Set all values to zero to prevent weird shenanigans from happening.
    totalSystemsGenerated = 0
    totalStarsGenerated = 0
    totalPlanetsGenerated = 0
    totalMoonsGenerated = 0

    surfaceMaterials = ["SrfRock","SrfSilica","SrfVulcan","SrfRockMetal","SrfRockIce","SrfIceWater","SrfIceMethane","SrfIceNitrogen","SrfAlumina","SrfMetalCarbon","SrfMetalSulfur","SrfRockMineral"]
    oceanMaterials = ["OcnTerra","OcnNitrogen","OcnMethane","OcnAmmonia","OcnLava","OcnMudWarm","OcnMudCold","OcnOxygen","OcnOxygenN","OcnOxygenC","OcnAcid","OcnKerosene"]
    atmosphereMaterials = ["AtmDefault","AtmTerra","AtmVulcan","AtmSteam","AtmSteamC","AtmSteamN","AtmIceWaterThick","AtmIceWaterThin","AtmIceAmmonia","AtmIceMethane","AtmIceNitrogen","AtmOxygen","AtmAcidC","AtmAcidN","AtmGasHelium","AtmGasI","AtmGasII","AtmGasIII","AtmGasIV","AtmGasIV","StarPop1","StarPop2","StarPop3","StarDyingRedGiant","StarCarbon","StarNeutron","BlackHole","WormHole"]
    exoticMaterials = ["ExoRock","ExoIce","ExoNone"]

    availableGalaxies = ["Sun","Sun","Sun","Sun","LKC_CtrlB","LKC_CtrlB","SKC_CtrlB"] # "Sun" is the milky way.

    print("Starting generator...")
    allPlanets = []
    wormholeList = []

    # !!!!! THE GLOBAL SEED!!! THIS IS VERY IMPORTANT !!!!!!
    gloablSeed = 42

    # Gets star color multiplier I guess
    def getStarColorMult(radi):
        starRadiusMult = radi/261600000
        if starRadiusMult < 1:
            colorMult = np.interp(starRadiusMult, [0, 1], [0, 45])
        elif starRadiusMult > 1:
            colorMult = np.interp(starRadiusMult, [1, 7], [45, 99])
        else:
            colorMult = 45
        return colorMult

    # Generates a singularity config for neutron stars. (nevermind it doesn't exist now)

    # Make resourced for Rational Resourced because yummy
    def createResourceConfig(seed,config,bodyName,lava,icy,temp,pressure,ocean,gasGiant,life,starType):
        resourceRNG = random.Random()
        resourceRNG.seed(seed)
        resources = []

        if not starType == None:
            if starType == "RedGiant": 
                resources.append("StarDyingRedGiant")
            elif starType == "Neutron":
                resources.append("StarNeutron")
            else:
                if resourceRNG.randint(0,100) > 10:
                    resources.append("StarPop1")
                else:
                    resources.append("StarPop2")

        if starType == None:
            if gasGiant == False:
                #resources.append("SrfRock")
                #resources.append("SrfSilica")
                #resources.append("SrfRockMetal")
                #resources.append("SrfRockMineral")

                #if resourceRNG.randint(0,10) == 0:
                #    resources.append("ExoRock")
                #
                #if resourceRNG.randint(0,1) == 0:
                #    resources.append("SrfAlumina")
                #if resourceRNG.randint(0,1) == 0:
                #    resources.append("SrfMetalCarbon")
                #if resourceRNG.randint(0,1) == 0:
                #    resources.append("SrfMetalSulfur")
                if lava == True:
                    resources.append("SrfVulcan")
                    resources.append("OcnLava")
                elif icy == True:    
                    if ocean == False:            
                        if temp < 273:
                            resources.append("SrfIceWater")
                        if temp < 91:
                            resources.append("SrfIceMethane")
                        if temp < 63:
                            resources.append("SrfIceNitrogen")
                    else:
                        resources.append("SrfRockIce")
                else:
                    randomGroundResource = resourceRNG.randint(0,100)
                    if randomGroundResource > 0 and randomGroundResource < 10:
                        resources.append("ExoRock")
                    elif randomGroundResource >= 10 and randomGroundResource < 20:
                        resources.append("SrfAlumina")
                    elif randomGroundResource >= 20 and randomGroundResource < 30:
                        resources.append("SrfMetalCarbon")
                    elif randomGroundResource >= 30 and randomGroundResource < 40:
                        resources.append("SrfMetalSulfur")
                    elif randomGroundResource >= 40 and randomGroundResource < 50:
                        resources.append("SrfRockMineral")
                    elif randomGroundResource >= 50 and randomGroundResource < 60:
                        resources.append("SrfSilica")
                    elif randomGroundResource >= 60 and randomGroundResource < 70:
                        resources.append("SrfRockMetal")
                    else:
                        resources.append("SrfRock")
                
                if ocean == True:
                    if life == "exotic":
                        if resourceRNG.randint(0,2) == 0:
                            resources.append("OcnAcid")
                        else:
                            resources.append("OcnKerosene")
                    else:
                        if temp < 240:
                            resources.append("OcnAmmonia")
                        elif temp < 195:
                            resources.append("OcnOxygenC")
                        elif temp < 121:
                            resources.append("OcnOxygenN")
                        elif temp < 111:
                            resources.append("OcnMethane")
                        elif temp < 90:
                            resources.append("OcnOxygen")
                        elif temp < 77:
                            resources.append("OcnNitrogen")
                        else:
                            resources.append("OcnTerra")

                if pressure > 0:
                    #if life == "organic":
                    #    resources.append("AtmOxygen")
                    #else:
                    #    resources.append("AtmDefault")
                    #if lava == True:
                    #    resources.append("AtmVulcan")
                    if life == "organic":
                        resources.append("AtmOxygen")
                    else:
                        if ocean == True:
                            if temp < 273:
                                resources.append(resourceRNG.choice(["AtmIceWaterThick","AtmIceWaterThin"]))
                            elif temp < 194:
                                resources.append("AtmIceAmmonia")
                            elif temp < 91:
                                resources.append("AtmIceMethane")
                            elif temp < 63:
                                resources.append("AtmIceNitrogen")
                            else:
                                resources.append("AtmDefault")
                        elif lava == True:
                            resources.append("AtmVulcan")
                        else:
                            if temp < 373:
                                resources.append("AtmDefault")
                            elif temp < 273:
                                resources.append(resourceRNG.choice(["AtmIceWaterThick","AtmIceWaterThin"]))
                            elif temp < 194:
                                resources.append("AtmIceAmmonia")
                            elif temp < 91:
                                resources.append("AtmIceMethane")
                            elif temp < 63:
                                resources.append("AtmIceNitrogen")
                            else:
                                resources.append(resourceRNG.choice(["AtmSteam","AtmSteamC","AtmSteamN"]))
            else: # "AtmGasI","AtmGasII","AtmGasIII","AtmGasIV","AtmGasIV"
                if temp < 150:
                    resources.append("AtmGasI")
                elif temp < 250:
                    resources.append("AtmGasII")
                elif temp < 800:
                    resources.append("AtmGasIII")
                elif temp < 1400:
                    resources.append("AtmGasIV")
                else:
                    resources.append("AtmGasV")

        #config.write(
        #    "+PLANETARY_RESOURCE:HAS[#Tag[SrfRock]]\n"
        #    "{\n"
        #    "    @PlanetName = Kerbin\n"
        #    "    @Tag = Applied\n"
        #    "}\n"
        #)
        print(resources)
        for resource in resources:
            config.write(
                "+PLANETARY_RESOURCE:HAS[#Tag[" + resource + "]]\n"
                "{\n"
                "    @PlanetName = "+ bodyName +"\n"
                "    @Tag = Applied\n"
                "}\n"
            )
    # Generates a spiral effect for WR binaries.
    def generateWRBinarySpiral(bodyName):
        spiralCfg = open(targetPath + "/Configs/" + bodyName + "_SPIRAL" + ".cfg","x")
        spiralCfg.write(
            "@Kopernicus\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + bodyName + "-WR-SPIRAL1\n"
            "        Tag = InfD_WR_SPIRAL\n"
            "        Template\n"
            "        {\n"
            "            name = Jool\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            description = \n"
            "            radius = 1000\n"
            "            mass = 420\n"
            "            rotationPeriod = 420000\n"
            "            initialRotation = 0\n"
            "            sphereOfInfluence = 1\n"
            "            selectable = False\n"
            "        }\n"
            "        Orbit\n"
            "        {\n"
            "            referenceBody = " + bodyName + "\n"
            "            semiMajorAxis = 1\n"
            "            period = 100000000000000000000000\n"
            "            argumentOfPeriapsis = 90\n"
            "            mode = 0\n"
            "            icon = NONE\n"
            "        }\n"
            "        Rings\n"
            "        {\n"
            "            // Disks\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1450\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -1\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1350\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 0\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1250\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 1\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1150\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1050\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "    Body\n"
            "    {\n"
            "        name = " + bodyName + "-WR-SPIRAL2\n"
            "        Tag = InfD_WR_SPIRAL\n"
            "        Template\n"
            "        {\n"
            "            name = Jool\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            description = \n"
            "            radius = 1000\n"
            "            mass = 420\n"
            "            rotationPeriod = 420000\n"
            "            initialRotation = 90\n"
            "            sphereOfInfluence = 1\n"
            "            selectable = False\n"
            "        }\n"
            "        Orbit\n"
            "        {\n"
            "            referenceBody = " + bodyName + "\n"
            "            semiMajorAxis = 1\n"
            "            period = 100000000000000000000000\n"
            "            argumentOfPeriapsis = 90\n"
            "            mode = 0\n"
            "            icon = NONE\n"
            "        }\n"
            "        Rings\n"
            "        {\n"
            "            // Disks\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1450\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -1\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1350\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 0\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1250\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 1\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1150\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 150000000000\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/WR_BinaryRings.dds\n"
            "                tiles = 1\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1050\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )
    # Generate nebula for something
    def generateNebula(bodyName):
        nebulaCfg = open(targetPath + "/Visuals/NiftyNebulae/" + bodyName + "_NEBULA" + ".cfg","x")
        nebulaCfg.write(
            "NiftyNebula\n"
            "{\n"
            "    name = " + bodyName + "_NEBULA\n"
            "    nebulaRadius = 600\n"
            "    domainScale = 1,1,1\n"
            "    parentName = " + bodyName + "\n"
            "    densityMultiplier = 0.7\n"
            "    shouldFadeWithSkybox = true\n"
            "    fadeAmount = 0.25\n"
            "    texture = InfiniteDiscoveries/Textures/Misc/WR_Nebula.png\n"
            "    textureTileSize = 256\n"
            "    noiseStrength = 0.2\n"
            "    noiseFrequency = 30\n"
            "}\n"
        )
    # Generate glowing clouds for gas giants because idk lmfao they look cool why else?
    def generateSuperheatedClouds(eveCfg,planetName,temp):
        spot = int((temp/10000)*99)

        color = Color.get_rgb(Color(colorsReversed[spot]))
        colorHSV = colorsys.rgb_to_hsv(color[0],color[1],color[2])
        colorSaturated = colorsys.hsv_to_rgb(colorHSV[0],colorHSV[1]*2,colorHSV[2])
        eveCfg.write(
                "    OBJECT\n"
                "    {\n"
                "        name = " + planetName + "_HEATEDCLOUDS" + "\n"
                "        body = " + planetName + "\n"
                "        altitude = 10000\n"
                "        detailSpeed = 0,6,0\n"
                "        settings\n"
                "        {\n"
                "            _DetailTex = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                "            _DetailScale = 30\n"
                "            _Color = " + str(colorSaturated[0]*255) + "," + str(colorSaturated[1]*255) + "," + str(colorSaturated[2]*255) + ", 128\n"
                "            _MainTex\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Textures/Clouds/" + str(planetName) + "_CLOUDS\n"
                "                type = AlphaMap\n"
				"                alphaMask = ALPHAMAP_R\n"
                "            }\n"
                "            _FlowMap\n"
                "            {\n"
                "				 texture = Infinite_VolumetricClouds/Textures/FlowMap\n"
				"                speed = 0.01\n"
                "                displacement = 0.5\n"
                "            }\n"
                "        }\n"
                "        layer2D\n"
                "        {\n"
                "            macroCloudMaterial\n"
                "            {\n"
                "                _MinLight = 2\n"
                "            }\n"
                "        }\n"
                "    }\n"
        )
    # Process a name
    def processName(seed,tTable,length):
        generated_word = generateName2(tTable, length, seed)
        generatedWords = generated_word.split(" ")
        max_len = -1
        for ele in generatedWords:
            if len(ele) > max_len:
                max_len = len(ele)
                res = ele
        finalword = res
        return finalword
    # Generate a bunch of wormholes for some reason
    def generateWormholes(seed):
        WormholeRNG = random.Random()
        WormholeRNG.seed(seed)
        global targetPath
        global allPlanets
        #print(str(len(allPlanets)) + "<------------------------------------------------------------------------ all planata legth")
        if len(allPlanets) > 0:
            wormholesConfig = open(targetPath + "Configs/wormholes" + str(WormholeRNG.randint(0,100000)) + ".cfg", "x") # random number to avoid existing file errors.
            wormholesConfig.write(
                "@Kopernicus:LAST[InfiniteDiscoveries]:HAS[@InfiniteDiscoveriesSettings:HAS[#Wormholes[?rue]]]:NEEDS[KopernicusExpansion]\n"
                "{\n"
            )
            for i in range(0,StarAmount + 1):
                target1 = allPlanets[WormholeRNG.randint(0,len(allPlanets)-1)]
                while True:
                    target2 = allPlanets[WormholeRNG.randint(0,len(allPlanets)-1)]
                    if not target2 == target1:
                        break
                wormholeName1 = alphabet[WormholeRNG.randint(0,len(alphabet)-1)] + alphabet[WormholeRNG.randint(0,len(alphabet)-1)] + alphabet[WormholeRNG.randint(0,len(alphabet)-1)] + "-" + str(WormholeRNG.randint(0,100000))
                wormholeName2 = alphabet[WormholeRNG.randint(0,len(alphabet)-1)] + alphabet[WormholeRNG.randint(0,len(alphabet)-1)] + alphabet[WormholeRNG.randint(0,len(alphabet)-1)] + "-" + str(WormholeRNG.randint(0,100000))
                singularCfg = open(targetPath + "Visuals/Singularity/" + wormholeName1 + "-" + wormholeName2 + "_SNG.cfg", "x")
                singularCfg.write(
                    "Singularity\n"
                    "{\n"
                    "    Singularity_object\n"
                    "    {\n"
                    "        name = " + wormholeName1 + "\n"
                    "        gravity = 5\n"
                    "        hideCelestialBody = true\n"
                    "        useAccretionDisk = false\n"
                    "        wormholeTarget = " + wormholeName2 + "\n"
                    "    }\n"
                    "    Singularity_object\n"
                    "    {\n"
                    "        name = " + wormholeName2 + "\n"
                    "        gravity = 5\n"
                    "        hideCelestialBody = true\n"
                    "        useAccretionDisk = false\n"
                    "        wormholeTarget = " + wormholeName1 + "\n"
                    "    }\n"
                    "}\n"
                )
                wormholesConfig.write(
                    "    Body\n"
                    "    {\n"
                    "        name = " + wormholeName1 + "\n"
                    "        cacheFile = InfiniteDiscoveries/Cache/" + wormholeName1 + ".bin\n"
                    "        Template\n"
                    "        {\n"
                    "            name = Dres\n"
                    "            removeAllPQSMods = True\n"
                    "        }\n"
                    "        Properties\n"
                    "        {\n"
                    "            displayName = " + wormholeName1 + "\n"
                    "            description = A mysterious object, supposedly going under 5 kilometers on here will send you to another star system...\n"
                    "            radius = 100000\n"
                    "            geeASL = 10\n"
                    "            tidallyLocked = false\n"
                    "            rotationPeriod = 10000\n"
                    "        }\n"
                    "        Wormhole\n"
                    "        {\n"
                    "            partner = " + wormholeName2 + "\n"
                    "            influenceAltitude = 8000\n"
                    "            jumpMaxAltitude = 5000\n"
                    "            jumpMinAltitude = 10\n"
                    "            entryMessage = Entering a wormhole... We are not responsible for any casualties within, before, or after entering the wormhole. We also do not know where you may end up, good luck!\n"
                    "            exitMessage = Succesfully survived spacetime bending. Welcome to " + target1 + "!\n"
                    "            heatRate = 0.1\n"
                    "            entryMsgDuration = 7\n"
                    "            exitMsgDuration = 7\n"
                    "        }\n"
                    "        ScaledVersion\n"
                    "        {\n"
                    "            type = Vacuum\n"
                    "            fadeStart = 7000\n"
                    "            fadeEnd = 10000\n"
                    "            Material\n"
                    "            {\n"
                    "                texture = InfiniteDiscoveries/Textures/Misc/literallynothing.png\n"
                    "                normals = InfiniteDiscoveries/Textures/Misc/literallyjustablanknormalmap.dds\n"
                    "                color = 1,1,1,1\n"
                    "                specColor = 0.05,0.05,0.05,1\n"
                    "                shininess = 1\n"
                    "            }\n"
                    "        }\n"
                    "        Orbit\n"
                    "        {\n"
                    "            referenceBody = " + target1 + "\n"
                    "            inclination = " + str(WormholeRNG.randint(-15,15)) + "\n"
                    "            eccentricity = 0\n"
                    "            semiMajorAxis = " + str(WormholeRNG.randint(5000000,50000000)) + "\n"
                    "            longitudeOfAscendingNode = " + str(WormholeRNG.randint(0,360)) + "\n"
                    "            argumentOfPeriapsis = " + str(WormholeRNG.randint(0,360)) + "\n"
                    "            epoch = 0\n"
                    "            color = 0.2,0.2,0.2,0.2\n"
                    "            iconTexture = InfiniteDiscoveries/Textures/Misc/wormholeIco.png\n"
                    "        }\n"
                    "        PQS\n"
                    "        {\n"
                    "            Mods\n"
                    "            {			\n"
                    "                VertexHeightMap\n"
                    "                {\n"
                    "                    map = InfiniteDiscoveries/Textures/Misc/literallynothing.png\n"
                    "                    offset = -99999\n"
                    "                    deformity = 0\n"
                    "                    scaleDeformityByRadius = False\n"
                    "                    order = 10\n"
                    "                    enabled = True\n"
                    "                }\n"
                    "                VertexColorMap\n"
                    "                {\n"
                    "                    map = InfiniteDiscoveries/Textures/Misc/literallynothing.png\n"
                    "                    order = 90\n"
                    "                    enabled = True\n"
                    "                    name = VertexColorMap\n"
                    "                    index = 0\n"
                    "                } \n"
                    "            }\n"
                    "        }\n"
                    "    }\n"
                    "    Body\n"
                    "    {\n"
                    "        name = " + wormholeName2 + "\n"
                    "        cacheFile = InfiniteDiscoveries/Cache/" + wormholeName2 + ".bin\n"
                    "        Template\n"
                    "        {\n"
                    "            name = Dres\n"
                    "            removeAllPQSMods = True\n"
                    "        }\n"
                    "        Properties\n"
                    "        {\n"
                    "            displayName = " + wormholeName2 + "\n"
                    "            description = A mysterious object, supposedly going under 5 kilometers on here will send you to another star system...\n"
                    "            radius = 100000\n"
                    "            geeASL = 10\n"
                    "            tidallyLocked = false\n"
                    "            rotationPeriod = 10000\n"
                    "        }\n"
                    "        Wormhole\n"
                    "        {\n"
                    "            partner = " + wormholeName1 + "\n"
                    "            influenceAltitude = 8000\n"
                    "            jumpMaxAltitude = 5000\n"
                    "            jumpMinAltitude = 10\n"
                    "            entryMessage = Entering a wormhole... We are not responsible for any casualties within, before, or after entering the wormhole. We also do not know where you may end up, good luck!\n"
                    "            exitMessage = Succesfully survived spacetime bending. Welcome to " + target2 + "!\n"
                    "            heatRate = 0.1\n"
                    "            entryMsgDuration = 7\n"
                    "            exitMsgDuration = 7\n"
                    "        }\n"
                    "        ScaledVersion\n"
                    "        {\n"
                    "            type = Vacuum\n"
                    "            fadeStart = 7000\n"
                    "            fadeEnd = 10000\n"
                    "            Material\n"
                    "            {\n"
                    "                texture = InfiniteDiscoveries/Textures/Misc/literallynothing.png\n"
                    "                normals = InfiniteDiscoveries/Textures/Misc/literallyjustablanknormalmap.dds\n"
                    "                color = 1,1,1,1\n"
                    "                specColor = 0.05,0.05,0.05,1\n"
                    "                shininess = 1\n"
                    "            }\n"
                    "        }\n"
                    "        Orbit\n"
                    "        {\n"
                    "            referenceBody = " + target2 + "\n"
                    "            inclination = " + str(WormholeRNG.randint(-15,15)) + "\n"
                    "            eccentricity = 0\n"
                    "            semiMajorAxis = " + str(WormholeRNG.randint(5000000,50000000)) + "\n"
                    "            longitudeOfAscendingNode = " + str(WormholeRNG.randint(0,360)) + "\n"
                    "            argumentOfPeriapsis = " + str(WormholeRNG.randint(0,360)) + "\n"
                    "            epoch = 0\n"
                    "            color = 0.2,0.2,0.2,0.2\n"
                    "            iconTexture = InfiniteDiscoveries/Textures/Misc/wormholeIco.png\n"
                    "        }\n"
                    "        PQS\n"
                    "        {\n"
                    "            Mods\n"
                    "            {			\n"
                    "                VertexHeightMap\n"
                    "                {\n"
                    "                    map = InfiniteDiscoveries/Textures/Misc/literallynothing.png\n"
                    "                    offset = -99999\n"
                    "                    deformity = 0\n"
                    "                    scaleDeformityByRadius = False\n"
                    "                    order = 10\n"
                    "                    enabled = True\n"
                    "                }\n"
                    "                VertexColorMap\n"
                    "                {\n"
                    "                    map = InfiniteDiscoveries/Textures/Misc/literallynothing.png\n"
                    "                    order = 90\n"
                    "                    enabled = True\n"
                    "                    name = VertexColorMap\n"
                    "                    index = 0\n"
                    "                } \n"
                    "            }\n"
                    "        }\n"
                    "    }\n"
                )
            wormholesConfig.write(
                "}\n"
            )
    # Adds parallax scatters.
    def addParallaxScatter(seed, cfg, planetName, haslife, lifeclr, radius):
        pSctrRNG = random.Random()
        pSctrRNG.seed(seed)
        radiusDiv = 600 / (radius/1000)

        cfg.write(
            "ParallaxScatters\n"
            "{\n"
            "   body = " + planetName + "\n"
	        "   minimumSubdivision = 2\n"
        )
        cfg.write(
            "   Scatter\n"
            "   {\n"
            "       name = SmallRocks\n"
            "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockSmall/rock\n"
            "       updateFPS = 1\n"
            "       cullingRange = 20\n"
            "       cullingLimit = -30\n"
            "       alignToTerrainNormal = True\n"
            "       SubdivisionSettings\n"
            "       {\n"
            "           subdivisionLevel = 1\n"
            "           subdivisionRangeMode = FixedRange\n"
            "           subdivisionRange = 900\n"
            "       }\n"
            "       DistributionNoise\n"
            "       {\n"
            "           mode = Persistent\n"
            "           _Frequency = 180000\n"
            "           _Persistence = 0.300000012\n"
            "           _Lacunarity = 2\n"
            "           _Octaves = 6\n"
            "           _Seed = " + str(pSctrRNG.randint(0,10000)) + "\n"
            "           _NoiseType = 1\n"
            "           _NoiseQuality = Standard\n"
            "       }\n"
            "       Distribution\n"
            "       {\n"
            "           _Seed = 1\n"
            "           _SpawnChance = 1\n"
            "           _Range = 160\n"
            "           _PopulationMultiplier = "+ str((40/radiusDiv)/radiusDiv) + "\n"
        )
        cfg.write(
            "           _SizeNoiseStrength = 1\n"
            "           _MinScale = 0.02,0.02,0.02\n"
            "           _MaxScale = 1,1,1\n"
            "           _CutoffScale = 0.150000006\n"
            "           _SteepPower = 8\n"
            "           _SteepContrast = 4.5\n"
            "           _SteepMidpoint = 0.731000006\n"
            "           _NormalDeviance = 0.12\n"
            "           _MinAltitude = -1000\n"
            "           _MaxAltitude = 20000\n"
            "           _RangePow = 3\n"
            "           LODs\n"
            "           {\n"
            "               LOD\n"
            "               {\n"
            "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockSmall/rock1\n"
            "                   _MainTex = parent\n"
            "                   range = 80\n"
            "                   billboard = False\n"
            "               }\n"
            "               LOD\n"
            "               {\n"
            "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockSmall/rock1\n"
            "                   _MainTex = parent\n"
            "                   range = 200\n"
            "                   billboard = False\n"
            "               }\n"
            "           }\n"
            "       }\n"
            "       Material\n"
            "       {\n"
            "           shader = Custom/ParallaxInstancedUV\n"
            "           _MainColor = 1,1,1,1\n"
            "           _SubColor = 1,1,1,1\n"
            "           _ColorNoiseStrength = 1\n"
            "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockSmall/textureclr.dds\n"
            "           _EdgeBumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockSmall/texturenrm.dds\n"
            "           _Metallic = 0.25\n"
            "           _Gloss = 5\n"
            "           _NormalSpecularInfluence = 1\n"
            "           _Hapke = 0.300000012\n"
            "           _BumpScale = 1\n"
            "           _FresnelPower = 4\n"
            "           _MainTexScale = 1,1\n"
            "           _EdgeBumpMapScale = 1,1\n"
            "           _EmissionColor = 0,0,0,1\n"
            "           _MetallicTint = 0.5,0.5,0.5,1\n"
            "           _Color = 0.5,0.5,0.5,1\n"
            "           _FresnelColor = 0.0799999982,0.0799999982,0.0799999982,1\n"
            "       }\n"
            "       SubObjects\n"
            "       {\n"
            "       }\n"
            "   }\n"
        )
        cfg.write(
            "   Scatter\n"
            "   {\n"
            "       name = MedRocks\n"
            "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockMedium/rock\n"
            "       updateFPS = 1\n"
            "       cullingRange = 20\n"
            "       cullingLimit = -30\n"
            "       alignToTerrainNormal = True\n"
            "       collideable = True\n"
            "       maxObjects = 20000\n"
            "       //collisionMesh = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockMedium/rock1\n"
            "       SubdivisionSettings\n"
            "       {\n"
            "           subdivisionLevel = 1\n"
            "           subdivisionRangeMode = FixedRange\n"
            "           subdivisionRange = 1400\n"
            "       }\n"
            "       DistributionNoise\n"
            "       {\n"
            "           mode = Persistent\n"
            "           _Frequency = 18000\n"
            "           _Persistence = 0.300000012\n"
            "           _Lacunarity = 2\n"
            "           _Octaves = 6\n"
            "           _Seed = " + str(pSctrRNG.randint(0,10000)) + "\n"
            "           _NoiseType = 1\n"
            "           _NoiseQuality = Standard\n"
            "       }\n"
            "       Distribution\n"
            "       {\n"
            "           _Seed = 0\n"
            "           _SpawnChance = 1\n"
            "           _Range = 1200\n"
            "           _PopulationMultiplier = "+ str((5/radiusDiv)/radiusDiv) + "\n"
        )
        cfg.write(
            "           _SizeNoiseStrength = 1\n"
            "           _MinScale = 0.2,0.2,0.2\n"
            "           _MaxScale = 5,5,5\n"
            "           _CutoffScale = 0.5\n"
            "           _SteepPower = 8\n"
            "           _SteepContrast = 4.5\n"
            "           _SteepMidpoint = 0.731000006\n"
            "           _NormalDeviance = 0.2\n"
            "           _MinAltitude = -1000\n"
            "           _MaxAltitude = 20000\n"
            "           _RangePow = 4\n"
            "           LODs\n"
            "           {\n"
            "               LOD\n"
            "               {\n"
            "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockMedium/rock1\n"
            "                   _MainTex = parent\n"
            "                   range = 200\n"
            "                   billboard = False\n"
            "               }\n"
            "               LOD\n"
            "               {\n"
            "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockMedium/rock1\n"
            "                   _MainTex = parent\n"
            "                   range = 500\n"
            "                   billboard = False\n"
            "               }\n"
            "           }\n"
            "       }\n"
            "       Material\n"
            "       {\n"
            "           shader = Custom/ParallaxInstancedUV\n"
            "           _MainColor = 1,1,1,1\n"
            "           _SubColor = 1,1,1,1\n"
            "           _ColorNoiseStrength = 1\n"
            "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockMedium/textureclr.dds\n"
            "           _EdgeBumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockMedium/texturenrm.dds\n"
            "           _Metallic = 0.25\n"
            "           _Gloss = 2\n"
            "           _NormalSpecularInfluence = 1\n"
            "           _Hapke = 1\n"
            "           _BumpScale = 1\n"
            "           _FresnelPower = 4\n"
            "           _MainTexScale = 1,1\n"
            "           _EdgeBumpMapScale = 1,1\n"
            "           _EmissionColor = 0,0,0,1\n"
            "           _MetallicTint = 0.5,0.5,0.5,1\n"
            "           _Color = 0.5,0.5,0.5,1\n"
            "           _FresnelColor = 0.2,0.2,0.2,1\n"
            "       }\n"
            "       SubObjects\n"
            "       {\n"
            "       }\n"
            "   }\n"
        )   
        # NEW JAGGED ROCKERS
        cfg.write(
            "   Scatter\n"
            "   {\n"
            "       name = JaggedRocks\n"
            "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockJagged/rock\n"
            "       updateFPS = 1\n"
            "       cullingRange = 20\n"
            "       cullingLimit = -30\n"
            "       alignToTerrainNormal = True\n"
            "       collideable = True\n"
            "       maxObjects = 20000\n"
            "       //collisionMesh = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockJagged/rock1\n"
            "       SubdivisionSettings\n"
            "       {\n"
            "           subdivisionLevel = 1\n"
            "           subdivisionRangeMode = FixedRange\n"
            "           subdivisionRange = 1400\n"
            "       }\n"
            "       DistributionNoise\n"
            "       {\n"
            "           mode = Persistent\n"
            "           _Frequency = 1800\n"
            "           _Persistence = 0.300000012\n"
            "           _Lacunarity = 2\n"
            "           _Octaves = 6\n"
            "           _Seed = " + str(pSctrRNG.randint(0,10000)) + "\n"
            "           _NoiseType = 1\n"
            "           _NoiseQuality = Standard\n"
            "       }\n"
            "       Distribution\n"
            "       {\n"
            "           _Seed = 0\n"
            "           _SpawnChance = 1\n"
            "           _Range = 1200\n"
            "           _PopulationMultiplier = "+ str((15/radiusDiv)/radiusDiv) + "\n"
        )
        cfg.write(
            "           _SizeNoiseStrength = 1\n"
            "           _MinScale = 1,1,1\n"
            "           _MaxScale = 3,3,3\n"
            "           _CutoffScale = 0.5\n"
            "           _SteepPower = 8\n"
            "           _SteepContrast = 4.5\n"
            "           _SteepMidpoint = 0.731000006\n"
            "           _NormalDeviance = 0.2\n"
            "           _MinAltitude = -1000\n"
            "           _MaxAltitude = 20000\n"
            "           _RangePow = 4\n"
            "           LODs\n"
            "           {\n"
            "               LOD\n"
            "               {\n"
            "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockJagged/rock1\n"
            "                   _MainTex = parent\n"
            "                   range = 200\n"
            "                   billboard = False\n"
            "               }\n"
            "               LOD\n"
            "               {\n"
            "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockJagged/rock1\n"
            "                   _MainTex = parent\n"
            "                   range = 500\n"
            "                   billboard = False\n"
            "               }\n"
            "           }\n"
            "       }\n"
            "       Material\n"
            "       {\n"
            "           shader = Custom/ParallaxInstancedUV\n"
            "           _MainColor = 1,1,1,1\n"
            "           _SubColor = 1,1,1,1\n"
            "           _ColorNoiseStrength = 1\n"
            "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockJagged/textureclr.dds\n"
            "           _EdgeBumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Rocks/RockJagged/texturenrm.dds\n"
            "           _Metallic = 0.25\n"
            "           _Gloss = 2\n"
            "           _NormalSpecularInfluence = 1\n"
            "           _Hapke = 1\n"
            "           _BumpScale = 1\n"
            "           _FresnelPower = 4\n"
            "           _MainTexScale = 1,1\n"
            "           _EdgeBumpMapScale = 1,1\n"
            "           _EmissionColor = 0,0,0,1\n"
            "           _MetallicTint = 0.5,0.5,0.5,1\n"
            "           _Color = 0.5,0.5,0.5,1\n"
            "           _FresnelColor = 0.2,0.2,0.2,1\n"
            "       }\n"
            "       SubObjects\n"
            "       {\n"
            "       }\n"
            "   }\n"
        )   
        if haslife == "organic":
            cfg.write(
                "   Scatter\n"
                "   {\n"
                "       name = Fern\n"
                "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Foilage/Fern1/fern\n"
                "       updateFPS = 1\n"
                "       cullingRange = 20\n"
                "       cullingLimit = -30\n"
                "       alignToTerrainNormal = True\n"
                "       maxObjects = 20000\n"
                "       SubdivisionSettings\n"
                "       {\n"
                "           subdivisionLevel = 1\n"
                "           subdivisionRangeMode = FixedRange\n"
                "           subdivisionRange = 1400\n"
                "       }\n"
                "       DistributionNoise\n"
                "       {\n"
                "           mode = NonPersistent\n"
                "           _SizeNoiseScale = 4\n"
                "           _ColorNoiseScale = 32\n"
                "           _SizeNoiseOffset = 0\n"
                "       }\n"
                "       Distribution\n"
                "       {\n"
                "           _Seed = 0\n"
                "           _SpawnChance = 1\n"
                "           _Range = 1200\n"
                "           _PopulationMultiplier = "+ str((100/radiusDiv)/radiusDiv) + "\n"
                "           _SizeNoiseStrength = 2\n"
                "           _MinScale = 0.1,0.1,0.1\n"
                "           _MaxScale = 1,1,1\n"
                "           _CutoffScale = 0.75\n"
                "           _SteepPower = 8\n"
                "           _SteepContrast = 4.5\n"
                "           _SteepMidpoint = 0.731000006\n"
                "           _NormalDeviance = 0.2\n"
                "           _MinAltitude = 0\n"
                "           _MaxAltitude = 20000\n"
                "           _RangePow = 4\n"
                "           LODs\n"
                "           {\n"
                "               LOD\n"
                "               {\n"
                "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Foilage/Fern1/fern1\n"
                "                   _MainTex = parent\n"
                "                   range = 200\n"
                "                   billboard = False\n"
                "               }\n"
                "               LOD\n"
                "               {\n"
                "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Foilage/Fern1/fern1\n"
                "                   _MainTex = parent\n"
                "                   range = 500\n"
                "                   billboard = False\n"
                "               }\n"
                "           }\n"
                "           BiomeBlacklist\n"
                "           {\n"
                "               name = Icecaps\n"
                "           }\n"
                "       }\n"
                "       Material\n"
                "       {\n"
                "           shader = Custom/InstancedCutout\n"
                "           _MainColor = 1,1,1,1\n"
                "           _SubColor = 1,1,1,1\n"
                "           _ColorNoiseStrength = 1\n"
                "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Foilage/Fern1/textureclr.dds\n"
                "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Foilage/Fern1/texturenrm.dds\n"
                "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                "           _WaveSpeed = 0\n"
                "           _WaveAmp = 0.0399999991\n"
                "           _HeightCutoff = -0.898999989\n"
                "           _HeightFactor = 2.25999999\n"
                "           _Metallic = 0.5\n"
                "           _Gloss = 5\n"
                "           _Hapke = 1\n"
                "           _Cutoff = 0.5\n"
                "           _WindSpeed = 50,50,50\n"
                "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                "           _FresnelPower = 3\n"
                "           _FresnelColor = 0.05,0.05,0.05\n"
                "           _Transmission = 1\n"
                "       }\n"
                "       SubObjects\n"
                "       {\n"
                "       }\n"
                "   }\n"
            )
            if pSctrRNG.randint(0,1) == 0:
                print("Has regular trees!")
                cfg.write(
                    "   Scatter\n"
                    "   {\n"
                    "       name = tree1\n"
                    "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/trunk\n"
                    "       updateFPS = 0.330000013\n"
                    "       cullingRange = 200\n"
                    "       cullingLimit = -400\n"
                    "       alignToTerrainNormal = False\n"
                    "       maxObjects = 40000\n"
                    "       SubdivisionSettings\n"
                    "       {\n"
                    "           subdivisionLevel = 1\n"
                    "           subdivisionRangeMode = FixedRange\n"
                    "           subdivisionRange = 12500\n"
                    "           minimumSubdivision = 8\n"
                    "       }\n"
                    "       DistributionNoise\n"
                    "       {\n"
                    "           mode = Persistent\n"
                    "           _Frequency = 200\n"
                    "           _Persistence = 0.300000012\n"
                    "           _Lacunarity = 2\n"
                    "           _Octaves = 6\n"
                    "           _Seed = " + str(pSctrRNG.randint(0,10000)) + "\n"
                    "           _NoiseType = 1\n"
                    "           _NoiseQuality = Standard\n"
                    "       }\n"
                    "       Distribution\n"
                    "       {\n"
                    "           _Seed = 62.1199989\n"
                    "           _SpawnChance = 0.699999988\n"
                    "           _Range = 10500\n"
                    "           _PopulationMultiplier = "+ str((5/radiusDiv)/radiusDiv) + "\n"
                    "           _SizeNoiseStrength = 0.75\n"
                    "           _MinScale = 1,1,1\n"
                    "           _MaxScale = 3,3,3\n"
                    "           _CutoffScale = 0.550000012\n"
                    "           _SteepPower = 8\n"
                    "           _SteepContrast = 4.5\n"
                    "           _SteepMidpoint = 0.731000006\n"
                    "           _NormalDeviance = 0.5\n"
                    "           _MinAltitude = 0\n"
                    "           _MaxAltitude = 20000\n"
                    "           _RangePow = 250\n"
                    "           LODs\n"
                    "           {\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/trunk1\n"
                    "                   _MainTex = parent\n"
                    "                   range = 250\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/farside\n"
                    "                   _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/treeside.dds\n"
                    "                   _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/treeside_nrm.dds\n"
                    "                   range = 2250\n"
                    "                   billboard = True\n"
                    "               }\n"
                    "           }\n"
                    "           BiomeBlacklist\n"
                    "           {\n"
                    "               name = Icecaps\n"
                    "           }\n"
                    "       }\n"
                    "       Material\n"
                    "       {\n"
                    "           shader = Custom/InstancedCutout\n"
                    "           _MainColor = 1,1,1,1\n"
                    "           _SubColor = 1,1,1,1\n"
                    "           _ColorNoiseStrength = 1\n"
                    "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/trunkclr.dds\n"
                    "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/trunknrm.dds\n"
                    "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                    "           _WaveSpeed = 0\n"
                    "           _WaveAmp = 0.0399999991\n"
                    "           _HeightCutoff = -0.898999989\n"
                    "           _HeightFactor = 2.25999999\n"
                    "           _Metallic = 0.5\n"
                    "           _Gloss = 5\n"
                    "           _Hapke = 1\n"
                    "           _Cutoff = 0.5\n"
                    "           _WindSpeed = 50,50,50\n"
                    "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                    "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                    "           _FresnelPower = 3\n"
                    "           _FresnelColor = 0.05,0.05,0.05\n"
                    "           _Transmission = 1\n"
                    "       }\n"
                    "       SubObjects\n"
                    "       {\n"
                    "       }\n"
                    "   }\n"
                    "   SharedScatter	//Share the same distribution data as the tree1 scatter\n"
                    "   {\n"
                    "       parent = tree1\n"
                    "       name = tree1top\n"
                    "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/leaves\n"
                    "       Distribution\n"
                    "       {\n"
                    "           LODs\n"
                    "           {\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/leaves\n"
                    "                   _MainTex = parent\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/fartop\n"
                    "                   //_MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/leavesclr.dds\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "           }\n"
                    "       }\n"
                    "       Material\n"
                    "       {\n"
                    "           shader = Custom/InstancedCutout\n"
                    "           _MainColor = 1,1,1,1\n"
                    "           _SubColor = 1,1,1,1\n"
                    "           _ColorNoiseStrength = 1\n"
                    "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/leavesclr.dds\n"
                    "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Oak1/leavesnrm.dds\n"
                    "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                    "           _WaveSpeed = 0\n"
                    "           _WaveAmp = 0.0399999991\n"
                    "           _HeightCutoff = -0.898999989\n"
                    "           _HeightFactor = 2.25999999\n"
                    "           _Metallic = 0.5\n"
                    "           _Gloss = 5\n"
                    "           _Hapke = 1\n"
                    "           _Cutoff = 0.5\n"
                    "           _WindSpeed = 50,50,50\n"
                    "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                    "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                    "           _FresnelPower = 3\n"
                    "           _FresnelColor = 0.05,0.05,0.05\n"
                    "           _Transmission = 1\n"
                    "       }\n"
                    "   }\n"
                )
            if pSctrRNG.randint(0,1) == 0:
                cfg.write(
                    "   Scatter\n"
                    "   {\n"
                    "       name = palm1\n"
                    "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/trunk\n"
                    "       updateFPS = 0.330000013\n"
                    "       cullingRange = 200\n"
                    "       cullingLimit = -400\n"
                    "       alignToTerrainNormal = False\n"
                    "       maxObjects = 40000\n"
                    "       SubdivisionSettings\n"
                    "       {\n"
                    "           subdivisionLevel = 1\n"
                    "           subdivisionRangeMode = FixedRange\n"
                    "           subdivisionRange = 12500\n"
                    "           minimumSubdivision = 8\n"
                    "       }\n"
                    "       DistributionNoise\n"
                    "       {\n"
                    "           mode = Persistent\n"
                    "           _Frequency = 200\n"
                    "           _Persistence = 0.300000012\n"
                    "           _Lacunarity = 2\n"
                    "           _Octaves = 6\n"
                    "           _Seed = " + str(pSctrRNG.randint(0,10000)) + "\n"
                    "           _NoiseType = 1\n"
                    "           _NoiseQuality = Standard\n"
                    "       }\n"
                    "       Distribution\n"
                    "       {\n"
                    "           _Seed = 62.1199989\n"
                    "           _SpawnChance = 0.699999988\n"
                    "           _Range = 10500\n"
                    "           _PopulationMultiplier = "+ str((5/radiusDiv)/radiusDiv) + "\n"
                    "           _SizeNoiseStrength = 0.75\n"
                    "           _MinScale = 1,1,1\n"
                    "           _MaxScale = 3,3,3\n"
                    "           _CutoffScale = 0.550000012\n"
                    "           _SteepPower = 8\n"
                    "           _SteepContrast = 4.5\n"
                    "           _SteepMidpoint = 0.731000006\n"
                    "           _NormalDeviance = 0.5\n"
                    "           _MinAltitude = 0\n"
                    "           _MaxAltitude = 20000\n"
                    "           _RangePow = 250\n"
                    "           LODs\n"
                    "           {\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/trunk1\n"
                    "                   _MainTex = parent\n"
                    "                   range = 250\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/farside\n"
                    "                   _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/treeside.dds\n"
                    "                   _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/treeside_nrm.dds\n"
                    "                   range = 2250\n"
                    "                   billboard = True\n"
                    "               }\n"
                    "           }\n"
                    "           BiomeBlacklist\n"
                    "           {\n"
                    "               name = Icecaps\n"
                    "           }\n"
                    "       }\n"
                    "       Material\n"
                    "       {\n"
                    "           shader = Custom/InstancedCutout\n"
                    "           _MainColor = 1,1,1,1\n"
                    "           _SubColor = 1,1,1,1\n"
                    "           _ColorNoiseStrength = 1\n"
                    "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/trunkclr.dds\n"
                    "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/trunknrm.dds\n"
                    "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                    "           _WaveSpeed = 0\n"
                    "           _WaveAmp = 0.0399999991\n"
                    "           _HeightCutoff = -0.898999989\n"
                    "           _HeightFactor = 2.25999999\n"
                    "           _Metallic = 0.5\n"
                    "           _Gloss = 5\n"
                    "           _Hapke = 1\n"
                    "           _Cutoff = 0.5\n"
                    "           _WindSpeed = 50,50,50\n"
                    "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                    "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                    "           _FresnelPower = 3\n"
                    "           _FresnelColor = 0.05,0.05,0.05\n"
                    "           _Transmission = 1\n"
                    "       }\n"
                    "       SubObjects\n"
                    "       {\n"
                    "       }\n"
                    "   }\n"
                    "   SharedScatter	//Share the same distribution data as the palm1 scatter\n"
                    "   {\n"
                    "       parent = palm1\n"
                    "       name = palm1top\n"
                    "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/leaves\n"
                    "       Distribution\n"
                    "       {\n"
                    "           LODs\n"
                    "           {\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/leaves\n"
                    "                   _MainTex = parent\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/fartop\n"
                    "                   _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/treetop.dds\n"
                    "                   _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/treetop_nrm.dds\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "           }\n"
                    "       }\n"
                    "       Material\n"
                    "       {\n"
                    "           shader = Custom/InstancedCutout\n"
                    "           _MainColor = 1,1,1,1\n"
                    "           _SubColor = 1,1,1,1\n"
                    "           _ColorNoiseStrength = 1\n"
                    "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/leavesclr.dds\n"
                    "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Trees/Palm1/leavesnrm.dds\n"
                    "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                    "           _WaveSpeed = 0\n"
                    "           _WaveAmp = 0.0399999991\n"
                    "           _HeightCutoff = -0.898999989\n"
                    "           _HeightFactor = 2.25999999\n"
                    "           _Metallic = 0.5\n"
                    "           _Gloss = 5\n"
                    "           _Hapke = 1\n"
                    "           _Cutoff = 0.5\n"
                    "           _WindSpeed = 50,50,50\n"
                    "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                    "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                    "           _FresnelPower = 3\n"
                    "           _FresnelColor = 0.05,0.05,0.05\n"
                    "           _Transmission = 1\n"
                    "       }\n"
                    "   }\n"
                )
            if pSctrRNG.randint(1,1) == 1:
                cfg.write(
                    "   Scatter\n"
                    "   {\n"
                    "       name = BigTree\n"
                    "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/trunk\n"
                    "       updateFPS = 0.330000013\n"
                    "       cullingRange = 200\n"
                    "       cullingLimit = -400\n"
                    "       alignToTerrainNormal = False\n"
                    "       collideable = True\n"
                    "       maxObjects = 40000\n"
                    "       collisionMesh = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/trunk\n"
                    "       SubdivisionSettings\n"
                    "       {\n"
                    "           subdivisionLevel = 1\n"
                    "           subdivisionRangeMode = FixedRange\n"
                    "           subdivisionRange = 12500\n"
                    "           minimumSubdivision = 8\n"
                    "       }\n"
                    "       DistributionNoise\n"
                    "       {\n"
                    "           mode = Persistent\n"
                    "           _Frequency = 200\n"
                    "           _Persistence = 0.300000012\n"
                    "           _Lacunarity = 2\n"
                    "           _Octaves = 6\n"
                    "           _Seed = " + str(pSctrRNG.randint(0,10000)) + "\n"
                    "           _NoiseType = 1\n"
                    "           _NoiseQuality = Standard\n"
                    "       }\n"
                    "       Distribution\n"
                    "       {\n"
                    "           _Seed = 62.1199989\n"
                    "           _SpawnChance = 0.01\n"
                    "           _Range = 10500\n"
                    "           _PopulationMultiplier = "+ str((1/radiusDiv)/radiusDiv) + "\n"
                    "           _SizeNoiseStrength = 0.75\n"
                    "           _MinScale = 1,1,1\n"
                    "           _MaxScale = 200,200,200\n"
                    "           _CutoffScale = 0.550000012\n"
                    "           _SteepPower = 8\n"
                    "           _SteepContrast = 4.5\n"
                    "           _SteepMidpoint = 0.731000006\n"
                    "           _NormalDeviance = 0.5\n"
                    "           _MinAltitude = 0\n"
                    "           _MaxAltitude = 20000\n"
                    "           _RangePow = 250\n"
                    "           LODs\n"
                    "           {\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/trunk1\n"
                    "                   _MainTex = parent\n"
                    "                   range = 2500\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/farside\n"
                    "                   _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/treeside.dds\n"
                    "                   _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/treeside_nrm.dds\n"
                    "                   range = 10000\n"
                    "                   billboard = True\n"
                    "               }\n"
                    "           }\n"
                    "       }\n"
                    "       Material\n"
                    "       {\n"
                    "           shader = Custom/InstancedCutout\n"
                    "           _MainColor = 1,1,1,1\n"
                    "           _SubColor = 1,1,1,1\n"
                    "           _ColorNoiseStrength = 1\n"
                    "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/trunkclr.dds\n"
                    "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/trunknrm.dds\n"
                    "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                    "           _WaveSpeed = 0\n"
                    "           _WaveAmp = 0.0399999991\n"
                    "           _HeightCutoff = -0.898999989\n"
                    "           _HeightFactor = 2.25999999\n"
                    "           _Metallic = 0.5\n"
                    "           _Gloss = 5\n"
                    "           _Hapke = 1\n"
                    "           _Cutoff = 0.5\n"
                    "           _WindSpeed = 50,50,50\n"
                    "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                    "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                    "           _FresnelPower = 3\n"
                    "           _FresnelColor = 0.05,0.05,0.05\n"
                    "           _Transmission = 1\n"
                    "       }\n"
                    "       SubObjects\n"
                    "       {\n"
                    "       }\n"
                    "   }\n"
                    "   SharedScatter	//Share the same distribution data as the stupid big ass tree scatter\n"
                    "   {\n"
                    "       parent = BigTree\n"
                    "       name = BigTreeTop\n"
                    "       model = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/leaves\n"
                    "       Distribution\n"
                    "       {\n"
                    "           LODs\n"
                    "           {\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/leaves\n"
                    "                   _MainTex = parent\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "               LOD\n"
                    "               {\n"
                    "                   model = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/fartop\n"
                    "                   _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/treetop.dds\n"
                    "                   _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/treetop_nrm.dds\n"
                    "                   billboard = False\n"
                    "               }\n"
                    "           }\n"
                    "       }\n"
                    "       Material\n"
                    "       {\n"
                    "           shader = Custom/InstancedCutout\n"
                    "           _MainColor = 1,1,1,1\n"
                    "           _SubColor = 1,1,1,1\n"
                    "           _ColorNoiseStrength = 1\n"
                    "           _MainTex = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/leavesclr.dds\n"
                    "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Models/Special/BigTree/leavesnrm.dds\n"
                    "           _WindMap = Parallax_StockTextures/_Scatters/PluginData/grassuv2.dds\n"
                    "           _WaveSpeed = 0\n"
                    "           _WaveAmp = 0.0399999991\n"
                    "           _HeightCutoff = -0.898999989\n"
                    "           _HeightFactor = 2.25999999\n"
                    "           _Metallic = 0.5\n"
                    "           _Gloss = 5\n"
                    "           _Hapke = 1\n"
                    "           _Cutoff = 0.5\n"
                    "           _WindSpeed = 50,50,50\n"
                    "           _Color = " + str(lifeclr[0]) + "," + str(lifeclr[1]) + "," + str(lifeclr[2]) + "\n"
                    "           _MetallicTint = 0.100000001,0.100000001,0.100000001,1\n"
                    "           _FresnelPower = 3\n"
                    "           _FresnelColor = 0.05,0.05,0.05\n"
                    "           _Transmission = 1\n"
                    "       }\n"
                    "   }\n"
                )
        cfg.write(
            "}\n"
        )
    # This is required to make parallax scatters work lmfao
    def addToParallaxScatterFixCfg(cfg, planetName):
        cfg.write(
            "   @Body[" + planetName + "]\n"
            "   {\n"
            "       %PQS\n"
            "       {\n"
            "           %Mods\n"
            "           {\n"
            "               ParallaxScatter\n"
            "               {\n"
            "                   order = 999999\n"
            "               }\n"
            "               ScatterDistribute\n"
            "               {\n"
            "                   order = 999998\n"
            "               }\n"
            "           }\n"
            "       }\n"
            "   }\n"
        )
    # Generates disks for various thingamabobs.
    def generateDisks(body, diskRadius):
        diskObj = open(targetPath + "/Configs/" + body + "_JETS" + ".cfg","x")
        diskObj.write(
            "@Kopernicus\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + str(body) + "_JET1" + "\n"
            "        Tag = InfD_NeutronJets\n"
            "        Template\n"
            "        {\n"
            "            name = Jool\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            description = \n"
            "            radius = 1000\n"
            "            mass = 420\n"
            "            rotationPeriod = 420\n"
            "            initialRotation = 0\n"
            "            sphereOfInfluence = 1\n"
            "            selectable = False\n"
            "        }\n"
            "        Orbit\n"
            "        {\n"
            "            referenceBody = " + str(body) + "\n"
            "            semiMajorAxis = 1\n"
            "            period = 100000000000000000000000\n"
            "            argumentOfPeriapsis = 90\n"
            "            mode = 0\n"
            "            icon = NONE\n"
            "        }\n"
            "        Rings\n"
            "        {\n"
            "        \n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 2E+11\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronJet.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 90\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1260\n"
            "            }\n"
            "            // Disks\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -4\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1450\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1350\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 0\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1250\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1150\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 4\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1050\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "    Body\n"
            "    {\n"
            "        name = " + str(body) + "_JET2" + "\n"
            "        Tag = InfD_NeutronJets\n"
            "        Template\n"
            "        {\n"
            "            name = Jool\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            description = \n"
            "            radius = 1000\n"
            "            mass = 420\n"
            "            rotationPeriod = 420\n"
            "            initialRotation = 90\n"
            "            sphereOfInfluence = 1\n"
            "            selectable = False\n"
            "        }\n"
            "        Orbit\n"
            "        {\n"
            "            referenceBody = " + str(body) + "\n"
            "            semiMajorAxis = 1\n"
            "            period = 100000000000000000000000\n"
            "            argumentOfPeriapsis = 90\n"
            "            mode = 0\n"
            "            icon = NONE\n"
            "        }\n"
            "        Rings\n"
            "        {\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = 2E+11\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronJet.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 90\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1260\n"
            "            }\n"
            "            // Disks\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -4\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1450\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = -2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1350\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 0\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1250\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 2\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1150\n"
            "            }\n"
            "            Ring\n"
            "            {\n"
            "                innerRadius = 301\n"
            "                outerRadius = " + str(diskRadius) + "\n"
            "                steps = 10000\n"
            "                texture = InfiniteDiscoveries/Textures/Misc/neutronDisk.dds\n"
            "                tiles = 2\n"
            "                color = 1,1,1,1\n"
            "                unlit = True\n"
            "                useNewShader = False\n"
            "                penumbraMultiplier = 10\n"
            "                angle = 4\n"
            "                longitudeOfAscendingNode = 0\n"
            "                lockRotation = False\n"
            "                rotationPeriod = 1050\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )
    # Generates names (DEPRECATED).
    #def generateName(type,seed):
    #    nameRNG = random.Random()
    #    nameRNG.seed(seed)
    #    #np.random.seed(seed)
    #    word1 = synonymList[type][nameRNG.randint(0,len(synonymList[type])-1)]
    #    word1Cut = word1[:-int(len(word1)/2)]
    #    word2 = synonymList[type][nameRNG.randint(0,len(synonymList[type])-1)]
    #    word2Cut = word2[:int(len(word2)/2)]
    #    finalWord = word1Cut + word2Cut
    #    dispName = finalWord.replace(" ", "").replace("-", "").replace("'", "").capitalize()
#
    #    return dispName
    # Adds a subdivision fix for Parallax support.
    def addSubdividerFix(subdFixCfg, planetName):
        subdFixCfg.write(
            "   @Body[" + planetName + "]\n"
            "   {\n"
            "       %PQS\n"
            "       {\n"
            "           %Mods\n"
            "           {\n"
            "               Subdivide\n"
            "               {\n"
            "                   subdivisionLevel = 36\n"
            "                   subdivisionRadius = 150\n"
            "                   //advancedSubdivisionLevel = 64\n"
            "                   order = 999999\n"
            "               }\n"
            "           }\n"
            "       }\n"
            "   }\n"
        )
    # Writes the actual Parallax config.
    def addToParallaxCfg(seed, parallaxCfg, planetName, lava, lavaClr, groundType, icy):
        ParallaxRNG = random.Random()
        ParallaxRNG.seed(seed)

        #                [Name, [Variant, Scale, Displacement].
        allGroundTypes = [["Gravel",[[1,1,0.075]]],
                          ["Sand",[[1,1,0.075]]],
                          ["Rock",[[1,1.25,0.05]]],
                          ["Ice",[[1,1,0.05]]]]
        groundChoice = allGroundTypes[groundType][0]
        variantList = allGroundTypes[groundType][1]
        possibleValues = len(variantList)
        randomVar = ParallaxRNG.randint(0,possibleValues-1)

        allActions.append([time.localtime(),"Writing parallax config for : " + planetName])

        global allActionArrayUpdated
        allActionArrayUpdated = True
        if lava == False:
            parallaxCfg.write(
                "    Body\n"
                "    {\n"
                "        name = " + planetName + "\n"
                "        emissive = false\n"
                "        Textures\n"
                "        {\n"
                "            _SurfaceTextureScale = " + str(allGroundTypes[groundType][1][randomVar][1]) + "\n"
                "    \n"
                "            _SurfaceTexture = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/CLR.dds\n"
                "            _SurfaceTextureMid = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/CLR.dds\n"
                "            _SurfaceTextureHigh = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/CLR.dds\n"
                "            _SteepTex = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/CLR.dds\n"
                "    \n"
                "            _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/NRM.dds\n"
                "            _BumpMapMid = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/NRM.dds\n"
                "            _BumpMapHigh = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/NRM.dds\n"
                "            _BumpMapSteep = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/NRM.dds\n"
                "    \n"
                "            _DispTex = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/DSP.dds\n"
                "            _InfluenceMap = InfiniteDiscoveries/Visuals/Parallax/Textures/" + groundChoice + "/Var" + str(randomVar+1) + "/INF.dds\n"
                "    \n"
                "            _displacement_scale = " + str(allGroundTypes[groundType][1][randomVar][2]) + "\n"
                "            _displacement_offset = 0\n"
                "    \n"
                "            _SteepPower = 4\n"
                "            _SteepContrast = 4\n"
                "            _SteepMidpoint = 0.6\n"
                "    \n"
            )
            if icy == True:
                parallaxCfg.write(
                    "            _Metallic = 1\n"
                    "            _MetallicTint = 0.6,0.6,0.6\n"
                    "            _Gloss = 60\n"
                    "            _NormalSpecularInfluence = 0.75\n"
                )
            else:
                parallaxCfg.write(
                    "            _Metallic = 0.08\n"
                    "            _MetallicTint = 0.6,0.6,0.6\n"
                    "            _Gloss = 22\n"
                    "            _NormalSpecularInfluence = 1\n"
                )
            parallaxCfg.write(
                "            _Hapke = 1\n"
                "            _EmissionColor = 0, 0, 0\n"
                "    \n"
                "            _FresnelColor = 0.1,0.1,0.1\n"
                "            _FresnelPower = 3\n"
                "    \n"
                "            _LowStart = 0\n"
                "            _LowEnd = 1\n"
                "            _HighStart = 3000\n"
                "            _HighEnd = 3350\n"
                "        }\n"
                "    }\n"
            )
        elif lava == True:
            parallaxCfg.write(
                "   Body\n"
                "   {\n"
                "       name = " + planetName + "\n"
                "       emissive = true\n"
                "       Textures\n"
                "       {\n"
                "           _SurfaceTextureScale = 0.5\n"
                "   \n"
                "           _SurfaceTexture = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/CLR.dds\n"
                "           _SurfaceTextureMid = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/CLR.dds\n"
                "           _SurfaceTextureHigh = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/CLR.dds\n"
                "           _SteepTex = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/CLR.dds\n"
                "   \n"
                "           _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/NRM_E.dds\n"
                "           _BumpMapMid = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/NRM.dds\n"
                "           _BumpMapHigh = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/NRM.dds\n"
                "           _BumpMapSteep = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/NRM.dds\n"
                "   \n"
                "           _DispTex = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/DSP.dds\n"
                "           _InfluenceMap = InfiniteDiscoveries/Visuals/Parallax/Textures/Lava/Var1/INF.dds\n"
                "   \n"
                "           _displacement_scale = 0.05\n"
                "           _displacement_offset = 0\n"
                "   \n"
                "           _SteepPower = 14\n"
                "           _SteepContrast = 4\n"
                "           _SteepMidpoint = 0.6\n"
                "   \n"
                "           _Metallic = 0.08\n"
                "           _MetallicTint = 0.6,0.6,0.6\n"
                "           _Gloss = 22\n"
                "           _NormalSpecularInfluence = 1\n"
                "           _Hapke = 1\n"
                "           _EmissionColor = " +  str(lavaClr[0]) + ", " + str(lavaClr[1]) + ", " + str(lavaClr[2]) + "\n"
                "   \n"
                "           _FresnelColor = 0.1,0.1,0.1\n"
                "           _FresnelPower = 3\n"
                "   \n"
                "           _LowStart = 0\n"
                "           _LowEnd = 1200\n"
                "           _HighStart = 3000\n"
                "           _HighEnd = 3350\n"
                "       }\n"
                "   }\n"
            )
    # Makes EVE aurorae
    def addToEVEAurora(eveCfg, planetName, auroraBright, auroraClr):
        eveCfg.write(
            "    OBJECT\n"
            "    {\n"
            "        name = " + planetName + "_AURORAE" + "\n"
            "        body = " + planetName + "\n"
            "        altitude = 15000\n"
            "        settings\n"
            "        {\n"
            "            _Color = " + str(auroraClr[0]) + ", " + str(auroraClr[1]) + ", " + str(auroraClr[2]) + ", " + str(auroraBright) + "\n"
            "            _UVNoiseScale = 0.1\n"
            "            _UVNoiseStrength = 0.01\n"
            "            _MainTex\n"
            "            {\n"
            "                value = InfiniteDiscoveries/Presets/Aurora1\n"
            "            }\n"
            "            _UVNoiseTex\n"
            "            {\n"
            "                value = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
            "            }\n"
            "        }\n"
            "        layer2D\n"
            "        {\n"
            "            macroCloudMaterial\n"
            "            {\n"
            "                _MinLight = 1\n"
            "                _RimDistSub = 0.0001\n"
            "            }\n"
            "        }\n"
            "    }\n"
        )
    # Adds a PQS fix to gas giants so that they can have EVE clouds applied.
    def addPQSFix(evePQSCfg, planetName):
        evePQSCfg.write(
            "    OBJECT\n"
            "    {\n"
            "        body = " + planetName + "\n"
            "        deactivateDistance = 175000\n"
            "        overrideKillSphere:NEEDS[Infinite_VolumetricClouds]\n"
            "        {\n"
            "            altitude = -75000\n"
            "        }\n"
            "    }\n"
        )
    # Adds a body to the system's Eve config (but volumetric...)
    def addToVolumetricEveCfg(cloudRNG, eveCfg, cloudTexNum, planetName, locked, oceanic, gasGiant=None):
        volumeRNG = random.Random()
        volumeRNG.seed(cloudRNG)
        allActions.append([time.localtime(),"Writing volumetric EVE config for : " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        if cloudTexNum == 3:
            contrast = 0.9
        else:
            contrast = 0.5
        
        if locked == True:
            density = 0.001
        else:
            density = 0.05
        if gasGiant == None:
            if locked == True:
                eveCfg.write(
                    "    OBJECT\n"
                    "    {\n"
                    "        name = " + planetName + "_CLOUDS" + "\n"
                    "        body = " + planetName + "\n"
                    "        altitude = 6000\n"
                    "        detailSpeed = 0,6,0\n"
                    "        offset = 90,0,0\n"
                    "        settings\n"
                    "        {\n"
                    "            _DetailTex = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                    "            _DetailScale = 30\n"
                    "            _UVNoiseTex = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
                    "            _Color = 255,255,255, 255\n"
                    "            _UVNoiseStrength = 0.00050000001\n"
                    "            _MainTex\n"
                    "            {\n"
                    "                value = Infinite_VolumetricClouds/Textures/LockedClouds" + str(cloudTexNum) + "\n"
                    "                type = AlphaMap\n"
                    "                alphaMask = ALPHAMAP_R\n"
                    "            }\n"
                    "            _FlowMap\n"
                    "            {\n"
                    "            }\n"
                    "        }\n"
                    "        layer2D\n"
                    "        {\n"
                    "            shadowMaterial\n"
                    "            {\n"
                    "            }\n"
                    "            macroCloudMaterial\n"
                    "            {\n"
                    "                _DetailDist = 2E-06\n"
                    "            }\n"
                    "        }\n"
                    "        layerRaymarchedVolume\n"
                    "        {\n"
                    "            color = 255, 255, 255 255\n"
                    "            detailNoiseTiling = 785\n"
                    "            upwardsCloudSpeed = 5\n"
                    "            scaledFadeStartAltitude = 500000\n"
                    "            scaledFadeEndAltitude = 600000\n"
                    "            skylightTintMultiplier = 3\n"
                    "            raymarchingSettings\n"
                    "            {\n"
                    "            }\n"
                    "            noise\n"
                    "            {\n"
                    "                worley\n"
                    "                {\n"
                    "                    octaves = 8\n"
                    "                    periods = 3\n"
                    "                    brightness = 1.3\n"
                    "                    lift = 0.5\n"
                    "                    contrast = " + str(contrast) + "\n"
                    "                }\n"
                    "            }\n"
                    "            coverageMap\n"
                    "            {\n"
                    "                value = Infinite_VolumetricClouds/Textures/LockedClouds" + str(cloudTexNum) + "_coverage\n"
                    "                type = AlphaMap\n"
                    "                alphaMask = ALPHAMAP_R\n"
                    "            }\n"
                    "            cloudTypeMap\n"
                    "            {\n"
                    "                value = Infinite_VolumetricClouds/Textures/cloud_types\n"
                    "            }\n"
                    "            cloudTypes\n"
                    "            {\n"
                    "                Item\n"
                    "                {\n"
                    "                    typeName = Stratus\n"
                    "                    minAltitude = 5000\n"
                    "                    maxAltitude = 9000\n"
                    "                    interpolateCloudHeights = true\n"
                    "                    baseNoiseTiling = 1852\n"
                    "                    detailNoiseStrength = 0.2\n"
                    "                    lightningFrequency = " + str(0) + "\n"
                    "                    coverageCurve\n"
                    "                    {\n"
                    "                        key = 0 0.007974625 3.048113 3.048113\n"
                    "                        key = 0.3081625 0.9472886 0.8252979 0.8252979\n"
                    "                        key = 0.9876099 -0.002250671 -1.397517 -1.397517\n"
                    "                    }\n"
                    "                }\n"
                    "                Item\n"
                    "                {\n"
                    "                    typeName = Cumulus 1\n"
                    "                    minAltitude = 5000\n"
                    "                    maxAltitude = 6000\n"
                    "                    baseNoiseTiling = 1852\n"
                    "                    density = 0.05\n"
                    "                    detailNoiseStrength = 0.1\n"
                    "                    lightningFrequency = " + str(volumeRNG.randint(0,2)/10) + "\n"
                    "                    coverageCurve\n"
                    "                    {\n"
                    "                        key = 0.01728953 -0.004032524 1.633945 1.633945\n"
                    "                        key = 0.2118766 0.9367786 0.06669102 0.06669102\n"
                    "                        key = 0.9732781 -0.006797761 -0.5550035 -0.5550035\n"
                    "                    }\n"
                    "                }\n"
                    "                Item\n"
                    "                {\n"
                    "                    typeName = Cumulonimbus\n"
                    "                    minAltitude = 5000\n"
                    "                    maxAltitude = 11000\n"
                    "                    detailNoiseStrength = 0.3\n"
                    "                    density = 0.05\n"
                    "                    interpolateCloudHeights = False\n"
                    "                    lightningFrequency = " + str(volumeRNG.randint(0,20)/10) + "\n"
                    "                    coverageCurve\n"
                    "                    {\n"
                    "                        key = 0 0 0 0\n"
                    "                        key = 0.03 1 0 -1\n"
                    "                        key = 0.6 0.8 1.5 2\n"
                    "                        key = 0.7 1 2 5\n"
                    "                        key = 0.8 1 -5 -5\n"
                    "                        key = 1 0 0 0\n"
                    "                    }\n"
                    "                }\n"
                    "            }\n"
                    "            detailNoise\n"
                    "            {\n"
                    "            }\n"
                    "            lightning\n"
                    "            {\n"
                    "                lightningConfig = lightning\n"
                    "            }\n"
                    "        }\n"
                    "    }\n"
                )
                if oceanic == True or volumeRNG.randint(0,4) == 0:
                    eveCfg.write(
                        "    OBJECT\n"
                        "    {\n"
                        "        name = " + planetName + "_RAIN" + "\n"
                        "        body = " + planetName + "\n"
                        "        altitude = 6000\n"
                        "        detailSpeed = 0,6,0\n"
                        "        settings\n"
                        "        {\n"
                        "            _DetailTex = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                        "            _DetailScale = 30\n"
                        "            _UVNoiseTex = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
                        "            _Color = 255,255,255, 255\n"
                        "            _UVNoiseStrength = 0.00050000001\n"
                        "            _MainTex\n"
                        "            {\n"
                        "                value = Infinite_VolumetricClouds/Textures/Clouds" + str(cloudTexNum) + "\n"
                        "                type = AlphaMap\n"
                        "                alphaMask = ALPHAMAP_R\n"
                        "            }\n"
                        "            _FlowMap\n"
                        "            {\n"
                        "            }\n"
                        "        }\n"
                        "        layerRaymarchedVolume\n"
                        "        {\n"
                        "            color = 128, 128, 128 255\n"
                        "            detailNoiseTiling = 785\n"
                        "            upwardsCloudSpeed = -10\n"
                        "            scaledFadeStartAltitude = 500000\n"
                        "            scaledFadeEndAltitude = 600000\n"
                        "            skylightTintMultiplier = 3\n"
                        "            raymarchingSettings\n"
                        "            {\n"
                        "               baseStepSize = 450\n"
                        "            }\n"
                        "            noise\n"
                        "            {\n"
                        "                worley\n"
                        "                {\n"
                        "                    octaves = 8\n"
                        "                    periods = 3\n"
                        "                    brightness = 1\n"
                        "                    lift = 0.5\n"
                        "                    contrast = 0.2\n"
                        "                }\n"
                        "            }\n"
                        "            coverageMap\n"
                        "            {\n"
                        "                value = Infinite_VolumetricClouds/Textures/Clouds" + str(cloudTexNum) + "_coverage\n"
                        "                type = AlphaMap\n"
                        "                alphaMask = ALPHAMAP_R\n"
                        "            }\n"
                        "            cloudTypeMap\n"
                        "            {\n"
                        "                value = Infinite_VolumetricClouds/Textures/cloud_types\n"
                        "            }\n"
                        "            cloudTypes\n"
                        "            {\n"
                        "                Item\n"
                        "                {\n"
                        "                    typeName = norain\n"
                        "                    maxAltitude = 6000\n"
                        "                    density = 0\n"
                        "                    particleFieldDensity = 0\n"
                        "                    coverageCurve\n"
                        "                    {\n"
                        "                        key = 0 1 0 0\n"
                        "                        key = 0.5 1 0 0\n"
                        "                        key = 1 0.8 0 0\n"
                        "                    }\n"
                        "                }\n"
                        "                Item\n"
                        "                {\n"
                        "                    typeName = norain\n"
                        "                    maxAltitude = 6000\n"
                        "                    density = 0\n"
                        "                    coverageCurve\n"
                        "                    {\n"
                        "                        key = 0 1 0 0\n"
                        "                        key = 0.5 1 0 0\n"
                        "                        key = 1 0.8 0 0\n"
                        "                    }\n"
                        "                }\n"
                        "                Item\n"
                        "                {\n"
                        "                    typeName = rain\n"
                        "                    maxAltitude = 6000\n"
                        "                    density = 0.002\n"
                        "                    ambientVolume = 5\n"
                        "                    baseNoiseTiling = 1\n"
                        "                    detailNoiseStrength = 0\n"
                        "                    coverageCurve\n"
                        "                    {\n"
                        "                        key = 0 1 0 0\n"
                        "                        key = 0.5 1 0 0\n"
                        "                        key = 1 0.8 0 0\n"
                        "                    }\n"
                        "                }\n"
                        "            }\n"
                        "            detailNoise\n"
                        "            {\n"
                        "            }\n"
                        "            lightning\n"
                        "            {\n"
                        "                lightningConfig = lightning\n"
                        "            }\n"
                        "            particleField\n"
                        "            {\n"
                        "                particleFieldConfig = rain\n"
                        "            }\n"
                        "            ambientSound\n"
                        "            {\n"
                        "                soundName = Infinite_VolumetricClouds/Audio/rain\n"
                        "            }\n"
                        "        }\n"
                        "    }\n"
                    )
            else:
                eveCfg.write(
                    "    OBJECT\n"
                    "    {\n"
                    "        name = " + planetName + "_CLOUDS" + "\n"
                    "        body = " + planetName + "\n"
                    "        altitude = 6000\n"
                    "        detailSpeed = 0,6,0\n"
                    "        settings\n"
                    "        {\n"
                    "            _DetailTex = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                    "            _DetailScale = 30\n"
                    "            _UVNoiseTex = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
                    "            _Color = 255,255,255, 255\n"
                    "            _UVNoiseStrength = 0.00050000001\n"
                    "            _MainTex\n"
                    "            {\n"
                    "                value = Infinite_VolumetricClouds/Textures/Clouds" + str(cloudTexNum) + "\n"
                    "                type = AlphaMap\n"
                    "                alphaMask = ALPHAMAP_R\n"
                    "            }\n"
                    "            _FlowMap\n"
                    "            {\n"
                    "            }\n"
                    "        }\n"
                    "        layer2D\n"
                    "        {\n"
                    "            shadowMaterial\n"
                    "            {\n"
                    "            }\n"
                    "            macroCloudMaterial\n"
                    "            {\n"
                    "                _DetailDist = 2E-06\n"
                    "            }\n"
                    "        }\n"
                    "        layerRaymarchedVolume\n"
                    "        {\n"
                    "            color = 255, 255, 255 255\n"
                    "            detailNoiseTiling = 785\n"
                    "            upwardsCloudSpeed = 5\n"
                    "            scaledFadeStartAltitude = 500000\n"
                    "            scaledFadeEndAltitude = 600000\n"
                    "            skylightTintMultiplier = 3\n"
                    "            raymarchingSettings\n"
                    "            {\n"
                    "            }\n"
                    "            noise\n"
                    "            {\n"
                    "                worley\n"
                    "                {\n"
                    "                    octaves = 8\n"
                    "                    periods = 3\n"
                    "                    brightness = 1.3\n"
                    "                    lift = 0.5\n"
                    "                    contrast = " + str(contrast) + "\n"
                    "                }\n"
                    "            }\n"
                    "            coverageMap\n"
                    "            {\n"
                    "                value = Infinite_VolumetricClouds/Textures/Clouds" + str(cloudTexNum) + "_coverage\n"
                    "                type = AlphaMap\n"
                    "                alphaMask = ALPHAMAP_R\n"
                    "            }\n"
                    "            cloudTypeMap\n"
                    "            {\n"
                    "                value = Infinite_VolumetricClouds/Textures/cloud_types\n"
                    "            }\n"
                    "            cloudTypes\n"
                    "            {\n"
                    "                Item\n"
                    "                {\n"
                    "                    typeName = Stratus\n"
                    "                    minAltitude = 5000\n"
                    "                    maxAltitude = 9000\n"
                    "                    interpolateCloudHeights = true\n"
                    "                    baseNoiseTiling = 1852\n"
                    "                    detailNoiseStrength = 0.2\n"
                    "                    lightningFrequency = " + str(0) + "\n"
                    "                    coverageCurve\n"
                    "                    {\n"
                    "                        key = 0 0.007974625 3.048113 3.048113\n"
                    "                        key = 0.3081625 0.9472886 0.8252979 0.8252979\n"
                    "                        key = 0.9876099 -0.002250671 -1.397517 -1.397517\n"
                    "                    }\n"
                    "                }\n"
                    "                Item\n"
                    "                {\n"
                    "                    typeName = Cumulus 1\n"
                    "                    minAltitude = 5000\n"
                    "                    maxAltitude = 6000\n"
                    "                    baseNoiseTiling = 1852\n"
                    "                    density = 0.05\n"
                    "                    detailNoiseStrength = 0.1\n"
                    "                    lightningFrequency = " + str(volumeRNG.randint(0,2)/10) + "\n"
                    "                    coverageCurve\n"
                    "                    {\n"
                    "                        key = 0.01728953 -0.004032524 1.633945 1.633945\n"
                    "                        key = 0.2118766 0.9367786 0.06669102 0.06669102\n"
                    "                        key = 0.9732781 -0.006797761 -0.5550035 -0.5550035\n"
                    "                    }\n"
                    "                }\n"
                    "                Item\n"
                    "                {\n"
                    "                    typeName = Cumulonimbus\n"
                    "                    minAltitude = 5000\n"
                    "                    maxAltitude = 11000\n"
                    "                    detailNoiseStrength = 0.3\n"
                    "                    density = 0.05\n"
                    "                    interpolateCloudHeights = False\n"
                    "                    lightningFrequency = " + str(volumeRNG.randint(0,20)/10) + "\n"
                    "                    coverageCurve\n"
                    "                    {\n"
                    "                        key = 0 0 0 0\n"
                    "                        key = 0.03 1 0 -1\n"
                    "                        key = 0.6 0.8 1.5 2\n"
                    "                        key = 0.7 1 2 5\n"
                    "                        key = 0.8 1 -5 -5\n"
                    "                        key = 1 0 0 0\n"
                    "                    }\n"
                    "                }\n"
                    "            }\n"
                    "            detailNoise\n"
                    "            {\n"
                    "            }\n"
                    "            lightning\n"
                    "            {\n"
                    "                lightningConfig = lightning\n"
                    "            }\n"
                    "        }\n"
                    "    }\n"
                )
                if oceanic == True or volumeRNG.randint(0,4) == 0:
                    eveCfg.write(
                        "    OBJECT\n"
                        "    {\n"
                        "        name = " + planetName + "_RAIN" + "\n"
                        "        body = " + planetName + "\n"
                        "        altitude = 6000\n"
                        "        detailSpeed = 0,6,0\n"
                        "        settings\n"
                        "        {\n"
                        "            _DetailTex = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                        "            _DetailScale = 30\n"
                        "            _UVNoiseTex = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
                        "            _Color = 255,255,255, 255\n"
                        "            _UVNoiseStrength = 0.00050000001\n"
                        "            _MainTex\n"
                        "            {\n"
                        "                value = Infinite_VolumetricClouds/Textures/Clouds" + str(cloudTexNum) + "\n"
                        "                type = AlphaMap\n"
                        "                alphaMask = ALPHAMAP_R\n"
                        "            }\n"
                        "            _FlowMap\n"
                        "            {\n"
                        "            }\n"
                        "        }\n"
                        "        layerRaymarchedVolume\n"
                        "        {\n"
                        "            color = 128, 128, 128 255\n"
                        "            detailNoiseTiling = 785\n"
                        "            upwardsCloudSpeed = -10\n"
                        "            scaledFadeStartAltitude = 500000\n"
                        "            scaledFadeEndAltitude = 600000\n"
                        "            skylightTintMultiplier = 3\n"
                        "            raymarchingSettings\n"
                        "            {\n"
                        "            }\n"
                        "            noise\n"
                        "            {\n"
                        "                worley\n"
                        "                {\n"
                        "                    octaves = 8\n"
                        "                    periods = 3\n"
                        "                    brightness = 1\n"
                        "                    lift = 0.5\n"
                        "                    contrast = 1\n"
                        "                }\n"
                        "            }\n"
                        "            coverageMap\n"
                        "            {\n"
                        "                value = Infinite_VolumetricClouds/Textures/Clouds" + str(cloudTexNum) + "_coverage\n"
                        "                type = AlphaMap\n"
                        "                alphaMask = ALPHAMAP_R\n"
                        "            }\n"
                        "            cloudTypeMap\n"
                        "            {\n"
                        "                value = Infinite_VolumetricClouds/Textures/cloud_types\n"
                        "            }\n"
                        "            cloudTypes\n"
                        "            {\n"
                        "                Item\n"
                        "                {\n"
                        "                    typeName = norain\n"
                        "                    maxAltitude = 6000\n"
                        "                    density = 0\n"
                        "                    particleFieldDensity = 0\n"
                        "                    coverageCurve\n"
                        "                    {\n"
                        "                        key = 0 1 0 0\n"
                        "                        key = 0.5 1 0 0\n"
                        "                        key = 1 0.8 0 0\n"
                        "                    }\n"
                        "                }\n"
                        "                Item\n"
                        "                {\n"
                        "                    typeName = norain\n"
                        "                    maxAltitude = 6000\n"
                        "                    density = 0\n"
                        "                    coverageCurve\n"
                        "                    {\n"
                        "                        key = 0 1 0 0\n"
                        "                        key = 0.5 1 0 0\n"
                        "                        key = 1 0.8 0 0\n"
                        "                    }\n"
                        "                }\n"
                        "                Item\n"
                        "                {\n"
                        "                    typeName = rain\n"
                        "                    maxAltitude = 6000\n"
                        "                    density = 0.002\n"
                        "                    ambientVolume = 5\n"
                        "                    baseNoiseTiling = 1\n"
                        "                    detailNoiseStrength = 0\n"
                        "                    coverageCurve\n"
                        "                    {\n"
                        "                        key = 0 1 0 0\n"
                        "                        key = 0.5 1 0 0\n"
                        "                        key = 1 0.8 0 0\n"
                        "                    }\n"
                        "                }\n"
                        "            }\n"
                        "            detailNoise\n"
                        "            {\n"
                        "            }\n"
                        "            lightning\n"
                        "            {\n"
                        "                lightningConfig = lightning\n"
                        "            }\n"
                        "            particleField\n"
                        "            {\n"
                        "                particleFieldConfig = rain\n"
                        "            }\n"
                        "            ambientSound\n"
                        "            {\n"
                        "                soundName = Infinite_VolumetricClouds/Audio/rain\n"
                        "            }\n"
                        "        }\n"
                        "    }\n"
                    )
        else:
            eveCfg.write(
                "    OBJECT\n"
                "    {\n"
                "        name = " + planetName + "_CLOUDS" + "\n"
                "        body = " + planetName + "\n"
                "        altitude = 6000\n"
                "        detailSpeed = 0,6,0\n"
                "        settings\n"
                "        {\n"
                "            _DetailTex = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                "            _DetailScale = 30\n"
                "            _Color = 255,255,255, 255\n"
                "            _MainTex\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Textures/Clouds/" + str(gasGiant) + "_CLOUDS\n"
                "            }\n"
                "            _FlowMap\n"
                "            {\n"
                "				 texture = Infinite_VolumetricClouds/Textures/FlowMap\n"
				"                speed = 0.01\n"
                "                displacement = 0.5\n"
                "            }\n"
                "        }\n"
                "        layer2D\n"
                "        {\n"
                "            shadowMaterial\n"
                "            {\n"
                "            }\n"
                "            macroCloudMaterial\n"
                "            {\n"
                "                _DetailDist = 2E-06\n"
                "            }\n"
                "        }\n"
                "        layerRaymarchedVolume\n"
                "        {\n"
                "            color = 255, 255, 255 255\n"
                "            detailNoiseTiling = 4000\n"
                "            upwardsCloudSpeed = 5\n"
                "            scaledFadeStartAltitude = 500000\n"
                "            scaledFadeEndAltitude = 600000\n"
                "            skylightTintMultiplier = 3\n"
                "            raymarchingSettings\n"
                "            {\n"
                "            }\n"
                "            noise\n"
                "            {\n"
                "                worley\n"
                "                {\n"
                "                    octaves = 8\n"
                "                    brightness = 1.4\n"
                "                    lift = 0.5\n"
                "                    periods = 3\n"
                "                    contrast = 0.4\n"
                "                }\n"
                "            }\n"
                "            coverageMap\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Textures/Clouds/" + str(gasGiant) + "_CLOUDS\n"
                "                type = AlphaMap\n"
                "                alphaMask = ALPHAMAP_R\n"
                "            }\n"
                "            cloudTypeMap\n"
                "            {\n"
                "                value = Infinite_VolumetricClouds/Textures/cloud_types\n"
                "            }\n"
                "            cloudTypes\n"
                "            {\n"
                "                Item\n"
                "                {\n"
                "                    typeName = Stratus\n"
                "                    interpolateCloudHeights = true\n"
                "                    baseNoiseTiling = 50000\n"
                "                    detailNoiseStrength = 0.2\n"
                "                    lightningFrequency = 10\n"
                "                    minAltitude = -100000\n"
                "                    density = 0.8\n"
                "                    maxAltitude = 15000\n"
                "                    coverageCurve\n"
                "                    {\n"
                "                        key = 0 0.007974625 3.048113 3.048113\n"
                "                        key = 0.3081625 0.9472886 0.8252979 0.8252979\n"
                "                        key = 0.9876099 -0.002250671 -1.397517 -1.397517\n"
                "                    }\n"
                "                }\n"
                "                Item\n"
                "                {\n"
                "                    typeName = Cumulus 1\n"
                "                    baseNoiseTiling = 50000\n"
                "                    detailNoiseStrength = 0.1\n"
                "                    maxAltitude = 15000\n"
                "                    lightningFrequency = 10\n"
                "                    density = 0.8\n"
                "                    minAltitude = -100000\n"
                "                    coverageCurve\n"
                "                    {\n"
                "                        key = 0 0 0 0\n"
                "                        key = 0.05 1 0 0\n"
                "                        key = 0.1 0 0 0\n"
                "                        key = 0.7 1 0 0\n"
                "                        key = 1 0 0 0\n"
                "                    }\n"
                "                }\n"
                "                Item\n"
                "                {\n"
                "                    typeName = Cumulonimbus\n"
                "                    maxAltitude = 15000\n"
                "                    detailNoiseStrength = 0.3\n"
                "                    interpolateCloudHeights = False\n"
                "                    lightningFrequency = 10\n"
                "                    baseNoiseTiling = 50000\n"
                "                    minAltitude = -100000\n"
                "                    coverageCurve\n"
                "                    {\n"
                "                        key = 0 0 0 0\n"
                "                        key = 0.05 0 0 0\n"
                "                        key = 0.1 0 0 0\n"
                "                        key = 0.7 1 0 0\n"
                "                        key = 1 0 0 0\n"
                "                    }\n"
                "                }\n"
                "            }\n"
                "            detailNoise\n"
                "            {\n"
                "            }\n"
                "            lightning\n"
                "            {\n"
                "                lightningConfig = lightning\n"
                "            }\n"
                "            cloudColorMap\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Textures/Clouds/" + str(gasGiant) + "_CLOUDS\n"
                "            }\n"
                "        }\n"
                "    }\n"
            )
    # Adds a body to the system's EVE config.
    def addToEVECfg(eveCfg, cloudTexNum, planetName, locked, gasGiant=None):
        allActions.append([time.localtime(),"Writing EVE config for : " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        if gasGiant == None:
            if locked == True:
                eveCfg.write(
                    "OBJECT\n"
                    "{\n"
                    "    name = " + planetName + "_CLOUDS" + "\n"
                    "    body = " + planetName + "\n"
                    "    altitude = 10000\n"
                    "    offset = -90,0,0\n"
                    "    settings\n"
                    "    {\n"
                    "        _UVNoiseScale = 0.02\n"
                    "        _UVNoiseStrength = 0.002\n"
                    "        _MainTex\n"
                    "        {\n"
                    "            value = InfiniteDiscoveries/Presets/LockedClouds" + str(cloudTexNum) + "\n"
                    "        }\n"
                    "        _DetailTex\n"
                    "        {\n"
                    "            value = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                    "        }\n"
                    "        _UVNoiseTex\n"
                    "        {\n"
                    "            value = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
                    "        }\n"
                    "    }\n"
                    "    layerVolume\n"
                    "    {\n"
                    "        maxTranslation = 100,200,100\n"
                    "        size = 2000,2.2\n"
                    "        area = 18000,4\n"
                    "        noiseScale = 1.2,1.3,90\n"
                    "        particleMaterial\n"
                    "        {\n"
                    "            _LightScatter = 0.1\n"
                    "            _BumpMap = InfiniteDiscoveries/Visuals/EVE/particle/particle_NRM\n"
                    "            _Opacity = 0.5\n"
                    "            _MinScatter = 0.5\n"
                    "            _Tex\n"
                    "            {\n"
                    "                value = InfiniteDiscoveries/Visuals/EVE/particle/rgb\n"
                    "            }\n"
                    "        }\n"
                    "    }\n"
                    "    layer2D\n"
                    "    {\n"
                    "        macroCloudMaterial\n"
                    "        {\n"
                    "            _RimDistSub = 0.0001\n"
                    "        }\n"
                    "    }\n"
                    "}\n"
                )
            else:
                eveCfg.write(
                    "    OBJECT\n"
                    "    {\n"
                    "        name = " + planetName + "_CLOUDS" + "\n"
                    "        body = " + planetName + "\n"
                    "        altitude = 10000\n"
                    "        settings\n"
                    "        {\n"
                    "            _MainTex\n"
                    "            {\n"
                    "                value = InfiniteDiscoveries/Presets/Clouds" + str(cloudTexNum) + "\n"
                    "            }\n"
                    "            _DetailTex\n"
                    "            {\n"
                    "                value = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                    "            }\n"
                    "            _UVNoiseTex\n"
                    "            {\n"
                    "                value = InfiniteDiscoveries/Visuals/EVE/uvnoise1\n"
                    "            }\n"
                    "        }\n"
                    "        layerVolume\n"
                    "        {\n"
                    "            maxTranslation = 100,200,100\n"
                    "            size = 2000,2.2\n"
                    "            area = 18000,4\n"
                    "            noiseScale = 1.2,1.3,90\n"
                    "            particleMaterial\n"
                    "            {\n"
                    "                _LightScatter = 0.1\n"
                    "                _BumpMap = InfiniteDiscoveries/Visuals/EVE/particle/particle_NRM\n"
                    "                _Opacity = 0.5\n"
                    "                _MinScatter = 0.5\n"
                    "                _Tex\n"
                    "                {\n"
                    "                    value = InfiniteDiscoveries/Visuals/EVE/particle/rgb\n"
                    "                }\n"
                    "            }\n"
                    "        }\n"
                    "        layer2D\n"
                    "        {\n"
                    "            macroCloudMaterial\n"
                    "            {\n"
                    "                _RimDistSub = 0.0001\n"
                    "            }\n"
                    "        }\n"
                    "    }\n"
                )
        else:
            eveCfg.write(
                "    OBJECT\n"
                "    {\n"
                "        name = " + planetName + "_CLOUDS" + "\n"
                "        body = " + planetName + "\n"
                "        speed = 0,1000,0\n"
                "        altitude = 10000\n"
                "        settings\n"
                "        {\n"
                "            _Color = 255,255,255,200\n"
                "            _UVNoiseStrength = 0.005\n"
                "            _UVNoiseScale = 0.1\n"
                "            _UVNoiseAnimation = 0.2000000000,0.000000000\n"
                "            _MainTex\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Textures/Clouds/" + str(gasGiant) + "_CLOUDS\n"
                "            }\n"
                "            _DetailTex\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Visuals/EVE/detail1\n"
                "            }\n"
                "            _UVNoiseTex\n"
                "            {\n"
                "                value = InfiniteDiscoveries/Visuals/EVE/uvnoise2\n"
                "            }\n"
                "        }\n"
                "        layerVolume\n"
                "        {\n"
                "            maxTranslation = 100,200,100\n"
                "            size = 6000,2.2\n"
                "            area = 18000,4\n"
                "            noiseScale = 1.2,1.3,90\n"
                "            visibleRange = 10000\n"
                "            particleMaterial\n"
                "            {\n"
                "                _LightScatter = 0.1\n"
                "                _BumpMap = InfiniteDiscoveries/Visuals/EVE/particle/particle_NRM\n"
                "                _Opacity = 0.5\n"
                "                _MinScatter = 0.5\n"
                "                _Tex\n"
                "                {\n"
                "                    value = InfiniteDiscoveries/Visuals/EVE/particle/rgb\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "        layer2D\n"
                "        {\n"
                "            macroCloudMaterial\n"
                "            {\n"
                "            }\n"
                "        }\n"
                "    }\n"
            )
    # Adds a body to the system's scatterer ocean config.
    def addToOceanCfg(seed, oceanCfg, oceanR, oceanG, oceanB, planetName):
        oceanRNG = random.Random()
        oceanRNG.seed(seed)
        allActions.append([time.localtime(),"Writing scatterer ocean config for : " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        oceanCfg.write(
            "    Ocean\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        AMP = " + str(oceanRNG.randint(1,50)/10) + "\n"
            "        m_windSpeed = " + str(oceanRNG.randint(30,100)/10) + "\n"
            "        m_omega = 0.699999988\n"
            "        m_gravity = 0\n"
            "        maxWaveInteractionShipAltitude = 500\n"
            "        m_whiteCapStr = 0.319999993\n"
            "        shoreFoam = 1\n"
            "        m_farWhiteCapStr = 0.119999997\n"
            "        m_oceanUpwellingColor = " + str(oceanR/256) + ", " + str(oceanG/256) + ", " + str(oceanB/256) + "\n"
            "        m_UnderwaterColor = " + str(oceanR/256) + ", " + str(oceanG/256) + ", " + str(oceanB/256) + "\n"
            "        offScreenVertexStretch = 1.25\n"
            "        alphaRadius = 1400\n"
            "        transparencyDepth = 100\n"
            "        darknessDepth = 90\n"
            "        refractionIndex = 101.330002\n"
            "        skyReflectionStrength = 2\n"
            "        causticsTexturePath = \n"
            "        causticsLayer1Scale = 0,0\n"
            "        causticsLayer1Speed = 0,0\n"
            "        causticsLayer2Scale = 0,0\n"
            "        causticsLayer2Speed = 0,0\n"
            "        causticsMultiply = 0\n"
            "        causticsUnderwaterLightBoost = 0\n"
            "        causticsMinBrightness = 0\n"
            "        causticsBlurDepth = 0\n"
            "        lightRaysStrength = 1\n"
            "    }\n"
        )
    # Adds scatterer sunflares to stars.
    def addSunflareCfg(sunfCfg, starColor, starName, starType):
        sunfCfg.write(
            "Scatterer_sunflare:NEEDS[!Infinite_Sunflares]\n"
            "{\n"
            "    " + starName + "\n"
            "    {\n"
            "        syntaxVersion = 2\n"
            "        flareColor = " + str(starColor[0]) + "," + str(starColor[1]) + "," + str(starColor[2]) + "\n"
            "        flares\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/sunFlare.png\n"
            "                displayAspectRatio = 1\n"
        )
        if starType == "Neutron":
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1.5 0 0\n"
                "                    key = 2500000 1.05 -3E-07 -3E-07\n"
                "                    key = 1E+07 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.8 0 -1.6E-07\n"
                "                    key = 10000000 0.3 0 0\n"
                "                }\n"
            )
        else:
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1 0 -0.0004\n"
                "                    key = 5000 0.3 -4E-05 -3E-05\n"
                "                    key = 30000 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.7 0 -7E-05\n"
                "                    key = 30000 0.3 0 0\n"
                "                }\n"
            )
        sunfCfg.write(
            "            }\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/sunSpikes.png\n"
            "                displayAspectRatio = 1\n"
        )
        if starType == "Neutron":
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1.5 0 0\n"
                "                    key = 2500000 1.05 -3E-07 -3E-07\n"
                "                    key = 1E+07 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.8 0 -1.6E-07\n"
                "                    key = 10000000 0 0 0\n"
                "                }\n"
            )
        else:
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1 0 -0.0004\n"
                "                    key = 5000 0.3 -4E-05 -3E-05\n"
                "                    key = 30000 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.7 0 -7E-05\n"
                "                    key = 30000 0 0 0\n"
                "                }\n"
            )
        sunfCfg.write(
            "            }\n"
            "        }\n"
            "        ghosts\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/Ghost1.png\n"
            "                intensityCurve\n"
            "                {\n"
        )
        if starType == "Neutron":
            sunfCfg.write(
                "                key = 2 0.0 0 0\n"
                "                key = 2200 1 0 0\n"
                "                key = 1000000 1 0 0\n"
                "                key = 5000000 0 0 0\n"
            )
        else:
            sunfCfg.write(
                "                key = 0 0.0 0 0\n"
                "                key = 44 1 0 0\n"
                "                key = 2000 1 0 0\n"
                "                key = 10000 0 0 0\n"
            )
        sunfCfg.write(
            "                }\n"
            "                instances\n"
            "                {\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.54\n"
            "                        displayAspectRatio = 0.65\n"
            "                        scale = 0.434\n"
            "                        sunToScreenCenterPosition = 0.5\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.54\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.166\n"
            "                        sunToScreenCenterPosition = 0.7\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/Ghost2.png\n"
            "                intensityCurve\n"
            "                {\n"
            )
        if starType == "Neutron":
            sunfCfg.write(
                "                key = 2 0.0 0 0\n"
                "                key = 2200 1 0 0\n"
                "                key = 1000000 1 0 0\n"
                "                key = 5000000 0 0 0\n"
            )
        else:
            sunfCfg.write(
                "                key = 0 0.0 0 0\n"
                "                key = 44 1 0 0\n"
                "                key = 2000 1 0 0\n"
                "                key = 10000 0 0 0\n"
            )
        sunfCfg.write(
            "                }\n"
            "                instances\n"
            "                {\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.135\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.333\n"
            "                        sunToScreenCenterPosition = 0.9\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.054\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.125\n"
            "                        sunToScreenCenterPosition = 1.1\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.054\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.25\n"
            "                        sunToScreenCenterPosition = 1.3\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.054\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.2\n"
            "                        sunToScreenCenterPosition = 1.5\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )
        clrHSL = colorsys.rgb_to_hsv(starColor[0],starColor[1],starColor[2])
        clrDesaturated = colorsys.hsv_to_rgb(clrHSL[0], (clrHSL[1]/1.75), clrHSL[2]*1.2)
        sunfCfg.write(
            "Scatterer_sunflare:NEEDS[Infinite_Sunflares]\n"
            "{\n"
            "    " + starName + "\n"
            "    {\n"
            "        syntaxVersion = 2\n"
            "        flareColor = " + str(clrDesaturated[0]) + "," + str(clrDesaturated[1]) + "," + str(clrDesaturated[2]) + "\n"
            "        flares\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/sunFlare.png\n"
            "                displayAspectRatio = 1\n"
        )
        if starType == "Neutron":
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1.5 0 0\n"
                "                    key = 2500000 1.05 -3E-07 -3E-07\n"
                "                    key = 1E+07 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.8 0 -1.6E-07\n"
                "                    key = 10000000 0.3 0 0\n"
                "                }\n"
            )
        else:
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1 0 -0.0004\n"
                "                    key = 5000 0.3 -4E-05 -3E-05\n"
                "                    key = 30000 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.7 0 -7E-05\n"
                "                    key = 30000 0.3 0 0\n"
                "                }\n"
            )
        sunfCfg.write(
            "            }\n"
            "            Item\n"
            "            {\n"
            "                texture = Infinite_Sunflares/Sunflare/sunSpikes.png\n"
            "                displayAspectRatio = 1\n"
        )
        if starType == "Neutron":
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1.5 0 0\n"
                "                    key = 2500000 1.05 -3E-07 -3E-07\n"
                "                    key = 1E+07 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 0.8 0 -1.6E-07\n"
                "                    key = 10000000 0 0 0\n"
                "                }\n"
            )
        else:
            sunfCfg.write(
                "                scaleCurve\n"
                "                {\n"
                "                    key = 0 1 0 -0.0004\n"
                "                    key = 5000 0.3 -4E-05 -3E-05\n"
                "                    key = 30000 0.1 0 0\n"
                "                }\n"
                "                intensityCurve\n"
                "                {\n"
                "                    key = 0 0 0 0\n"
                "                    key = 5 1.2 0 -7E-05\n"
                "                    key = 30000 0 0 0\n"
                "                }\n"
            )
        sunfCfg.write(
            "            }\n"
            "        }\n"
            "        ghosts\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                texture = Infinite_Sunflares/Sunflare/Ghost1.png\n"
            "                intensityCurve\n"
            "                {\n"
            )
        if starType == "Neutron":
            sunfCfg.write(
                "                key = 2 0.0 0 0\n"
                "                key = 2200 1 0 0\n"
                "                key = 1000000 1 0 0\n"
                "                key = 5000000 0 0 0\n"
            )
        else:
            sunfCfg.write(
                "                key = 0 0.0 0 0\n"
                "                key = 44 1 0 0\n"
                "                key = 2000 1 0 0\n"
                "                key = 10000 0 0 0\n"
            )
        sunfCfg.write(
            "                }\n"
            "                instances\n"
            "                {\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.4\n"
            "                        displayAspectRatio = 0.85\n"
            "                        scale = 0.8\n"
            "                        sunToScreenCenterPosition = 0.3\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.3\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.3\n"
            "                        sunToScreenCenterPosition = 0.7\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "            Item\n"
            "            {\n"
            "                texture = Infinite_Sunflares/Sunflare/HexagonRed.png\n"
            "                intensityCurve\n"
            "                {\n"
            )
        if starType == "Neutron":
            sunfCfg.write(
                "                key = 2 0.0 0 0\n"
                "                key = 2200 1 0 0\n"
                "                key = 1000000 1 0 0\n"
                "                key = 5000000 0 0 0\n"
            )
        else:
            sunfCfg.write(
                "                key = 0 0.0 0 0\n"
                "                key = 44 1 0 0\n"
                "                key = 2000 1 0 0\n"
                "                key = 10000 0 0 0\n"
            )
        sunfCfg.write(
            "                }\n"
            "                instances\n"
            "                {\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.135\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.2\n"
            "                        sunToScreenCenterPosition = 0.9\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.1\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.15\n"
            "                        sunToScreenCenterPosition = 1.1\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "            Item\n"
            "            {\n"
            "                texture = Infinite_Sunflares/Sunflare/HexagonGreen.png\n"
            "                intensityCurve\n"
            "                {\n"
            )
        if starType == "Neutron":
            sunfCfg.write(
                "                key = 2 0.0 0 0\n"
                "                key = 2200 1 0 0\n"
                "                key = 1000000 1 0 0\n"
                "                key = 5000000 0 0 0\n"
            )
        else:
            sunfCfg.write(
                "                key = 0 0.0 0 0\n"
                "                key = 44 1 0 0\n"
                "                key = 2000 1 0 0\n"
                "                key = 10000 0 0 0\n"
            )
        sunfCfg.write(
            "                }\n"
            "                instances\n"
            "                {\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.05\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.15\n"
            "                        sunToScreenCenterPosition = 1.4\n"
            "                    }\n"
            "                    Item\n"
            "                    {\n"
            "                        intensityMultiplier = 0.05\n"
            "                        displayAspectRatio = 1\n"
            "                        scale = 0.15\n"
            "                        sunToScreenCenterPosition = 1.7\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )
    # Adds a body to the system's scatterer list.
    def addToScattererList(scattererCfg, starName, planetName, starColor, ocean, colorsRound, binaryParents=None, distBinaryParents=None):
        if not binaryParents == None:
            scattererCfg.write(
                "       Item\n"
                "       {\n"
                "            celestialBodyName = " + planetName + "\n"
                "            transformName = " + planetName + "\n"
                "            loadDistance = 500000000\n"
                "            unloadDistance = 1000000000\n"
                "            hasOcean = " + str(ocean) + "\n"
                "            flatScaledSpaceModel = True\n"
                "            usesCloudIntegration = True\n"
                "            cloudIntegrationUsesScattererSunColors = True\n"
                "            mainSunCelestialBody = " + binaryParents[0] + "\n"
                "            sunColor = " + str(colorsRound) + ", " + str(colorsRound) + ", " + str(colorsRound) + "\n"
                "            sunsUseIntensityCurves = True\n"
                "            secondarySuns\n"
                "            {\n"
                "                Item\n"
                "                {\n"
                "                    celestialBodyName = " + binaryParents[1] + "\n"
                "                    sunColor = 1.0,1.0,1.0\n"
                "                }\n"
                "            }\n"
                "        }\n"
            )
        elif not distBinaryParents == None:
            if distBinaryParents[0] == starName:
                otherStar = distBinaryParents[1]
            else:
                otherStar = distBinaryParents[0]
            scattererCfg.write(
                "       Item\n"
                "       {\n"
                "            celestialBodyName = " + planetName + "\n"
                "            transformName = " + planetName + "\n"
                "            loadDistance = 500000000\n"
                "            unloadDistance = 1000000000\n"
                "            hasOcean = " + str(ocean) + "\n"
                "            flatScaledSpaceModel = True\n"
                "            usesCloudIntegration = True\n"
                "            cloudIntegrationUsesScattererSunColors = True\n"
                "            mainSunCelestialBody = " + starName + "\n"
                "            sunColor = " + str(colorsRound) + ", " + str(colorsRound) + ", " + str(colorsRound) + "\n"
                "            sunsUseIntensityCurves = True\n"
                "            secondarySuns\n"
                "            {\n"
                "                Item\n"
                "                {\n"
                "                    celestialBodyName = " + otherStar + "\n"
                "                    sunColor = 1.0,1.0,1.0\n"
                "                }\n"
                "            }\n"
                "        }\n"
            )
        else:
            scattererCfg.write(
                "       Item\n"
                "       {\n"
                "            celestialBodyName = " + planetName + "\n"
                "            transformName = " + planetName + "\n"
                "            loadDistance = 500000000\n"
                "            unloadDistance = 1000000000\n"
                "            hasOcean = " + str(ocean) + "\n"
                "            flatScaledSpaceModel = True\n"
                "            usesCloudIntegration = True\n"
                "            cloudIntegrationUsesScattererSunColors = True\n"
                "            mainSunCelestialBody = " + starName + "\n"
                "            sunColor = " + str(colorsRound) + ", " + str(colorsRound) + ", " + str(colorsRound) + "\n"
                "            sunsUseIntensityCurves = True\n"
                "        }\n"
            )
    # Adds a body to the system's scatterer atmosphere config.
    def addToAtmoCfg(atmoCfg, starName, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean, gasGiant, atmoHeight, atmoPressure):
        allActions.append([time.localtime(),"Writing scatterer atmo config for : " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        if gasGiant == False:
            thicknessMult = ((atmoPressure/101.3)+1)/2
        else:
            thicknessMult = 1.5
        print(planetName + " ------------------------------------------ " + str(thicknessMult))
        atmoCfg.write(
            "    Atmo:NEEDS[!Infinite_VolumetricClouds]\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        atmosphereStartRadiusScale = 1\n"
        )
        if gasGiant == False:
            atmoCfg.write(
                "        HR = " + str(atmoHeight/20000) + "\n"
            )
        else:
            atmoCfg.write(
                "        HR = 15\n"
            )
        atmoCfg.write(
            "        HM = 1.79999995\n"
        )
        if gasGiant == False:
            atmoCfg.write(
                "        m_betaR = " + str(((sctrClrR/256)/50)*thicknessMult) + "," + str(((sctrClrG/256)/50)*thicknessMult) + "," + str(((sctrClrB/256)/50)*thicknessMult) + "\n"
                "        BETA_MSca = " + str(((sctrClrR/256)/50)*thicknessMult) + "," + str(((sctrClrG/256)/50)*thicknessMult) + "," + str(((sctrClrB/256)/50)*thicknessMult) + "\n"
            )
        else:
            atmoCfg.write(
                "        m_betaR = " + str((((sctrClrR/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrG/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrB/256)/50)*thicknessMult)*0.2) + "\n"
                "        BETA_MSca = " + str((((sctrClrR/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrG/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrB/256)/50)*thicknessMult)*0.2) + "\n"
            )
        atmoCfg.write(
            "        m_mieG = 0.850000024\n"
            "        averageGroundReflectance = 0.5\n"
            "        multipleScattering = True\n"
            "        godrayStrength = 0.5\n"
            "        flattenScaledSpaceMesh = 0.600000024\n"
            "        rimBlend = 1\n"
            "        rimpower = 5\n"
        )

        if ocean == True:
            atmoCfg.write(
                "        specR = 50\n"
                "        specG = 50\n"
                "        specB = 50\n"
            )
        else:
            atmoCfg.write(
                "        specR = 0\n"
                "        specG = 0\n"
                "        specB = 0\n"
            )
        if gasGiant == True:
            atmoCfg.write(
                "        shininess = 30\n"
                "        cloudColorMultiplier = 1.2\n"
                "        cloudScatteringMultiplier = 1.100000003\n"
                "        cloudSkyIrradianceMultiplier = 0.0000000000\n"
                "        volumetricsColorMultiplier = 1\n"
            )
        else:
            atmoCfg.write(
                "        shininess = 30\n"
                "        cloudColorMultiplier = 1.1\n"
                "        cloudScatteringMultiplier = 0.100000003\n"
                "        cloudSkyIrradianceMultiplier = 2.2000000007\n"
                "        volumetricsColorMultiplier = 1\n"
            )
        if gasGiant == True:
            atmoCfg.write(
                "        EVEIntegration_preserveCloudColors = False\n"
            )
        else:
            atmoCfg.write(
                "        EVEIntegration_preserveCloudColors = False\n"
            )
        atmoCfg.write(
            "        adjustScaledTexture = False\n"
            "        scaledLandBrightnessAdjust = 1\n"
            "        scaledLandContrastAdjust = 1\n"
            "        scaledLandSaturationAdjust = 1\n"
            "        scaledOceanBrightnessAdjust = 1\n"
            "        scaledOceanContrastAdjust = 1\n"
            "        scaledOceanSaturationAdjust = 1\n"
            "        configPoints\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                altitude = 200\n"
            "                skyExposure = 0.25\n"
            "                skyAlpha = 1\n"
            "                skyExtinctionTint = 1\n"
            "                scatteringExposure = 0.230000004\n"
            "                extinctionThickness = 1\n"
            "                postProcessAlpha = 1\n"
            "                postProcessDepth = 0.125\n"
            "                extinctionTint = 0.5\n"
            "            }\n"
            "        }\n"
            "    }\n"
        )
        atmoCfg.write(
            "    Atmo:NEEDS[Infinite_VolumetricClouds]\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        atmosphereStartRadiusScale = 1\n"
        )
        if gasGiant == False:
            atmoCfg.write(
                "        HR = " + str(atmoHeight/15000) + "\n"
            )
        else:
            atmoCfg.write(
                "        HR = 15\n"
            )
        atmoCfg.write(
            "        HM = 1.79999995\n"
            )
        if gasGiant == False:
            atmoCfg.write(
                "        m_betaR = " + str(((sctrClrR/256)/50)*thicknessMult) + "," + str(((sctrClrG/256)/50)*thicknessMult) + "," + str(((sctrClrB/256)/50)*thicknessMult) + "\n"
                "        BETA_MSca = " + str(((sctrClrR/256)/50)*thicknessMult) + "," + str(((sctrClrG/256)/50)*thicknessMult) + "," + str(((sctrClrB/256)/50)*thicknessMult) + "\n"
            )
        else:
            atmoCfg.write(
                "        m_betaR = " + str((((sctrClrR/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrG/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrB/256)/50)*thicknessMult)*0.2) + "\n"
                "        BETA_MSca = " + str((((sctrClrR/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrG/256)/50)*thicknessMult)*0.2) + "," + str((((sctrClrB/256)/50)*thicknessMult)*0.2) + "\n"
            )
        atmoCfg.write(
            "        m_mieG = 0.850000024\n"
            "        averageGroundReflectance = 0.5\n"
            "        multipleScattering = True\n"
            "        godrayStrength = 0.5\n"
            "        flattenScaledSpaceMesh = 0.600000024\n"
            "        rimBlend = 1\n"
            "        rimpower = 5\n"
        )

        if ocean == True:
            atmoCfg.write(
                "        specR = 50\n"
                "        specG = 50\n"
                "        specB = 50\n"
            )
        else:
            atmoCfg.write(
                "        specR = 0\n"
                "        specG = 0\n"
                "        specB = 0\n"
            )
        if gasGiant == True:
            atmoCfg.write(
                "        shininess = 30\n"
                "        cloudColorMultiplier = 1.2\n"
                "        cloudScatteringMultiplier = 1.100000003\n"
                "        cloudSkyIrradianceMultiplier = 0.0000000000\n"
                "        volumetricsColorMultiplier = 1\n"
            )
        else:
            atmoCfg.write(
                "        shininess = 30\n"
                "        cloudColorMultiplier = 1.1\n"
                "        cloudScatteringMultiplier = 0.100000003\n"
                "        cloudSkyIrradianceMultiplier = 2.2000000007\n"
                "        volumetricsColorMultiplier = 1\n"
            )
        if gasGiant == True:
            atmoCfg.write(
                "        EVEIntegration_preserveCloudColors = False\n"
            )
        else:
            atmoCfg.write(
                "        EVEIntegration_preserveCloudColors = False\n"
            )
        atmoCfg.write(
            "        adjustScaledTexture = False\n"
            "        scaledLandBrightnessAdjust = 1\n"
            "        scaledLandContrastAdjust = 1\n"
            "        scaledLandSaturationAdjust = 1\n"
            "        scaledOceanBrightnessAdjust = 1\n"
            "        scaledOceanContrastAdjust = 1\n"
            "        scaledOceanSaturationAdjust = 1\n"
            "        configPoints\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                altitude = 200\n"
            "                skyExposure = 0.25\n"
            "                skyAlpha = 1\n"
            "                skyExtinctionTint = 1\n"
            "                scatteringExposure = 0.230000004\n"
            "                extinctionThickness = 1\n"
            "                postProcessAlpha = 1\n"
            "                postProcessDepth = 0.125\n"
            "                extinctionTint = 0.5\n"
            "            }\n"
            "        }\n"
            "    }\n"
        )
    # Generates rings.
    def genRing(seed, planetName):
        ringRNG = random.Random()
        ringRNG.seed(seed)
        ring1 = Image.open(targetPath + "/Presets/" + "Ring" + str(1) + ".png")
        ringOffs1 = ImageChops.offset(ring1, ringRNG.randint(0,1024),0)
        bands = ringOffs1.split()
        randomMult = random.randint(1,10)/10
        print(randomMult)
        adj_alpha = bands[3].point(lambda x: int(x * randomMult))
        ringAlph = Image.merge('RGBA', [*bands[:3], adj_alpha])
        ringAlph.save(targetPath + "/Textures/PluginData/" + planetName + "_RINGS" + ".png")
    # Writes star configs.
    def writeStarCfg(cfgSeed, starCfg, starName, starRadius, starMass, starDist, RGBfinal, starDistG, dispName, Tag, typeOfStar, Lum, coronaColor, parentBarycenter=None, period=None, maaoD=None, parentGalaxy=None, binaryEccentricity=None, binaryType=None):
        starCfgRNG = random.Random()
        starCfgRNG.seed(cfgSeed)
        allActions.append([time.localtime(),"Writing config for star: " + starName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        print(starRadius)
        defaultSOIforNonBinaryStars = 350000000000
        #print(starMass)
        if typeOfStar == "RedGiant":
            brightnessThing = (starRadius/30)*5 # I honestly do not know what to call these variables anymore.
        elif typeOfStar == "BrownDwarf":
            brightnessThing = starRadius*4
            randomThingamabob = starCfgRNG.randint(1,3) # ????????????????????????
            if randomThingamabob == 1: # Redder brown dwarfs
                mainR = 0 #random.randint(0,100)/100
                mainG = 0 #mainR/2
                secR = starCfgRNG.randint(60,100)/100
                secG = starCfgRNG.randint(0,int((secR*100)/2))/100
            elif randomThingamabob == 2: # Same as 1 but inverted and a bit yellower
                mainR = starCfgRNG.randint(75,100)/100
                mainG = starCfgRNG.randint(0,int((mainR*100)*0.3))/100
                secR = 0
                secG = 0
            elif randomThingamabob == 3: # Random bullshit
                mainR = starCfgRNG.randint(50,100)/100
                mainG = mainR/1.5
                secR = starCfgRNG.randint(25,75)/100
                secG = 0
           
        elif typeOfStar == "Neutron":
            brightnessThing = starRadius*5450
        elif typeOfStar == "WhiteDwf":
            brightnessThing = starRadius*50
        elif typeOfStar == "WolfRayet":
            brightnessThing = 1048800000
            defaultSOIforNonBinaryStars = 2000000000000
        else:
            if starRadius > 523200000:
                brightnessThing = 523200000
            elif starRadius < 348800000:
                brightnessThing = 348800000
            else:
                brightnessThing = starRadius

        print(starName + " brightness: " + str(brightnessThing))
        starCfg.write(
            "@Kopernicus:AFTER[Kopernicus]\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + starName + "\n"
        )
        if typeOfStar == "RedGiant":
            starCfg.write(
                "        cacheFile = InfiniteDiscoveries/Misc/RedGiantBump.bin\n"
            )
        else:
            starCfg.write(
                "        cacheFile = InfiniteDiscoveries/Cache/" + starName + ".bin" + "\n"
            )
        starCfg.write(
            "        Tag = " + Tag + "\n"
            "        Template\n"
            "        {\n"
            "            name = Sun\n"
            "        }\n"
        )
        if not parentBarycenter == None:
            starCfg.write(
                "        Properties\n"
                "        {\n"
                "            displayName = " + dispName + "^N" + "\n"
            )
            starCfg.write(
                "            radius = " + str(starRadius) + "\n"
                "            mass = " + str(starMass) + "\n"
                "            rotationPeriod = 1063000.6069891\n"
                "            tidallyLocked = true\n"
                "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol! \\n<color=#faff9e>This star was generated using seed " + str(cfgSeed) + "." + str(AmountOfPlanetsToGenerate) + ":" + str(AmountOfMoonsToGenerate) + ":" + str(AmountOfAsteroidsToGenerate) + ":" + str(minPlanets) + ":" + str(minMoons) +  " (CHECK BARYCENTER FOR SYSTEM SEED)\n"
            )
            if binaryType == "Distant":
                starCfg.write(
                    "            sphereOfInfluence = 100000000000\n"
                )
            starCfg.write(
                "            ScienceValues\n"
                "            {\n"
                "                landedDataValue = 10000\n"
                "                flyingLowDataValue = 20\n"
                "                flyingHighDataValue = 20\n"
                "                inSpaceLowDataValue = 20\n"
                "                inSpaceHighDataValue = 5\n"
                "                recoveryValue = 10\n"
                "                flyingAltitudeThreshold = 18000\n"
                "                spaceAltitudeThreshold = 1E+09\n"
                "            }\n"	
                "        }\n"
            )
            if binaryType == "Near":
                starCfg.write(
                    "        Orbit\n"
                    "        {\n"
                    "            referenceBody = " + parentBarycenter + "\n"
                    "            color = " + RGBfinal + ", 1\n"
                    "            semiMajorAxis = " + str(starDist*4.2) + "\n"
                    "            inclination = " + str(0) + "\n"
                    "            eccentricity = " + str(0) + "\n"
                    "            longitudeOfAscendingNode = " + str(0) + "\n"
                    "            argumentOfPeriapsis = " + str(0) + "\n"
                    "            meanAnomalyAtEpochD = " + str(maaoD) + "\n"
                    "            period = " + str(period) + "\n"
                    "            epoch = 0\n"
                    "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                    "        }\n"
                )
            else:
                starCfg.write(
                    "        Orbit\n"
                    "        {\n"
                    "            referenceBody = " + parentBarycenter + "\n"
                    "            color = " + RGBfinal + ", 1\n"
                    "            semiMajorAxis = " + str(starDist*4.2) + "\n"
                    "            inclination = " + str(0) + "\n"
                    "            eccentricity = " + str(binaryEccentricity) + "\n"
                    "            longitudeOfAscendingNode = " + str(maaoD) + "\n"
                    "            argumentOfPeriapsis = " + str(0) + "\n"
                    "            meanAnomalyAtEpochD = " + str(0) + "\n"
                    "            period = " + str(period) + "\n"
                    "            epoch = 0\n"
                    "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                    "        }\n"
                )
        else:
            starCfg.write(
                "        Properties\n"
                "        {\n"
                "            displayName = " + dispName + "^N" + "\n"
            )
            if not typeOfStar == "neutron":
                starCfg.write(
                    "            radius = " + str(starRadius) + "\n"
                )
            else:
                starCfg.write(
                    "            radius = " + str(10000) + "\n"
                )
            print(str(starMass) + " <------------ WHY")
            print(parentGalaxy)
            starCfg.write(
                "            mass = " + str(starMass) + "\n"
                "            rotationPeriod = 5000.6069891\n"
                "            tidallyLocked = false\n"
                "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol! \\n<color=#faff9e>This system was generated using seed " + str(cfgSeed) + "." + str(AmountOfPlanetsToGenerate) + ":" + str(AmountOfMoonsToGenerate) + ":" + str(AmountOfAsteroidsToGenerate) + ":" + str(minPlanets) + ":" + str(minMoons) + "\n"
                "            sphereOfInfluence = " + str(defaultSOIforNonBinaryStars) + "\n"
                "            ScienceValues\n"
                "            {\n"
                "                landedDataValue = 10000\n"
                "                flyingLowDataValue = 20\n"
                "                flyingHighDataValue = 20\n"
                "                inSpaceLowDataValue = 20\n"
                "                inSpaceHighDataValue = 5\n"
                "                recoveryValue = 10\n"
                "                flyingAltitudeThreshold = 18000\n"
                "                spaceAltitudeThreshold = 1E+09\n"
                "            }\n"	
                "        }\n"
                "        Orbit\n"
                "        {\n"
                "            referenceBody = Sun\n"
                "            color = " + RGBfinal + ", 1\n"
                "            semiMajorAxis = " + str(starDist) + "\n"
                "            inclination = " + str(starCfgRNG.randint(0,360)) + "\n"
                "            eccentricity = " + str(starCfgRNG.randint(0,500)/1000) + "\n"
                "            longitudeOfAscendingNode = 0\n"
                "            argumentOfPeriapsis = 0\n"
                "            meanAnomalyAtEpochD = " + str(starCfgRNG.randint(0,360)) + "\n"
                "            epoch = 0\n"
                "            mode = OFF\n"
                "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                "        }\n"
            )
        
        starCfg.write(
            "        ScaledVersion\n"
            "        {\n"
            "            type = Star\n"
        ) 
        if parentBarycenter == None or binaryType == "Distant":
            starCfg.write(
                "            Light\n"
                "            {\n"
                "                sunlightColor = " + RGBfinal + ", 1\n"
                "                sunlightShadowStrength = 0.75\n"
                "                scaledSunlightColor = " + RGBfinal + ", 1\n"
                "                IVASunColor = " + RGBfinal + ", 1\n"
                "                sunLensFlareColor = " + RGBfinal + ", 1\n"
                "                givesOffLight = true\n"
            )
            if typeOfStar == "neutron":
                starCfg.write(
                    "                sunAU = 18000000\n"
                )
            else:
                starCfg.write(
                    "                sunAU = " + str(16000000000 * (starRadius/261600000)) + "\n"
                )
            starCfg.write(
                "                luminosity = " + str(Lum) + "\n"
                "                insolation = 0.15\n"
                "                brightnessCurve\n"
                "                {\n"
                "                   key = -0.01573471 0 1.706627 1.706627\n"
                "                   key = 5.084181 5.997075 -0.001802375\n"
                "                   key = 38.56295 10.82142 0.0001713 0.0001713\n"
                "                }\n"
                "                IntensityCurve\n"
                "                {\n"
                "                    key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
                "   			     key = " + str((760320000000*(brightnessThing / 261600000))) + " 0 0 0\n"
                "                }\n"
                "                ScaledIntensityCurve\n"
                "                {\n"
                "                   key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
                "                   key = " + str((126720000*(brightnessThing / 261600000))) + " 0 0 0\n"
                "                }\n"
                "                IVAIntensityCurve\n"
                "                {\n"
                "                   key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
                "          			key = " + str((760320000000*(brightnessThing / 261600000))) + " 0 0 0\n"
                "                }\n"
                "            }\n"
            )
        else:
            #starCfg.write(
            #    "            Light:NEEDS[Parallax]\n"
            #    "            {\n"
            #    "                sunlightColor = " + RGBfinal + ", 1\n"
            #    "                sunlightShadowStrength = 0.75\n"
            #    "                scaledSunlightColor = " + RGBfinal + ", 1\n"
            #    "                IVASunColor = " + RGBfinal + ", 1\n"
            #    "                sunLensFlareColor = " + RGBfinal + ", 1\n"
            #    "                givesOffLight = false\n"
            #)
            #if typeOfStar == "neutron":
            #    starCfg.write(
            #        "                sunAU = 18000000\n"
            #    )
            #else:
            #    starCfg.write(
            #        "                sunAU = " + str(16000000000 * (starRadius/261600000)) + "\n"
            #    )
            #starCfg.write(
            #    "                luminosity = " + str(Lum) + "\n"
            #    "                insolation = 0.15\n"
            #    "                brightnessCurve\n"
            #    "                {\n"
            #    "                   key = -0.01573471 0 1.706627 1.706627\n"
            #    "                   key = 5.084181 5.997075 -0.001802375\n"
            #    "                   key = 38.56295 10.82142 0.0001713 0.0001713\n"
            #    "                }\n"
            #    "                IntensityCurve\n"
            #    "                {\n"
            #    "                    key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
            #    "   			     key = " + str((760320000000*(brightnessThing / 261600000))) + " 0 0 0\n"
            #    "                }\n"
            #    "                ScaledIntensityCurve\n"
            #    "                {\n"
            #    "                   key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
            #    "                   key = " + str((126720000*(brightnessThing / 261600000))) + " 0 0 0\n"
            #    "                }\n"
            #    "                IVAIntensityCurve\n"
            #    "                {\n"
            #    "                   key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
            #    "          			key = " + str((760320000000*(brightnessThing / 261600000))) + " 0 0 0\n"
            #    "                }\n"
            #    "            }\n"
            #)
            starCfg.write(
                "            Light\n"
                "            {\n"
                "                sunlightColor = " + RGBfinal + ", 1\n"
                "                sunlightShadowStrength = 0.75\n"
                "                scaledSunlightColor = " + RGBfinal + ", 1\n"
                "                IVASunColor = " + RGBfinal + ", 1\n"
                "                sunLensFlareColor = " + RGBfinal + ", 1\n"
                "                givesOffLight = true\n"
            )
            if typeOfStar == "neutron":
                starCfg.write(
                    "                sunAU = 18000000\n"
                )
            else:
                starCfg.write(
                    "                sunAU = " + str(13599840256 * (starRadius/261600000)) + "\n"
                )
            starCfg.write(
                "                luminosity = " + str(Lum) + "\n"
                "                insolation = 0.15\n"
                "                brightnessCurve\n"
                "                {\n"
                "                   key = -0.01573471 0 1.706627 1.706627\n"
                "                   key = 5.084181 5.997075 -0.001802375\n"
                "                   key = 38.56295 10.82142 0.0001713 0.0001713\n"
                "                }\n"
                "                IntensityCurve\n"
                "                {\n"
                "                    key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
                "   			     key = " + str((760320000000*(brightnessThing / 261600000))) + " 0 0 0\n"
                "                }\n"
                "                ScaledIntensityCurve\n"
                "                {\n"
                "                   key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
                "                   key = " + str((126720000*(brightnessThing / 261600000))) + " 0 0 0\n"
                "                }\n"
                "                IVAIntensityCurve\n"
                "                {\n"
                "                   key = 0 " + str((brightnessThing / 261600000)/1.1) + " 0 0\n"
                "          			key = " + str((760320000000*(brightnessThing / 261600000))) + " 0 0 0\n"
                "                }\n"
                "            }\n"

            )
        if typeOfStar == "RedGiant":
            starCfg.write(
                "            Material\n"
                "            {\n"
                "               emitColor0 = " + RGBfinal + ", 1\n"
                "               emitColor1 = " + RGBfinal + ", 1\n"
                "               sunspotTex = InfiniteDiscoveries/Textures/Misc/redGiantMap.dds\n"
                "               sunspotPower = 2\n"
                "               sunspotColor = 0,0,0,1\n"
                "               rimColor = 0,0,0,1\n"
                "               rimPower = 1\n"
                "               rimBlend = -0.3\n"
                "            }\n"
            )
        elif typeOfStar == "BrownDwarf":
            starCfg.write(
                "            Material\n"
                "            {\n"
                "               emitColor0 = " + str(mainR) + ", " + str(mainG) + ", 0, 1\n"
                "               emitColor1 = " + str(mainR) + ", " + str(mainG) + ", 0, 1\n"
                "               sunspotTex = InfiniteDiscoveries/Textures/Misc/brownDwarfMap.dds\n"
                "               sunspotPower = 1\n"
                "               sunspotColor = " + str(secR) + ", " + str(secG) + ", 0, 1\n"
                "               rimColor = 0,0,0,1\n"
                "               rimPower = 1\n"
                "               rimBlend = -0.3\n"
                "            }\n"
            )
        else:
            starCfg.write(
                "            Material\n"
                "            {\n"
                "               emitColor0 = " + RGBfinal + ", 1\n"
                "               emitColor1 = " + RGBfinal + ", 1\n"
                "               sunspotTex = BUILTIN/sunsurfacenew\n"
                "               sunspotPower = 1\n"
                "               sunspotColor = 0.283582091,0.126710668,0.0208224356,1\n"
                "               rimColor = 0,0,0,1\n"
                "               rimPower = 1\n"
                "               rimBlend = -0.3\n"
                "            }\n"
            )
        starCfg.write(
            "            Coronas\n"
            "            {\n"
            "                Value\n"
            "                {\n"
            "                    scaleSpeed = 0.007\n"
            "                    scaleLimitY = 3\n"
            "                    scaleLimitX = 5\n"
            "                    updateInterval = 5\n"
            "                    speed = -1\n"
            "                    rotation = 0\n"
            "                    Material\n"
            "                    {\n"
            "                        texture = InfiniteDiscoveries/Textures/Misc/" + coronaColor + ".dds\n"
            "                        mainTexScale = 1,1\n"
            "                        mainTexOffset = 0,0\n"
            "                        invFade = 2.553731\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )
        if parentBarycenter == None:
            starCfg.write(
                "@Kopernicus:LAST[InfiniteDiscoveries]:HAS[@InfiniteDiscoveriesSettings:HAS[#GalaxyMode[?rue]]]\n"
                "{\n"
                "    @Body:HAS[#name[" + starName + "]]\n"
                "    {\n"
                "        !Orbit{}\n"
                "        Orbit\n"
                "        {\n"
                "            referenceBody = " + parentGalaxy + "\n"
                "            color = " + RGBfinal + ", 1\n"
                "            semiMajorAxis = " + str(starDistG) + "\n"
            )
            if parentGalaxy == "LKC_CtrlB":
                starCfg.write(
                    "            inclination = " + str(starCfgRNG.randint(80,100)) + "\n"
                )
            elif parentGalaxy == "SKC_CtrlB":
                starCfg.write(
                    "            inclination = " + str(starCfgRNG.randint(80,100)) + "\n"
                )
            else:
                starCfg.write(
                    "            inclination = " + str(starCfgRNG.randint(0,10)) + "\n"
                )
            starCfg.write(
                "            eccentricity = " + str(starCfgRNG.randint(0,200)/1000) + "\n"
                "            longitudeOfAscendingNode = 0\n"
                "            argumentOfPeriapsis = 0\n"
                "            meanAnomalyAtEpochD = " + str(starCfgRNG.randint(0,360)) + "\n"
                "            epoch = 0\n"
                "            mode = OFF\n"
                "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                "        }\n"
                "    }\n"
                "}\n"
            )
        allActions.append([time.localtime(),"Wrote config for star: " + starName])
        allActionArrayUpdated = True
    # Writes barycenter configs.
    def writeBarycenterCfg(barySeed, baryCfg, baryName, baryRadius, baryMass, baryDist, systemName, starColors, baryDistG, baryDispName, averageClr, baryBrightness, parentGalaxy, binaryType, starTypes):
        baryRNG = random.Random()
        baryRNG.seed(barySeed)
        baryCfg.write(
            "@Kopernicus:AFTER[Kopernicus]\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + baryName + "\n"
            "        cacheFile = InfiniteDiscoveries/Cache/" + baryName + ".bin" + "\n"
            "        Tag = InfD_Barycenter\n"
            "        Template\n"
            "        {\n"
            "            name = Sun\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            displayName = " + baryDispName + "^N" + "\n"
            "            radius = " + str(baryRadius/4.2) + "\n"
            "            mass = " + str(baryMass) + "\n"
            "            rotationPeriod = 1063000.6069891\n"
            "            tidallyLocked = false\n"
            "            description = The barycenter of the " + str(systemName) + " system. \\n<color=#faff9e>This system was generated using seed " + str(barySeed) + "." + str(AmountOfPlanetsToGenerate) + ":" + str(AmountOfMoonsToGenerate) + ":" + str(AmountOfAsteroidsToGenerate) + ":" + str(minPlanets) + ":" + str(minMoons) + "\n"
        )
        if binaryType == "Distant":
            baryCfg.write(
                "            sphereOfInfluence = 3000000000000\n"
            )
        else:
            if starTypes[0] == "WolfRayet" or starTypes[1] == "WolfRayet":
                baryCfg.write(
                    "            sphereOfInfluence = 2000000000000\n"
                )
            else:
                baryCfg.write(
                    "            sphereOfInfluence = 350000000000\n"
                )
        baryCfg.write(
            "            ScienceValues\n"
            "            {\n"
            "                landedDataValue = 100000000000000\n"
            "                flyingLowDataValue = 2000000000\n"
            "                flyingHighDataValue = 20000000\n"
            "                inSpaceLowDataValue = 200000\n"
            "                inSpaceHighDataValue = 5\n"
            "                recoveryValue = 10\n"
            "                flyingAltitudeThreshold = 18000\n"
            "                spaceAltitudeThreshold = 1E+09\n"
            "            }\n"	
            "        }\n"
            "        Orbit\n"
            "        {\n"
            "            referenceBody = Sun\n"
            "            color = " + starColors + ", 1\n"
            "            semiMajorAxis = " + str(baryDist) + "\n"
            "            inclination = " + str(baryRNG.randint(0,360)) + "\n"
            "            eccentricity = " + str(baryRNG.randint(0,500)/1000) + "\n"
            "            longitudeOfAscendingNode = 0\n"
            "            argumentOfPeriapsis = 0\n"
            "            meanAnomalyAtEpochD = " + str(baryRNG.randint(0,360)) + "\n"
            "            epoch = 0\n"
            "            mode = OFF\n"
            "            iconTexture = InfiniteDiscoveries/Textures/Misc/binaryStarIco.png\n"
            "        }\n"
            "        ScaledVersion\n"
            "        {\n"
            "            type = Star\n"
            "            invisible = True\n"
        )
        if binaryType == "Near":
            baryCfg.write(
                "            Light\n"
                "            {\n"
                "                givesOffLight = false\n"
                "            }\n"
                "            //Light:NEEDS[Parallax]\n"
                "            //{\n"
                "            //    sunlightColor = " + str(averageClr[0]) + ", " + str(averageClr[1]) + ", " + str(averageClr[2]) + "\n"
                "            //    sunlightShadowStrength = 0.75\n"
                "            //    scaledSunlightColor = " + str(averageClr[0]) + ", " + str(averageClr[1]) + ", " + str(averageClr[2]) + "\n"
                "            //    IVASunColor = " + str(averageClr[0]) + ", " + str(averageClr[1]) + ", " + str(averageClr[2]) + "\n"
                "            //    sunLensFlareColor = 0, 0, 0, 0\n"
                "            //    givesOffLight = true\n"
                "            //    sunAU = 1\n"
                "            //    luminosity = 1\n"
                "            //    insolation = 0.15\n"
                "            //    brightnessCurve\n"
                "            //    {\n"
                "            //       key = -0.01573471 0 1.706627 1.706627\n"
                "            //       key = 5.084181 5.997075 -0.001802375\n"
                "            //       key = 38.56295 10.82142 0.0001713 0.0001713\n"
                "            //    }\n"
                "            //    IntensityCurve\n"
                "            //    {\n"
                "            //        key = 0 " + str((baryBrightness / 261600000)/1.1) + " 0 0\n"
                "   		 //	     key = " + str((90000000000*(baryBrightness / 261600000))) + " " + str((baryBrightness / 261600000)/1.5) + " -2E-12 -2E-12\n"
                "   		 //	     key = " + str((150000000000*(baryBrightness / 261600000))) + " 0 0 0\n"
                "            //    }\n"
                "            //    ScaledIntensityCurve\n"
                "            //    {\n"
                "            //       key = 0 " + str((baryBrightness / 261600000)/1.1) + " 0 0\n"
                "         	 //		key = " + str((15000000*(baryBrightness / 261600000))) + " " + str((baryBrightness / 261600000)/1.5) + " -1.2E-08 -1.2E-08\n"
                "            //       key = " + str((30000000*(baryBrightness / 261600000))) + " 0 0 0\n"
                "            //    }\n"
                "            //    IVAIntensityCurve\n"
                "            //    {\n"
                "            //       key = 0 " + str((baryBrightness / 261600000)/1.1) + " 0 0\n"
                "          	 //		key = " + str((90000000000*(baryBrightness / 261600000))) + " " + str((baryBrightness / 261600000)/1.5) + " -1.8E-12 -1.8E-12\n"
                "          	 //		key = " + str((150000000000*(baryBrightness / 261600000))) + " 0 0 0\n"
                "            //    }\n"
                "            //}\n"
                "        }\n"
                "    }\n"
                "}\n"
            )
        else:
            baryCfg.write(
                "            Light\n"
                "            {\n"
                "                givesOffLight = false\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "}\n"
            )
        baryCfg.write(
            "@Kopernicus:LAST[InfiniteDiscoveries]:HAS[@InfiniteDiscoveriesSettings:HAS[#GalaxyMode[?rue]]]\n"
            "{\n"
            "    @Body:HAS[#name[" + baryName + "]]\n"
            "    {\n"
            "        !Orbit{}"
            "        Orbit\n"
            "        {\n"
            "            referenceBody = " + parentGalaxy + "\n"
            "            color = " + starColors + ", 1\n"
            "            semiMajorAxis = " + str(baryDistG) + "\n"
        )
        if parentGalaxy == "LKC_CtrlB":
            baryCfg.write(
                "            inclination = " + str(baryRNG.randint(80,100)) + "\n"
            )
        elif parentGalaxy == "SKC_CtrlB":
            baryCfg.write(
                "            inclination = " + str(baryRNG.randint(80,100)) + "\n"
            )
        else:
            baryCfg.write(
                "            inclination = " + str(baryRNG.randint(0,10)) + "\n"
            )
        baryCfg.write(
            "            eccentricity = " + str(baryRNG.randint(0,200)/1000) + "\n"
            "            longitudeOfAscendingNode = 0\n"
            "            argumentOfPeriapsis = 0\n"
            "            meanAnomalyAtEpochD = " + str(baryRNG.randint(0,360)) + "\n"
            "            epoch = 0\n"
            "            mode = OFF\n"
            "            iconTexture = InfiniteDiscoveries/Textures/Misc/binaryStarIco.png\n"
            "        }\n"
            "    }\n"
            "}\n"
        )
    # Writes planet/moon configs.
    def writeBodyCfg(planetCfgSeed, planetCfg, planetName, planetRadius, planetMass, planetSMA, parentN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon, Tag, Lava, tidallyLocked, oceanFactor, isAsteroid, icy, inclinationLimits, sciValue):
        planetCfgRNG = random.Random()
        planetCfgRNG.seed(planetCfgSeed)
        allActions.append([time.localtime(),"Writing config for body: " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        
        description = ""
        if moon == True:
            description = planetName + " is a moon"

            if not life == None:
                description = description + " <color=#bada55>with " + life + " life</color>"

            description = description + " generated by Infinite Discoveries, roughly " + str(round(planetRadius / 200000, 2)) + " times the size of The Mun!\\n"

            if atmo == "Atmospheric":
                description = description + "This moon has an atmosphere with a pressure of " + str(round(atmoPress, 2)) + " kilopascals (" + str(round(atmoPress/101.3, 2)) + " atmospheres.)\\n"
            else:
                description = description + "This moon has no atmosphere.\\n"

            if ocean == True:
                description = description + "This moon has oceans.\\n"
            else:
                description = description + "This moon has no oceans.\\n"
        elif isAsteroid == True:
            description = planetName + " is an asteroid"

            description = description + " generated by Infinite Discoveries, roughly " + str(round(planetRadius / 200000, 2)) + " times the size of Gilly!\\n"
        else:
            description = planetName + " is a planet"

            if not life == None:
                description = description + " <color=#bada55>with " + life + " life</color>"

            description = description + " generated by Infinite Discoveries, roughly " + str(round(planetRadius / 600000, 2)) + " times the size of Kerbin!\\n"

            if atmo == "Atmospheric":
                description = description + "This planet has an atmosphere with a pressure of " + str(round(atmoPress, 2)) + " kilopascals (" + str(round(atmoPress/101.3, 2)) + " atmospheres.)\\n"
            else:
                description = description + "This planet has no atmosphere.\\n"

            if ocean == True:
                description = description + "This planet has oceans.\\n"
            else:
                description = description + "This planet has no oceans.\\n"

            if tidallyLocked == True:
                description = description + "This planet is tidally locked.\\n"
            else:
                description = description + "This planet is not tidally locked.\\n"
        
        planetCfg.write(
            "@Kopernicus:AFTER[Kopernicus]\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        cacheFile = InfiniteDiscoveries/Cache/" + planetName + ".bin" + "\n"
            "        Tag = " + Tag + "\n"
            "        Template\n"
            "        {\n"
            "            name = " + templates[templ] + "\n"
            "            removeAllPQSMods = true\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            displayName = " + dispName + "^N" + "\n"
            "            radius = " + str(planetRadius) + "\n"
            #"            mass = " + str(planetMass) + "\n"
        )
        if planetRadius < 30000:
            planetCfg.write(
                "            geeASL = " + str(planetRadius/300000) + "\n"
            )
        else:
            if gasGiant == False:
                planetCfg.write(
                    "            geeASL = " + str((planetRadius/600000)*(random.randint(900,1100)/1000)) + "\n"
                )
            else:
                planetCfg.write(
                    "            geeASL = " + str((planetRadius/6000000)*(random.randint(900,1100)/1000)) + "\n"
                )
        
        planetCfg.write(
            "            rotationPeriod = " + str(planetCfgRNG.randint(360,360000)) + "\n"
            "            initialRotation = 0\n"
        )
        if tidallyLocked == True:
            planetCfg.write(
                "            tidallyLocked = true\n"
            )
        else:
            planetCfg.write(
                "            tidallyLocked = false\n"
            )
        planetCfg.write(
            "            description = " + description + "\n"
            "            ScienceValues\n"
            "            {\n"
            "                landedDataValue = " + str(int(sciValue)) + "\n"
            "                flyingLowDataValue = " + str(int(sciValue/4)) + "\n"
            "                flyingHighDataValue = " + str(int(sciValue/4)) + "\n"
            "                inSpaceLowDataValue = " + str(int(sciValue/2)) + "\n"
            "                inSpaceHighDataValue = " + str(int(sciValue/3)) + "\n"
            "                recoveryValue = " + str(int(sciValue)) + "\n"
            "                flyingAltitudeThreshold = " + str(int(atmoHeight/2)) + "\n"
            "                spaceAltitudeThreshold = 1E+09\n"
            "            }\n"	
        )
        if gasGiant == False:
            planetCfg.write(
                "            biomeMap = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_BIO" + ".png" + "\n"
                "	         Biomes\n"
                "            {\n"
                "                Biome\n"
                "                {\n"
                "                    name = Lowlands\n"
                "                    displayName = Lowlands\n"
                "                    value = 1.0\n"
                "                    color = RGB(0,0,0)\n"
                "                }\n"  
                "                Biome\n"
                "                {\n"
                "                    name = Midlands\n"
                "                    displayName = Midlands\n"
                "                    value = 1.0\n"
                "                    color = RGB(64,64,64)\n"
                "                }\n"        
                "                Biome\n"
                "                {\n"
                "                    name = Highlands\n"
                "                    displayName = Lowlands\n"
                "                    value = 1.0\n"
                "                    color = RGB(128,128,128)\n"
                "                }\n"  
                "                Biome\n"
                "                {\n"
                "                    name = Peaks\n"
                "                    displayName = Peaks\n"
                "                    value = 1.0\n"
                "                    color = RGB(192,192,192)\n"
                "                }\n"  
                "                Biome\n"
                "                {\n"
                "                    name = Icecaps\n"
                "                    displayName = Icecaps\n"
                "                    value = 1.2\n"
                "                    color = RGB(150,200,255)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Oceans\n"
                "                    displayName = Oceans\n"
                "                    value = 1.5\n"
                "                    color = RGB(0, 0, 50)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Mountains\n"
                "                    displayName = Mountains\n"
                "                    value = 1.0\n"
                "                    color = RGB(255,255,0)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Volcanoes\n"
                "                    displayName = Volcanoes\n"
                "                    value = 1.5\n"
                "                    color = RGB(255,0,0)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Lava\n"
                "                    displayName = Lava\n"
                "                    value = 2.0\n"
                "                    color = RGB(255,98,0)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Canyons\n"
                "                    displayName = Canyons\n"
                "                    value = 1.0\n"
                "                    color = RGB(255,0,255)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Crater_Rays\n"
                "                    displayName = Crater Rays\n"
                "                    value = 1.0\n"
                "                    color = RGB(150, 255, 150)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Craters\n"
                "                    displayName = Craters\n"
                "                    value = 1.0\n"
                "                    color = RGB(0, 255, 150)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = AnomalousStructure\n"
                "                    displayName = Anomalous Structure\n"
                "                    value = 1.0\n"
                "                    color = RGB(119, 198, 247)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = CrashedShip\n"
                "                    displayName = Crashed Ship\n"
                "                    value = 1.0\n"
                "                    color = RGB(82, 96, 105)\n"
                "                }\n"
                "            }\n"
            )
        planetCfg.write(
            "        }\n"
        )
        if isAsteroid == True:
            planetCfg.write(
                "        Orbit\n"
                "        {\n"
                "            referenceBody = " + parentN + "\n"
                "            color = RGBA(" + terrainClr + ")\n"
                "            semiMajorAxis = " + str(planetSMA) + "\n"
                "            inclination = " + str(planetCfgRNG.randint(inclinationLimits[0],inclinationLimits[1])) + "\n"
                "            eccentricity = " + str(planetCfgRNG.randint(0,600)/1000) + "\n"
                "            longitudeOfAscendingNode = 0\n"
                "            argumentOfPeriapsis = 0\n"
                "            meanAnomalyAtEpochD = " + str(planetCfgRNG.randint(0,360)) + "\n"
                "            epoch = 0\n"
            )
        else:
            if tidallyLocked == True:
                planetCfg.write(
                    "        Orbit\n"
                    "        {\n"
                    "            referenceBody = " + parentN + "\n"
                    "            color = RGBA(" + terrainClr + ")\n"
                    "            semiMajorAxis = " + str(planetSMA) + "\n"
                    "            inclination = " + str(planetCfgRNG.randint(inclinationLimits[0],inclinationLimits[1])) + "\n"
                    "            eccentricity = " + str(planetCfgRNG.randint(0,10)/1000) + "\n"
                    "            longitudeOfAscendingNode = 90\n"
                    "            argumentOfPeriapsis = 0\n"
                    "            meanAnomalyAtEpochD = " + str(0) + "\n"
                    "            epoch = 0\n"
                )
            else:
                planetCfg.write(
                    "        Orbit\n"
                    "        {\n"
                    "            referenceBody = " + parentN + "\n"
                    "            color = RGBA(" + terrainClr + ")\n"
                    "            semiMajorAxis = " + str(planetSMA) + "\n"
                    "            inclination = " + str(planetCfgRNG.randint(inclinationLimits[0],inclinationLimits[1])) + "\n"
                    "            eccentricity = " + str(planetCfgRNG.randint(0,200)/1000) + "\n"
                    "            longitudeOfAscendingNode = 0\n"
                    "            argumentOfPeriapsis = 0\n"
                    "            meanAnomalyAtEpochD = " + str(planetCfgRNG.randint(0,360)) + "\n"
                    "            epoch = 0\n"
                )
        if atmo == "Atmospheric":
            if gasGiant == True:
                if rings == True:
                    planetCfg.write(
                        "            iconTexture = InfiniteDiscoveries/Textures/Misc/gasGiantRingedIco.png\n"
                    )
                else:
                    planetCfg.write(
                        "            iconTexture = InfiniteDiscoveries/Textures/Misc/gasGiantIco.png\n"
                    )
            else:
                if rings == True:
                    planetCfg.write(
                        "            iconTexture = InfiniteDiscoveries/Textures/Misc/rockAtmoRingedIco.png\n"
                    )
                else:
                    planetCfg.write(
                        "            iconTexture = InfiniteDiscoveries/Textures/Misc/rockAtmoIco.png\n"
                    )
        else:
            if rings == True:
                planetCfg.write(
                    "            iconTexture = InfiniteDiscoveries/Textures/Misc/rockVacuumRingedIco.png\n"
                )
            else:
                planetCfg.write(
                    "            iconTexture = InfiniteDiscoveries/Textures/Misc/rockVacuumIco.png\n"
                )
        planetCfg.write(
            "        }\n"
            "        ScaledVersion\n"
            "        {\n"
            "            type = " + atmo + "\n"
            "            Material\n"
            "            {\n"
        )
        if canConvertToDDS == True:
            planetCfg.write(
                "                texture = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_CLR" + ".dds" + "\n"
                "                normals = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_NRM" + ".dds" + "\n"
                "                color = 1,1,1,1\n"
            )
        else:
            planetCfg.write(
                "                texture = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_CLR" + ".png" + "\n"
                "                normals = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_NRM" + ".png" + "\n"
                "                color = 1,1,1,1\n"
            )
        if ocean == True:
            planetCfg.write(
                "                specColor = 0.5, 0.5, 0.5, 1\n"
                "                shininess = 0.3\n"
            )
        elif icy == True:
            planetCfg.write(
                "                specColor = 0.3, 0.3, 0.3, 1\n"
                "                shininess = 0.1\n"
            )
        else:
            planetCfg.write(
                "                specColor = 0, 0, 0, 1\n"
                "                shininess = 0.3\n"
            )
        planetCfg.write(
            "\n"
            "                rimPower = 1\n"
            "		         rimBlend = 0.5\n"
            "                Gradient\n"
            "                {\n"
            "                    0.0 = RGBA(" + str(sctrClrR) + ", " + str(sctrClrG) + ", " + str(sctrClrB) + ", 100" + ")\n"
            "                    0.3 = RGBA(" + str(atmClrR/2) + ", " + str(atmClrG/2) + ", " + str(atmClrB/2) + ", 100" + ")\n"
            "                    0.6 = RGBA(0, 0, 0, 0)\n"
            "                    1 = RGBA(0, 0, 0, 0)\n"
            "                }\n"
            "            }\n"
            "        }\n"
        )
        planetCfg.write(
            "        Rings\n"
            "        {\n"
            "           Ring\n"
            "            {\n"
            
            "\n"
            "                thickness = 0\n"
            "                steps = 120\n"
            "\n"
        )
        if rings == True:
            planetCfg.write(
            "                innerRadius = " + str(ringInn) + "\n"
            "                outerRadius = " + str(ringOut) + "\n"
            "                texture = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_RINGS" + ".png\n"
            )
        else:
            planetCfg.write(
            "                innerRadius = 2000\n"
            "                outerRadius = 2001\n"
            "                texture = InfiniteDiscoveries/Presets/RingNone.png\n"
            )
        planetCfg.write(
            "                tiles = 0\n"
            "                color = 1,1,1,1\n"
            "                unlit = false\n"
            "                useNewShader = true\n"
            "                penumbraMultiplier = 1\n"
            "\n"
            "                angle = 0\n"
            "                lockRotation = true\n"
            "                longitudeOfAscendingNode = 30\n"
            "                rotationPeriod = 600\n"
            "            }\n"
            "        }\n"
        )
        if ocean == True:
            planetCfg.write(
            "        Ocean\n"
            "        {\n"
            "            ocean = True\n"
            "            oceanColor = RGBA(" + str(oceanR) + ", " + str(oceanG) + ", " + str(oceanB) + ", 100)\n"
            "            oceanHeight = 0\n"
            "            density = 1\n"
            "            minLevel = 1\n"
            "            maxLevel = 10\n"
            "            minDetailDistance = 8\n"
            "            maxQuadLengthsPerFrame = 0.03\n"
            "            Material\n"
            "            {\n"
            "                color = RGBA(" + str(oceanR) + ", " + str(oceanG) + ", " + str(oceanB) + ", 100)\n"
            "                colorFromSpace = RGBA(" + str(oceanR) + ", " + str(oceanG) + ", " + str(oceanB) + ", 100)\n"
            "                specColor = 1,1,1,1\n"
            "                shininess = 1\n"
            "                gloss = 0.2\n"
            "                tiling = 1000\n"
            "                waterTex = BUILTIN/sea-water8\n"
            "                waterTexScale = 1,1\n"
            "                waterTexOffset = 0,0\n"
            "                waterTex1 = BUILTIN/sea-water1\n"
            "                waterTex1Scale = 1,1\n"
            "                waterTex1Offset = 0,0\n"
            "                bTiling = 800\n"
            "                bumpMap = BUILTIN/quiet\n"
            "                bumpMapScale = 1,1\n"
            "                bumpMapOffset = 0,0\n"
            "                displacement = 0.05\n"
            "                texDisplacement = 0.31\n"
            "                dispFreq = 0.15\n"
            "                mix = 0.4032745\n"
            "                oceanOpacity = 0.3\n"
            "                falloffPower = 3\n"
            "                falloffExp = 0.05\n"
            "                fogColor = 0.321443439,0.611232221,0.947761178,1\n"
            "                heightFallOff = 0.2\n"
            "                globalDensity = -8E-06\n"
            "                atmosphereDepth = 50000\n"
            "                //fogColorRamp = BUILTIN/blue_atmogradient\n"
            "                fogColorRampScale = 1,1\n"
            "                fogColorRampOffset = 0,0\n"
            "                fadeStart = 20000\n"
            "                fadeEnd = 60000\n"
            "                planetOpacity = 1\n"
            "                normalXYFudge = 1.4\n"
            "                normalZFudge = 1.18\n"
            "            }\n"
            "            FallbackMaterial\n"
            "            {\n"
            "                color = RGBA(" + str(oceanR) + ", " + str(oceanG) + ", " + str(oceanB) + ", 100)\n"
            "                colorFromSpace = RGBA(" + str(oceanR) + ", " + str(oceanG) + ", " + str(oceanB) + ", 100)\n"
            "                specColor = 0.8493402,0.8493402,0.8493402,1\n"
            "                shininess = 1\n"
            "                gloss = 0.3336538\n"
            "                tiling = 1000\n"
            "                waterTex = BUILTIN/sea-water1\n"
            "                waterTexScale = 1,1\n"
            "                waterTexOffset = 0,0\n"
            "                waterTex1 = BUILTIN/sea-water2\n"
            "                waterTex1Scale = 1,1\n"
            "                waterTex1Offset = 0,0\n"
            "                fadeStart = 20000\n"
            "                fadeEnd = 60000\n"
            "                planetOpacity = 1\n"
            "            }\n"
            "            Fog\n"
            "            {\n"
            "                afgAltMult = 0.05\n"
            "                afgBase = 0.6\n"
            "                afgLerp = False\n"
            "                afgMin = 0.05\n"
            "                fogColorEnd = 0,0.0850000009,0.122500002,1\n"
            "                fogColorStart = 0,0.340000004,0.49000001,1\n"
            "                fogDensityAltScalar = -0.0008\n"
            "                fogDensityEnd = 0.025\n"
            "                fogDensityExponent = 1\n"
            "                fogDensityPQSMult = 0.02\n"
            "                fogDensityStart = 0.005\n"
            "                skyColorMult = 1.1\n"
            "                skyColorOpacityAltMult = 15\n"
            "                skyColorOpacityBase = 0.25\n"
            "                sunAltMult = 0.01\n"
            "                sunBase = 0.5\n"
            "                sunMin = 0.05\n"
            "                useFog = True\n"
            "            }\n"
            "            Mods\n"
            "            {\n"
            "                AerialPerspectiveMaterial\n"
            "                {\n"
            "                    atmosphereDepth = 5000\n"
            "                    DEBUG_SetEveryFrame = False\n"
            "                    globalDensity = -7.5E-06\n"
            "                    heightFalloff = 0.2\n"
            "                    oceanDepth = 0\n"
            "                    order = 100\n"
            "                    enabled = True\n"
            "                    name = _Material_AerialPerspective\n"
            "                }\n"
            "                OceanFX\n"
            "                {\n"
            "                    angle = 0\n"
            "                    blendA = 0\n"
            "                    blendB = 0\n"
            "                    framesPerSecond = 10\n"
            "                    oceanOpacity = 0\n"
            "                    spaceAltitude = 0\n"
            "                    spaceSurfaceBlend = 0\n"
            "                    specColor = 0,0,0,0\n"
            "                    texBlend = 0\n"
            "                    txIndex = 0\n"
            "                    order = 100\n"
            "                    enabled = True\n"
            "                    name = OceanFX\n"
            "                    Watermain\n"
            "                    {\n"
            "                        value = BUILTIN/sea-water1\n"
            "                        value = BUILTIN/sea-water2\n"
            "                        value = BUILTIN/sea-water3\n"
            "                        value = BUILTIN/sea-water4\n"
            "                        value = BUILTIN/sea-water5\n"
            "                        value = BUILTIN/sea-water6\n"
            "                        value = BUILTIN/sea-water7\n"
            "                        value = BUILTIN/sea-water8\n"
            "                        value = BUILTIN/sea-water1\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            )
        if atmo == "Atmospheric":
            planetCfg.write(
                "        Atmosphere\n"
                "        {\n"
                "            enabled = true\n"
            )
            if oxygen == True:
                planetCfg.write(
                    "            oxygen = true\n"
                )
            else:
                planetCfg.write(
                    "            oxygen = false\n"
                )
            planetCfg.write(
                "            ambientColor = RGBA(" + str(sctrClrR/5) + ", " + str(sctrClrG/5) + ", " + str(sctrClrB/5) + ", 100" + ")\n"
                "            altitude = " + str(atmoHeight) + "\n"
                "            pressureCurveIsNormalized = false\n"
                "            staticPressureASL = " + str(atmoPress) + "\n"
                "            temperatureSeaLevel = " + str(finalTemp) + "\n"
                "            pressureCurve\n"
                "            {\n"
                "                key = 0 " + str(atmoPress) + " 0 " + str((-8E-05*atmoPress)/(atmoHeight/70000)) + "\n"
                "                key = " + str(atmoHeight/2) + " " + str(atmoPress/20) + " " + str((-5E-06*atmoPress)/(atmoHeight/70000)) + " " + str((-5E-06*atmoPress)/(atmoHeight/70000)) + "\n"
                "                key = " + str(atmoHeight) + " 0 0 0\n"
                "            }\n"
            )
            # This is based off BS science but it works so who cares. (I am NOT making a 1000 line calculator for this.)
            if oxygen == True:
                planetCfg.write(
                    "            temperatureCurve\n"
                    "            {\n"
                    "                key = " + str(0)               + " " + str(finalTemp) + " 0 0\n"
                    "                key = " + str(atmoHeight*0.25) + " " + str(finalTemp/1.35849056) + " 0 0\n"
                    "                key = " + str(atmoHeight*0.75) + " " + str(finalTemp/1.09923664) + " 0 0\n"
                    "                key = " + str(atmoHeight)      + " " + str(finalTemp/1.5483871) + " 0 0\n"
                    "            }\n"
                )
            else:
                planetCfg.write(
                    "            temperatureCurve\n"
                    "            {\n"
                    "                key = " + str(0)               + " " + str(finalTemp) + " 0 0\n"
                    "                key = " + str(atmoHeight*0.25) + " " + str(finalTemp/1.24137931) + " 0 0\n"
                    "                key = " + str(atmoHeight*0.75) + " " + str(finalTemp/1.6) + " 0 0\n"
                    "                key = " + str(atmoHeight)      + " " + str(finalTemp/1.30909090909) + " 0 0\n"
                    "            }\n"
                )
            planetCfg.write(
                "            temperatureSunMultCurve\n"
                "            {\n"
                "                key = 0 0 0 0\n"
                "                key = 35000 0 0 0\n"
                "            }\n"
                "            AtmosphereFromGround\n"
                "            {"
                "                DEBUG_alwaysUpdateAll = False\n"
                "                doScale = False\n"
                "                waveLength = RGBA(" + str(atmClrR+75) + ", " + str(atmClrG+75) + ", " + str(atmClrB+75) + ", 100" + ")\n"
                "                samples = 4\n"
                "		 		 innerRadius = 595626.9\n"
                "                outerRadius = 635865.6\n"
                "                innerRadiusMult = 0.9563388\n"
                "                outerRadiusMult = 1.045001\n"
                "                transformScale = 1.095,1.095,1.095\n"
                "            }\n"
                "        }\n"
            )
        if gasGiant == False:
            planetCfg.write(
                "        PQS\n"
                "        {\n"
                "            minLevel = 2\n"
            )
            if planetRadius < 30000:
                planetCfg.write(
                    "            maxLevel = 5\n"
                )
            else:
                planetCfg.write(
                    "            maxLevel = 10\n"
                )
            planetCfg.write(
                "            minDetailDistance = 8\n"
                "            maxQuadLengthsPerFrame = 0.03\n"
                "            fadeStart = 20000\n"
                "            fadeEnd = 120000\n"
                "            deactivateAltitude = 140000\n"
                "            mapMaxHeight = 20000\n"
                "            materialType = AtmosphericTriplanarZoomRotation\n"
                "            allowFootprints = True\n"
                "            Material\n"
                "            {\n"
                "                factor = 10\n"
                "                factorBlendWidth = 0.05\n"
                "                factorRotation = 135\n"
                "                saturation = 1.4\n"
                "                contrast = 1.3\n"
                "                tintColor = 1,1,1,1\n"
                "                specularColor = 0.1,0.1,0.1,1\n"
                "                albedoBrightness = 1.5\n"
                "                steepPower = 2\n"
                "                steepTexStart = 10000\n"
                "                steepTexEnd = 200000\n"
                "                steepTex = BUILTIN/ikeSteep_diffuse\n"
                "                steepTexScale = 1,1\n"
                "                steepTexOffset = 0,0\n"
                "                steepBumpMap = BUILTIN/ikeSteep_nrm\n"
                "                steepBumpMapScale = 1,1\n"
                "                steepBumpMapOffset = 0,0\n"
                "                steepNearTiling = 50\n"
                "                steepTiling = 50\n"
                "                midTex = BUILTIN/gillyMedTerrain_diffuse\n"
                "                midTexScale = 1,1\n"
                "                midTexOffset = 0,0\n"
                "                midTiling = 150000\n"
                "                midBumpMap = BUILTIN/gillyMedTerrain_nrm\n"
                "                midBumpMapScale = 1,1\n"
                "                midBumpMapOffset = 0,0\n"
                "                midBumpTiling = 150000\n"
                "                lowStart = -1\n"
                "                lowEnd = -1\n"
                "                highStart = 2\n"
                "                highEnd = 2\n"
                "                globalDensity = 1\n"
                "                planetOpacity = 0\n"
                "                oceanFogDistance = 1000\n"
                "            }\n"
                "            Mods\n"
                "            {\n"
                "                VertexMitchellNetravaliHeightMap:NEEDS[VertexMitchellNetravaliHeightMap]\n"
                "                {\n"
            )
            if canConvertToDDS == False:
                planetCfg.write(
                    "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_HGT" + ".png" + "\n"
                )
            else:
                planetCfg.write(
                    "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_HGT" + ".dds" + "\n"
                )
            if ocean == True:
                if tidallyLocked == True and moon == False:
                    planetCfg.write(
                        "                    offset = -1300\n"   
                    )
                else:
                    planetCfg.write(
                        "                    offset = " + str((((oceanFactor/255)*8000)*-1)-50) + "\n"   
                    )
            else:
                planetCfg.write(
                    "                    offset = 0\n"   
                )
            if ocean == True:
                planetCfg.write(
                    "                    deformity = 8000\n"
                    "                    scaleDeformityByRadius = False\n"
                )
            else:
                if planetRadius < 30000:
                    planetCfg.write(
                        "                    deformity = 10000\n"
                        "                    scaleDeformityByRadius = True\n"
                    )
                else:
                    planetCfg.write(
                        "                    deformity = 8000\n"
                        "                    scaleDeformityByRadius = True\n"
                    )
            planetCfg.write(
                "                    order = 10\n"
                "                    enabled = True\n"
                "                    B = 1\n"
                "                    C = 0\n"
                "                }\n"
                "\n"
                "                VertexHeightMap:NEEDS[!VertexMitchellNetravaliHeightMap]\n"
                "                {\n"
            )
            if canConvertToDDS == False:
                planetCfg.write(
                    "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_HGT" + ".png" + "\n"
                )
            else:
                planetCfg.write(
                    "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_HGT" + ".dds" + "\n"
                )
            if ocean == True:
                if tidallyLocked == True and moon == False:
                    planetCfg.write(
                        "                    offset = -1300\n"   
                    )
                else:
                    planetCfg.write(
                        "                    offset = " + str((((oceanFactor/255)*8000)*-1)-50) + "\n"  
                    )
            else:
                planetCfg.write(
                    "                    offset = 0\n"   
                )
            if ocean == True:
                planetCfg.write(
                    "                    deformity = 8000\n"
                    "                    scaleDeformityByRadius = False\n"
                )
            else:
                planetCfg.write(
                    "                    deformity = 8000\n"
                    "                    scaleDeformityByRadius = True\n"
                )
            planetCfg.write(
                "                    order = 10\n"
                "                    enabled = True\n"
                "                }\n"
                "                VertexColorMap\n"
                "                {\n"
            )
            if ocean == True:
                if canConvertToDDS == True:
                    planetCfg.write(
                        "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_VERTCLR" + ".dds" + "\n"
                    )
                else:
                    planetCfg.write(
                        "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_VERTCLR" + ".png" + "\n"
                    )
            else:
                if canConvertToDDS == True:
                    planetCfg.write(
                        "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_CLR" + ".dds" + "\n"
                    )
                else:
                    planetCfg.write(
                        "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_CLR" + ".png" + "\n"
                    )
            planetCfg.write(
                "                   order = 20\n"
                "                   enabled = true\n"
                "                }\n"
            )
            if ocean == False:
                if planetRadius < 30000:
                    planetCfg.write(
                        "                VertexHeightNoiseVertHeightCurve2\n"
                        "                {\n"
                        "                    deformity = 200\n"
                        "                    ridgedAddFrequency = 32\n"
                        "                    ridgedAddLacunarity = 2\n"
                        "                    ridgedAddOctaves = 8\n"
                        "                    ridgedAddSeed = 456352342\n"
                        "                    ridgedMode = Low\n"
                        "                    ridgedSubFrequency = 32\n"
                        "                    ridgedSubLacunarity = 2\n"
                        "                    ridgedSubOctaves = 8\n"
                        "                    ridgedSubSeed = 234352\n"
                        "                    simplexFrequency = 32\n"
                        "                    simplexHeightEnd = 6000\n"
                        "                    simplexHeightStart = 0\n"
                        "                    simplexOctaves = 8\n"
                        "                    simplexPersistence = 0.5\n"
                        "                    simplexSeed = 345463425\n"
                        "                    order = 40\n"
                        "                    enabled = True\n"
                        "                    simplexCurve\n"
                        "                    {\n"
                        "                        key = 0 0 0 0\n"
                        "                        key = 0.6311918 0.4490898 1.432598 1.432598\n"
                        "                        key = 1 1 0 0\n"
                        "                    }\n"
                        "                }\n"
                    )
                else:
                    planetCfg.write(
                        "                VertexHeightNoiseVertHeightCurve2\n"
                        "                {\n"
                        "                    deformity = 2000\n"
                        "                    ridgedAddFrequency = 64\n"
                        "                    ridgedAddLacunarity = 2\n"
                        "                    ridgedAddOctaves = 8\n"
                        "                    ridgedAddSeed = 456352342\n"
                        "                    ridgedMode = Low\n"
                        "                    ridgedSubFrequency = 64\n"
                        "                    ridgedSubLacunarity = 2\n"
                        "                    ridgedSubOctaves = 8\n"
                        "                    ridgedSubSeed = 234352\n"
                        "                    simplexFrequency = 64\n"
                        "                    simplexHeightEnd = 6000\n"
                        "                    simplexHeightStart = 0\n"
                        "                    simplexOctaves = 8\n"
                        "                    simplexPersistence = 0.5\n"
                        "                    simplexSeed = 345463425\n"
                        "                    order = 40\n"
                        "                    enabled = True\n"
                        "                    simplexCurve\n"
                        "                    {\n"
                        "                        key = 0 0 0 0\n"
                        "                        key = 0.6311918 0.4490898 1.432598 1.432598\n"
                        "                        key = 1 1 0 0\n"
                        "                    }\n"
                        "                }\n"
                    )
            else:
                planetCfg.write(
                    "                VertexHeightNoiseVertHeightCurve2\n"
                    "                {\n"
                    "                    deformity = 1000\n"
                    "                    ridgedAddFrequency = 64\n"
                    "                    ridgedAddLacunarity = 2\n"
                    "                    ridgedAddOctaves = 8\n"
                    "                    ridgedAddSeed = 456352342\n"
                    "                    ridgedMode = Low\n"
                    "                    ridgedSubFrequency = 64\n"
                    "                    ridgedSubLacunarity = 2\n"
                    "                    ridgedSubOctaves = 8\n"
                    "                    ridgedSubSeed = 234352\n"
                    "                    simplexFrequency = 64\n"
                    "                    simplexHeightEnd = 6000\n"
                    "                    simplexHeightStart = 0\n"
                    "                    simplexOctaves = 8\n"
                    "                    simplexPersistence = 0.5\n"
                    "                    simplexSeed = 345463425\n"
                    "                    order = 40\n"
                    "                    enabled = True\n"
                    "                    simplexCurve\n"
                    "                    {\n"
                    "                        key = 0 0 0 0\n"
                    "                        key = 0.6311918 0.4490898 1.432598 1.432598\n"
                    "                        key = 1 1 0 0\n"
                    "                    }\n"
                    "                }\n"
                )
            if anomaly == "fltStrc":
                planetCfg.write(
                "                City2\n"
                "                {\n"
                "                    snapToSurface = True\n"
                "                    alt = 2000\n"
                "                    lat = " + str(anLatLon[0]) + "\n"
                "                    lon = " + str(anLatLon[1]) + "\n"
                "                    objectName = Gravity Deflector\n"
                "                    up = 0,1,0\n"
                "                    rotation = 0\n"
                "                    snapHeightOffset = 0\n"
                "                    commnetStation = False\n"
                "                    isKSC = False\n"
                "                    order = 100\n"
                "                    enabled = True\n"
                "                    name = floatyBoi\n"
                "                    LOD\n"
                "                    {\n"
                "                        Value\n"
                "                        {\n"
                "                            visibleRange = 30000\n"
                "                            keepActive = False\n"
                "                            model = InfiniteDiscoveries/Objects/floatingStrucutre/floatyBoi\n"
                "                            scale = 10,10,10\n"
                "                            delete = False\n"
                "                        }\n"
                "                    }\n"
                "                }\n"
                )
            if anomaly == "crshShp":
                planetCfg.write(
                "                City2\n"
                "                {\n"
                "                    snapToSurface = True\n"
                "                    alt = 2651.57348651835\n"
                "                    lat = " + str(anLatLon[0]) + "\n"
                "                    lon = " + str(anLatLon[1]) + "\n"
                "                    objectName = Crashed Ship\n"
                "                    up = 0,1,0\n"
                "                    rotation = 0\n"
                "                    snapHeightOffset = 0\n"
                "                    commnetStation = False\n"
                "                    isKSC = False\n"
                "                    order = 100\n"
                "                    enabled = True\n"
                "                    name = crashedShip\n"
                "                    LOD\n"
                "                    {\n"
                "                        Value\n"
                "                        {\n"
                "                            visibleRange = 30000\n"
                "                            keepActive = False\n"
                "                            model = InfiniteDiscoveries/Objects/spaceship/spaceship\n"
                "                            scale = 10,10,10\n"
                "                            delete = False\n"
                "                        }\n"
                "                    }\n"
                "                }\n"
                )
            planetCfg.write(
                "                LandControl\n"
                "                {\n"
                "                    altitudeBlend = 0.01\n"
                "                    altitudeFrequency = 2\n"
                "                    altitudeOctaves = 2\n"
                "                    altitudePersistance = 0.5\n"
                "                    altitudeSeed = 53453\n"
                "                    createColors = True\n"
                "                    createScatter = True\n"
                "                    latitudeBlend = 0.05\n"
                "                    latitudeFrequency = 12\n"
                "                    latitudeOctaves = 6\n"
                "                    latitudePersistance = 0.5\n"
                "                    latitudeSeed = 53456345\n"
                "                    longitudeBlend = 0.05\n"
                "                    longitudeFrequency = 12\n"
                "                    longitudeOctaves = 4\n"
                "                    longitudePersistance = 0.5\n"
                "                    longitudeSeed = 98888\n"
                "                    useHeightMap = False\n"
                "                    vHeightMax = 6000\n"
                "                    order = 100\n"
                "                    enabled = True\n"
                "                    name = LCExample\n"
                "                    landClasses\n"
                "                    {\n"
                "                        Value\n"
                "                        {\n"
                "                            alterApparentHeight = 0\n"
                "                            alterRealHeight = 0\n"
                "                            color = 0,0,0,1\n"
                "                            coverageBlend = 1\n"
                "                            coverageFrequency = 1.5\n"
                "                            coverageOctaves = 4\n"
                "                            coveragePersistance = 0.5\n"
                "                            coverageSeed = 171214\n"
                "                            name = Base\n"
                "                            latDelta = 1\n"
                "                            latitudeDouble = False\n"
                "                            lonDelta = 1\n"
                "                            minimumRealHeight = 0\n"
                "                            noiseBlend = 0.5\n"
                "                            noiseColor = 0,0,0,1\n"
                "                            noiseFrequency = 8\n"
                "                            noiseOctaves = 4\n"
                "                            noisePersistance = 0.5\n"
                "                            noiseSeed = 453737\n"
                "                            delete = False\n"
                "                            altitudeRange\n"
                "                            {\n"
                "                                endEnd = 1\n"
                "                                endStart = 0.5\n"
                "                                startEnd = 0.5\n"
                "                                startStart = 0\n"
                "                            }\n"
                "                            latitudeRange\n"
                "                            {\n"
                "                                endEnd = 0.8\n"
                "                                endStart = 0.75\n"
                "                                startEnd = 0.25\n"
                "                                startStart = 0.2\n"
                "                            }\n"
                "                            longitudeRange\n"
                "                            {\n"
                "                                endEnd = 2\n"
                "                                endStart = 2\n"
                "                                startEnd = -1\n"
                "                                startStart = -1\n"
                "                            }\n"
                "                        }\n"
                "                    }\n"
                "                }\n"
                "            }\n"
                "        }\n"
            )
        if Lava == True:
            planetCfg.write(
                "        HazardousBody\n"
                "        {\n"
                "            Item\n"
                "            {\n"
                "                biomeName = Lava\n"
                "                ambientTemp = 2000\n"
                "                AltitudeCurve\n"
                "                {\n"
                "                    key = " + str(planetRadius) + " 1\n"
                "                    key = " + str(planetRadius + 1500) + " 0\n"
                "                }\n"
                "            }\n"
                "        }\n"
            )
        planetCfg.write(
            "    }\n"
            "}\n"
        )
        allActions.append([time.localtime(),"Wrote config for body : " + planetName])
        allActionArrayUpdated = True
    # Generates terrestrial maps.
    def GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, kpaASL, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano, lava, tidallyLocked, oceanFactor, isAsteroid, planetSeed, icy):
        terrainGenRNG = random.Random()
        terrainGenRNG_NP = np.random.RandomState()

        print(planetSeed)
        terrainGenRNG.seed(planetSeed)
        terrainGenRNG_NP.seed(planetSeed)

        print(threading.current_thread())
        allActions.append([time.localtime(),"Generating maps for: " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        albedoMap = Image.new("RGBA", (4096,2048), (0,0,0,0))

        if planetRadius < 30000:
            isAsteroid = True
        else:
            isAsteroid = False

        eyeballType = ""

        if finalTemp >= 700:
            eyeballType = "Hot"
        elif finalTemp < 700 and finalTemp >= 215:
            eyeballType = "Temperate"
        elif finalTemp < 215:
            eyeballType = "Cold"

        if tidallyLocked == True:
            if vacuum == False:
                isEyeball = True
                print("Eyeball planet! " + eyeballType)
            else:
                isEyeball = False
        else:
            isEyeball = False

        #if tidallyLocked == True:
        #    print(eyeballType + "< IN WHAT FUCKING UNIVERSE" + str(finalTemp))

        def convertToBiomeFeature(featureMap, colour, brighten1):
            biomeFeature = Image.new("RGBA", (4096,2048), colour)
            biomeFeature.putalpha(ImageEnhance.Brightness(ImageOps.posterize(ImageEnhance.Brightness((featureMap.getchannel("A"))).enhance(brighten1), 1)).enhance(2))
            biomeMap.paste(biomeFeature, (0,0), mask=biomeFeature)

        def add_Surface_Features(noiseImg, type, amount, alphaAdd, minMax, types, mean, std_dev, albedo=None):
            allActions.append([time.localtime(),"Adding feature " + type + " to: " + planetName])
            global allActionArrayUpdated
            allActionArrayUpdated = True
            #print(multiprocessing.current_process)
            featureMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
            minSize = minMax[0]
            maxSize = minMax[1]
            for i in range(0,amount):
                feature = Image.open(filepath + "/Presets/" + type + str(terrainGenRNG.randint(1,types)) + ".png")
                featureSizeInt = int(terrainGenRNG_NP.normal(mean, std_dev))
                featureSize = max(minSize, min(maxSize, featureSizeInt))
                featurePreRes = feature.resize((featureSize,featureSize))
                featureA = featurePreRes.getchannel("A")
                alpha1 = Image.new("L", (featureSize, featureSize), (int(alphaAdd*(featureSize/minMax[1])))*2)
                featureA2 = ImageChops.multiply(alpha1,featureA)
                featurePreRes.putalpha(featureA2)

                print("Generating " + type + " " + str(i) + "...", end="\r")

                offs1 = terrainGenRNG.randint(0,4096-featureSize)
                offs2 = terrainGenRNG.randint(0,2048)
                #print(str(offs1) + " " + str(offs2))
                dist = (((offs2/2048)*2)*90)-90
                distCos = math.cos(math.radians(dist))
                featureRot = featurePreRes.rotate(terrainGenRNG.randint(0,360))
                featureRes = featureRot.resize((featureSize,math.ceil(featureSize*distCos)))
                
                featureMap.paste(featureRes, (int(offs1),int(offs2-featureSize//4)), mask=featureRes)

                if not albedo == None:
                    albFeature = Image.open(filepath + "/Presets/" + albedo + str(terrainGenRNG.randint(1,types)) + ".png")
                    albFeaturePreRes = albFeature.resize((featureSize,featureSize))
                    albFeatureA = albFeaturePreRes.getchannel("A")
                    albAlpha1 = Image.new("L", (featureSize, featureSize), (200))
                    albFeatureA2 = ImageChops.multiply(albAlpha1,albFeatureA)
                    albFeaturePreRes.putalpha(albFeatureA2)
                    albFeatureRot = albFeaturePreRes.rotate(terrainGenRNG.randint(0,360))
                    albFeatureRes = albFeatureRot.resize((featureSize,math.ceil(featureSize*distCos)))
                    albedoMap.paste(albFeatureRes, (int(offs1),int(offs2-featureSize//4)), mask=albFeatureRes)
            noiseImg.paste(featureMap, (0,0), featureMap)
            if not albedo == None:
                return featureMap, albedoMap
            else:
                return featureMap

        if round(finalTemp/100) < 17:
            lavaClr = (lavaSpectrum[round(finalTemp/100)])
            lavaClr2 = (lavaSpectrum[round(finalTemp/100)-7])
        else:
            lavaClr =  Color('#ff2100')  #lavaSpectrum[11]
            lavaClr2 = (lavaSpectrum[11])

        print(lavaClr)
        print(lavaClr2)
        
        lavaClrRGB = Color.get_rgb(lavaClr)
        lavaClr2RGB = Color.get_rgb(lavaClr2)

        print("Generating noise...")
        texStartTime = time.time()
        seed = terrainGenRNG.randint(0,10000)
        size = 1024
        radius = 1.0
        octaves = Settings.noiseOctaves
        #lacunarity = Settings.noiseLacunarity
        persistence = 0.5
        heightmap = np.zeros((size, size))
        #freq_random = random.randint(Settings.noiseFrequencyMin,Settings.noiseFrequencyMax)/10
        if isAsteroid == True:
            freq_random = terrainGenRNG.randint(2,8)/10
            lacunarity = 5
        else:
            freq_random = terrainGenRNG.randint(Settings.noiseFrequencyMin,Settings.noiseFrequencyMax)/10
            lacunarity = Settings.noiseLacunarity

        allActions.append([time.localtime(),"Generating noise for : " + planetName])
        allActionArrayUpdated = True

        for i in range(size):
            if everythingEnded == True:
                raise Exception("UI thread isn't running.")
            print("Generating for " + str(time.time()-texStartTime) + " seconds...", end="\r")
            for j in range(size):
                # Convert the pixel coordinates to spherical coordinates
                theta = 2 * math.pi * i / size
                phi = math.pi * j / size
                x = radius * math.sin(phi) * math.cos(theta)
                y = radius * math.sin(phi) * math.sin(theta)
                z = radius * math.cos(phi)

                # Sample the noise function at the current point using multiple octaves
                noise_value = 0.0
                frequency = freq_random
                amplitude = 1.0
                for k in range(octaves):
                    noise_value += amplitude * noise.snoise4(x * frequency, y * frequency, z * frequency, seed)
                    frequency *= lacunarity
                    amplitude *= persistence

                # Store the noise value in the heightmap
                heightmap[i, j] = noise_value

        #if lava == True:
        #    lavaNoise = np.zeros((size, size))
        #    for i in range(size):
        #        print("Generating for " + str(time.time()-texStartTime) + " seconds...", end="\r")
        #        for j in range(size):
        #            # Convert the pixel coordinates to spherical coordinates
        #            theta = 2 * math.pi * i / size
        #            phi = math.pi * j / size
        #            x = radius * math.sin(phi) * math.cos(theta)
        #            y = radius * math.sin(phi) * math.sin(theta)
        #            z = radius * math.cos(phi)
#
        #            # Sample the noise function at the current point using multiple octaves
        #            noise_value = 0.0
        #            frequency = 1
        #            amplitude = 1.0
        #            for k in range(octaves):
        #                noise_value += amplitude * noise.snoise4(x * frequency, y * frequency, z * frequency, seed)
        #                frequency *= 10
        #                amplitude *= 0.5
#
        #            # Store the noise value in the heightmap
        #            lavaNoise[i, j] = noise_value
#
        #    lavaNoise = (lavaNoise - lavaNoise.min()) / (lavaNoise.max() - lavaNoise.min())
        #    lavaNoiseImage = Image.fromarray((lavaNoise * 255).astype(np.uint8), mode='L')
        #    lavaImage90 = lavaNoiseImage.rotate(90)
        #    lavaImageRes = lavaImage90.resize((4096,2048), resample=Image.Resampling.BICUBIC)

        heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
        image = Image.fromarray((heightmap * 255).astype(np.uint8), mode='L')
        image90 = image.rotate(90)
        imageRes = image90.resize((4096,2048), resample=Image.Resampling.BICUBIC)
        brtAmount = 1 # terrainGenRNG.randint(50,100)/100
        contrAmount = 1/brtAmount
        imageContr = ImageEnhance.Contrast(ImageEnhance.Brightness(imageRes).enhance(brtAmount)).enhance(contrAmount)
        texEndTime = time.time()
        noiseEndTime = texEndTime-texStartTime

        smallNoise = Image.new("L", [2048,1024], (0))

        for w in range(1024):
            for h in range(2048):
                randomValue = terrainGenRNG.randint(0,255)
                smallNoise.putpixel((h,w),randomValue)

        smallNoiseRes = smallNoise.resize((4096,2048)).convert("RGBA")
        smallNoiseRes.putalpha(terrainGenRNG.randint(2,8))

        imageContr.paste(smallNoiseRes,(0,0),mask=smallNoiseRes)

        print("Finished generating noise. Time elapsed: " + str(noiseEndTime) + " seconds.")

        # For future me. The function (in order) takes the Original Image, decal name, amount, alpha, min/max size, variants, mean, standard deviation, and an optional albedo feature.
        if kpaASL < 35:
            if icy == False:
                if planetRadius < 30000 and planetRadius > 5000:
                    large_craterMap = add_Surface_Features(imageContr, "crater", 50, 100, [500,1024], 2, 500, 750)
                elif planetRadius > 30000:
                    craterMap = add_Surface_Features(imageContr, "crater", 250, 225, [200,800], 3, 250, 200)
                    craterClusterMap = add_Surface_Features(imageContr, "craterCluster", 100, 225, [200,800], 1, 250, 200)
                    small_craterMap = add_Surface_Features(imageContr, "crater", 500, 100, [25,250], 2, 100, 100)
                if planetRadius > 75000 and ocean == False:
                    ray_craterMap, ray_albedoMap = add_Surface_Features(imageContr, "rayCrater", 200, 50, [100,700], 1, 100, 200, "rayCrater_alb")
            else:
                if kpaASL < 35:
                    craterMap = add_Surface_Features(imageContr, "crater", 50, 225, [200,800], 3, 250, 200)
                icy_Crack_Map = add_Surface_Features(imageContr, "crack", 300, 255, [400,600], 2, 50, 500)
        if geoActive == True and planetRadius > 80000:
            volcanoMap = add_Surface_Features(imageContr, "volcano", 200, 150, [50,200], 1, 50, 100)
            if activeVolcano == True:
                activeVolcanoMap, lavaAlbedoMap = add_Surface_Features(imageContr, "volcano", 100, 150, [200,300], 1, 50, 100, "volcano_Lava")
            canyonMap = add_Surface_Features(imageContr, "canyon", 400, 125, [50,400], 2, 50, 100)
        if vacuum == False and planetRadius > 30000:
            mountainMap = add_Surface_Features(imageContr, "mountain", 400, 175, [50,600], 3, 50, 300)
            plateauMap = add_Surface_Features(imageContr, "plateau", 400, 175, [50,600], 4, 50, 300)
        if lava == True and planetRadius > 50000:
            crackMap = add_Surface_Features(imageContr, "canyon", 200, 255, [100,500], 2, 50, 500)

        if icecaps == True:
            allActions.append([time.localtime(),"Generating icecaps for : " + planetName])
            allActionArrayUpdated = True
            # Generate the icecap image and open the displacement map image
            icecap_img = Image.new("RGBA", (4096,2048), (255,255,255,255))
            map_img = imageRes.convert("RGBA")
            Height = finalTemp * 6
            backg_black = Image.new("L", (4096,2048), (0))
            img_black = Image.new("L", (4096,Height), (255))
            center_y = icecap_img.size[1] // 2
            top_left_y = center_y - img_black.size[1] // 2
            backg_black.paste(img_black, (0,top_left_y+(int(top_left_y/((280/finalTemp)*(280/finalTemp))))), mask=img_black)
            icecap_img.putalpha(ImageOps.invert(backg_black))

            blurred_map_img = map_img.filter(ImageFilter.GaussianBlur(radius=3))
            # Get the pixel access objects for both images
            img_pixels = icecap_img.load()
            map_pixels = blurred_map_img.load()
            # Define the displacement amount (in pixels)
            displacement = Settings.icecapDisplacement
            # Loop through each pixel in the image
            for y in range(icecap_img.size[1]):
                if everythingEnded == True:
                    raise Exception("UI thread isn't running.")
                print("Calculating icecap deformity for pixel row " + str(y), end="\r")
                for x in range(icecap_img.size[0]):
                    # Get the displacement value from the map image
                    map_value = map_pixels[x, y][0]  # Use the first channel of the map image

                    # Calculate the new x-coordinate with the displacement value
                    new_y = y + (map_value - 16) * displacement / 16

                    # Get the pixel value from the original image at the new coordinates
                    try:
                        pixel = img_pixels[x, new_y]
                    except IndexError:
                        pixel = (255, 255, 255)

                    # Set the pixel value in the displaced image
                    img_pixels[x, y] = pixel
            print("Finished generating icecaps!")
            if ocean == True: # Icecaps for the fucking thing
                heightmapFiltered = imageContr.point( lambda p: 255 if p > oceanFactor else 0 )
                #heightmapFilteredButAlsoInverted = ImageOps.invert(heightmapFiltered)
                icecap_foroceans = Image.new("RGBA", (4096,2048), (oceanFactor+8,oceanFactor+8,oceanFactor+8,255))
                #icecap_foroceans.putalpha(heightmapFilteredButAlsoInverted)
                anotherFUCKINGBLACKBOX = Image.new("L", (4096,2048), (0))
                anotherFUCKINGBLACKBOX.putalpha(heightmapFiltered)
                blackFuckingBoxWhyTheFuckDoINeedToDoThis = Image.new("L", (4096,2048), (0))
                blackFuckingBoxWhyTheFuckDoINeedToDoThis.paste(icecap_img, (0,0), mask=icecap_img)
                blackFuckingBoxWhyTheFuckDoINeedToDoThis.paste(anotherFUCKINGBLACKBOX, (0,0), mask=anotherFUCKINGBLACKBOX)
                icecap_foroceans.putalpha(blackFuckingBoxWhyTheFuckDoINeedToDoThis)
                #heightmapFilteredButAlsoInverted.show()
                #icecap_foroceans.show()
                #icecap_img.show()
                imageContr.paste(icecap_foroceans, (0,0), mask=icecap_foroceans)

        if isEyeball == True:
            allActions.append([time.localtime(),"Generating eyeball overlay with type '" + eyeballType + "' for: " + planetName])
            allActionArrayUpdated = True

            eyeball = Image.new("RGBA", (4096,2048), (255,255,255,255))
            blackCircle = Image.open(filepath + "/Presets/blackcircle.png")

            if eyeballType == "Temperate":
                circleSize = 1500
                backCircleSize = 2048
            elif eyeballType == "Cold":
                circleSize = finalTemp * 7
                backCircleSize = 2500
            elif eyeballType == "Hot":
                circleSize = finalTemp * 2
                backCircleSize = 2500

            blackCircleResized = blackCircle.resize((circleSize,circleSize))

            backBlackCircleResized = blackCircle.resize((backCircleSize,backCircleSize))

            circlePosX = int(2048 - (circleSize / 2))
            circlePosY = int(1024 - (circleSize / 2))

            backCirclePosX = int(2048 - (backCircleSize / 2))
            backCirclePosY = int(1024 - (backCircleSize / 2))

            Thingamabob = Image.new("RGBA", (4096,2048), (0,0,0,0))
            Thingamabob.paste(blackCircleResized, (circlePosX,circlePosY), mask=blackCircleResized)

            backThingamabob = Image.new("RGBA", (4096,2048), (0,0,0,0))
            backThingamabob.paste(backBlackCircleResized, (backCirclePosX,backCirclePosY), mask=backBlackCircleResized)

            blackCircle = Thingamabob
            backBlackCircleMoved = ImageChops.offset(backThingamabob, 2048,0)

            #backBlackCircleMoved.show()

            if eyeballType == "Temperate":
                eyeball.paste(blackCircle, (0,0), mask=blackCircle)

                eyeball.paste(backBlackCircleMoved, (0,0), mask=backBlackCircleMoved)
            elif eyeballType == "Cold":
                eyeball.paste(blackCircle, (0,0), mask=blackCircle)
            elif eyeballType == "Hot":
                eyeball.paste(blackCircle, (0,0), mask=blackCircle)

            map_img = imageRes.convert("RGBA")
            #Height = temp * 6
            #backg_black = Image.new("L", (4096,2048), (0))
            #img_black = Image.new("L", (4096,Height), (255))
            #center_y = icecap_img.size[1] // 2
            #top_left_y = center_y - img_black.size[1] // 2
            #backg_black.paste(img_black, (0,top_left_y+(int(top_left_y/((280/temp)*(280/temp))))), mask=img_black)
            #icecap_img.putalpha(ImageOps.invert(backg_black))

            #eyeball.show()

            #blurred_map_img = map_img.filter(ImageFilter.GaussianBlur(radius=2))
            # Get the pixel access objects for both images
            img_pixels = eyeball.load()
            map_pixels = map_img.load()
            # Define the displacement amount (in pixels)
            displacement = 25
            # Loop through each pixel in the image
            for y in range(eyeball.size[1]):
                if everythingEnded == True:
                    raise Exception("UI thread isn't running.")
                #print("Calculating icecap deformity for pixel row " + str(y), end="\r")
                for x in range(eyeball.size[0]):
                    # Get the displacement value from the map image
                    map_value = map_pixels[x, y][0]  # Use the first channel of the map image

                    # Calculate the new x-coordinate with the displacement value
                    new_x = x + (map_value - 16) * displacement / 16

                    # Get the pixel value from the original image at the new coordinates
                    try:
                        pixel = img_pixels[new_x, y]
                    except IndexError:
                        pixel = img_pixels[x, y]

                    # Set the pixel value in the displaced image
                    img_pixels[x, y] = pixel
            #print("Finished generating icecaps!")
            eyeballMoved = ImageChops.offset(eyeball, 150,0)
            eyeballDist = eyeballMoved.convert("L")
            #eyeballDist.show()

        print("Finished overlaying surface features!")

        print("Generating normals...")
        texStartTime = time.time()
        # Load the grayscale image and normalize to [0, 1]
        img_gray = imageContr.convert("L")
        img_gray_data = np.array(img_gray) / 64.0
        # Compute the height map by subtracting from 1.0
        height_map = 1.0 - img_gray_data
        # Compute the partial derivatives using Sobel operator
        dx = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
        dy = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
        height_dx = convolve2d(height_map, dx, mode="same")
        height_dy = convolve2d(height_map, dy, mode="same")
        # Compute the normal vectors at each pixel
        normal_vectors = np.dstack((-height_dx, -height_dy, np.ones_like(height_dx)))
        norm = np.linalg.norm(normal_vectors, axis=-1, keepdims=True)
        normal_vectors = normal_vectors / norm
        # Scale the normal vectors to [0, 255]
        normal_vectors = ((normal_vectors + 1) / 2) * 255
        # Create a new image from the normal vectors
        img_normal = Image.fromarray(normal_vectors.astype(np.uint8))

        img_normalFilter = img_normal.filter(ImageFilter.SMOOTH)
        nrm_Patch = Image.open(targetPath + "/Presets/" + "normalPatch.png")
        img_normalFilter.paste(nrm_Patch, (0,0), mask=nrm_Patch)
        texEndTime = time.time()
        nrmEndTime = texEndTime-texStartTime
        print("Finished generating normals. Time elapsed: " + str(nrmEndTime) + " seconds.")

        ImageResFilter = imageContr.filter(ImageFilter.SMOOTH_MORE)

        print("Generating color...")
        texStartTime = time.time()

        grayMap = ImageOps.grayscale(ImageResFilter)
        if life == "organic":
            randomB_R = plantColor[0]*255
            randomB_G = plantColor[1]*255
            randomB_B = plantColor[2]*255
            randomM_R = terrainGenRNG.randint(Settings.LIFE_M_RedMin,Settings.LIFE_M_RedMax)
            randomM_G = terrainGenRNG.randint(Settings.LIFE_M_GreenMin,Settings.LIFE_M_GreenMax)
            randomM_B = terrainGenRNG.randint(Settings.LIFE_M_BlueMin,Settings.LIFE_M_BlueMax)
            randomW_R = terrainGenRNG.randint(Settings.LIFE_W_RedMin,Settings.LIFE_W_RedMax)
            randomW_G = terrainGenRNG.randint(Settings.LIFE_W_GreenMin,Settings.LIFE_W_GreenMax)
            randomW_B = terrainGenRNG.randint(Settings.LIFE_W_BlueMin,Settings.LIFE_W_BlueMax)
        elif life == None and ocean == True and icy == False:
            randomB_R = terrainGenRNG.randint(Settings.OCEAN_B_RedMin,Settings.OCEAN_B_RedMax)
            randomB_G = terrainGenRNG.randint(Settings.OCEAN_B_GreenMin,Settings.OCEAN_B_GreenMax)
            randomB_B = terrainGenRNG.randint(Settings.OCEAN_B_BlueMin,Settings.OCEAN_B_BlueMax)
            randomM_R = terrainGenRNG.randint(Settings.OCEAN_M_RedMin,Settings.OCEAN_M_RedMax)
            randomM_G = terrainGenRNG.randint(Settings.OCEAN_M_GreenMin,Settings.OCEAN_M_GreenMax)
            randomM_B = terrainGenRNG.randint(Settings.OCEAN_M_BlueMin,Settings.OCEAN_M_BlueMax)
            randomW_R = terrainGenRNG.randint(Settings.OCEAN_W_RedMin,Settings.OCEAN_W_RedMax)
            randomW_G = terrainGenRNG.randint(Settings.OCEAN_W_GreenMin,Settings.OCEAN_W_GreenMax)
            randomW_B = terrainGenRNG.randint(Settings.OCEAN_W_BlueMin,Settings.OCEAN_W_BlueMax)
        elif icy == True:
            randomB_R = terrainGenRNG.randint(Settings.ICY_B_RedMin,Settings.ICY_B_RedMax)
            randomB_G = terrainGenRNG.randint(Settings.ICY_B_GreenMin,Settings.ICY_B_GreenMax)
            randomB_B = terrainGenRNG.randint(Settings.ICY_B_BlueMin,Settings.ICY_B_BlueMax)
            randomM_R = terrainGenRNG.randint(Settings.ICY_M_RedMin,Settings.ICY_M_RedMax)
            randomM_G = terrainGenRNG.randint(Settings.ICY_M_GreenMin,Settings.ICY_M_GreenMax)
            randomM_B = terrainGenRNG.randint(Settings.ICY_M_BlueMin,Settings.ICY_M_BlueMax)
            randomW_R = terrainGenRNG.randint(Settings.ICY_W_RedMin,Settings.ICY_W_RedMax)
            randomW_G = terrainGenRNG.randint(Settings.ICY_W_GreenMin,Settings.ICY_W_GreenMax)
            randomW_B = terrainGenRNG.randint(Settings.ICY_W_BlueMin,Settings.ICY_W_BlueMax)
        else:
            randomB_R = terrainGenRNG.randint(Settings.OTHER_B_RedMin,Settings.OTHER_B_RedMax)
            randomB_G = terrainGenRNG.randint(Settings.OTHER_B_GreenMin,Settings.OTHER_B_GreenMax)
            randomB_B = terrainGenRNG.randint(Settings.OTHER_B_BlueMin,Settings.OTHER_B_BlueMax)
            randomM_R = terrainR
            randomM_G = terrainG
            randomM_B = terrainB
            randomW_R = terrainGenRNG.randint(Settings.OTHER_W_RedMin,Settings.OTHER_W_RedMax)
            randomW_G = terrainGenRNG.randint(Settings.OTHER_W_GreenMin,Settings.OTHER_W_GreenMax)
            randomW_B = terrainGenRNG.randint(Settings.OTHER_W_BlueMin,Settings.OTHER_W_BlueMax)
        print(str(randomB_R) + " " + str(randomB_G) + " " + str(randomB_B))
        print(str(randomM_R) + " " + str(randomM_G) + " " + str(randomM_B))
        print(str(randomW_R) + " " + str(randomW_G) + " " + str(randomW_B))
        if life == "organic":
            blackP = terrainGenRNG.randint(0,85)
            midP = terrainGenRNG.randint(85,150)
            whiteP = terrainGenRNG.randint(150,200)
        else:
            blackP = terrainGenRNG.randint(0,74)
            midP = terrainGenRNG.randint(150,200)
            whiteP = terrainGenRNG.randint(200,255)
        colorMap = ImageOps.colorize(grayMap, (randomB_R,randomB_G,randomB_B), (randomW_R,randomW_G,randomW_B), (randomM_R,randomM_G,randomM_B), blackpoint=blackP, midpoint=midP, whitepoint=whiteP)

        if isEyeball == True:
            if eyeballType == "Temperate":
                blackCircleA = blackCircle.getchannel("A")
                desertColor = ImageOps.colorize(blackCircle.convert("L"), (randomM_R, randomM_G, randomM_B), (0,0,0))
                desertColor.putalpha(blackCircleA)
                colorNoGrass = ImageOps.colorize(grayMap, (randomM_R,randomM_R,randomM_R), (randomW_R,randomW_G,randomW_B), (randomM_R,randomM_G,randomM_B), blackpoint=blackP, midpoint=midP, whitepoint=whiteP)
                #colorNoGrass.show()
                desertColorBlur = desertColor.filter(ImageFilter.GaussianBlur(radius=50))
                #desertColorBlur.show()
                colorMap.paste(colorNoGrass, (0,0), mask=desertColorBlur)
                iceSize = 2048
                iceColorBackg = Image.new("RGBA", (4096,2048), (0,0,0,0))
                iceColor = Image.new("RGBA", (iceSize,iceSize), (255,255,255,255))
                icePosX = int(2048 - (iceSize / 2))
                icePosY = int(1024 - (iceSize / 2))
                iceColorBackg.paste(iceColor, (icePosX,icePosY), mask=iceColor)
                iceColorMoved = ImageChops.offset(iceColorBackg, 2048,0)
                #iceColorMoved.show()
                iceColorBlur = iceColorMoved.filter(ImageFilter.GaussianBlur(radius=50))
                #iceColorBlur.show()
                colorMap.paste(iceColorBlur, (0,0), mask=iceColorBlur)
            elif eyeballType == "Cold":
                #iceSize = 2500
                iceColor = (eyeballDist)
                #iceColor.show()
                #icePosX = int(2048 - (iceSize / 2))
                #icePosY = int(1024 - (iceSize / 2))
                #iceColorBackg.paste(iceColor, (icePosX,icePosY), mask=iceColor)
                #iceColorMoved = ImageChops.offset(iceColorBackg, 2048,0)
                #iceColorMoved.show()
                
                if ocean == True:
                    iceColorBlur = iceColor.filter(ImageFilter.GaussianBlur(radius=0))
                else:
                    iceColorBlur = iceColor.filter(ImageFilter.GaussianBlur(radius=200))
                
                #iceColorBlur.show()

                colorMap.paste(iceColorBlur, (0,0), mask=iceColorBlur)

        if ocean == True:
            if tidallyLocked == True: # TIDALLY LOCKED OCEANS <----------------------------------------------------------------
                if eyeballType == "Temperate":
                    brightFac = int(terrainGenRNG.randint(1,300)/100)
                elif eyeballType == "Cold":
                    brightFac = int(terrainGenRNG.randint(1,50)/1000)

                print("Ocean exists! Dryness factor is " + str(brightFac))

                brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
                contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
                posted = ImageOps.posterize(contrHeight.convert("RGB"),2).convert("L")

                #posted.show()

                eyeball = Image.open(filepath + "/Presets/eyeball.png").convert("L")

                brightFinal = ImageEnhance.Brightness(posted).enhance(100)
                
                oceanRGBA = brightFinal.convert("RGBA")

                if eyeballType == "Temperate":
                    eyeballInvPosterized = ImageEnhance.Brightness(ImageEnhance.Contrast(ImageOps.invert(eyeballDist)).enhance(100)).enhance(100)
                elif eyeballType == "Cold":
                    eyeballInvPosterized = ImageEnhance.Brightness(ImageEnhance.Contrast((eyeballDist)).enhance(100)).enhance(100)

                eyeballInvPosterizedA = eyeballInvPosterized.convert("L")

                eyeballInvPosterized.putalpha(eyeballInvPosterizedA)

                brightFinal.paste(eyeballInvPosterized, (0,0), mask=eyeballInvPosterized)

                #oceanRGBA = brightFinal.convert("RGBA")

                #eyeballInvPosterized.show()
                #oceanRGBA.show()

                oceanInv = ImageOps.invert(brightFinal).convert("RGBA")

                ocInvL = oceanInv.convert("L")
                maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
                maxHeightMask.putalpha(posted)
                heightWithinThresh = ImageResFilter.convert("L")
                heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
                min_value, max_value = heightWithinThresh.getextrema()
                oceanGray = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
                #oceanGray.show()
                colorOcean = ImageOps.colorize(oceanGray, (oceanR,oceanG,oceanB), (oceanR,oceanG*2,oceanB), blackpoint=int(brightFac/2))
                colorOcean.putalpha(ocInvL)
                #colorOcean.show()
                
                #oceanInv.show()

                # Brighten the non-ocean parts to avoid invisible lakes from appearing
                eyeballInvPosterizedADrknd = ImageEnhance.Brightness(eyeballInvPosterizedA).enhance(0.5)
                eyeballInvPosterizedDrknd = Image.new("RGBA", (4096,2048), (255,255,255,255))
                eyeballInvPosterizedDrknd.putalpha(eyeballInvPosterizedADrknd)
                eyeballInvPosterizedBlur = eyeballInvPosterizedDrknd.filter(ImageFilter.GaussianBlur(5))
                ImageResFilter.paste(eyeballInvPosterizedBlur, (0,0), mask=eyeballInvPosterizedBlur)

                #oceanRGBA.putalpha(ocInvL)
                oceanBlurA = oceanInv.filter(ImageFilter.GaussianBlur(5)).convert("L")
                heightOcean = Image.new("RGBA", (4096,2048), (0,0,0))
                heightOcean.putalpha(oceanBlurA)
                
                ImageResFilter.paste(heightOcean, (0,0), mask=heightOcean)

                #ImageResFilter.show()

                normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
                normalOcean.putalpha(ocInvL)
                img_normalFilter.paste(normalOcean, (0,0), mask=ocInvL)

                #beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
                #beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
                #beachColor.putalpha(beachMask)
                #colorMap.paste(beachColor, (0,0), mask=beachColor)
                #colorOcean = Image.new("RGBA", (4096,2048), (oceanR+60,oceanG+60,oceanB+60))
                #colorOcean2 = Image.new("RGBA", (4096,2048), (oceanR, oceanG, oceanB))
                #ocInvL_Blur = ocInvL.filter(ImageFilter.GaussianBlur(15))
                #colorOcean2.putalpha(ocInvL_Blur)
                #colorOcean.paste(colorOcean2, (0,0), mask=colorOcean2)
                #colorOcean.putalpha(ocInvL)

                colorMap.putalpha(ocInvL)
            else: # NOT TIDALLY LOCKED OCEANS <----------------------------------------------------------------
                #brightFac = float(random.randint(1,500)/100)
                if terrainGenRNG.randint(0,3) == 0:
                    brightFac = oceanFactor
                else:
                    brightFac = oceanFactor

                print("Ocean exists! Dryness factor is " + str(brightFac))

                #brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
                #contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
                #posted = ImageOps.posterize(contrHeight.convert("RGB"),2)

                imageThreshold = ImageResFilter.point( lambda p: 255 if p > brightFac else 0 )
                # To mono
                imageThreshold = imageThreshold.convert('RGB')
                #imageThreshold.show()
                posted = imageThreshold.convert("L")

                ocInvL = ImageOps.invert(posted)
                maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
                maxHeightMask.putalpha(posted)
                heightWithinThresh = ImageResFilter.convert("L")
                heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
                min_value, max_value = heightWithinThresh.getextrema()
                oceanGray = image_stretched = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
                colorOcean = ImageOps.colorize(oceanGray, (oceanR,oceanG,oceanB), (oceanR,oceanG*2,oceanB), blackpoint=int(brightFac/2))
                colorOcean.putalpha(ocInvL)
                #colorOcean.show()
                
                #ImageResFilter.paste(heightOcean, (0,0), mask=heightOcean)

                #ImageResFilter.show()

                normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
                normalOcean.putalpha(ocInvL)
                img_normalFilter.paste(normalOcean, (0,0), mask=ocInvL)
    #
                #beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
                #beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
                #beachColor.putalpha(beachMask)
                #colorMap.paste(beachColor, (0,0), mask=beachColor)
                #colorOcean = Image.new("RGBA", (4096,2048), (oceanR+60,oceanG+60,oceanB+60))
                #colorOcean2 = Image.new("RGBA", (4096,2048), (oceanR, oceanG, oceanB))
                #ocInvL_Blur = ocInvL.filter(ImageFilter.GaussianBlur(15))
                #colorOcean2.putalpha(ocInvL_Blur)
                #colorOcean.paste(colorOcean2, (0,0), mask=colorOcean2)
                #colorOcean.putalpha(ocInvL)

                if icecaps == True:
                    #icecap_alph = icecap_img.getchannel("A")
                    #icecap_alph_blur = icecap_alph.filter(ImageFilter.GaussianBlur(10))
                    #icecap_inv = ImageOps.invert(icecap_img.convert("RGB"))
                    #icecap_inv.putalpha(icecap_alph_blur)
                    #ocInvL.paste(icecap_inv, (0,0), mask=icecap_inv)
                    icecapBlur = icecap_img.filter(ImageFilter.GaussianBlur(5))
                    colorMap.paste(icecapBlur, (0,0), mask=icecapBlur)
                    colorMap.putalpha(ocInvL)
                    #icecap_img.show()
                else:
                    colorMap.putalpha(ocInvL)
        elif icecaps == True and ocean == False and tidallyLocked == False:
            icecapBlur = icecap_img.filter(ImageFilter.GaussianBlur(5))
            colorMap.paste(icecapBlur, (0,0), mask=icecapBlur)

        if lava == True:
            if tidallyLocked == True:
                lavaFactor = np.interp(finalTemp, [700, 2000], [32, 200])
                brightFac = int(lavaFactor*(terrainGenRNG.randint(80,120)/100))

                print("Lava exists! Dryness factor is " + str(brightFac))

                imageThreshold = ImageResFilter.point( lambda p: 255 if p > brightFac else 0 )
                # To mono
                imageThreshold = imageThreshold.convert('RGB')
                posted = imageThreshold.convert("L")

                eyeballInvPosterized = ImageEnhance.Brightness(ImageEnhance.Contrast((eyeballDist)).enhance(100)).enhance(100)

                eyeballInvPosterizedA = eyeballInvPosterized.convert("L")

                eyeballInvPosterized.putalpha(eyeballInvPosterizedA)

                posted.paste(eyeballInvPosterized, (0,0), mask=eyeballInvPosterized)

                #normalLava = Image.new("RGBA", (4096,2048), (128,128,255))
                #normalLava.putalpha(lvInvL)
                #img_normalFilter.paste(normalLava, (0,0), mask=lvInvL)

                lvInvL = ImageOps.invert(posted)
                maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
                maxHeightMask.putalpha(posted)
                heightWithinThresh = ImageResFilter.convert("L")
                heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
                min_value, max_value = heightWithinThresh.getextrema()
                lavaGray = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
                colorLava = ImageOps.colorize(lavaGray, (255, 204, 0), (255, 0, 0))
                colorLava.putalpha(lvInvL)
                #colorLava.show()

                if isAsteroid == False:
                    heightLava = Image.new("RGBA", (4096,2048), (0,0,0))
                    lvInvLBLUR = lvInvL.filter(ImageFilter.GaussianBlur(10))
                    heightLava.putalpha(lvInvLBLUR)
                    ImageResFilter.paste(heightLava, (0,0), mask=lvInvLBLUR)

                #normalLava = Image.new("RGBA", (4096,2048), (128,128,255))
                #normalLava.putalpha(lvInvL)
                #img_normalFilter.paste(normalLava, (0,0), mask=lvInvL)
                
                #colorLava = Image.new("RGBA", (4096,2048), (int(lavaClrRGB[0]*255),int(lavaClrRGB[1]*255),int(lavaClrRGB[2]*255)))
                #colorLava.show()
                #colorLava2 = ImageOps.colorize(lavaImageRes, (0,0,0), (lavaClrRGB[0]*255,lavaClrRGB[1]*255,lavaClrRGB[2]*255))
                #colorLava2.show()
                #lvInvL_Blur = lvInvL.filter(ImageFilter.GaussianBlur(10))
                #colorLava2.putalpha(lvInvL_Blur)
                #colorLava.paste(colorLava2, (0,0), mask=colorLava2)
                #colorLavaContr = ImageEnhance.Contrast(ImageEnhance.Brightness(colorLava).enhance(2)).enhance(2)
                #colorLava.putalpha(lvInvL)
            else:
                lavaFactor = np.interp(finalTemp, [700, 2000], [32, 200])
                brightFac = int(lavaFactor*(terrainGenRNG.randint(80,120)/100))

                print("Lava exists! Dryness factor is " + str(brightFac))

                #brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
                #contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
                #posted = ImageOps.posterize(contrHeight.convert("RGB"),2)

                imageThreshold = ImageResFilter.point( lambda p: 255 if p > brightFac else 0 )
                # To mono
                imageThreshold = imageThreshold.convert('RGB')
                posted = imageThreshold.convert("L")
                lvInvL = ImageOps.invert(posted)
                maxHeightMask = Image.new("RGBA",(4096,2048),(brightFac,brightFac,brightFac,brightFac))
                maxHeightMask.putalpha(posted)
                heightWithinThresh = ImageResFilter.convert("L")
                heightWithinThresh.paste(maxHeightMask, (0,0), mask=maxHeightMask)
                min_value, max_value = heightWithinThresh.getextrema()
                lavaGray = heightWithinThresh.point(lambda x: (x - min_value) * 255 / (max_value - min_value))
                colorLava = ImageOps.colorize(lavaGray, (255, 204, 0), (255, 0, 0))
                colorLava.putalpha(lvInvL)
                #colorLava.show()

                #normalLava = Image.new("RGBA", (4096,2048), (128,128,255))
                #normalLava.putalpha(lvInvL)
                #img_normalFilter.paste(normalLava, (0,0), mask=lvInvL)
                
                if isAsteroid == False:
                    heightLava = Image.new("RGBA", (4096,2048), (0,0,0))
                    lvInvLBLUR = lvInvL.filter(ImageFilter.GaussianBlur(10))
                    heightLava.putalpha(lvInvLBLUR)
                    ImageResFilter.paste(heightLava, (0,0), mask=lvInvLBLUR)
                
                #colorLava = Image.new("RGBA", (4096,2048), (int(lavaClrRGB[0]*255),int(lavaClrRGB[1]*255),int(lavaClrRGB[2]*255)))
                #colorLava.show()
                #colorLava2 = ImageOps.colorize(lavaImageRes, (0,0,0), (lavaClrRGB[0]*255,lavaClrRGB[1]*255,lavaClrRGB[2]*255))
                #colorLava2.show()
                #lvInvL_Blur = lvInvL.filter(ImageFilter.GaussianBlur(10))
                #colorLava2.putalpha(lvInvL_Blur)
                #colorLava.paste(colorLava2, (0,0), mask=colorLava2)
                #colorLavaContr = ImageEnhance.Contrast(ImageEnhance.Brightness(colorLava).enhance(2)).enhance(2)
                #colorLava.putalpha(lvInvL)

        nR,nG,nB,nA = img_normalFilter.convert("RGBA").split()
        nRinv = ImageOps.invert(nR)
        nRbl = Image.new("L", (4096,2048), (255))
        img_normal_Final = Image.merge("RGBA", (nRbl,nG,nB,nRinv))
        
        if life == "organic":
            colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.75)).enhance(0.75)
        elif lava == True:
            colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.3)).enhance(0.4)
        else:
            colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.25)).enhance(1.2)

        if ocean == True:
            vertColorMap = Image.new("RGB", (4096,2048), (0,0,0))
            vertColorMap.paste(colorMap_Filter)

        colorMap_Filter.paste(albedoMap, (0,0), mask=albedoMap)
        if lava == True:
            colorMap_Filter.paste(colorLava, (0,0), mask=colorLava)
        if ocean == True:
            colorMap_Filter.paste(colorOcean, (0,0), mask=colorOcean)

        biomeMap = ImageOps.posterize(imageContr, 2).convert("RGBA")

        try:
            convertToBiomeFeature(canyonMap, (255,0,255), 10)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(mountainMap, (255,255,0), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(craterMap, (0, 255, 150), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(small_craterMap, (0, 255, 150), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(large_craterMap, (0, 255, 150), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(ray_craterMap, (0, 255, 150), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(ray_albedoMap, (150, 255, 150), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(volcanoMap, (255,0,0), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(activeVolcanoMap, (255,0,0), 1.75)
        except NameError:
            print("Ignoring")

        try:
            convertToBiomeFeature(lavaAlbedoMap, (255, 98, 0), 1.75)
        except NameError:
            print("Ignoring")

        if ocean == True:
            ocean_colored = Image.new("RGBA", (4096,2048), (0, 0, 50))
            ocean_colored.putalpha(ocInvL)
            biomeMap.paste(ocean_colored, (0,0), mask=ocean_colored)

        if lava == True:
            ocean_colored = Image.new("RGBA", (4096,2048), (255, 98, 0))
            ocean_colored.putalpha(lvInvL)
            biomeMap.paste(ocean_colored, (0,0), mask=ocean_colored)

        if icecaps == True:
            icecap_colored = Image.new("RGBA", (4096,2048), (150, 200, 255))
            icecap_colored.putalpha(icecap_img.getchannel("A"))
            biomeMap.paste(icecap_colored, (0,0), mask=icecap_colored)

        if anomaly == "fltStrc":
            anomalyMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
            anomalyDot = Image.new("RGBA", (2,2), (119, 198, 247))
            x_pixel = round((anLatLon[1]+180) * (4096 / 360) - 1024)
            y_pixel = round((90 - anLatLon[0]) * (2048 / 180))
            print(x_pixel)
            print(y_pixel)
            anomalyMap.paste(anomalyDot, (int(x_pixel-(anomalyDot.size[0])/2), int(y_pixel-(anomalyDot.size[1])/2)), mask=anomalyDot)
            anomalyMapOffs = ImageChops.offset(anomalyMap,-1024,0)
            anomalyMapFlip = anomalyMapOffs.transpose(Image.FLIP_LEFT_RIGHT)
            biomeMap.paste(anomalyMapFlip, (0,0), mask=anomalyMapFlip)

        if anomaly == "crshShp":
            anomalyMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
            anomalyDot = Image.new("RGBA", (2,2), (82, 96, 105))
            x_pixel = round((anLatLon[1] + 180) * (4096 / 360) - 1024)
            y_pixel = round((90 - anLatLon[0]) * (2048 / 180))
            print(x_pixel)
            print(y_pixel)
            anomalyMap.paste(anomalyDot, (int(x_pixel-(anomalyDot.size[0])/2), int(y_pixel-(anomalyDot.size[1])/2)), mask=anomalyDot)
            anomalyMapOffs = ImageChops.offset(anomalyMap,-1024,0)
            anomalyMapFlip = anomalyMapOffs.transpose(Image.FLIP_LEFT_RIGHT)
            biomeMap.paste(anomalyMapFlip, (0,0), mask=anomalyMapFlip)

        if canConvertToDDS == True:
            img_normal_FinalFlip = img_normal_Final.transpose(Image.FLIP_TOP_BOTTOM)
            ImageResFilterFlip = ImageResFilter.transpose(Image.FLIP_TOP_BOTTOM)
            colorMap_FilterFlip = colorMap_Filter.transpose(Image.FLIP_TOP_BOTTOM)
            if ocean == True:
                vertColorMap_FilterFlip = vertColorMap.transpose(Image.FLIP_TOP_BOTTOM)

            biomeMap.save(targetPath + "/Textures/PluginData/" + planetName + "_BIO" + ".png", compress_level=1)
            img_normal_FinalFlip.save(targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png", compress_level=1)

            if isAsteroid == True:
                heightBlur = ImageResFilterFlip.filter(ImageFilter.GaussianBlur(10))
                heightDownScale = heightBlur.resize((1024,512), resample=Image.Resampling.BICUBIC)
                heightDownScale.save(targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".png", compress_level=1)
            else:
                ImageResFilterFlip.save(targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".png", compress_level=1)

            colorMap_FilterFlip.save(targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png", compress_level=1)
            if ocean == True:
                vertColorMap_FilterFlip.save(targetPath + "/Textures/PluginData/" + planetName + "_VERTCLR" + ".png", compress_level=1)
        else:
            biomeMap_Flip = biomeMap.transpose(Image.FLIP_TOP_BOTTOM)

            biomeMap_Flip.save(targetPath + "/Textures/PluginData/" + planetName + "_BIO" + ".png", compress_level=1)
            img_normal_Final.save(targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png", compress_level=1)

            if isAsteroid == True:
                heightBlur = ImageResFilter.filter(ImageFilter.GaussianBlur(10))
                heightDownScale = heightBlur.resize((1024,512), resample=Image.Resampling.BICUBIC)
                heightDownScale.save(targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".png", compress_level=1)
            else:
                ImageResFilter.save(targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".png", compress_level=1)

            colorMap_Filter.save(targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png", compress_level=1)
            if ocean == True:
                vertColorMap.save(targetPath + "/Textures/PluginData/" + planetName + "_VERTCLR" + ".png", compress_level=1)
        
        texEndTime = time.time()
        clrEndTime = texEndTime-texStartTime
        print("Finished generating colors. Time elapsed: " + str(clrEndTime) + " seconds.")

        print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime) + " seconds.")
        if canConvertToDDS == True:
            allActions.append([time.localtime(),"Converting maps to DDS for : " + planetName])
            allActionArrayUpdated = True
            print("Converting maps to DDS for " + planetName + "...")
            texStartTime = time.time()

            #finalHeight2 = finalHeight.transpose(Image.FLIP_TOP_BOTTOM)
            hgtConv = wImage.Image(filename= targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")
            hgtConv.options['dds:mipmaps'] = '0'
            hgtConv.compression = 'dxt5'
            hgtConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".dds")
            os.remove(targetPath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")

            nrmConv = wImage.Image(filename= targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
            #nrmConv.options['dds:mipmaps'] = '0'
            nrmConv.compression = 'dxt5'
            nrmConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".dds")
            os.remove(targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")

            clrConv = wImage.Image(filename= targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
            clrConv.options['dds:mipmaps'] = '0'
            clrConv.compression = 'dxt5'
            clrConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".dds")
            os.remove(targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")

            if ocean == True:
                vertClrConv = wImage.Image(filename= targetPath + "/Textures/PluginData/" + planetName + "_VERTCLR" + ".png")
                vertClrConv.options['dds:mipmaps'] = '0'
                vertClrConv.compression = 'dxt5'
                vertClrConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_VERTCLR" + ".dds")
                os.remove(targetPath + "/Textures/PluginData/" + planetName + "_VERTCLR" + ".png")

            texEndTime = time.time()
            ddsEndTime = texEndTime-texStartTime

            print("Finished coverting maps to dds. Time elapsed: " + str(ddsEndTime) + " seconds.")

            print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime + ddsEndTime) + " seconds.")
            
        allActions.append([time.localtime(),"Generated maps for: " + planetName])
        allActionArrayUpdated = True
    # Generates gas giant maps.
    def generateGasGiantMaps(seed, terrainR, terrainG, terrainB, planetName):
        ggMapRNG = random.Random()
        ggMapRNG.seed(seed)
        print(threading.current_thread())
        types = ["Jupiter", "Saturn"]
        type = types[ggMapRNG.randint(0,len(types)-1)]

        allActions.append([time.localtime(),"Generating maps for gas giant: " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True

        print(type)
        ggClr = (terrainR,terrainG,terrainB)
        ggMap = Image.new("RGBA", (8192,4096), (terrainR,terrainG,terrainB,255))
        for i in range(1,100):
            if type == "Jupiter":
                randomNum = ggMapRNG.randint(1,3)
                randomBand = Image.open(filepath + "/Presets/jupiterBand" + str(randomNum) + ".png")
            else:
                randomNum = ggMapRNG.randint(1,3)
                randomBand = Image.open(filepath + "/Presets/saturnBand" + str(randomNum) + ".png")
            randomPos = ggMapRNG.randint(0,4096)
            randomBandOffs = ImageChops.offset(randomBand, xoffset=ggMapRNG.randint(0,4096), yoffset=0)
            bandHeight = randomBandOffs.height
            bandA = randomBand.getchannel("A")
            bandClrd = ImageOps.colorize(randomBandOffs.convert("L"), (0,0,0), (0,0,0), (int(ggClr[0]*(ggMapRNG.randint(80,120)/100)), int(ggClr[1]*(ggMapRNG.randint(80,120)/100)), int(ggClr[2]*(ggMapRNG.randint(80,120)/100))))
            bandClrd.putalpha(bandA)
            if type == "Jupiter":
                ggMap.paste(bandClrd, (0,int(randomPos-bandHeight/2)), mask=bandClrd)
            else:
                ggMap.paste(bandClrd, (0,int(randomPos-bandHeight/1.5)), mask=bandClrd)

        #if type == "Jupiter":
        #    for e in range(1,random.randint(0,20)):
        #        randomStormNum = random.randint(1,1)
        #        randomStorm = Image.open(filepath + "/Presets/jupiterStorm" + str(randomStormNum) + ".png")
        #        stormSizeMult = random.randint(50,200)/100
        #        randomStormSize = randomStorm.size
        #        randomStorm.resize((int(randomStormSize[0]*stormSizeMult),int(randomStormSize[1]*stormSizeMult)))
        #        randomPosX = random.randint(0,4096)
        #        randomPosY = random.randint(0,2048)
        #        stormA = randomStorm.getchannel("A")
        #        stormClrd = ImageOps.colorize(randomStorm.convert("L"), (0,0,0), (0,0,0), (int(ggClr[0]*(random.randint(90,110)/100)), int(ggClr[1]*(random.randint(90,110)/100)), int(ggClr[2]*(random.randint(00,110)/100))))
        #        stormClrd.putalpha(stormA)
        #
        #        ggMap.paste(stormClrd, (randomPosX,randomPosY), mask=stormClrd)

        ggNrm = Image.new("RGBA", (4096,2048), (128,128,255))

        print("Added normals for gas giant " + planetName + "!")
        nR,nG,nB,nA = ggNrm.split()
        ggNrm.putalpha(nR)

        ggNrm.save(targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
        ggMap.save(targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
        ggMap.save(targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".png")

        if canConvertToDDS == False:
            cloudPath1 = targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".png"
            cloudPath2 = targetPath + "/Textures/Clouds/" + planetName + "_CLOUDS" + ".png"
            shutil.move(cloudPath1,cloudPath2)
            #os.remove(targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".png")

        if canConvertToDDS == True:
            print("Converting maps to dds for gas giant " + planetName + "...")

            nrmConv = wImage.Image(filename= targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
            nrmConv.compression = 'dxt5'
            nrmConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".dds")
            os.remove(targetPath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")

            clrConv = wImage.Image(filename= targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
            clrConv.options['dds:mipmaps'] = '0'
            clrConv.compression = 'dxt5'
            clrConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".dds")
            os.remove(targetPath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")

            cloudConv = wImage.Image(filename = targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".png")
            cloudConv.options['dds:mipmaps'] = '0'
            cloudConv.compression = 'dxt5'
            cloudConv.save(filename= targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".dds")
            os.remove(targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".png")
            cloudPath1 = targetPath + "/Textures/PluginData/" + planetName + "_CLOUDS" + ".dds"
            cloudPath2 = targetPath + "/Textures/Clouds/" + planetName + "_CLOUDS" + ".dds"
            shutil.move(cloudPath1,cloudPath2)
            print("Converted maps to dds for gas giant " + planetName + "!")

        texEndTime = time.time()
        #print("Finished coverting maps to dds. Time elapsed: " + str(texEndTime-texStartTime) + " seconds.")
        allActions.append([time.localtime(),"Generated maps for gas giant: " + planetName])
        allActionArrayUpdated = True
    # Picks parameters for a moon.
    def generateMoon(planetSeed, moonNum, parentPlanet, moonsGenerated, parentRadius, gasGiantP, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, parentSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, isAsteroid, binaryParents=None, distBinaryParents=None,distBinaryStarNum=None):
        global gloablSeed
        
        #global amountOfThingsToDo
        #global amountOfThingsDone

        #amountOfThingsToDo += 1

        moonRNG = random.Random()

        if not distBinaryParents == None:
            moonSeed = planetSeed+moonNum+(int(distBinaryStarNum)*-1)
        else:
            moonSeed = planetSeed+moonNum

        moonRNG.seed(moonSeed)

        if isAsteroid == True:
            print(str(moonsGenerated) + "<---------------------------------------------------------------------------------------------------------------------------------- asterodfs ")
        print(moonsGenerated)
        if isAsteroid == True:
            planetName = parentPlanet + "-SUB-" + str(moonsGenerated)
        else:
            planetName = parentPlanet + "-" + str(moonsGenerated)
        global totalMoonsGenerated
        totalMoonsGenerated = totalMoonsGenerated + 1
        print(planetName)

        if isAsteroid == True:
            inclinationLimits = [-20,20]
            if gasGiantP == True:
                planetRadius = moonRNG.randint(5,29)*1000
                planetSMA = (moonRNG.randint(1000000,10000000)*moonsGenerated)*(parentRadius/600000)
            else:
                planetRadius = moonRNG.randint(5,29)*1000
                planetSMA = (moonRNG.randint(1000000,10000000)*moonsGenerated)*(parentRadius/600000)
        else:
            if gasGiantP == True:
                planetRadius = moonRNG.randint(50,700)*1000
                planetSMA = (moonRNG.randint(3300000,5000000)*moonsGenerated)*(parentRadius/600000)
            else:
                planetRadius = (parentRadius*moonRNG.randint(40,80)/100)/2
                planetSMA = ((moonRNG.randint(3300000,5000000)*moonsGenerated)*moonDistMult)*(parentRadius/600000)

        gasGiant = False
        planetMass = (5.29151583439215E+22 / (600000/planetRadius)**3.7)
        
        allActions.append([time.localtime(),"Picking parameters for moon: " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True

        try:
            inclinationLimits
        except:
            inclinationLimits = [0,10]

        atmoPress = 0
        atmClrR = 0
        atmClrG = 0
        atmClrB = 0
        sctrClrR = 0
        sctrClrG = 0
        sctrClrB = 0
        if planetRadius > 300000:
            atmo = "Atmospheric"
            vacuum = False
            lessOrMore = moonRNG.choice([0,1,2])
            if lessOrMore == 1:
                numberguy = moonRNG.randint(100,1000)
            else:
                numberguy = moonRNG.randint(1,100)
            atmoPress = numberguy*((planetRadius/600000)*0.5)
        else:
            atmo = "Vacuum"
            vacuum = True
        
        if atmo == "Atmospheric":
            templ = 1
        elif atmo == "Vacuum":
            templ = 0
        
        starLum = Lum
        starLumMult = starLum/1360
        smaMult = 13599840256/parentSMA
        
        pressureMultiplier = atmoPress/100

        randomGreenhouse = moonRNG.randint(5,20)/10

        vacuumTemp = 233*starLumMult*smaMult # Base temperature without any greenhouse.

        greenhouse = 80*(pressureMultiplier*randomGreenhouse) # Additional temperature to add above the base temperature, assuming there's an atmosphere.

        finalTemp = round(vacuumTemp + greenhouse)
        if atmo == "Atmospheric":
            if gasGiant == False:
                if moonRNG.randint(1,3) == 1:
                    if finalTemp > 200 and finalTemp < 600:
                        ocean = True
                    else:
                        ocean = False
                else:
                    ocean = False
            else:
                ocean = False
        else:
            ocean = False

        if finalTemp < 200 and moonRNG.randint(1,2) == 1 and isAsteroid == False:
            icy = True
        else:
            icy = False

        possibleLife = []

        if finalTemp > 223 and finalTemp < 373:
            if gasGiant == False and ocean == True and atmo == "Atmospheric" and atmoPress > 10:
                if moonRNG.randint(0,0) == 0:
                    possibleLife.append("organic")
        if finalTemp < 223 or finalTemp > 373:
            if gasGiant == False and atmo == "Atmospheric":
                if moonRNG.randint(0,3) == 0:
                    possibleLife.append("exotic")
        if finalTemp < 223 and gasGiant == False and ocean == False and atmo == "Vacuum" and icy == True:
            if moonRNG.randint(0,3) == 0:
                possibleLife.append("subglacial")
        if gasGiant == True or atmoPress > 700:
            if moonRNG.randint(0,3) == 0:
                possibleLife.append("aerial")

        if len(possibleLife) > 0:
            life = random.choice(possibleLife)
            if life == "organic":
                oxygen = True
                atmClrR = moonRNG.randint(100,200)
                atmClrG = moonRNG.randint(75,150)
                atmClrB = moonRNG.randint(0,50)
            else:
                oxygen = False
                atmClrR = moonRNG.randint(0,200)
                atmClrG = moonRNG.randint(0,200)
                atmClrB = moonRNG.randint(0,200)
        else:
            oxygen = False
            life = None
            atmClrR = moonRNG.randint(0,200)
            atmClrG = moonRNG.randint(0,200)
            atmClrB = moonRNG.randint(0,200)

        sctrClrR = (atmClrR*-1)+255
        sctrClrG = (atmClrG*-1)+255
        sctrClrB = (atmClrB*-1)+255

        if Settings.fantasyNames == True:
            if atmo == "Atmospheric":
                if finalTemp > 600:
                    dispName = processName(moonSeed,lavaTransisionTable,10)
                elif finalTemp < 100:
                    dispName = processName(moonSeed,icyTransisionTable,10)
                elif ocean == True:
                    if not life == None:
                        dispName = processName(moonSeed,lifeTransisionTable,10)
                    else:
                        dispName = processName(moonSeed,oceanicTransisionTable,10)
                else:
                    dispName = processName(moonSeed,rockyTransisionTable,10)
            else:
                dispName = processName(moonSeed,vacuumTransisionTable,10)
        else:
            dispName = planetName

        print("Display name for " + planetName + " is " + dispName)

        black = Color("#000000")
        Pcolors1 = list(black.range_to(Color("#700000"),5))
        red = Color("#700000")
        Pcolors2 = list(red.range_to(Color("#9e008c"),90))
        pink = Color("#9e008c")
        Pcolors3 = list(pink.range_to(Color("#fcf2fa"),5))
        PfinalColors = Pcolors1 + Pcolors2 + Pcolors3

        PMult = starRadius*30 / 261600000
        if PMult > len(PfinalColors):
            PMult = len(PfinalColors)
        PmultRound = round(PMult)
        plantColor = Color.get_rgb(PfinalColors[PmultRound-1])

        if atmo == "Atmospheric" and finalTemp >= 50 and finalTemp <= 300:
            icecaps = True
        else:
            icecaps = False

        if finalTemp > 700:
            lava = True
            if round(finalTemp/100) < 17:
                lavaClr = (lavaSpectrum[round(finalTemp/100)])
            else:
                lavaClr = lavaSpectrum[16]
        else:
            lava = False
            lavaClr = Color("#000000")

        lavaClrRGB = Color.get_rgb(lavaClr)

        oceanR = moonRNG.randint(5,20)
        oceanG = moonRNG.randint(5,35)
        oceanB = moonRNG.randint(10,75)

        moon = True

        terrainR = moonRNG.randint(50,175)
        terrainG = moonRNG.randint(50,175)
        terrainB = moonRNG.randint(50,175)

        #if gasGiant == False:
        #    if random.randint(1,1) == 1:
        #        if random.randint(0,1) == 1:
        #            print("??????????!!!?!??")
        #            anomaly = "crshShp"
        #            anLat = random.randint(-45,45)
        #            anLon = random.randint(-180,180)
        #        else:
        #            print("?????????")
        #            anomaly = "fltStrc"
        #            anLat = random.randint(-45,45)
        #            anLon = random.randint(-180,180)
        #        anLatLon = [anLat,anLon]
        #    else:
        #        anomaly = "None"
        #        anLatLon = []
        #else:
        #    anomaly = "None"
        #    anLatLon = []
        anLatLon = []
        anomaly = "None"

        if atmo == "Atmospheric":
            if ocean == True:
                if icy == True:
                    groundType = 3
                else:
                    groundType = moonRNG.choice([0,1,2])
            else:
                if icy == True:
                    groundType = 3
                else:
                    groundType = moonRNG.choice([0,1,2])
        else:
            if icy == True:
                groundType = 3
            else:
                groundType = moonRNG.choice([0,1,2])

        if gasGiant == False:
            addSubdividerFix(subdfixCfg, planetName)
            addToParallaxCfg(moonSeed, parallaxCfg, planetName, lava, lavaClrRGB, groundType, icy)
            addToParallaxScatterFixCfg(parallax_scatterfix_Cfg, planetName)
            addParallaxScatter(moonSeed, parallax_scatter_Cfg, planetName, life, plantColor, planetRadius)

        terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"

        print("-------Physical Values-------")
        print("Radius: " + str(planetRadius))
        print("Mass: " + str(planetMass))
        print("Semimajor Axis: " + str(planetSMA))
        print("Terrain tint: " + str(terrainClr))
        if not life == None:
            print("Has life!")

        print("-------Atmosphere Values-------")
        if atmo == "Atmospheric":
            print("Atmosphere scattering color: " + str(atmClrR) + " " + str(atmClrG) + " " + str(atmClrB))
            print("Atmosphere main color: " + str(sctrClrR) + " " + str(sctrClrG) + " " + str(sctrClrB))
            print("kPa at sea level: " + str(atmoPress))
            print("Temperature at sea level: " + str(finalTemp) + " kelvin.")
            if oxygen == True:
                print("Oxygenated!")
        else:
            print("No atmosphere!")

        print("-------------------------------")
        planetCfg = open(targetPath + "/Configs/" + planetName + "-" + str(moonsGenerated) + ".cfg","x")
        if moonRNG.randint(1,2) == 1:
            geoActive = True
            if moonRNG.randint(1,2) == 1:
                activeVolcano = True
            else:
                activeVolcano = False
        else:
            geoActive = False
            activeVolcano = False

        if moonRNG.randint(0,3) == 0:
            oceanFactor = moonRNG.randint(16,255)
        else:
            oceanFactor = moonRNG.randint(16,128)

        GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, atmoPress, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano, lava, False, oceanFactor, isAsteroid, moonSeed, icy)

        ringInn = 2000
        ringOut = 2001
        rings = False

        atmoHeight = moonRNG.randint(50,90)*1000

        if ocean == True:
            addToOceanCfg(moonSeed, oceanCfg, oceanR, oceanG, oceanB, planetName)

        Tag = "InfD_Moon"

        if atmo == "Atmospheric":
            addToAtmoCfg(atmoCfg, starN, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean, gasGiant, atmoHeight, atmoPress)
            if binaryParents == None:
                if distBinaryParents == None:
                    addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound)
                else:
                    addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound, None, distBinaryParents)
            else:
                addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound, binaryParents)
            if gasGiant == False:
                if ocean == True or moonRNG.randint(1,2) == 1:
                    cloudTexNum = moonRNG.randint(1,5)
                    addToEVECfg(eveCfg, cloudTexNum, planetName, False)
                    addToVolumetricEveCfg(moonSeed, VolumetricEveCfg, cloudTexNum, planetName, False, ocean)

        createResourceConfig(moonSeed,rationalResources_Cfg,planetName,lava,icy,finalTemp,atmoPress,ocean,gasGiant,life,None)

        sciValue = 3

        if atmo == "Atmospheric":
            sciValue += 5

        if ocean == True:
            sciValue += 10

        if life == "Organic":
            sciValue += 15
        elif life == "Exotic":
            sciValue += 25
        elif life == "Aerial":
            sciValue += 20
        elif life == "Subglacial":
            sciValue += 10

        if lava == True:
            sciValue += 10

        if icy == True:
            sciValue += 5

        tidallyLocked = True
        writeBodyCfg(moonSeed, planetCfg, planetName, planetRadius, planetMass, planetSMA, parentPlanet, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon, Tag, lava, tidallyLocked, oceanFactor, isAsteroid, icy, inclinationLimits, sciValue)
        #amountOfThingsDone += 1
    
    # Picks parameters for a planet.
    def generate(seedThing,starN,starRadius,starMass,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,subdfixCfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,typeOfStar,currentPlanetNum,binaryParents=None,binaryTypes=None,gSMA=None,distanceThingamabob=None,distBinaryParents=None,distBinaryStarNum=None):
        planetRNG = random.Random()

        global amountOfThingsToDo
        global amountOfThingsDone

        amountOfThingsToDo += 1

        if not distBinaryParents == None:
            planetSeed = seedThing+currentPlanetNum+(int(distBinaryStarNum)*-1)
        else:
            planetSeed = seedThing+currentPlanetNum

        planetRNG.seed(planetSeed) # I'm throwing stuff at the wall to see what sticks. This one has tape on it, one-sided tape.

        # Set them to 0 because python is like that smh
        moonsGenerated = 0
        asteroidsGenerated = 0
        global totalPlanetsGenerated
        totalPlanetsGenerated = totalPlanetsGenerated + 1

        if typeOfStar == "MainSeq":
            starSizeToSun = starRadius/261600000
            if starSizeToSun >= 1:
                starSizeToSun = 1
        else:
            starSizeToSun = 1

        planetName = starN + "-" + alphabet[currentPlanetNum]

        allActions.append([time.localtime(),"Picking parameters for planet: " + planetName])
        global allActionArrayUpdated
        allActionArrayUpdated = True

        print(planetName)
        allPlanets.append(planetName)
        gasGiant = False
        if planetRNG.randint(1,3) == 1:
            planetRadius = planetRNG.randint(100,800)*10000
            gasGiant = True
        else:
            planetRadius = planetRNG.randint(50,800)*1000
            gasGiant = False
        #planetRadius = random.randint(50,800)*1000
        #gasGiant = False
        if gasGiant == False:
            planetMass = (5.29151583439215E+22 / (600000/planetRadius)**3.7)
        else:
            planetMass = (4.23321273059351E+24 / (6000000/planetRadius)**3.7)

        print(typeOfStar + "AAYGAUYGYUFEYHUEYUHEGAHYAEUYHFUIAEFUIHASUIFASUFHUIASHFIUASHFASHFASASFASF")

        if typeOfStar == "MainSeq":
            if not gSMA == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(distanceThingamabob/261600000))+gSMA)
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius/261600000)))
        elif typeOfStar == "Neutron":
            if not gSMA == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(distanceThingamabob/261600000))+gSMA)
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius*2378/261600000)))*5
        elif typeOfStar == "RedGiant":
            if binaryParents == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius/261600000)))/8
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(distanceThingamabob/261600000))+gSMA)/6
        elif typeOfStar == "BrownDwarf":
            if not gSMA == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(distanceThingamabob/261600000))+gSMA)
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius/261600000)))/4
            planetRadius = int(planetRadius / 1.5)
        elif typeOfStar == "WhiteDwf":
            if not gSMA == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*((distanceThingamabob)/261600000))+gSMA)
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius*43.6/261600000)))*5
        elif typeOfStar == "WolfRayet":
            if not gSMA == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*((distanceThingamabob)/261600000))+gSMA)
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius/261600000)))*7
            inclinationLimits = [-25,25]
        else:
            if not gSMA == None:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(distanceThingamabob/261600000))+gSMA)
                print("AYUAGYUGHYURHYGURSYUGHSREHUYSRGHYUIRSHYUGHYUSRGHUYRGSUHYGRSUYRHSGUYHGYU*IRSHYURGHYURGHYUR BALLS BVALLB BALLS BALLS BALL WR WR WR WR AHHHH")
            else:
                planetSMA = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(starRadius/261600000)))

        if currentPlanetNum > 1:
            maxMoonsPossible = round(np.interp(planetSMA, [0,68773560320*(starMass/1.75654591319326E+28)*(5.29151583439215E+22/planetMass)], [0,AmountOfMoonsToGenerate]))
            moonAmount = int(planetRNG.randint(0,maxMoonsPossible))
        else:
            moonAmount = 0

        if gasGiant == True:
            maxAsteroidsPossible = round(np.interp(planetSMA, [0,68773560320*(starMass/1.75654591319326E+28)*(5.29151583439215E+22/planetMass)], [0,AmountOfAsteroidsToGenerate]))
            asteroidAmount = int(planetRNG.randint(0,maxAsteroidsPossible))
        else:
            if planetRNG.randint(1,2) == True:
                maxAsteroidsPossible = round(np.interp(planetSMA, [0,68773560320*(starMass/1.75654591319326E+28)*(5.29151583439215E+22/planetMass)], [0,AmountOfAsteroidsToGenerate]))
                asteroidAmount = int(planetRNG.randint(0,maxAsteroidsPossible)/2)
            else:
                asteroidAmount = 0

        if typeOfStar == "BrownDwarf":
            moonAmount = 0
            asteroidAmount = 0

        print("Number Of Moons For " + planetName + ": " + str(moonAmount))

        #if binaryTypes[0] == "WolfRayet" or binaryTypes[0] == "WolfRayet":
        #    inclinationLimits = [-25,25]

        try:
            inclinationLimits
        except:
            inclinationLimits = [0,10]

        atmoPress = 0
        atmClrR = 0
        atmClrG = 0
        atmClrB = 0
        sctrClrR = 0
        sctrClrG = 0
        sctrClrB = 0

        if planetRadius > 300000:
            atmo = "Atmospheric"
            vacuum = False
            if gasGiant == True:
                atmoPress = planetRNG.randint(200,1600)
            else:
                lessOrMore = planetRNG.choice([0,1,2])
                if lessOrMore == 1:
                    numberguy = planetRNG.randint(100,1000)
                else:
                    numberguy = planetRNG.randint(1,100)
                atmoPress = numberguy*((planetRadius/600000)*0.5)
        else:
            atmo = "Vacuum"
            vacuum = True
                
        # Tidally locked or not? This is where we find that out!
        tdSMAmult = starRadius/261600000
        requiredTidalLockingSMA = int(5263138304/0.5) # Moho's SMA divided by a number. 13526298302
        finalTidalLockingSMA = requiredTidalLockingSMA/tdSMAmult

        #if binaryParents == None:
        if not typeOfStar == "Neutron" and not typeOfStar == "WhiteDwf" and not typeOfStar == "RedGiant":
            if atmoPress < 400:
                if moonAmount > 0:
                    randomshit = planetRNG.randint(0,2)
                    if randomshit == 0:
                        if planetSMA < finalTidalLockingSMA:
                            print("At an SMA of " + str(planetSMA) + ", the planet " + planetName + " is tidally locked.")
                            tidallyLocked = True
                        else:
                            tidallyLocked = False
                    else:
                        tidallyLocked = False
                else:
                    if planetSMA < finalTidalLockingSMA:
                        print("At an SMA of " + str(planetSMA) + ", the planet " + planetName + " is tidally locked.")
                        tidallyLocked = True
                    else:
                        tidallyLocked = False
            else:
                tidallyLocked = False
        else:
            tidallyLocked = False
        #else:
        #    tidallyLocked = False

        starLum = Lum
        starLumMult = starLum/1360
        smaMult = 13599840256/planetSMA

        pressureMultiplier = atmoPress/100

        randomGreenhouse = planetRNG.randint(5,20)/10

        vacuumTemp = 233*starLumMult*smaMult # Base temperature without any greenhouse.

        if gasGiant == False:
            greenhouse = 80*(pressureMultiplier*randomGreenhouse) # Additional temperature to add above the base temperature, assuming there's an atmosphere.
        else:
            greenhouse = 1

        finalTemp = round(vacuumTemp + greenhouse)
        if atmo == "Atmospheric":
            if gasGiant == False:
                if finalTemp > 100 and finalTemp < 500:
                    if planetRNG.randint(1,2) == 1:
                        ocean = True
                    else:
                        ocean = False
                else:
                    ocean = False
            else:
                ocean = False
        else:
            ocean = False

        if finalTemp < 200 and planetRNG.randint(1,2) == 1:
            icy = True
        else:
            icy = False

        possibleLife = []

        if finalTemp > 223 and finalTemp < 373:
            if gasGiant == False and ocean == True and atmo == "Atmospheric" and atmoPress > 10:
                if planetRNG.randint(0,0) == 0: # Juuuuuuust in case I want it to be rarer.
                    possibleLife.append("organic")
        if finalTemp < 223 or finalTemp > 373:
            if gasGiant == False and atmo == "Atmospheric":
                if planetRNG.randint(0,5) == 0:
                    possibleLife.append("exotic")
        if finalTemp < 223 and gasGiant == False and ocean == False and atmo == "Vacuum" and icy == True:
            if planetRNG.randint(0,3) == 0:
                possibleLife.append("subglacial")
        if gasGiant == True or atmoPress > 700:
            if planetRNG.randint(0,3) == 0:
                possibleLife.append("aerial")

        if len(possibleLife) > 0:
            life = random.choice(possibleLife)
            if life == "organic":
                oxygen = True
                atmClrR = planetRNG.randint(100,200)
                atmClrG = planetRNG.randint(75,150)
                atmClrB = planetRNG.randint(0,50)
            else:
                oxygen = False
                atmClrR = planetRNG.randint(0,200)
                atmClrG = planetRNG.randint(0,200)
                atmClrB = planetRNG.randint(0,200)
        else:
            oxygen = False
            life = None
            atmClrR = planetRNG.randint(0,200)
            atmClrG = planetRNG.randint(0,200)
            atmClrB = planetRNG.randint(0,200)

        sctrClrR = (atmClrR*-1)+255
        sctrClrG = (atmClrG*-1)+255
        sctrClrB = (atmClrB*-1)+255

        if Settings.fantasyNames == True:
            if atmo == "Atmospheric":
                if finalTemp > 600:
                    dispName = processName(planetSeed,lavaTransisionTable,10)
                elif finalTemp < 100:
                    dispName = processName(planetSeed,icyTransisionTable,10)
                elif ocean == True:
                    if not life == None:
                        dispName = processName(planetSeed,lifeTransisionTable,10)
                    else:
                        dispName = processName(planetSeed,oceanicTransisionTable,10)
                elif gasGiant == True:
                    dispName = processName(planetSeed,gaseousTransisionTable,10)
                else:
                    dispName = processName(planetSeed,rockyTransisionTable,10)
            else:
                dispName = processName(planetSeed,vacuumTransisionTable,10)
        else:
            dispName = planetName

        print("Display name for " + planetName + " is " + dispName)

        black = Color("#000000")
        Pcolors1 = list(black.range_to(Color("#700000"),5))
        red = Color("#700000")
        Pcolors2 = list(red.range_to(Color("#9e008c"),90))
        pink = Color("#9e008c")
        Pcolors3 = list(pink.range_to(Color("#fcf2fa"),5))
        PfinalColors = Pcolors1 + Pcolors2 + Pcolors3

        PMult = starRadius*30 / 261600000
        if PMult > len(PfinalColors):
            PMult = len(PfinalColors)
        PmultRound = round(PMult)
        plantColor = Color.get_rgb(PfinalColors[PmultRound-1])

        if atmo == "Atmospheric" and finalTemp >= 50 and finalTemp <= 300:
            icecaps = True
        else:
            icecaps = False

        oceanR = planetRNG.randint(5,20)
        oceanG = planetRNG.randint(5,35)
        oceanB = planetRNG.randint(10,75)

        moon = False
        
        if gasGiant == True:
            terrainR = planetRNG.randint(50,255)
            terrainG = planetRNG.randint(50,255)
            terrainB = planetRNG.randint(50,255)

            terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"
        else:
            terrainR = planetRNG.randint(50,175)
            terrainG = planetRNG.randint(50,175)
            terrainB = planetRNG.randint(50,175)

            terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"

        if atmo == "Atmospheric" and gasGiant == False:
            templ = 1
        elif atmo == "Atmospheric" and gasGiant == True:
            templ = 4
        elif atmo == "Vacuum":
            templ = 0

        #if gasGiant == False:
        #    if random.randint(1,1) == 1:
        #        if random.randint(0,1) == 1:
        #            print("??????????!!!?!??")
        #            anomaly = "crshShp"
        #            anLat = random.randint(-45,45)
        #            anLon = random.randint(-180,180)
        #        else:
        #            print("?????????")
        #            anomaly = "fltStrc"
        #            anLat = random.randint(-45,45)
        #            anLon = random.randint(-180,180)
        #        anLatLon = [anLat,anLon]
        #    else:
        #        anomaly = "None"
        #        anLatLon = []
        #else:
        #    anomaly = "None"
        #    anLatLon = []
        anLatLon = []
        anomaly = "None"
        #print(anLatLon)

        #print("-------Physical Values-------")
        #print("Radius: " + str(planetRadius))
        #print("Mass: " + str(planetMass))
        #print("Semimajor Axis: " + str(planetSMA))
        #print("Terrain tint: " + str(terrainClr))
        #if life == True:
        #    print("Has life!")

        #print("-------Atmosphere Values-------")
        #if atmo == "Atmospheric":
        #    print("Atmosphere scattering color: " + str(atmClrR) + " " + str(atmClrG) + " " + str(atmClrB))
        #    print("Atmosphere main color: " + str(sctrClrR) + " " + str(sctrClrG) + " " + str(sctrClrB))
        #    print("kPa at sea level: " + str(atmoPress))
        #    print("Temperature at sea level: " + str(finalTemp) + " kelvin.")
        #    if oxygen == True:
        #        print("Oxygenated!")
        #else:
        #    print("No atmosphere!")

        #print("-------------------------------")

        if planetRNG.randint(1,2) == 1:
            geoActive = True
            if planetRNG.randint(1,2) == 1:
                activeVolcano = True
            else:
                activeVolcano = False
        else:
            geoActive = False
            activeVolcano = False

        if finalTemp > 700:
            lava = True
            if round(finalTemp/100) < 17:
                lavaClr = (lavaSpectrum[round(finalTemp/100)])
            else:
                lavaClr = lavaSpectrum[16]
        else:
            lava = False
            lavaClr = Color("#000000")

        lavaClrRGB = Color.get_rgb(lavaClr)

        if planetRNG.randint(0,3) == 0:
            oceanFactor = planetRNG.randint(16,255)
        else:
            oceanFactor = planetRNG.randint(16,128)

        planetCfg = open(targetPath + "/Configs/" + planetName + ".cfg","x")
        if gasGiant == True:
            #gasGiantMapThread = threading.Thread(target=generateGasGiantMaps, args=(terrainR, terrainG, terrainB, planetName))
            #gasGiantMapThread.run()
            generateGasGiantMaps(planetSeed, terrainR, terrainG, terrainB, planetName)
        else:
            #rockyPlanetMapThread = threading.Thread(target=GeneratePlanetMaps, args=(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, atmoPress, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano, lava))
            #rockyPlanetMapThread.run()
            GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, atmoPress, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano, lava, tidallyLocked, oceanFactor, False, planetSeed, icy)
        
        ringChance = int((AmountOfPlanetsToGenerate - currentPlanetNum)+1)

        #print("Ring chance: 1 in " + str(ringChance))
        if ringChance < 1:
            print("I'm not sure what kind of black magic was performed to cause this stupid thing to happen, but the ring change is 1 in 0. Don't worry, the program will continue as usual.")
            print("No rings were generated.")
            rings = False
            ringInn = 2000
            ringOut = 2001
        else:
            if planetRNG.randint(1,ringChance) == 1:
                print("RINGS!")
                print("-------------------------------")
                rings = True
                genRing(planetSeed, planetName)
                ringInn = planetRNG.randint(1000,4000)
                ringOut = ringInn + planetRNG.randint(100,3000)
            else:
                rings = False
                ringInn = 2000
                ringOut = 2001

        atmoHeight = planetRNG.randint(50,90)*1000

        if ocean == True:
            addToOceanCfg(planetSeed, oceanCfg, oceanR, oceanG, oceanB, planetName)

        if atmo == "Atmospheric":
            addToAtmoCfg(atmoCfg, starN, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean, gasGiant, atmoHeight, atmoPress)
            if binaryParents == None:
                if distBinaryParents == None:
                    addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound)
                else:
                    addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound, None, distBinaryParents)
            else:
                addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound, binaryParents)
            if gasGiant == False:
                if ocean == True or planetRNG.randint(1,2) == 1:
                    if tidallyLocked == True:
                        cloudTexNum = planetRNG.randint(1,3)
                    else:
                        cloudTexNum = planetRNG.randint(1,5)
                    addToEVECfg(eveCfg, cloudTexNum, planetName, tidallyLocked)
                    addToVolumetricEveCfg(planetSeed, VolumetricEveCfg, cloudTexNum, planetName, tidallyLocked, ocean)
                if atmoPress > 10:
                    auroraBright = planetRNG.randint(128,255)
                    aurR = planetRNG.randint(0,255)
                    aurG = planetRNG.randint(100,255)
                    aurB = planetRNG.randint(0,255)
                    auroraClr = (aurR,aurG,aurB)
                    addToEVEAurora(VolumetricEveCfg, planetName, auroraBright, auroraClr)
            else:
                auroraBright = planetRNG.randint(200,512)
                aurR = planetRNG.randint(0,255)
                aurG = planetRNG.randint(0,255)
                aurB = 255
                auroraClr = (aurR,aurG,aurB)
                addPQSFix(evePQSCfg, planetName)
                addToEVECfg(eveCfg, 1, planetName, tidallyLocked, planetName)
                addToVolumetricEveCfg(planetSeed, VolumetricEveCfg, 1, planetName, tidallyLocked, ocean, planetName)
                addToEVEAurora(eveCfg, planetName, auroraBright, auroraClr)
                if finalTemp > 700:
                    generateSuperheatedClouds(eveCfg,planetName,finalTemp)
                    generateSuperheatedClouds(VolumetricEveCfg,planetName,finalTemp)

        if atmo == "Atmospheric":
            if ocean == True:
                if icy == True:
                    groundType = 3
                else:
                    groundType = planetRNG.choice([0,1,2])
            else:
                if icy == True:
                    groundType = 3
                else:
                    groundType = planetRNG.choice([0,1,2])
        else:
            if icy == True:
                groundType = 3
            else:
                groundType = planetRNG.choice([0,1,2])

        if gasGiant == False:
            addSubdividerFix(subdfixCfg, planetName)
            addToParallaxCfg(planetSeed, parallaxCfg, planetName, lava, lavaClrRGB, groundType, icy)
            addToParallaxScatterFixCfg(parallax_scatterfix_Cfg, planetName)
            addParallaxScatter(planetSeed, parallax_scatter_Cfg, planetName, life, plantColor, planetRadius)

        Tag = "InfD_Planet"

        sciValue = 3

        if atmo == "Atmospheric":
            sciValue += 5

        if ocean == True:
            sciValue += 10

        if life == "Organic":
            sciValue += 15
        elif life == "Exotic":
            sciValue += 25
        elif life == "Aerial":
            sciValue += 20
        elif life == "Subglacial":
            sciValue += 10

        if lava == True:
            sciValue += 10

        if icy == True:
            sciValue += 5

        createResourceConfig(planetSeed,rationalResources_Cfg,planetName,lava,icy,finalTemp,atmoPress,ocean,gasGiant,life,None)
        writeBodyCfg(planetSeed, planetCfg, planetName, planetRadius, planetMass, planetSMA, starN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon, Tag, lava, tidallyLocked, oceanFactor, False, icy, inclinationLimits, sciValue)
        
        moonDistMult = planetRNG.randint(10,50)/10
        for a in range(moonAmount):
            moonsGenerated = moonsGenerated + 1
            moonNum = a
            if binaryParents == None:
                #generateMoonThread = threading.Thread(target=generateMoon, args=(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg))
                #generateMoonThread.start()
                if distBinaryParents == None:
                    generateMoon(planetSeed, a, planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, False)
                else:
                    generateMoon(planetSeed, a, planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, False, None, distBinaryParents, distBinaryStarNum)
            else:
                #generateMoonThread = threading.Thread(target=generateMoon, args=(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, binaryParents))
                #generateMoonThread.start()
                generateMoon(planetSeed, a, planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, False, binaryParents)

        for b in range(asteroidAmount):
            asteroidsGenerated = asteroidsGenerated + 1
            if binaryParents == None:
                #generateMoonThread = threading.Thread(target=generateMoon, args=(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg))
                #generateMoonThread.start()
                if distBinaryParents == None:
                    generateMoon(planetSeed, b, planetName, asteroidsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, True)
                else:
                    generateMoon(planetSeed, b, planetName, asteroidsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, True, None, distBinaryParents, distBinaryStarNum)
            else:
                #generateMoonThread = threading.Thread(target=generateMoon, args=(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, binaryParents))
                #generateMoonThread.start()
                generateMoon(planetSeed, b, planetName, asteroidsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, VolumetricEveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, parallax_scatterfix_Cfg, parallax_scatter_Cfg, rationalResources_Cfg, moonDistMult, True, binaryParents)
    
        amountOfThingsDone += 1

    # Picks parameters for stars
    def generateStar(starSeed, AmountOfPlanetsToGenerate, systemName, targetFilepath, parentBarycenter=None, binarySMA=None, binaryP=None, binaryRad=None, maaoD=None, baryOrder=None, starType=None, binaryType=None, binaryEccentricity=None):
        print(str(starType) + " sooooooooooooo like it's right and all but????")
        #print(str(starType) + " BRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUH")
        
        global targetPath
        targetPath = targetFilepath
        global planetsGenerated
        planetsGenerated = 0
        global totalSystemsGenerated
        global totalStarsGenerated

        starGenRNG = random.Random()
        starGenRNG.seed(starSeed)

        if parentBarycenter == None:
            totalSystemsGenerated = totalSystemsGenerated + 1
            parentGalaxy = availableGalaxies[starGenRNG.randint(0,len(availableGalaxies)-1)]
            if Settings.starTypeOverride == None:
                typeOfStar = starGenRNG.randint(0,175)
            else:
                try:
                    typeOfStar = Settings.starTypeOverride
                except:
                    print('Incredible star type override failue, check if it is "None" or a number.')
                    typeOfStar = starGenRNG.randint(0,175)
        else:
            allActions.append([time.localtime(),"Generating star: " + systemName + str(baryOrder)])
            global allActionArrayUpdated
            allActionArrayUpdated = True
            typeOfStar = starType

        totalStarsGenerated = totalStarsGenerated + 1
        
        print(typeOfStar)
        if 0 <= typeOfStar <= 18:
            redGiant = True
        elif 19 <= typeOfStar <= 28:
            whiteDwarf = True
        elif 29 <= typeOfStar <= 39:
            neutron = True
        elif 40 <= typeOfStar <= 50:
            brownDwarf = True
        elif 51 <= typeOfStar <= 55:
            wolfRayet = True
        else:
            mainSeq = True
            
        if parentBarycenter == None:
            starName = str(alphabet[starGenRNG.randint(0,len(alphabet)-1)]) + str(alphabet[starGenRNG.randint(0,len(alphabet)-1)]) + "-" + str(starGenRNG.randint(0,99999))
            allActions.append([time.localtime(),"Generating system: " + starName])
        else:
            starName = systemName + str(baryOrder)

        try:
            if mainSeq:
                print("Main sequence")
                starTypeStr = "MainSeq"
                if parentBarycenter == None:
                    Tag = "InfD_Star"
                else:
                    if binaryType == "Distant":
                        Tag = "InfD_DistantBinaryStar"
                    else:
                        Tag = "InfD_BinaryStar"
                minStarSize = Settings.minStarSize
                maxStarSize = Settings.maxStarSize

                if binaryRad == None:
                    randomSizeType = starGenRNG.randint(1,3)
                    if randomSizeType == 1:
                        starRadius = starGenRNG.randint(minStarSize,maxStarSize)
                    else:
                        starRadius = starGenRNG.randint(minStarSize,maxStarSize/6)
                    #starRadius =  math.floor(abs(random.random() - random.random()) * (10 + maxStarSize - minStarSize) + minStarSize)
                    starMass = starRadius * 6.7146251e+19
                else:
                    starRadius =  binaryRad
                    starMass = starRadius * 6.7146251e+19

                coronaMult = (starRadius*10 / 261600000)/200
                coronaMultRound = round(coronaMult)

                mult = int(getStarColorMult(starRadius))

                print(mult)

                if mult < 100 and mult > 0:
                    starColorHex = colorsReversed[mult]
                    starColor = Color.get_rgb(Color(starColorHex))
                    RGBfinal = str(starColor)[1:][:-1]
                    print(starColorHex)
                    print(RGBfinal)
                elif mult >= 100:
                    starColorHex = colorsReversed[99]
                    starColor = Color.get_rgb(Color(starColorHex))
                    RGBfinal = str(starColor)[1:][:-1]
                    print(starColorHex)
                    print(RGBfinal)
                elif mult < 0:
                    starColorHex = colorsReversed[0]
                    starColor = Color.get_rgb(Color(starColorHex))
                    RGBfinal = str(starColor)[1:][:-1]
                    print(starColorHex)
                    print(RGBfinal)
                
                Lum = 1360 * starRadius / 261600000
                
                planetsNum = starGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)

                if mult > 0 and mult <= 20:
                    coronaColor = "coronaRed"
                elif mult > 20 and mult <= 40:
                    coronaColor = "coronaOrange"
                elif mult > 40 and mult <= 50:
                    coronaColor = "coronaYellow"
                elif mult > 50 and mult <= 70:
                    coronaColor = "coronaWhite"
                else:
                    coronaColor = "coronaBlue"
        except UnboundLocalError:
            #print("God why")
            #logging.error(traceback.format_exc())
            #print(traceback.format_exc())
            #input("Type anything or press enter to close: ")
            pass
        try:
            if wolfRayet:
                print("Wolf Rayet")
                starTypeStr = "WolfRayet"
                if parentBarycenter == None:
                    Tag = "InfD_WolfRayet"
                else:
                    if binaryType == "Distant":
                        Tag = "InfD_DistantBinaryWolfRayet"
                    else:
                        Tag = "InfD_BinaryWolfRayet"
                minStarSize = 130800000 #Settings.minStarSize
                maxStarSize = 6016800000 #Settings.maxStarSize

                if binaryRad == None:
                    starRadius =  int(math.floor(abs(starGenRNG.random() - starGenRNG.random()) * (10 + maxStarSize - minStarSize) + minStarSize))
                    starMass = (((starRadius/10)/261600000) * 1.75654591319326E+28)*15
                else:
                    starRadius =  binaryRad
                    starMass = (((starRadius)/261600000) * 1.75654591319326E+28)*15

                #Mult = (starRadius*10 / 261600000)/200
                #multRound = round(Mult)
                starColor = Color.get_rgb(Color("#568bff"))
                RGBfinal = str(starColor)[1:][:-1]
                Lum = (((starRadius)/261600000)*15) * 1200
                
                planetsNum = starGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/2

                coronaColor = "None"
        except UnboundLocalError:
            pass
        try:
            if redGiant:
                print("Red Giant")
                starTypeStr = "RedGiant"
                if parentBarycenter == None:
                    Tag = "InfD_RedGiant"
                else:
                    if binaryType == "Distant":
                        Tag = "InfD_DistantBinaryRedGiant"
                    else:
                        Tag = "InfD_BinaryRedGiant"
                minStarSize = 66160000 #Settings.minStarSize
                maxStarSize = 784800000 #Settings.maxStarSize

                if binaryRad == None:
                    starRadius =  int(math.floor(abs(starGenRNG.random() - starGenRNG.random()) * (10 + maxStarSize - minStarSize) + minStarSize)*10)
                    starMass = (starRadius/10) * 6.7146251e+19
                else:
                    starRadius =  binaryRad
                    starMass = starRadius * 6.7146251e+19

                #Mult = (starRadius*10 / 261600000)/200
                #multRound = round(Mult)
                starColor = Color.get_rgb(Color("#fa4b28"))
                RGBfinal = str(starColor)[1:][:-1]
                Lum = (1360 * (starRadius/4) / 261600000)
                
                planetsNum = starGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/1.5

                coronaColor = "None"
        except UnboundLocalError:
            pass
        try:
            if whiteDwarf:
                print("White Dwarf")
                starTypeStr = "WhiteDwf"
                if parentBarycenter == None:
                    Tag = "InfD_WhiteDwarfStar"
                else:
                    if binaryType == "Distant":
                        Tag = "InfD_DistantBinaryWhiteDwarfStar"
                    else:
                        Tag = "InfD_BinaryWhiteDwarfStar"
                minStarSize = 500000
                maxStarSize = 700000

                if binaryRad == None:
                    starRadius =  (math.floor(abs(starGenRNG.random() - starGenRNG.random()) * (10 + maxStarSize - minStarSize) + minStarSize))*4.24
                    starMass = (((starRadius/4.42) * 6.7146251e+19)*436)/2
                else:
                    starRadius =  binaryRad
                    starMass = (((starRadius/4.42) * 6.7146251e+19)*436)/2

                #Mult = 33
                #multRound = round(Mult)
                starColor = Color.get_rgb(Color(colorsReversed[50]))
                RGBfinal = str(starColor)[1:][:-1]
                Lum = 150
                
                planetsNum = starGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/2

                coronaColor = "None"
        except UnboundLocalError:
            pass
        try:
            if neutron:
                print("Neutron Star")
                starTypeStr = "Neutron"
                if parentBarycenter == None:
                    Tag = "InfD_NeutronStar"
                else:
                    if binaryType == "Distant":
                        Tag = "InfD_DistantBinaryNeutronStar"
                    else:
                        Tag = "InfD_BinaryNeutronStar"
                minStarSize = Settings.minStarSize
                maxStarSize = Settings.maxStarSize

                if binaryRad == None:
                    starRadius =  48000
                    starMass = 3.5130918e+28
                else:
                    starRadius =  binaryRad
                    starMass = 3.5130918e+28

                #Mult = 80
                #multRound = round(Mult)
                starColor = Color.get_rgb(Color(colorsReversed[75]))
                RGBfinal = str(starColor)[1:][:-1]
                Lum = 1260
                
                diskRadius = starGenRNG.randint(3000000000,6000000000)
                generateDisks(starName, diskRadius)

                planetsNum = starGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/1.5

                coronaColor = "None"
        except UnboundLocalError:
            pass
        try:
            if brownDwarf:
                print("Brown Dwarf")
                starTypeStr = "BrownDwarf"
                if parentBarycenter == None:
                    Tag = "InfD_BrownDwfStar"
                else:
                    if binaryType == "Distant":
                        Tag = "InfD_DistantBinaryBrownDwfStar"
                    else:
                        Tag = "InfD_BinaryBrownDwfStar"
                minStarSize = 5592000
                maxStarSize = 10487000

                if binaryRad == None:
                    starRadius =  (math.floor(abs(starGenRNG.random() - starGenRNG.random()) * (10 + maxStarSize - minStarSize) + minStarSize))*4.24
                    starMass = (((starRadius/4.42) * 6.7146251e+19))*10
                else:
                    starRadius =  binaryRad
                    starMass = (starRadius * 6.7146251e+19)*3

                #Mult = 1
                #multRound = round(Mult)
                starColor = Color.get_rgb(Color(colorsReversed[5]))
                RGBfinal = str(starColor)[1:][:-1]
                Lum = 1360 * (starRadius / 261600000)/8
                
                planetsNum = starGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/1.5

                coronaColor = "None"
        except UnboundLocalError:
            pass

        # Wolf Rayet Thingamajigs
        if binaryType == "Distant" or parentBarycenter == None:
            if starTypeStr == "WolfRayet":
                generateNebula(starName)

        # Not type-specific settings.
        if parentBarycenter == None:
            starDist = starGenRNG.randint(Settings.minStarDistance,Settings.maxStarDistance)
            if parentGalaxy == "LKC_CtrlB":
                starDistG = starGenRNG.randint(Settings.minStarDistance/5,Settings.maxStarDistance*10)/3.5
            elif parentGalaxy == "SKC_CtrlB":
                starDistG = starGenRNG.randint(Settings.minStarDistance/5,Settings.maxStarDistance*10)/11
            else:
                starDistG = starGenRNG.randint(Settings.minStarDistance/5,Settings.maxStarDistance*10)
        else:
            starDist = binarySMA
            starDistG = binarySMA

        dispName = processName(starSeed, starTransisionTable, 10)

        #if parentBarycenter == None:
        print("Number of planets for " + dispName + "(" + starName + "): " + str(int(planetsNum)))

        colorsRound = (starColor[0] + starColor[1] + starColor[2])/3

        starCfg = open(targetPath + "/Configs/" + starName + ".cfg","x")

        print("-------------------------------------------------------")
        print(starName + " is a " + starTypeStr)
        print(" ")
        print("Star radius: " + str(starRadius) + " meters.")
        print("Star mass: " + str(starMass) + " kilograms.")
        print("Star luminosity: " + str(Lum) + " (" + str(Lum/1360) + " times Kerbol's luminosity!)")
        print("-------------------------------------------------------")

        if parentBarycenter == None:
            writeStarCfg(starSeed, starCfg, starName, starRadius, starMass, starDist, RGBfinal, starDistG, dispName, Tag, starTypeStr, Lum, coronaColor, None, None, None, parentGalaxy)
        else:
            writeStarCfg(starSeed, starCfg, starName, starRadius, starMass, starDist, RGBfinal, starDistG, dispName, Tag, starTypeStr, Lum, coronaColor, parentBarycenter, binaryP, maaoD, None, binaryEccentricity, binaryType)

        if parentBarycenter == None or binaryType == "Distant":
            #if binaryType == "Distant":
            #    if planetsNum > 9:
            #        planetsNum == 9
            #    planetsNum = planetsNum/1.5
            listCfg = open(targetPath + "/Visuals/Scatterer/" + starName + "_ScattererList" + ".cfg","x")
            listCfg.write(
                "@Scatterer_planetsList:FINAL\n"
                "{\n"
                "    @scattererCelestialBodies\n"
                "    {\n"
            )
            atmoCfg = open(targetPath + "/Visuals/Scatterer/" + starName + "_ScattererAtmo" + ".cfg","x")
            atmoCfg.write(
                "Scatterer_atmosphere\n"
                "{\n"
            )
            oceanCfg = open(targetPath + "/Visuals/Scatterer/" + starName + "_ScattererOcean" + ".cfg","x")
            oceanCfg.write(
                "Scatterer_ocean\n"
                "{\n"
            )
            eveCfg = open(targetPath + "/Visuals/EVE/Configs/" + starName + "_EVE" + ".cfg","x")
            eveCfg.write(
                "EVE_CLOUDS:NEEDS[!Infinite_VolumetricClouds]\n"
                "{\n"
            )
            VolumetricEveCfg = open(targetPath + "/Visuals/EVE/Configs/" + starName + "_VOLUMEEVE" + ".cfg","x")
            VolumetricEveCfg.write(
                "EVE_CLOUDS:NEEDS[Infinite_VolumetricClouds]\n"
                "{\n"
            )
            evePQSCfg = open(targetPath + "/Visuals/EVE/Configs/" + starName + "_PQSFIX" + ".cfg","x")
            evePQSCfg.write(
                "PQS_MANAGER\n"
                "{\n"
            )
            parallaxCfg = open(targetPath + "/Visuals/Parallax/Configs/" + starName + "_PARALLAX" + ".cfg","x")
            parallaxCfg.write(
                "Parallax\n"
                "{\n"
            )
            parallax_subd_Cfg = open(targetPath + "/Visuals/Parallax/Configs/" + starName + "_PARALLAX_SUBDFIX" + ".cfg","x")
            parallax_subd_Cfg.write(
                "@Kopernicus:LAST[InfiniteDiscoveries]:NEEDS[Parallax]\n"
                "{\n"
            )
            parallax_scatterfix_Cfg = open(targetPath + "/Visuals/Parallax/Configs/" + starName + "_PARALLAX_SCATTERFIX" + ".cfg","x")
            parallax_scatterfix_Cfg.write(
                "@Kopernicus:LAST[InfiniteDiscoveries]:NEEDS[Parallax]\n"
                "{\n"
            )
            # Empty for now.
            parallax_scatter_Cfg = open(targetPath + "/Visuals/Parallax/Configs/" + starName + "_PARALLAX_SCATTERS" + ".cfg","x")

            rationalResources_Cfg = open(targetPath + "/Misc/RR/" + starName + "_RationalResources" + ".cfg","x")
            createResourceConfig(starSeed,rationalResources_Cfg,starName,False,False,0,0,False,False,None,starTypeStr)

            sunfCfg = open(targetPath + "/Visuals/Scatterer/" + starName + "_ScattererSunflare" + ".cfg","x")
            addSunflareCfg(sunfCfg, starColor, starName, starTypeStr)

            allPlanetThreads = []

            if binaryType == "Distant":
                distBinaryParents = [systemName + "-1", systemName + "-2"]

            if binaryType == "Distant":
                for x in range(int(planetsNum)):
                    if everythingEnded == True:
                        raise Exception("UI thread isn't running.")
                    print("wowowowowowowowoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooohohohohohohohohololololooleeeeheeeeee")
                    planetsGenerated = planetsGenerated + 1
                    if Settings.useMultithreading == True:
                        generatePlanetProcess = threading.Thread(target=generate, args=(starSeed,starName,starRadius,starMass,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,parallax_subd_Cfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,starTypeStr,x+1,None,None,None,None,distBinaryParents,baryOrder))
                        allThreads.append(generatePlanetProcess)
                        allActions.append([time.localtime(),"Starting thread: " + str(generatePlanetProcess)])
                        allActions.append([time.localtime(),"Thread for planet: " + str(x)])
                        allActions.append([time.localtime(),"Total threads:" + str(threading.active_count())])
                        allActionArrayUpdated = True
                        allPlanetThreads.append(generatePlanetProcess)
                        generatePlanetProcess.start()
                    else:
                        generate(starSeed,starName,starRadius,starMass,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,parallax_subd_Cfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,starTypeStr,x+1,None,None,None,None,distBinaryParents,baryOrder)
            else:
                for x in range(int(planetsNum)):
                    if everythingEnded == True:
                        raise Exception("UI thread isn't running.")
                    print("wowowowowowowowoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooohohohohohohohohololololooleeeeheeeeee")
                    planetsGenerated = planetsGenerated + 1
                    if Settings.useMultithreading == True:
                        generatePlanetProcess = threading.Thread(target=generate, args=(starSeed,starName,starRadius,starMass,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,parallax_subd_Cfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,starTypeStr,x+1))
                        allThreads.append(generatePlanetProcess)
                        allActions.append([time.localtime(),"Starting thread: " + str(generatePlanetProcess)])
                        allActions.append([time.localtime(),"Thread for planet: " + str(x)])
                        allActions.append([time.localtime(),"Total threads:" + str(threading.active_count())])
                        allActionArrayUpdated = True
                        allPlanetThreads.append(generatePlanetProcess)
                        generatePlanetProcess.start()
                    else:
                        generate(starSeed,starName,starRadius,starMass,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,parallax_subd_Cfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,starTypeStr,x+1,parentBarycenter)

            for thread in allPlanetThreads:
                thread.join()

            listCfg.write(
                "   }\n"
                "}\n"
            )
            atmoCfg.write(
                "}\n"
            )
            oceanCfg.write(
                "}\n"
            )
            eveCfg.write(
                "}\n"
            )
            VolumetricEveCfg.write(
                "}\n"
            )
            evePQSCfg.write(
                "}\n"
            )
            parallaxCfg.write(
                "}\n"
            )
            parallax_subd_Cfg.write(
                "}\n"
            )
            parallax_scatterfix_Cfg.write(
                "}\n"
            )
        return starColor, starName, dispName, Lum, starTypeStr
    # Picks parameters for a barycenter. Influences star generation.
    def generateBarycenter(starSeed, AmountOfPlanetsToGenerate, targetFilepath):
        global gloablSeed
        global targetPath
        targetPath = targetFilepath
        global totalSystemsGenerated
        totalSystemsGenerated = totalSystemsGenerated + 1
        global planetsGenerated
        planetsGenerated = 0

        baryGenRNG = random.Random()
        baryGenRNG.seed(starSeed)
        print(str(starSeed) + " <-------------- barycenter seed thing")
        randomfucker = baryGenRNG.randint(1,2)
        print(randomfucker)
        if Settings.binaryTypeOverride == None:
            binaryType = baryGenRNG.choice(["Near","Distant"])
        elif Settings.binaryTypeOverride == True:
            binaryType = "Distant"
        elif Settings.binaryTypeOverride == False:
            binaryType = "Near"
        else:
            binaryType = baryGenRNG.choice(["Near","Distant"])

        print(binaryType)

        systemName = str(alphabet[baryGenRNG.randint(0,len(alphabet)-1)]) + str(alphabet[baryGenRNG.randint(0,len(alphabet)-1)]) + "-" + str(baryGenRNG.randint(0,99999))

        allActions.append([time.localtime(),"Generating binary system: " + systemName])
        global allActionArrayUpdated
        allActionArrayUpdated = True

        parentGalaxy = availableGalaxies[baryGenRNG.randint(0,len(availableGalaxies)-1)]

        minStarSize = Settings.minStarSize
        maxStarSize = Settings.maxStarSize

        star1Radius = baryGenRNG.randint(392400000,784800000)
        star1Mass = star1Radius * 6.7146251e+19

        star2Radius = math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + maxStarSize - minStarSize) + maxStarSize)
        star2Mass = star2Radius * 6.7146251e+19

        totalSystemsGenerated = totalSystemsGenerated + 1

        if Settings.starTypeOverrideBinary1 == None:
            if binaryType == "Near":
                typeOfStar1 = baryGenRNG.randint(19,175)
            elif binaryType == "Distant":
                typeOfStar1 = baryGenRNG.randint(0,175)
        else:
            typeOfStar1 = Settings.starTypeOverrideBinary1
        print(typeOfStar1)
        if 0 <= typeOfStar1 <= 18:
            redGiant1 = True
        elif 19 <= typeOfStar1 <= 28:
            whiteDwarf1 = True
        elif 29 <= typeOfStar1 <= 39:
            neutron1 = True
        elif 40 <= typeOfStar1 <= 50:
            brownDwarf1 = True
        elif 51 <= typeOfStar1 <= 55:
            wolfRayet1 = True
        else:
            mainSeq1 = True

        if Settings.starTypeOverrideBinary2 == None:
            if binaryType == "Near":
                typeOfStar2 = baryGenRNG.randint(19,175)
            elif binaryType == "Distant":
                typeOfStar2 = baryGenRNG.randint(0,175)
        else:
            typeOfStar2 = Settings.starTypeOverrideBinary2
        if 0 <= typeOfStar2 <= 18:
            redGiant2 = True
        elif 19 <= typeOfStar2 <= 28:
            whiteDwarf2 = True
        elif 29 <= typeOfStar2 <= 39:
            neutron2 = True
        elif 40 <= typeOfStar2 <= 50:
            brownDwarf2 = True
        elif 51 <= typeOfStar2 <= 55:
            wolfRayet2 = True
        else:
            mainSeq2 = True

        #print(str(typeOfStar2) + " GGGGGGGGGGAHHHHHHHHHHHHHHHHH TTYOE IF STAR @")

        try:
            if mainSeq1:
                print("Main sequence")
                randomSizeType = baryGenRNG.randint(1,3)
                if randomSizeType == 1:
                    if binaryType == "Distant":
                        star1Radius = baryGenRNG.randint(minStarSize,maxStarSize/3)
                    else:
                        star1Radius = baryGenRNG.randint(minStarSize,maxStarSize)
                else:
                    star1Radius = baryGenRNG.randint(minStarSize,maxStarSize/6)
                #star1Radius =  math.floor(abs(random.random() - random.random()) * (10 + maxStarSize - minStarSize) + minStarSize)
                distanceRadiusThing1 = star1Radius
                star1Mass = star1Radius * 6.7146251e+19
        except UnboundLocalError:
            pass
        try:
            if wolfRayet1:
                print("Wolf Rayet")
                minWRStarSize = 130800000 #Settings.minStarSize
                maxWRStarSize = 6016800000 #Settings.maxStarSize
                star1Radius =  int(math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + maxWRStarSize - minWRStarSize) + minWRStarSize))
                distanceRadiusThing1 = star1Radius*2
                star1Mass = (((star1Radius/10)/261600000) * 1.75654591319326E+28)*15
        except UnboundLocalError:
            pass
        try:
            if redGiant1:
                print("Red Giant")
                minRGSize = 66160000 #Settings.minStarSize
                maxRGSize = 784800000 #Settings.maxStarSize
                star1Radius =  int(math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + maxRGSize - minRGSize) + minRGSize)*10)
                distanceRadiusThing1 = star1Radius
                star1Mass = (star1Radius/10) * 6.7146251e+19
        except UnboundLocalError:
            pass
        try:
            if whiteDwarf1:
                print("White Dwarf")
                WDmin = 500000
                WDmax = 700000

                star1Radius =  (math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + WDmax - WDmin) + WDmin))*4.24
                distanceRadiusThing1 = 261600000
                star1Mass = (((star1Radius/4.42) * 6.7146251e+19)*436)/2
        except UnboundLocalError:
            pass
        try:
            if neutron1:
                print("Neutron Star")
                star1Radius = 48000
                distanceRadiusThing1 = 261600000
                star1Mass = 3.5130918e+28
        except UnboundLocalError:
            pass
        try:
            if brownDwarf1:
                print("Brown Dwarf")
                BDmax = 5592000
                BDmin = 10487000
                star1Radius =  (math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + BDmax - BDmin) + BDmin))*4.24
                distanceRadiusThing1 = 161600000
                star1Mass = (((star1Radius/4.42) * 6.7146251e+19))*3
        except UnboundLocalError:
            pass

            # AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        try:
            if mainSeq2:
                randomSizeType = baryGenRNG.randint(1,3)
                if randomSizeType == 1:
                    if binaryType == "Distant":
                        star2Radius = baryGenRNG.randint(minStarSize,maxStarSize/3)
                    else:
                        star2Radius = baryGenRNG.randint(minStarSize,maxStarSize)
                else:
                    star2Radius = baryGenRNG.randint(minStarSize,maxStarSize/6)
                #star2Radius =  math.floor(abs(random.random() - random.random()) * (10 + maxStarSize - minStarSize) + minStarSize)
                distanceRadiusThing2 = star2Radius
                star2Mass = star2Radius * 6.7146251e+19
        except UnboundLocalError:
            pass
        try:
            if wolfRayet2:
                print("Wolf Rayet")
                minWRStarSize = 130800000 #Settings.minStarSize
                maxWRStarSize = 6016800000 #Settings.maxStarSize
                star2Radius =  int(math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + maxWRStarSize - minWRStarSize) + minWRStarSize))
                distanceRadiusThing2 = star2Radius*2
                star2Mass = (((star2Radius/10)/261600000) * 1.75654591319326E+28)*15
        except UnboundLocalError:
            pass
        try:
            if redGiant2:
                print("Red Giant")
                minRGSize = 66160000 #Settings.minStarSize
                maxRGSize = 784800000 #Settings.maxStarSize
                star2Radius =  int(math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + maxRGSize - minRGSize) + minRGSize)*10)
                distanceRadiusThing2 = star2Radius
                star2Mass = (star2Radius/10) * 6.7146251e+19
        except UnboundLocalError:
            pass
        try:
            if whiteDwarf2:
                print("White Dwarf")
                WDmin = 500000
                WDmax = 700000

                star2Radius =  (math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + WDmax - WDmin) + WDmin))*4.24
                distanceRadiusThing2 = 261600000
                star2Mass = (((star2Radius/4.42) * 6.7146251e+19)*436)/2
        except UnboundLocalError:
            pass
        try:
            if neutron2:
                print("Neutron Star")
                star2Radius = 48000
                distanceRadiusThing2 = 261600000
                star2Mass = 3.5130918e+28
        except UnboundLocalError:
            pass
        try:
            if brownDwarf2:
                print("Brown Dwarf")
                BDmax = 5592000
                BDmin = 10487000
                star2Radius =  (math.floor(abs(baryGenRNG.random() - baryGenRNG.random()) * (10 + BDmax - BDmin) + BDmin))*4.24
                distanceRadiusThing2 = 261600000
                star2Mass = (((star2Radius/4.42) * 6.7146251e+19))*3
        except UnboundLocalError:
            pass

        print(systemName)

        largerStarRadius = max([star1Radius,star2Radius])
        largerDistance = max([distanceRadiusThing1,distanceRadiusThing2])

        barycenterMass = star1Mass + star2Mass
        barycenterRadius = largerStarRadius
        distanceThingamabob = largerDistance
        barycenterDist = baryGenRNG.randint(Settings.minStarDistance,Settings.maxStarDistance)
        if parentGalaxy == "LKC_CtrlB":
            barycenterDistG = baryGenRNG.randint(Settings.minStarDistance/5,Settings.maxStarDistance*10)/3.5
        elif parentGalaxy == "SKC_CtrlB":
            barycenterDistG = baryGenRNG.randint(Settings.minStarDistance/5,Settings.maxStarDistance*10)/11
        else:
            barycenterDistG = baryGenRNG.randint(Settings.minStarDistance/5,Settings.maxStarDistance*10)
        if star1Mass > star2Mass:
            ML = star1Mass # Larger object mass.
            MS = star2Mass # Smaller object mass.
        else:
            ML = star2Mass # Larger object mass.
            MS = star1Mass # Smaller object mass.

        neutronInSystem = False
        try:
            if neutron1 == True:
               neutronInSystem = True
        except:
            pass
        try:
            if neutron2 == True:
                neutronInSystem = True
        except:
            pass

        if neutronInSystem == True:
            if binaryType == "Near":
                gSMA = int(baryGenRNG.randint(Settings.binaryMinSMA + 50000000, Settings.binaryMaxSMA) + ((star1Radius + star2Radius)/2)) # Distance between both bodies in meters.
            else:
                gSMA = int(baryGenRNG.randint(Settings.distantBinaryMinSMA,Settings.distantBinaryMaxSMA))
        else:
            if binaryType == "Near":
                gSMA = int(baryGenRNG.randint(Settings.binaryMinSMA,Settings.binaryMaxSMA) + ((star1Radius + star2Radius)/2)) # Distance between both bodies in meters.
            else:
                gSMA = int(baryGenRNG.randint(Settings.distantBinaryMinSMA,Settings.distantBinaryMaxSMA))

        print(gSMA)
        diff = ML/MS
        # math lol
        gSMA_km = gSMA/1000
        distL = gSMA_km * 1/(1+diff)
        distS = gSMA_km * diff/(1+diff)
        pi = math.pi
        Period = 2 * pi * math.sqrt(gSMA**3 / (6.67408E-11*(ML + MS)))

        binarySMA1 = distL * 1000
        binarySMA2 = distS * 1000

        listCfg = open(targetPath + "/Visuals/Scatterer/" + systemName + "_ScattererList" + ".cfg","x")
        listCfg.write(
            "@Scatterer_planetsList:FINAL\n"
            "{\n"
            "    @scattererCelestialBodies\n"
            "    {\n"
        )
        atmoCfg = open(targetPath + "/Visuals/Scatterer/" + systemName + "_ScattererAtmo" + ".cfg","x")
        atmoCfg.write(
            "Scatterer_atmosphere\n"
            "{\n"
        )
        oceanCfg = open(targetPath + "/Visuals/Scatterer/" + systemName + "_ScattererOcean" + ".cfg","x")
        oceanCfg.write(
            "Scatterer_ocean\n"
            "{\n"
        )
        eveCfg = open(targetPath + "/Visuals/EVE/Configs/" + systemName + "_EVE" + ".cfg","x")
        eveCfg.write(
            "EVE_CLOUDS:NEEDS[!Infinite_VolumetricClouds]\n"
            "{\n"
        )
        VolumetricEveCfg = open(targetPath + "/Visuals/EVE/Configs/" + systemName + "_VOLUMEEVE" + ".cfg","x")
        VolumetricEveCfg.write(
            "EVE_CLOUDS:NEEDS[Infinite_VolumetricClouds]\n"
            "{\n"
        )
        evePQSCfg = open(targetPath + "/Visuals/EVE/Configs/" + systemName + "_PQSFIX" + ".cfg","x")
        evePQSCfg.write(
            "PQS_MANAGER\n"
            "{\n"
        )
        if binaryType == "Near":
            parallaxCfg = open(targetPath + "/Visuals/Parallax/Configs/" + systemName + "_PARALLAX" + ".cfg","x")
            parallaxCfg.write(
                "Parallax\n"
                "{\n"
            )
            parallax_subd_Cfg = open(targetPath + "/Visuals/Parallax/Configs/" + systemName + "_PARALLAX_SUBDFIX" + ".cfg","x")
            parallax_subd_Cfg.write(
                "@Kopernicus:LAST[InfiniteDiscoveries]:NEEDS[Parallax]\n"
                "{\n"
            )
            parallax_scatterfix_Cfg = open(targetPath + "/Visuals/Parallax/Configs/" + systemName + "_PARALLAX_SCATTERFIX" + ".cfg","x")
            parallax_scatterfix_Cfg.write(
                "@Kopernicus:LAST[InfiniteDiscoveries]:NEEDS[Parallax]\n"
                "{\n"
            )
            # Empty
            parallax_scatter_Cfg = open(targetPath + "/Visuals/Parallax/Configs/" + systemName + "_PARALLAX_SCATTERS" + ".cfg","x")
            rationalResources_Cfg = open(targetPath + "/Misc/RR/" + systemName + "_RationalResources" + ".cfg","x")
        if binaryType == "Distant":
            binaryEccentricity = baryGenRNG.randint(0,60)/100
        else:
            binaryEccentricity = 0

        # Turns out I don't need it.

        #star1_IsBarycenter = False
        #star2_IsBarycenter = False

        #if star1Mass > star2Mass:
        #    massDiff = star1Mass/star2Mass
        #    if massDiff > 4:
        #        star1_IsBarycenter = True
        #    else:
        #        star1_IsBarycenter = False
        #else:
        #    massDiff = star2Mass/star1Mass
        #    if massDiff > 4:
        #        star2_IsBarycenter = True
        #    else:
        #        star2_IsBarycenter = False

        print("-------------------------- STAR THINGS")
        print(star1Radius)
        print(star2Radius)
        print(typeOfStar1)
        print(typeOfStar2)
        print("-------------------------- STAR THINGS")

        if star1Mass > star2Mass:
            star1Color, star1Name, dispName1, Lum1, starTypeStr1 = generateStar(starSeed+1, AmountOfPlanetsToGenerate, systemName, targetPath, systemName, binarySMA1, Period, star1Radius, 0, "-1", typeOfStar1, binaryType, binaryEccentricity)
            star2Color, star2Name, dispName2, Lum2, starTypeStr2 = generateStar(starSeed+2, AmountOfPlanetsToGenerate, systemName, targetPath, systemName, binarySMA2, Period, star2Radius, 180, "-2", typeOfStar2, binaryType, binaryEccentricity)
        else:
            star1Color, star1Name, dispName1, Lum1, starTypeStr1 = generateStar(starSeed+1, AmountOfPlanetsToGenerate, systemName, targetPath, systemName, binarySMA2, Period, star1Radius, 0, "-1", typeOfStar1, binaryType, binaryEccentricity)
            star2Color, star2Name, dispName2, Lum2, starTypeStr2 = generateStar(starSeed+2, AmountOfPlanetsToGenerate, systemName, targetPath, systemName, binarySMA1, Period, star2Radius, 180, "-2", typeOfStar2, binaryType, binaryEccentricity)

        if binaryType == "Near":
            if starTypeStr1 == "WolfRayet" or starTypeStr2 == "WolfRayet":
                generateWRBinarySpiral(systemName)
                generateNebula(systemName)

        if starTypeStr1 == "WolfRayet" or starTypeStr2 == "WolfRayet":
            planetsNum = baryGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/2
        elif starTypeStr1 == "RedGiant" or starTypeStr2 == "RedGiant":
            planetsNum = baryGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/1.5
        elif starTypeStr1 == "Neutron" or starTypeStr2 == "Neutron":
            planetsNum = baryGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/1.5
        elif starTypeStr1 == "WhiteDwf" or starTypeStr2 == "WhiteDwf":
            planetsNum = baryGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)/1.5
        else:
            planetsNum = baryGenRNG.randint(minPlanets,AmountOfPlanetsToGenerate)
        baryCfg = open(targetPath + "/Configs/" + systemName + ".cfg","x")
        if star1Mass > star2Mass:
            starColors = star1Color
        else:
            starColors = star2Color

        print("Number Of Planets For " + systemName + ": " + str(int(planetsNum)))

        RGBfinal = str(starColors)[1:][:-1]
        baryDispName = dispName1 + "-" + dispName2 + " Barycenter"
        averageClrR = (star1Color[0] + star2Color[0])/2
        averageClrG = (star1Color[1] + star2Color[1])/2
        averageClrB = (star1Color[2] + star2Color[2])/2
        averageClr = [averageClrR, averageClrG, averageClrB]

        if starTypeStr1 == "RedGiant":
            brightnessThing1 = (star1Radius/30)*2 # I honestly do not know what to call these variables anymore.
        elif starTypeStr1 == "BrownDwarf":
            brightnessThing1 = star1Radius*10
        elif starTypeStr1 == "Neutron":
            brightnessThing1 = star1Radius*5450
        elif starTypeStr1 == "WhiteDwf":
            brightnessThing1 = star1Radius*50
        elif starTypeStr1 == "WolfRayet":
            brightnessThing1 = star1Radius*30
        else:
            brightnessThing1 = star1Radius

        if starTypeStr2 == "RedGiant":
            brightnessThing2 = (star2Radius/30)*2 # I honestly do not know what to call these variables anymore.
        elif starTypeStr2 == "BrownDwarf":
            brightnessThing2 = star2Radius*10
        elif starTypeStr2 == "Neutron":
            brightnessThing2 = star2Radius*5450
        elif starTypeStr2 == "WhiteDwf":
            brightnessThing2 = star2Radius*50
        elif starTypeStr2 == "WolfRayet":
            brightnessThing2 = star2Radius*30
        else:
            brightnessThing2 = star2Radius

        baryBrightness = (brightnessThing1 + brightnessThing2)
        print("Barycenter brightness info:")
        print("Total brightness: " + str(baryBrightness))
        print("Star 1 brightness : " + str(brightnessThing1) + " (" + starTypeStr1 + ")")
        print("Star 2 brightness: " + str(brightnessThing2) + " (" + starTypeStr2 + ")")

        if star1Mass > star2Mass:
            binaryParents = [star1Name,star2Name]
        else:
            binaryParents = [star2Name,star1Name]
        binaryTypes = [starTypeStr1,starTypeStr2]

        #if star1_IsBarycenter == False and star2_IsBarycenter == False:
        writeBarycenterCfg(starSeed, baryCfg, systemName, barycenterRadius, barycenterMass, barycenterDist, systemName, RGBfinal, barycenterDistG, baryDispName, averageClr, baryBrightness, parentGalaxy, binaryType, binaryTypes)

        print(star1Color)
        colorsRound1 = (star1Color[0] + star1Color[1] + star1Color[2])/3
        colorsRound2 = (star2Color[0] + star2Color[1] + star2Color[2])/3
        colorsRound = colorsRound1 + colorsRound2

        Lum = (Lum1 + Lum2)/2

        sunfCfg = open(targetPath + "/Visuals/Scatterer/" + systemName + "_ScattererSunflare" + ".cfg","x")
        addSunflareCfg(sunfCfg, star1Color, star1Name, starTypeStr1)
        addSunflareCfg(sunfCfg, star2Color, star2Name, starTypeStr2)

        if binaryType == "Near":
            allPlanetThreads = []
            for x in range(int(planetsNum)):
                if everythingEnded == True:
                    raise Exception("UI thread isn't running.")
                #print("wowowowowowowowoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooohohohohohohohohololololooleeeeheeeeee")
                planetsGenerated = planetsGenerated + 1
                if Settings.useMultithreading == True:
                    generatePlanetProcess = threading.Thread(target=generate, args=(starSeed,systemName,barycenterRadius,barycenterMass,star1Color,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,parallax_subd_Cfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,starTypeStr1,x+1,binaryParents,binaryTypes,gSMA,distanceThingamabob))
                    allThreads.append(generatePlanetProcess)
                    allActions.append([time.localtime(),"Starting thread: " + str(generatePlanetProcess)])
                    allActions.append([time.localtime(),"Total threads:" + str(threading.active_count())])
                    allActionArrayUpdated = True
                    allPlanetThreads.append(generatePlanetProcess)
                    generatePlanetProcess.start()
                else:
                    generate(starSeed,systemName,barycenterRadius,barycenterMass,star1Color,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,VolumetricEveCfg,Lum,parallaxCfg,parallax_subd_Cfg,parallax_scatterfix_Cfg,parallax_scatter_Cfg,evePQSCfg,rationalResources_Cfg,starTypeStr1,x+1,binaryParents,binaryTypes,gSMA,distanceThingamabob)

            for thread in allPlanetThreads:
                thread.join()

        listCfg.write(
            "   }\n"
            "}\n"
        )
        atmoCfg.write(
            "}\n"
        )
        oceanCfg.write(
            "}\n"
        )
        eveCfg.write(
            "}\n"
        )
        VolumetricEveCfg.write(
            "}\n"
        )
        evePQSCfg.write(
            "}\n"
        )
        if binaryType == "Near":
            parallaxCfg.write(
                "}\n"
            )
            parallax_subd_Cfg.write(
                "}\n"
            )
            parallax_scatterfix_Cfg.write(
                "}\n"
            )
    # Tests if inputted numbers are actual numbers, currently broken. Also useless.
    def testNum(Numer):
        try:
            val = int(Numer)
        except ValueError:
            print("That's not an number!")
            exit()

    #print("---------------------------------------------------------------")
    #print("Infinite-Discoveries Version 0.9.8 (public beta!)")
    #print("---------------------------------------------------------------")
    #print("WARNING: Generating a large amount of stars will take longer to... generate! The more stars you generate, the more it has to generate. You can find a settings file in the mod directory if you want to adjust some parameters.")
    #print("---------------------------------------------------------------")
#
    #StarAmount = int(input("Amount of stars to generate: "))
    #testNum(StarAmount)
#
    #print("---------------------------------------------------------------")
    #print("If you happened to input a very high number just now, it's recommended to lower the amount of planets per star to reduce KSP loading times.")
    #print("---------------------------------------------------------------")
    #AmountOfPlanetsToGenerate = int(input("Maximum number of planets to add around stars: "))
    #testNum(AmountOfPlanetsToGenerate)
    #print("---------------------------------------------------------------")
    #print("Last thing to input before you can generate! Please input the maximum number of moons to add around a planet.")
    #print("---------------------------------------------------------------")
    #AmountOfMoonsToGenerate = int(input("Maximum number of moons per planet: "))
    #testNum(AmountOfMoonsToGenerate)
    #print("---------------------------------------------------------------")
    #estTime = ((AmountOfPlanetsToGenerate * AmountOfMoonsToGenerate) * StarAmount)*15
    #print("The generator should take AT MOST " + str(round((estTime/60),2)) + " minutes.")
    #if Settings.deleteUnnecessarFolders == True:
    #    print("The program WILL delete itself once it's done!")
    #print("---------------------------------------------------------------")
    #input("Type anything or press enter to continue: ")
    #planetsGenerated = 0
    #startTime = time.time()

    StarAmount = 0
    AmountOfPlanetsToGenerate = 0
    AmountOfMoonsToGenerate = 0
    AmountOfAsteroidsToGenerate = 0
    minPlanets = 0
    minMoons = 0
    minAsteroids = 0

    startTime = time.time()

    loopProcess = None

    def systemLoop(queue, starAmnt, planetAmnt, moonAmnt, asteroidAmnt, targetFilepath, customSeed=None, overrideValues=None):
        print(str(customSeed) + " <------------------------------------------ THE FUCKING SEED BITCH")
        print(multiprocessing.current_process())
        importlib.reload(Settings)
        os.makedirs(targetFilepath + "/InfiniteDiscoveries", exist_ok=True)
        allActions.append([time.localtime(),"Creating Directory"])
        os.makedirs(targetFilepath + "/InfiniteDiscoveries/Configs", exist_ok=True)
        allActions.append([time.localtime(),targetFilepath + "/InfiniteDiscoveries/Configs"])
        os.makedirs(targetFilepath + "/InfiniteDiscoveries/Cache", exist_ok=True)
        allActions.append([time.localtime(),targetFilepath + "/InfiniteDiscoveries/Cache"])
        try:
            shutil.copytree(filepath + "/Misc", targetFilepath + "/InfiniteDiscoveries/Misc")
            allActions.append([time.localtime(),"Cloning: " + "filepath" + "/Misc"])
        except FileExistsError:
            allActions.append([time.localtime(),filepath + "/Misc" + " Already exists."])
            pass
        try:
            shutil.copytree(filepath + "/Visuals", targetFilepath + "/InfiniteDiscoveries/Visuals")
            allActions.append([time.localtime(),"Cloning: " + "filepath" + "/Visuals"])
        except FileExistsError:
            allActions.append([time.localtime(),filepath + "/Visuals" + " Already exists."])
            pass
        try:
            shutil.copytree(filepath + "/Textures", targetFilepath + "/InfiniteDiscoveries/Textures")
            allActions.append([time.localtime(),"Cloning: " + "filepath" + "/Textures"])
        except FileExistsError:
            allActions.append([time.localtime(),filepath + "/Textures" + " Already exists."])
            pass
        try:
            shutil.copytree(filepath + "/Presets", targetFilepath + "/InfiniteDiscoveries/Presets")
            allActions.append([time.localtime(),"Cloning: " + "filepath" + "/Presets"])
        except FileExistsError:
            allActions.append([time.localtime(),filepath + "/Presets" + " Already exists."])
            pass
        try:
            shutil.copy(filepath + "/_Gameplay Settings.cfg", targetFilepath + "/InfiniteDiscoveries/")
            allActions.append([time.localtime(),"Cloning: " + "filepath" + "/_Gameplay Settings.cfg"])
        except FileExistsError:
            pass
            allActions.append([time.localtime(),filepath + "/_Gameplay Settings.cfg" + " Already exists."])

        global allActionArrayUpdated
        allActionArrayUpdated = True

        queue.append("heeeeeheeeeeeeeee")

        global StarAmount
        global AmountOfPlanetsToGenerate
        global AmountOfMoonsToGenerate
        global AmountOfAsteroidsToGenerate
        global minPlanets
        global minMoons
        global minAsteroids

        if customSeed == None:
            StarAmount = starAmnt
        else:
            StarAmount = 1
        
        if overrideValues == None:
            AmountOfPlanetsToGenerate = planetAmnt
            AmountOfMoonsToGenerate = moonAmnt
            AmountOfAsteroidsToGenerate = asteroidAmnt
            minPlanets = Settings.minPlanets
            minMoons = Settings.minMoons
        else:
            #AmountOfPlanetsToGenerate = overrideValues[0]
            #AmountOfMoonsToGenerate = overrideValues[1]
            #AmountOfAsteroidsToGenerate = overrideValues[2]
            #minPlanets = overrideValues[3]
            #minMoons = overrideValues[4]
            AmountOfPlanetsToGenerate, AmountOfMoonsToGenerate, AmountOfAsteroidsToGenerate, minPlanets, minMoons = overrideValues

        global targetPath
        targetPath = targetFilepath + "/InfiniteDiscoveries/"

        for i in range(0,StarAmount):
            randomSeedRNG = random.Random()
            starChoiceRNG = random.Random()
            if customSeed == None:
                generatorSeed = randomSeedRNG.randint(0,(2**32)-1)
                global gloablSeed
                gloablSeed = generatorSeed
            else:
                if int(customSeed) >= 0:
                    generatorSeed = int(customSeed)
                    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" + str(generatorSeed))
                    gloablSeed = generatorSeed
                else:
                    generatorSeed = int(0)
                    gloablSeed = generatorSeed
            starChoiceRNG.seed(generatorSeed)
            starSeed = generatorSeed
            if Settings.binaryOverride == None:
                binaryChoice = starChoiceRNG.randint(0,1)
            elif Settings.binaryOverride == True:
                binaryChoice = 0
            elif Settings.binaryOverride == False:
                binaryChoice = 1
            else:
                print("epic binary override fail")
                binaryChoice = starChoiceRNG.randint(0,1)
            if binaryChoice == 0:
                barycenter = True
                if Settings.useMultithreading == True:
                    generateBarycenterProcess = threading.Thread(target=generateBarycenter, args=(starSeed, AmountOfPlanetsToGenerate, targetPath))
                    allThreads.append(generateBarycenterProcess)
                    generateBarycenterProcess.start()
                else:
                    generateBarycenter(starSeed, AmountOfPlanetsToGenerate, targetPath)
            else:
                barycenter = False
                if Settings.useMultithreading == True:
                    generateStarProcess = threading.Thread(target=generateStar, args=(starSeed, AmountOfPlanetsToGenerate, barycenter, targetPath))
                    allThreads.append(generateStarProcess)
                    generateStarProcess.start()
                else:
                    generateStar(starSeed, AmountOfPlanetsToGenerate, barycenter, targetPath)

        if everythingEnded == True:
            raise Exception("UI thread isn't running.")

    def waitForThreadsToFinish(mainThread, idk):
        mainThread.join()
        for thread in allThreads:
            thread.join()
        global mainThreadFinished
        mainThreadFinished = True
        allActions.append([time.localtime(),"Generating wormholes..."])
        global allActionArrayUpdated
        allActionArrayUpdated = True

        #generateWormholes()

        allActions.append([time.localtime(),"Finished generation."])
        allActionArrayUpdated = True

    def startLoop(starAm,planetAm,moonAM,asteroidAM,targetPath,customSeed=None,overrides=None):
        global loopProcess
        loopProcess = threading.Thread(target=systemLoop, args=(queue,starAm,planetAm,moonAM,asteroidAM,targetPath,customSeed,overrides))
        allThreads.append(loopProcess)
        allActions.append([time.localtime(),"Starting thread: " + str(loopProcess)])
        allActions.append([time.localtime(),"Total threads:" + str(threading.active_count())])
        global allActionArrayUpdated
        allActionArrayUpdated = True
        loopProcess.start()
        waitForThreadsToFinishThread = threading.Thread(target=waitForThreadsToFinish, args=(loopProcess,None))
        waitForThreadsToFinishThread.start()

    def openSettings():

        importlib.reload(Settings)

        print(filepath)

        with open(filepath + "/Settings.py", "r") as settingsFile:
            settingsData = settingsFile.readlines()

        usesMultithreading = Settings.useMultithreading

        convertsToDDS = Settings.convertTexturesToDDS

        fantasyNames = Settings.fantasyNames

        minPlanets = Settings.minPlanets
        minMoons = Settings.minMoons

        showConsole = Settings.showConsole

        useThreadingText = sg.Text(textwrap.fill("Multithreading drastically improves efficiency but might increase CPU usage.", 40), background_color="#1f2836")
        useThreadingCheck = sg.Checkbox("Use Multithreading", default=usesMultithreading, key="useMultithreading")
        useThreadingLayout = [[useThreadingCheck],[useThreadingText]]
        useThreadingFrame = sg.Frame("Multithreading",layout=useThreadingLayout)

        convertToDDSText = sg.Text(textwrap.fill("Converting maps to DDS improves RAM usage ingame, but takes a bit longer and requires ImageMagick.", 40), background_color="#1f2836")
        convertToDDSCheck = sg.Checkbox("Convert Textures to DDS", default=convertsToDDS, key="convertsToDDS")
        convertToDDSLayout = [[convertToDDSCheck],[convertToDDSText]]
        convertToDDSrame = sg.Frame("DDS Conversion",layout=convertToDDSLayout)

        fantasyNamesText = sg.Text(textwrap.fill("Fantasy names do not affect anything, but simply adds some more creative names to celestial bodies.", 40), background_color="#1f2836")
        fantasyNamesCheck = sg.Checkbox("Use Fantasy Names", default=fantasyNames, key="fantasyNames")
        fantasyNamesLayout = [[fantasyNamesCheck],[fantasyNamesText]]
        fantasyNamesrame = sg.Frame("Fancy Names",layout=fantasyNamesLayout)

        minPlanetsBox = sg.Input(str(minPlanets), key="minPlanetsInp", enable_events=True, size=(12,10), expand_y=False, expand_x=False)
        minPlanetsLayout = [[minPlanetsBox]]
        minPlanetsFrame = sg.Frame("Minimum Planets", layout=minPlanetsLayout)

        minMoonsBox = sg.Input(str(minMoons), key="minMoonsInp", enable_events=True, size=(12,10), expand_y=False, expand_x=False)
        minMoonsLayout = [[minMoonsBox]]
        minMoonsFrame = sg.Frame("Minimum Moons", layout=minMoonsLayout)

        variablesLayout = [[useThreadingFrame],[convertToDDSrame],[fantasyNamesrame],[minPlanetsFrame,minMoonsFrame]]

        variablesFrame = sg.Frame("Generator Settings", layout=variablesLayout, expand_x=True, expand_y=True)

        showConsoleText = sg.Text(textwrap.fill("Shows the console in the background. Requires a restart to apply.", 40), background_color="#1f2836")
        showConsoleCheck = sg.Checkbox("Show Console", default=showConsole, key="showConsole")
        showConsoleLayout = [[showConsoleCheck],[showConsoleText]]
        showConsoleFrame = sg.Frame("Console",layout=showConsoleLayout)

        UIvariablesLayout = [[showConsoleFrame]]

        UIvariablesFrame = sg.Frame("UI Settings", layout=UIvariablesLayout, expand_x=True, expand_y=True)

        applyButton = sg.Button("Apply", key="Apply")

        applyLayout = [[applyButton]]

        applyFrame = sg.Frame("", layout=applyLayout)

        openFileButton = sg.Button("Open File", key="openFile")

        openFileLayout = [[openFileButton]]

        openFileFrame = sg.Frame("", layout=openFileLayout)

        settingsLayout = [[variablesFrame,UIvariablesFrame],[applyFrame,openFileFrame]]

        print(filepath + "/UIdata/funnyicon.ico")

        settingsWindow = sg.Window(title="Settings", layout=settingsLayout, size=(300,450), resizable=False, finalize=True, background_color="#1f2836", icon=filepath + "/UIdata/funnyicon.ico")

        settingsWindow.TKroot.minsize(600,450)

        def openSettingsFile():
            os.system("notepad.exe " + filepath + "/Settings.py")

        while True:
            event, values = settingsWindow.read()

            if event == "minPlanetsInp":
                try: 
                    int(values["minPlanetsInp"])
                except:
                    print("Not a number!")
                    settingsWindow["minPlanetsInp"].update(values["minPlanetsInp"][:-1])

            if event == "minMoonsInp":
                try: 
                    int(values["minMoonsInp"])
                except:
                    print("Not a number!")
                    settingsWindow["minMoonsInp"].update(values["minMoonsInp"][:-1])

            if event == "Apply":
                usesMultithreading = values["useMultithreading"]
                print(usesMultithreading)
                settingsData[2] = "useMultithreading = " + str(usesMultithreading) + " # Will use multithreading, this will drastically increase generator efficiency and thus result in faster generation, but may increase CPU usage." + "\n"

                convertsToDDS = values["convertsToDDS"]
                print(convertsToDDS)
                settingsData[6] = "convertTexturesToDDS = " + str(convertsToDDS) + " # Will remove the requirement for ImageMagick and reduce generator time if false. Will also increase KSP loading time so setting to false is not recommended." + "\n"

                fantasyNames = values["fantasyNames"]
                print(fantasyNames)
                settingsData[11] = "fantasyNames = " + str(fantasyNames) + " # Generate a fantasy name for bodies. Will not affect internal names!" + "\n"

                minPlanets = int(values["minPlanetsInp"])
                print(minPlanets)
                settingsData[8] = "minPlanets = " + str(minPlanets) + " # Minimum number of planets per star." + "\n"

                minMoons = int(values["minMoonsInp"])
                print(minMoons)
                settingsData[9] = "minMoons = " + str(minMoons) + " # Minimum number of moons per star." + "\n"

                showConsole = values["showConsole"]
                print(showConsole)
                settingsData[13] = "showConsole = " + str(showConsole) + " # Whether or not to show the console." + "\n"

                with open(filepath + "/Settings.py", "w") as settingsFile:
                    settingsFile.writelines( settingsData )

                print(threading.current_thread())

            if event == "openFile":
                openSettingsFileThread = threading.Thread(target=openSettingsFile)
                openSettingsFileThread.start()

            if event == sg.WIN_CLOSED:
                break

    def openDelete(targetPath):
        import PySimpleGUI as sg

        explText = textwrap.fill("The below input requires the star's internal name. You can find it by going ingame and looking at the description, where the name is formatted as 'AA-11111' WARNING: will delete EVERY config/texture containing what you inputted! Leave blank to delete everything.", width=40)

        explanation = sg.Text(explText)

        starDelInput = sg.Input(key="deleteStarValue")

        starDelButton = sg.Button("Delete", button_color="#e65045", key="deleteStar")

        deleteSystemsLayout = [[explanation],[starDelInput],[starDelButton]]

        deleteSystemsFrame = sg.Frame("Delete star", layout=deleteSystemsLayout, expand_x=True, expand_y=False)

        deleteAllButton = sg.Button("Remove Directory", button_color="#e65045", key="deleteALL")

        deleteAllLayout = [[deleteAllButton]]

        deleteAllFrame = sg.Frame("Warning: this will delete the mod from KSP!", layout=deleteAllLayout, expand_x=True, expand_y=False)

        deleteLayout = [[deleteSystemsFrame],[deleteAllFrame]]

        deleteWindow = sg.Window(title="Delete Systems", layout=deleteLayout, size=(300,300), resizable=False, finalize=True, background_color="#1f2836", icon=filepath + "/UIdata/funnyicon.ico")

        deleteStarAreYouSure = False

        deleteDirAreYouSure = False

        targetPath

        print(targetPath)

        textureDir = targetPath + "/InfiniteDiscoveries" + "/Textures/PluginData"
        configDir = targetPath + "/InfiniteDiscoveries" + "/Configs"
        cacheDir = targetPath + "/InfiniteDiscoveries" + "/Cache"
        visual_ScattererDir = targetPath + "/InfiniteDiscoveries" + "/Visuals/Scatterer"
        visual_EveConfigDir = targetPath + "/InfiniteDiscoveries" + "/Visuals/Eve/Configs"
        visual_ParallaxDir = targetPath + "/InfiniteDiscoveries" + "/Visuals/Parallax/Configs"
        visual_CloudMapDir = targetPath + "/InfiniteDiscoveries" + "/Textures/Clouds"
        visual_NiftyNebulaeDir = targetPath + "/InfiniteDiscoveries" + "/Visuals/NiftyNebulae"
        misc_RRDir = targetPath + "/InfiniteDiscoveries" + "/Misc/RR"

        allDirs = [textureDir, configDir, cacheDir, visual_ScattererDir, visual_EveConfigDir, visual_ParallaxDir, visual_CloudMapDir, visual_NiftyNebulaeDir, misc_RRDir]

        def areYouSureWait(thing, text):
            time.sleep(2)
            global deleteStarAreYouSure
            deleteStarAreYouSure = False
            thing.update(text)

        def areYouSureAllWait(thing, text):
            time.sleep(2)
            global deleteDirAreYouSure
            deleteDirAreYouSure = False
            thing.update(text)

        while True:
            event, values = deleteWindow.read()

            if event == "deleteStar":
                if deleteStarAreYouSure == False:
                    deleteStarAreYouSure = True
                    deleteWindow["deleteStar"].update("Are You Sure? This CANNOT be undone!")
                    areYouSureThread = threading.Thread(target=areYouSureWait, args=(deleteWindow["deleteStar"], "Delete"))
                    areYouSureThread.start()
                else:
                    targetStar = values["deleteStarValue"]
                    print(targetStar)
                    try:
                        for e in range(0,len(allDirs)):
                            currentDir = allDirs[e]
                            for f in os.listdir(currentDir):
                                if targetStar in f:
                                    os.remove(os.path.join(currentDir, f))
                    except FileNotFoundError:
                        deleteWindow["deleteStar"].update("Directory doesn't exist!")
                        areYouSureThread = threading.Thread(target=areYouSureWait, args=(deleteWindow["deleteStar"], "Delete"))
                        areYouSureThread.start()

            if event == "deleteALL":
                if deleteDirAreYouSure == False:
                    deleteDirAreYouSure = True
                    deleteWindow["deleteALL"].update("Are You Sure? This CANNOT be undone!")
                    areYouSureThread = threading.Thread(target=areYouSureAllWait, args=(deleteWindow["deleteALL"], "Remove Directory"))
                    areYouSureThread.start()
                else:
                    try:
                        shutil.rmtree(targetPath + "/InfiniteDiscoveries")
                    except FileNotFoundError:
                        deleteWindow["deleteALL"].update("Directory doesn't exist!")
                        areYouSureThread = threading.Thread(target=areYouSureAllWait, args=(deleteWindow["deleteALL"], "Remove Directory"))
                        areYouSureThread.start()

            if event == sg.WIN_CLOSED:
                break

    def openHelp():
        noticeWindow = sg.Window(title="Infinite Discoveries Help", layout=[[]])
        noticeWindow.read()

    def startUI():
        #print(multiprocessing.current_process())
        cachePath = filepath + "/UIdata/cache.py"
        sys.path.insert(0, filepath + "/UIdata/")
        import cache

        targetPath = cache.filepath

        amountValues = cache.numbers

        #sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

        actionText = ""

        inputButtonSize = (12,10)

        currentObjectText = sg.Text("Generator is not currently running.", background_color=("#0c0f1a"), key="currentFocusText")

        currentActionText = sg.Multiline(background_color=("#0c0f1a"), key="currentActionText", expand_y=True, expand_x=True, text_color=("#ffffff"), autoscroll=True, enable_events=True, do_not_clear=True)

        currentActionLayout = [[currentObjectText],[currentActionText]]

        currentActionFrame = sg.Column(layout=currentActionLayout, background_color=("#0c0f1a"), key="currentActionFrame", expand_y=True, expand_x=True)

        startAmountDescText = "Recommended values are however many stars, 7 planets and 3 moons. Higher amounts will generate planets/moons further out and might start causing issues. Make sure to select the KSP GameData folder as the directory."

        starAmountDescription = sg.Text(textwrap.fill(startAmountDescText, 49), expand_y=False, expand_x=True, pad=(5,5), key="starAmountDesc")

        starAmountInp = sg.Input(default_text=amountValues[0], key="starAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
        starAmountLayout = [[starAmountInp]]
        starAmountFrame = sg.Frame("Star amount", layout=starAmountLayout, expand_y=True, expand_x=True, pad=(5,5))
        planetAmountInp = sg.Input(default_text=amountValues[1], key="planetAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
        planetAmountLayout = [[planetAmountInp]]
        planetAmountFrame = sg.Frame("Max planets", layout=planetAmountLayout, expand_y=True, expand_x=True, pad=(5,5))
        moonAmountInp = sg.Input(default_text=amountValues[2], key="moonAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
        moonAmountLayout = [[moonAmountInp]]
        moonAmountFrame = sg.Frame("Max moons", layout=moonAmountLayout, expand_y=True, expand_x=True, pad=(5,5))
        asteroidAmountInp = sg.Input(default_text=amountValues[3], key="asteroidAmountInput", enable_events=True, size=inputButtonSize, expand_y=False, expand_x=True)
        asteroidAmountLayout = [[asteroidAmountInp]]
        asteroidAmountFrame = sg.Frame("Max asteroids", layout=asteroidAmountLayout, expand_y=True, expand_x=True, pad=(5,5))

        numInpLayout = [[starAmountFrame, planetAmountFrame, moonAmountFrame, asteroidAmountFrame],[starAmountDescription]]

        amountInpFrame = sg.Frame("", layout=numInpLayout, background_color=("#43474d"), expand_y=False, expand_x=True, pad=(10,0))

        startButton = sg.pin(sg.Button(button_text="Start Generator", size=(25,5), key="startGenerator", visible=True, expand_y=False, expand_x=True, pad=(10,0)), expand_x=True)

        estTimeText = sg.Text("Estimated Generator Time: 26.25 minutes.", key="timeRemainingText", background_color=("#43474d"), expand_y=False, expand_x=True)

        directoryText = sg.Input(targetPath, size=(30,10), key="directoryText", enable_events=True, expand_y=False, expand_x=True)

        directoryBrowser = sg.FolderBrowse("Set GameData folder...", key="directoryButton", enable_events=True, initial_folder=targetPath)

        #statsDesc = sg.Text("Current Statistics:", key="stats_Desc", background_color=("#43474d"), expand_y=False, expand_x=True)
        
        statsSystemAmount = sg.Text("Amount of systems: ????", key="stats_SystemAmount", background_color=("#43474d"), expand_y=False, expand_x=True)
        statsConfigAmount = sg.Text("Amount of configs: ????", key="stats_ConfigAmount", background_color=("#43474d"), expand_y=False, expand_x=True)
        statsTextureAmount = sg.Text("Amount of textures: ????", key="stats_TextureAmount", background_color=("#43474d"), expand_y=False, expand_x=True)

        statsLayout = [[statsSystemAmount],[statsConfigAmount],[statsTextureAmount]]

        statsFrame = sg.Frame("Current statistics", layout=statsLayout, expand_y=False, expand_x=True, background_color="#43474d")

        okToAccess = sg.Text("To write or not to write? That is the question.", background_color=("#43474d"), expand_x=True, key="okToAccess")

        InfDLayout = [[sg.Text("Infinite Discoveries", background_color=("#43474d"))], [amountInpFrame], [directoryText,directoryBrowser], [okToAccess], [estTimeText], [startButton], [statsFrame]]

        InfDOutputLayout = [[currentActionFrame]]

        settingsButton = sg.Button("Settings", image_size=(50,50), key="openSettings")

        settingsLayout = [[settingsButton]]

        settingsFrame = sg.Frame("", layout=settingsLayout)

        deleteButton = sg.Button("Delete", image_size=(50,50), key="openDelete")

        deleteLayout = [[deleteButton]]

        deleteFrame = sg.Frame("", layout=deleteLayout)

        infoButton = sg.Button("Help", image_size=(50,50), key="openHelp")

        infoLayout = [[infoButton]]

        infoFrame = sg.Frame("", layout=infoLayout)

        seedText = sg.Text("Custom Seed")
        seedInput = sg.Input("", key="setSeed", enable_events=True, size=(20,0))

        seedLayout = [[seedInput,seedText]]

        seedFrame = sg.Frame("", layout=seedLayout, element_justification="c",tooltip="Setting a custom seed will limit the star amount to 1. Seeds must be integers between 0 and 2^32 - 1")

        InputFrame = sg.Frame("", layout=InfDLayout, expand_y=True, expand_x=True, element_justification="c", background_color="#50535c")

        OutputFrame = sg.Frame("", layout=InfDOutputLayout, expand_y=True, expand_x=True, element_justification="c", background_color="#50535c")

        fullLayout = [[InputFrame,OutputFrame],[settingsFrame,deleteFrame,infoFrame,seedFrame]]

        InfDWindow = sg.Window(title="Infinite Discoveries 0.9.9", layout=fullLayout, size=(800,500), margins=(5,0), resizable=True, finalize=True, icon=filepath + "/UIdata/funnyicon.ico", background_color="#1f2836")

        InfDWindow.TKroot.minsize(700,500)

        # Things??

        lastMoment = 0

        ActionLog = open(filepath + "/ActionLog.txt", "w")
        ActionLog = open(filepath + "/ActionLog.txt", "a")

        if Settings.convertTexturesToDDS == True:
            try:
                from wand import image as wImage
            except:
                #print("ImageMagick is not installed, install it from: https://docs.wand-py.org/en/latest/guide/install.html#install-imagemagick-on-windows")
                noticeText = textwrap.fill("ImageMagick is not installed! You can continue to run the program as intended, but it will not convert textures to DDS.", 40)
                noticeLayour = [[sg.Text(noticeText)]]
                noticeWindow = sg.Window(title="Notice", layout=noticeLayour)
                noticeWindow.read()     

            def setStarAmntToOverriden():
                InfDWindow["starAmountInput"].update(disabled=True)
                InfDWindow["starAmountInput"].update("SEED SET")
                InfDWindow["starAmountInput"].update(text_color="#6e6e6e")
                InfDWindow["starAmountInput"].set_tooltip("Overriden due to setting a custom seed.")

            def setStarAmntToDefault():
                InfDWindow["starAmountInput"].update(disabled=False)
                InfDWindow["starAmountInput"].update(amountValues[0])
                InfDWindow["starAmountInput"].update(text_color="#000000")
                InfDWindow["starAmountInput"].set_tooltip(None)

            def setOtherAmntToOverriden():
                InfDWindow["planetAmountInput"].update(disabled=True)
                InfDWindow["planetAmountInput"].update("SEED SET")
                InfDWindow["planetAmountInput"].update(text_color="#6e6e6e")
                InfDWindow["planetAmountInput"].set_tooltip("Overriden due to setting a custom seed.")

                InfDWindow["moonAmountInput"].update(disabled=True)
                InfDWindow["moonAmountInput"].update("SEED SET")
                InfDWindow["moonAmountInput"].update(text_color="#6e6e6e")
                InfDWindow["moonAmountInput"].set_tooltip("Overriden due to setting a custom seed.")

                InfDWindow["asteroidAmountInput"].update(disabled=True)
                InfDWindow["asteroidAmountInput"].update("SEED SET")
                InfDWindow["asteroidAmountInput"].update(text_color="#6e6e6e")
                InfDWindow["asteroidAmountInput"].set_tooltip("Overriden due to setting a custom seed.")

            def setOtherAmntToDefault():
                InfDWindow["planetAmountInput"].update(disabled=False)
                InfDWindow["planetAmountInput"].update(amountValues[1])
                InfDWindow["planetAmountInput"].update(text_color="#000000")
                InfDWindow["planetAmountInput"].set_tooltip(None)

                InfDWindow["moonAmountInput"].update(disabled=False)
                InfDWindow["moonAmountInput"].update(amountValues[2])
                InfDWindow["moonAmountInput"].update(text_color="#000000")
                InfDWindow["moonAmountInput"].set_tooltip(None)

                InfDWindow["asteroidAmountInput"].update(disabled=False)
                InfDWindow["asteroidAmountInput"].update(amountValues[3])
                InfDWindow["asteroidAmountInput"].update(text_color="#000000")
                InfDWindow["asteroidAmountInput"].set_tooltip(None)

        running = False
        import os
        while True:
            event, values = InfDWindow.read(timeout=100)

            if event == "starAmountInput":
                try: 
                    int(values["starAmountInput"])
                except:
                    print("Not a number!")
                    InfDWindow["starAmountInput"].update(values["starAmountInput"][:-1])

            if event == "planetAmountInput":
                try: 
                    int(values["planetAmountInput"])
                    if int(values["planetAmountInput"]) > 25:
                        InfDWindow["planetAmountInput"].update(25)
                except:
                    print("Not a number!")
                    InfDWindow["planetAmountInput"].update(values["planetAmountInput"][:-1])

            if event == "moonAmountInput":
                try: 
                    int(values["moonAmountInput"])
                except:
                    print("Not a number!")
                    InfDWindow["moonAmountInput"].update(values["moonAmountInput"][:-1])
            
            if event == "asteroidAmountInput":
                try: 
                    int(values["asteroidAmountInput"])
                except:
                    print("Not a number!")
                    InfDWindow["asteroidAmountInput"].update(values["asteroidAmountInput"][:-1])
            try:
                starAmount = int(values["starAmountInput"])
            except:
                starAmount = 0
            try:
                planetAmount = int(values["planetAmountInput"])
            except:
                planetAmount = 0
            try:
                moonAmount = int(values["moonAmountInput"])
            except:
                moonAmount = 0
            try:
                asteroidAmount = int(values["asteroidAmountInput"])
            except:
                asteroidAmount = 0

            #overrideSeed = False
            #overrideValues = False

            if event == "setSeed":
                customSeedInput = values["setSeed"]
                seperatedValues = customSeedInput.split(".")
                if not customSeedInput == "":
                    if len(seperatedValues) > 1:
                        if len(seperatedValues[1]) >= 9 and len(seperatedValues[1]) <= 14:
                            try:
                                customSeed = int(seperatedValues[0])
                                fullySeperatedValues = seperatedValues[1].split(":")
                                maxPlanetOvrd = int(fullySeperatedValues[0])
                                maxMoonOvrd = int(fullySeperatedValues[1])
                                maxAsteroidOvrd = int(fullySeperatedValues[2])
                                minPlanetOvrd = int(fullySeperatedValues[3])
                                minMoonOvrd = int(fullySeperatedValues[4])
                                #maxPlanetOvrd, maxMoonOvrd, maxAsteroidOvrd, minPlanetOvrd, minMoonOvrd = seperatedValues[1].split(":")
                                if customSeed >= 0 and customSeed < (2**32):
                                    print("Seed and overrides set.") # This is the part where there is both valid seed and overrides!
                                    setStarAmntToOverriden()
                                    setOtherAmntToOverriden()
                                    overrideSeed = True # True
                                    overrideValues = True # True
                                else:
                                    print("ERROR: Seed out of bounds!")
                                    setStarAmntToDefault()
                                    setOtherAmntToDefault()
                                    overrideSeed = False
                                    overrideValues = False
                            except:
                                print("ERROR: Seed or overrides not integers!")
                                setStarAmntToDefault()
                                setOtherAmntToDefault()
                                overrideSeed = False
                                overrideValues = False
                        else:
                            try:
                                customSeed = int(seperatedValues[0])
                                if customSeed >= 0 and customSeed < (2**32):
                                    print("Only seed applied. Invalid overrides.") # This is the part where a valid seed is set despite invalid overrides!
                                    setStarAmntToOverriden()
                                    setOtherAmntToDefault()
                                    overrideSeed = True # True
                                    overrideValues = False
                                else:
                                    print("ERROR: Seed out of bounds! (Also invalid overrides.)")
                                    setStarAmntToDefault()
                                    setOtherAmntToDefault()
                                    overrideSeed = False
                                    overrideValues = False
                            except:
                                print("ERROR: Seed not integer! (Also invalid overrides.)")
                                setStarAmntToDefault()
                                setOtherAmntToDefault()
                                overrideSeed = False
                                overrideValues = False
                    else:
                        try:
                            customSeed = int(seperatedValues[0])
                            if customSeed >= 0 and customSeed < (2**32):
                                print("Only seed applied.") # This is the part where a valid seed is set! (ONLY SEED, NO OVERRIDES.)
                                setStarAmntToOverriden()
                                setOtherAmntToDefault()
                                overrideSeed = True # True
                                overrideValues = False
                            else:
                                setStarAmntToDefault()
                                setOtherAmntToDefault()
                                print("ERROR: Seed out of bounds!")
                                overrideSeed = False
                                overrideValues = False
                        except:
                            print("ERROR: Seed not integer!")
                            setStarAmntToDefault()
                            setOtherAmntToDefault()
                            overrideSeed = False
                            overrideValues = False
                else:
                    print("No seed set.")
                    setStarAmntToDefault()
                    setOtherAmntToDefault()
                    overrideSeed = False
                    overrideValues = False


            if event == "directoryText" or event == "starAmountInput" or event == "planetAmountInput" or event == "moonAmountInput" or event == "asteroidAmountInput":
                targetPath = values["directoryText"]
                print("Setting directory to: " + targetPath)
                print("Values are: " + "[" + str(starAmount) + "," + str(planetAmount) + "," + str(moonAmount) + "," + str(asteroidAmount) + "]")
                cacheFile = open(cachePath, "w")
                cacheFile.write(
                    'filepath = "' + targetPath + '"' + "\n"
                    "numbers = " + "[" + str(starAmount) + "," + str(planetAmount) + "," + str(moonAmount) + "," + str(asteroidAmount) + "]" + "\n"
                )
                cacheFile.close()

            if event == "openSettings":
                openSettings()

            if event == "openDelete":
                openDelete(targetPath)

            if event == "openHelp":
                openHelp()

            if Settings.useMultithreading == True:
                estTime = (((planetAmount * moonAmount * asteroidAmount) * starAmount)*15)/6.17
            else:
                estTime = ((planetAmount * moonAmount * asteroidAmount) * starAmount)*15

            if estTime >= 60:
                if estTime >= 3600:
                    if estTime >= 86400:
                        if estTime >= 604800:
                            if estTime >= 2.628e+6:
                                if estTime >= 3.154e+7:
                                    InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/3.154e+7),2)) + " years.")
                                else:
                                    InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/2.628e+6),2)) + " months.")
                            else:
                                InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/604800),2)) + " weeks.")
                        else:
                            InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/86400),2)) + " days.")
                    else:
                        InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/3600),2)) + " hours.")
                else:
                    InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime/60),2)) + " minutes.")
            else:
                InfDWindow["timeRemainingText"].update("Estimated Generator Time: " + str(round((estTime),2)) + " seconds.")

            #print("fine")

            #if not len(queue) < 1:
            #    for i in len(queue):
            #        allActions.append(queue[i])

            actionText = ""

            global allActionArrayUpdated
            if allActionArrayUpdated == True:
                for a in range(lastMoment,len(allActions)):
                    lastMoment = lastMoment + 1
                    currentAction = allActions[a]
                    actionText = str(currentAction[0].tm_hour) + ":" + str(currentAction[0].tm_min) + ":" + str(currentAction[0].tm_sec) + " - " + currentAction[1] + "\n"
                    InfDWindow["currentActionText"].update(actionText,append=True)
                    ActionLog.write(actionText)
                    ActionLog.flush()
                allActionArrayUpdated = False

            if running == True:
                #print(amountOfThingsDone/amountOfThingsToDo)
                try:
                    InfDWindow["startGenerator"].update(str((amountOfThingsDone/amountOfThingsToDo)*100) + "%")
                except ZeroDivisionError:
                    print("Division by zero (ignore this)")

            if event == "startGenerator":
                InfDWindow.set_icon(filepath + "/UIdata/StatusIcons/Icon_Working.ico")
                try: 
                    int(values["starAmountInput"])
                    try: 
                        int(values["planetAmountInput"])
                        try: 
                            int(values["moonAmountInput"])
                            try:
                                int(values["asteroidAmountInput"])
                            except:
                                print("Not a number!")
                        except:
                            print("Not a number!")
                    except:
                        print("Not a number!")
                except:
                    print("Not a number!")

                print("The generator should take AT MOST " + str(round((estTime/60),2)) + " minutes.")

                InfDWindow["currentFocusText"].update("Generator is active.")
                InfDWindow["startGenerator"].update("0%")
                InfDWindow["startGenerator"].update(disabled=True)

                running = True

                #InfDWindow["startGenerator"].hide_row()

                #allActions.append("Making directory at: " + targetPath)

                #os.makedirs(targetPath + "/InfiniteDiscoveries_Systems", exist_ok=True)

                #print(currentActionLayout)

                #time.sleep(1)

                #systemThread = threading.Thread(target=systemLoop, args=(queue,starAmount,planetAmount,moonAmount,targetPath))
                #systemThread.run()

                if not values["setSeed"] == "":
                    if overrideSeed == True and overrideValues == False:
                        startLoop(starAmount,planetAmount,moonAmount,asteroidAmount,targetPath,customSeed)
                    elif overrideSeed == True and overrideValues == True:
                        startLoop(starAmount,planetAmount,moonAmount,asteroidAmount,targetPath,customSeed,[maxPlanetOvrd,maxMoonOvrd,maxAsteroidOvrd,minPlanetOvrd,minMoonOvrd])
                    else:
                        startLoop(starAmount,planetAmount,moonAmount,asteroidAmount,targetPath)
                    global mainThreadFinished
                    mainThreadFinished = False
                else:
                    startLoop(starAmount,planetAmount,moonAmount,asteroidAmount,targetPath)
                    mainThreadFinished = False

                #for a in allThreads:
                #    a.join()
            if mainThreadFinished == True:
                InfDWindow.set_icon(filepath + "/UIdata/StatusIcons/Icon_Idle.ico")
                #InfDWindow["startGenerator"].unhide_row()
                InfDWindow["currentFocusText"].update("Generator is finished!")
                InfDWindow["startGenerator"].update("Generate")
                InfDWindow["startGenerator"].update(disabled=False)

                running = False

                InfDWindow.refresh()

            try:
                allKopConfigs = os.listdir(targetPath + "/InfiniteDiscoveries/Configs/")
                allEVEConfigs = os.listdir(targetPath + "/InfiniteDiscoveries/Visuals/EVE/Configs/")
                allParallaxConfigs = os.listdir(targetPath + "/InfiniteDiscoveries/Visuals/Parallax/Configs/")
                #allKopConfigs = os.listdir(targetPath + "/InfiniteDiscoveries/Visuals/Parallax/Configs/")
                allTextures = os.listdir(targetPath + "/InfiniteDiscoveries/Textures/PluginData/")
                allCloudTextures = os.listdir(targetPath + "/InfiniteDiscoveries/Textures/Clouds/")
                allALLTextures = allTextures + allCloudTextures
                #print(len(allKopConfigs))
                allScattererConfigs = os.listdir(targetPath + "/InfiniteDiscoveries/Visuals/Scatterer/")
                allRRConfigs = os.listdir(targetPath + "/InfiniteDiscoveries/Misc/RR/")
                #print(len(allScattererConfigs))
                allSystems = []
                for scattererCfg in allScattererConfigs:
                    if "ScattererSunflare" in scattererCfg:
                        systemName = scattererCfg.replace("ScattererSunflare", "").replace("_", "").replace(".cfg", "").replace("1","").replace("2","").replace("-","")
                        allSystems.append(systemName)
                        #print(systemName)
                #print(len(allSystems))
                allSystemsREAL = np.unique(allSystems)

                allConfigs = allKopConfigs + allEVEConfigs + allParallaxConfigs + allScattererConfigs + allRRConfigs
                #print(allConfigs)
                InfDWindow["stats_SystemAmount"].update("Amount of systems: " + str(len(allSystemsREAL)))
                InfDWindow["stats_ConfigAmount"].update("Amount of configs: " + str(len(allConfigs)))
                InfDWindow["stats_TextureAmount"].update("Amount of textures: " + str(len(allALLTextures)))
            except:
                InfDWindow["stats_SystemAmount"].update("Amount of systems: No directory!")
                InfDWindow["stats_ConfigAmount"].update("Amount of configs: No directory!")
                InfDWindow["stats_TextureAmount"].update("Amount of textures: No directory!")

            if os.access(targetPath, os.W_OK):
                InfDWindow["okToAccess"].update("Selected directory can be written to.")
                InfDWindow["okToAccess"].update(text_color=("#8fff8f"))
            else:
                InfDWindow["okToAccess"].update("Cannot write to selected directory!")
                InfDWindow["okToAccess"].update(text_color=("#ff8f8f"))

            if event == sg.WINDOW_CLOSED:
                global everythingEnded
                everythingEnded = True
                import os
                import signal

                # Get the process ID (PID) of the current Python process
                current_pid = os.getpid()

                print(current_pid)

                # Terminate the current process using its PID
                os.kill(current_pid, signal.SIGTERM)

                break

    if currentProcess.name == "MainThread":
        startUI()

    #print("gagagaga")

    #systemLoop(StarAmount, AmountOfPlanetsToGenerate, AmountOfMoonsToGenerate)

    print("All done!")
    print("---------------------------------------------------------------")
    print("Total number of stars generated: " + str(totalStarsGenerated))
    print("Total number of planets generated: " + str(totalPlanetsGenerated))
    print("Total number of moons generated: " + str(totalMoonsGenerated))
    print("---------------------------------------------------------------")
    print("Total objects generated: " + str(totalStarsGenerated + totalPlanetsGenerated + totalMoonsGenerated))
    print("---------------------------------------------------------------")
    #print("Now it's REALLY all done!")
    #print("---------------------------------------------------------------")
    endTime = time.time()
    elapsedTime = endTime - startTime
    if elapsedTime > 60:
        print("Time elapsed: " + str(round(elapsedTime/60,2)) + " minutes.")
    elif elapsedTime < 60:
        print("Time elapsed: " + str(round(elapsedTime,2)) + " seconds.")
#
    ##print(allPlanets)
#
    #if Settings.deleteUnnecessarFolders == False:
    #    print("Make sure to delete the GenerateSystem folder so that KSP can load!")
    #    input("Type anything or press enter to close: ")
    #else:
    #    print("The program will now self-destruct!")
    #    print("NOTICE BEFORE CONTINUING: This greatly increases the size of temporary files! Make sure to clean out your temporary files folder.")
    #    input("Type anything or press enter to self-destruct: ")
    #    import tempfile
    #    tempDirectory = tempfile.gettempdir()
    #    dirName = "infD_" + str(random.randint(0,9999999))
    #    os.mkdir(tempDirectory + "/" + dirName)
#
    #    destFolder = tempDirectory + "/" + dirName
    #    for f in os.listdir(destFolder):
    #        os.remove(f)
    #    for f in os.listdir(filepath1):
    #        target = filepath1 + "/" + f
    #        print(target)
    #        try:
    #            shutil.move(target,destFolder)
    #        except Exception as e:
    #            input(e)
    #            print("Something failed to delete itself!! Make sure you manually delete the GenerateSystem folder!!")
    #            pass

except Exception:
    logging.error(traceback.format_exc())
    print(traceback.format_exc())
    input("Type anything or press enter to close: ")