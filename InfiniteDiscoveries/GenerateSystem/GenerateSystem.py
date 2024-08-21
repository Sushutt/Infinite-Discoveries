import logging
import traceback
import os
filepath1 = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
filepath = filepath1.replace("/GenerateSystem", "")
logging.basicConfig(filename=filepath +'/InfiniteDiscoveries.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger=logging.getLogger(__name__)

try:
    import random
    import string
    from PIL import Image, ImageEnhance, ImageChops, ImageOps, ImageFilter
    from colour import Color
    import sys
    import time
    import math
    import numpy as np
    import scipy
    from scipy.signal import convolve2d
    import noise
    import sys

    # Variables lamo
    templates = ["Dres", "Duna", "Laythe", "Mun", "Jool"] # Laythe and Mun are unused lmao lol oops.
    planetsGenerated = 0
    alphabet = list(string.ascii_uppercase)

    # Star Colors
    red = Color("#eb0000")
    colors1 = list(red.range_to(Color("#f7e297"),10))
    yellow = Color("#f7e297")
    colors2 = list(yellow.range_to(Color("#f7f9fa"),25))
    white = Color("#f7f9fa")
    colors3 = list(white.range_to(Color("#0051ff"),65))
    finalColors = colors1 + colors2 + colors3
    print(filepath)

    sys.path.insert(0, filepath)
    import Settings # Ignore the warning, it still works.

    if Settings.convertTexturesToDDS == True:
        from wand import image as wImage

    if Settings.fantasyNames == True:
        try:
            synonymCache = open(filepath + "/synonymCache.py", "x", encoding='utf-8')
            from wordhoard import Synonyms
            print("Loading synonyms (1/7).", end="\r")
            synonym = Synonyms(search_string='hot')
            synonym_results_hot = synonym.find_synonyms()
            print("Loading synonyms (2/7).", end="\r")
            synonym = Synonyms(search_string='cold')
            synonym_results_cold = synonym.find_synonyms()
            print("Loading synonyms (3/7).", end="\r")
            synonym = Synonyms(search_string='oceanic')
            synonym_results_oceanic = synonym.find_synonyms()
            print("Loading synonyms (4/7).", end="\r")
            synonym = Synonyms(search_string='rocky')
            synonym_results_rocky = synonym.find_synonyms()
            print("Loading synonyms (5/7).", end="\r")
            synonym = Synonyms(search_string='life')
            synonym_results_life = synonym.find_synonyms()
            print("Loading synonyms (6/7).", end="\r")
            synonym = Synonyms(search_string='dry')
            synonym_results_dry = synonym.find_synonyms()
            print("Loading synonyms (7/7).", end="\r")
            synonym = Synonyms(search_string='bright')
            synonym_results_light = synonym.find_synonyms()
            print("Finished loading synonyms!")
            synonymList = [synonym_results_hot, synonym_results_cold, synonym_results_oceanic, synonym_results_rocky, synonym_results_life, synonym_results_dry, synonym_results_light]
            synonymCache.write("synonyms = " + str(synonymList))
            synonymCache.flush()
        except FileExistsError:
            import synonymCache # Imports the file so that it can be read xdd
            synonymList = synonymCache.synonyms

    # Set all values to zero to prevent weird shenanigans from happening.
    totalStarsGenerated = 0
    totalPlanetsGenerated = 0
    totalMoonsGenerated = 0

    print("Starting generator...")
    # Generates names.
    def generateName(type):
        word1 = synonymList[type][random.randint(0,len(synonymList[type])-1)]
        word1Cut = word1[:-int(len(word1)/2)]
        word2 = synonymList[type][random.randint(0,len(synonymList[type])-1)]
        word2Cut = word2[:int(len(word2)/2)]
        finalWord = word1Cut + word2Cut
        dispName = finalWord.replace(" ", "").replace("-", "").replace("'", "").capitalize()

        return dispName
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
    def addToParallaxCfg(parallaxCfg, planetName):
        parallaxCfg.write(
            "    Body\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        emissive = false\n"
            "        Textures\n"
            "        {\n"
            "            _SurfaceTextureScale = 0.72\n"
            "    \n"
            "            _SurfaceTexture = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1.dds\n"
            "            _SurfaceTextureMid = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1.dds\n"
            "            _SurfaceTextureHigh = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1.dds\n"
            "            _SteepTex = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1.dds\n"
            "    \n"
            "            _BumpMap = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1NRM.dds\n"
            "            _BumpMapMid = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1NRM.dds\n"
            "            _BumpMapHigh = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1NRM.dds\n"
            "            _BumpMapSteep = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1NRM.dds\n"
            "    \n"
            "            _DispTex = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1DSP.dds\n"
            "            _InfluenceMap = InfiniteDiscoveries/Visuals/Parallax/Textures/ground1INF.dds\n"
            "    \n"
            "            _displacement_scale = 0.05\n"
            "            _displacement_offset = 0\n"
            "    \n"
            "            _SteepPower = 14\n"
            "            _SteepContrast = 4\n"
            "            _SteepMidpoint = 0.6\n"
            "    \n"
            "            _Metallic = 0.08\n"
            "            _MetallicTint = 0.6,0.6,0.6\n"
            "            _Gloss = 22\n"
            "            _NormalSpecularInfluence = 1\n"
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
    # Makes EVE aurorae
    def addToEVEAurora(eveCfg, planetName, auroraBright):
        eveCfg.write(
            "    OBJECT\n"
            "    {\n"
            "        name = " + planetName + "_AURORAE" + "\n"
            "        body = " + planetName + "\n"
            "        altitude = 10000\n"
            "        settings\n"
            "        {\n"
            "            _Color = 255,255,255," + str(auroraBright) + "\n"
            "            _UVNoiseScale = 0.79999998\n"
            "            _UVNoiseStrength = 0.010000001\n"
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
            "            }\n"
            "        }\n"
            "    }\n"
        )

    def addPQSFix(evePQSCfg, planetName):
        evePQSCfg.write(
            "    OBJECT"
            "    {"
            "        body = " + planetName + "\n"
            "        deactivateDistance = 175000"
            "    }"
        )

    def addToEVECfg(eveCfg, cloudTexNum, planetName):
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
            "            }\n"
            "        }\n"
            "    }\n"
        )

    def addToOceanCfg(oceanCfg, oceanR, oceanG, oceanB, planetName):
        oceanCfg.write(
            "    Ocean\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        AMP = 4\n"
            "        m_windSpeed = 8\n"
            "        m_omega = 0.699999988\n"
            "        m_gravity = 9.81000042\n"
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

    def addSunflareCfg(sunfCfg, starColor, starName):
        sunfCfg.write(
            "Scatterer_sunflare\n"
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
            "                scaleCurve\n"
            "                {\n"
            "                    key = 0 5 0 -0.200\n"
            "                    key = 55 1.05 -0.007 -0.0012\n"
            "                    key = 2500 0.2 0 0\n"
            "                }\n"
            "                intensityCurve\n"
            "                {\n"
            "                    key = 0 0.0 0 0\n"
            "                    key = 11 0.6 0 0\n"
            "                }\n"
            "            }\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/sunSpikes.png\n"
            "                displayAspectRatio = 1\n"
            "                scaleCurve\n"
            "                {\n"
            "                    key = 0 5 0 -0.200\n"
            "                    key = 55 1.05 -0.007 -0.0012\n"
            "                    key = 2500 0.0 0 0\n"
            "                }\n"
            "                intensityCurve\n"
            "                {\n"
            "                    key = 0 0.0 0 0\n"
            "                    key = 11 0.6 0 0\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        ghosts\n"
            "        {\n"
            "            Item\n"
            "            {\n"
            "                texture = Scatterer/config/Sunflares/Sun/Ghost1.png\n"
            "                intensityCurve\n"
            "                {\n"
            "                    key = 0 0.0 0 0\n"
            "                    key = 11 1 0 0\n"
            "                    key = 500 1 0 0\n"
            "                    key = 2500 0 0 0\n"
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
            "                    key = 0 0 0 0\n"
            "                    key = 11 1 0 0\n"
            "                    key = 500 1 0 0\n"
            "                    key = 2500 0 0 0\n"
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

    def addToScattererList(scattererCfg, starName, planetName, starColor, ocean, colorsRound, binaryParents=None):
        if binaryParents == None:
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
                "            cloudIntegrationUsesScattererSunColors = False\n"
                "            mainSunCelestialBody = " + starName + "\n"
                "            sunColor = " + str(colorsRound) + ", " + str(colorsRound) + ", " + str(colorsRound) + "\n"
                "            sunsUseIntensityCurves = False\n"
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
                "            cloudIntegrationUsesScattererSunColors = False\n"
                "            mainSunCelestialBody = " + binaryParents[0] + "\n"
                "            sunColor = " + str(colorsRound) + ", " + str(colorsRound) + ", " + str(colorsRound) + "\n"
                "            sunsUseIntensityCurves = False\n"
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

    def addToAtmoCfg(atmoCfg, starName, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean):
        atmoCfg.write(
            "    Atmo\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        atmosphereStartRadiusScale = 1\n"
            "        HR = 7.5\n"
            "        HM = 1.79999995\n"
            "        m_betaR = " + str(((sctrClrR/256)/100)) + "," + str(((sctrClrG/256)/100)) + "," + str(((sctrClrB/256)/100)) + "\n"
            "        BETA_MSca = 0.0150000000,0.0150000000,0.0150000000\n"
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
                "        specR = 100\n"
                "        specG = 100\n"
                "        specB = 100\n"
            )
        else:
            atmoCfg.write(
                "        specR = 0\n"
                "        specG = 0\n"
                "        specB = 0\n"
            )

        atmoCfg.write(
        "        shininess = 100\n"
        "        cloudColorMultiplier = 1.1\n"
        "        cloudScatteringMultiplier = 0.100000003\n"
        "        cloudSkyIrradianceMultiplier = 2.2000000007\n"
        "        volumetricsColorMultiplier = 1\n"
        "        EVEIntegration_preserveCloudColors = False\n"
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
        "                postProcessDepth = 0.00999999978\n"
        "                extinctionTint = 0.5\n"
        "            }\n"
        "        }\n"
        "    }\n"
        )

    def genRing(planetName):
        ring1 = Image.open(filepath + "/Presets/" + "Ring" + str(1) + ".png")
        ringOffs1 = ImageChops.offset(ring1, random.randint(0,1024),0)
        bands = ringOffs1.split()
        randomMult = random.randint(1,10)/10
        print(randomMult)
        adj_alpha = bands[3].point(lambda x: int(x * randomMult))
        ringAlph = Image.merge('RGBA', [*bands[:3], adj_alpha])
        ringAlph.save(filepath + "/Textures/PluginData/" + planetName + "_RINGS" + ".png")

    def writeStarCfg(starCfg, starName, starRadius, starMass, starDist, RGBfinal, starDistG, dispName, parentBarycenter=None, period=None, maaoD=None):
        starCfg.write(
            "@Kopernicus:AFTER[Kopernicus]\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + starName + "\n"
            "        cacheFile = InfiniteDiscoveries/Cache/" + starName + ".bin" + "\n"
            "        Template\n"
            "        {\n"
            "            name = Sun\n"
            "        }\n"
        )
        if not parentBarycenter == None:
            starCfg.write(
                "        Properties:NEEDS[!Infinite_DeflateStars]\n"
                "        {\n"
                "            displayName = " + dispName + "^N" + "\n"
                "            radius = " + str(starRadius) + "\n"
                "            mass = " + str(starMass) + "\n"
                "            rotationPeriod = 1063000.6069891\n"
                "            tidallyLocked = false\n"
                "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol!" + "\n"
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
                "        Properties:NEEDS[Infinite_DeflateStars]\n"
                "        {\n"
                "            displayName = " + dispName + "^N" + "\n"
                "            radius = " + str(starRadius/4.2) + "\n"
                "            mass = " + str(starMass) + "\n"
                "            rotationPeriod = 1063000.6069891\n"
                "            tidallyLocked = false\n"
                "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol!" + "\n"
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
                "            referenceBody = " + parentBarycenter + "\n"
                "            color = " + RGBfinal + ", 1\n"
                "            semiMajorAxis = " + str(starDist) + "\n"
                "            inclination = " + str(0) + "\n"
                "            eccentricity = " + str(0) + "\n"
                "            longitudeOfAscendingNode = 0\n"
                "            argumentOfPeriapsis = 0\n"
                "            meanAnomalyAtEpochD = " + str(maaoD) + "\n"
                "            period = " + str(period) + "\n"
                "            epoch = 0\n"
                "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                "        }\n"
            )
        else:
            starCfg.write(
                "        Properties:NEEDS[!Infinite_DeflateStars]\n"
                "        {\n"
                "            displayName = " + dispName + "^N" + "\n"
                "            radius = " + str(starRadius) + "\n"
                "            mass = " + str(starMass) + "\n"
                "            rotationPeriod = 1063000.6069891\n"
                "            tidallyLocked = false\n"
                "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol!" + "\n"
                "            sphereOfInfluence = 336413913169.9\n"
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
                "        Properties:NEEDS[Infinite_DeflateStars]\n"
                "        {\n"
                "            displayName = " + dispName + "^N" + "\n"
                "            radius = " + str(starRadius/4.2) + "\n"
                "            mass = " + str(starMass) + "\n"
                "            rotationPeriod = 1063000.6069891\n"
                "            tidallyLocked = false\n"
                "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol!" + "\n"
                "            sphereOfInfluence = 336413913169.9\n"
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
                "        Orbit:NEEDS[!Infinite_GalaxyMode]\n"
                "        {\n"
                "            referenceBody = Sun\n"
                "            color = " + RGBfinal + ", 1\n"
                "            semiMajorAxis = " + str(starDist) + "\n"
                "            inclination = " + str(random.randint(0,360)) + "\n"
                "            eccentricity = " + str(random.randint(0,500)/1000) + "\n"
                "            longitudeOfAscendingNode = 0\n"
                "            argumentOfPeriapsis = 0\n"
                "            meanAnomalyAtEpochD = " + str(random.randint(0,360)) + "\n"
                "            epoch = 0\n"
                "            mode = OFF\n"
                "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                "        }\n"
                "        Orbit:NEEDS[Infinite_GalaxyMode]\n"
                "        {\n"
                "            referenceBody = Sun\n"
                "            color = " + RGBfinal + ", 1\n"
                "            semiMajorAxis = " + str(starDistG) + "\n"
                "            inclination = " + str(random.randint(0,10)) + "\n"
                "            eccentricity = " + str(random.randint(0,200)/1000) + "\n"
                "            longitudeOfAscendingNode = 0\n"
                "            argumentOfPeriapsis = 0\n"
                "            meanAnomalyAtEpochD = " + str(random.randint(0,360)) + "\n"
                "            epoch = 0\n"
                "            mode = OFF\n"
                "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
                "        }\n"
            )
        
        starCfg.write(
            "        ScaledVersion\n"
            "        {\n"
            "            type = Star\n"
            "            Light:NEEDS[!Infinite_DeflateStars]\n"
            "            {\n"
            "                sunlightColor = " + RGBfinal + ", 1\n"
            "                sunlightShadowStrength = 0.75\n"
            "                scaledSunlightColor = " + RGBfinal + ", 1\n"
            "                IVASunColor = " + RGBfinal + ", 1\n"
            "                sunLensFlareColor = " + RGBfinal + ", 1\n"
            "                givesOffLight = true\n"
            "                sunAU = " + str(13599840256 * (starRadius/261600000)) + "\n"
            "                luminosity = " + str(1360 * starRadius / 261600000) + "\n"
            "                insolation = 0.15\n"
            "                brightnessCurve\n"
            "                {\n"
            "                   key = -0.01573471 0 1.706627 1.706627\n"
            "                   key = 5.084181 5.997075 -0.001802375\n"
            "                   key = 38.56295 10.82142 0.0001713 0.0001713\n"
            "                }\n"
            "                IntensityCurve\n"
            "                {\n"
            "                    key = 0 " + str((starRadius / 261600000)/1.1) + " 0 0\n"
            "   			     key = " + str((60000000000*(starRadius / 261600000))) + " " + str((starRadius / 261600000)/1.5) + " -2E-12 -2E-12\n"
            "   			     key = " + str((120000000000*(starRadius / 261600000))) + " 0 0 0\n"
            "                }\n"
            "                ScaledIntensityCurve\n"
            "                {\n"
            "                   key = 0 " + str((starRadius / 261600000)/1.1) + " 0 0\n"
            "         			key = " + str((10000000*(starRadius / 261600000))) + " " + str((starRadius / 261600000)/1.5) + " -1.2E-08 -1.2E-08\n"
            "                   key = " + str((20000000*(starRadius / 261600000))) + " 0 0 0\n"
            "                }\n"
            "                IVAIntensityCurve\n"
            "                {\n"
            "                   key = 0 " + str((starRadius / 261600000)/1.1) + " 0 0\n"
            "          			key = " + str((60000000000*(starRadius / 261600000))) + " " + str((starRadius / 261600000)/1.5) + " -1.8E-12 -1.8E-12\n"
            "          			key = " + str((120000000000*(starRadius / 261600000))) + " 0 0 0\n"
            "                }\n"
            "            }\n"
            "            Light:NEEDS[Infinite_DeflateStars]\n"
            "            {\n"
            "                sunlightColor = " + RGBfinal + ", 1\n"
            "                sunlightShadowStrength = 0.75\n"
            "                scaledSunlightColor = " + RGBfinal + ", 1\n"
            "                IVASunColor = " + RGBfinal + ", 1\n"
            "                sunLensFlareColor = " + RGBfinal + ", 1\n"
            "                givesOffLight = true\n"
            "                sunAU = " + str((13599840256 * (starRadius/261600000))/4.2) + "\n"
            "                luminosity = " + str(1360 * starRadius / 261600000) + "\n"
            "                insolation = 0.15\n"
            "                brightnessCurve\n"
            "                {\n"
            "                   key = -0.01573471 0 1.706627 1.706627\n"
            "                   key = 5.084181 5.997075 -0.001802375\n"
            "                   key = 38.56295 10.82142 0.0001713 0.0001713\n"
            "                }\n"
            "                IntensityCurve\n"
            "                {\n"
            "                    key = 0 " + str((starRadius / 261600000)/1.1) + " 0 0\n"
            "   			     key = " + str((60000000000*(starRadius / 261600000))) + " " + str((starRadius / 261600000)/1.5) + " -2E-12 -2E-12\n"
            "   			     key = " + str((120000000000*(starRadius / 261600000))) + " 0 0 0\n"
            "                }\n"
            "                ScaledIntensityCurve\n"
            "                {\n"
            "                   key = 0 " + str((starRadius / 261600000)/1.1) + " 0 0\n"
            "         			key = " + str((10000000*(starRadius / 261600000))) + " " + str((starRadius / 261600000)/1.5) + " -1.2E-08 -1.2E-08\n"
            "                   key = " + str((20000000*(starRadius / 261600000))) + " 0 0 0\n"
            "                }\n"
            "                IVAIntensityCurve\n"
            "                {\n"
            "                   key = 0 " + str((starRadius / 261600000)/1.1) + " 0 0\n"
            "          			key = " + str((60000000000*(starRadius / 261600000))) + " " + str((starRadius / 261600000)/1.5) + " -1.8E-12 -1.8E-12\n"
            "          			key = " + str((120000000000*(starRadius / 261600000))) + " 0 0 0\n"
            "                }\n"
            "            }\n"
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
            "                        texture = InfiniteDiscoveries/Textures/Misc/None.dds\n"
            "                        mainTexScale = 1,1\n"
            "                        mainTexOffset = 0,0\n"
            "                        invFade = 2.553731\n"
            "                    }\n"
            "                }\n"
            "            }\n"
            "        }\n"
            "        Atmosphere\n"
            "        {\n"
            "            enabled = true\n"
            "            oxygen = false\n"
            "            ambientColor = 0.716,0.815,0.580,0.1\n"
            "            altitude = 56000\n"
            "            pressureCurveIsNormalized = false\n"
            "            temperatureSeaLevel = 133.33\n"
            "            staticDensityASL = 0.2\n"
            "            staticPressureASL = 30\n"
            "            AtmosphereFromGround\n"
            "            {"
            "                DEBUG_alwaysUpdateAll = False\n"
            "                doScale = False\n"
            "                waveLength = 0.5538463,0.4192308,0.4384614,0.5\n"
            "                samples = 4\n"
            "                innerRadius = 355777.5\n"
            "                outerRadius = 372020.4\n"
            "                innerRadiusMult = 0.9563388\n"
            "                outerRadiusMult = 1.045001\n"
            "                transformScale = 1.095,1.095,1.095\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )

    def writeBarycenterCfg(baryCfg, baryName, baryRadius, baryMass, baryDist, systemName, starColors, baryDistG, baryDispName):
        baryCfg.write(
            "@Kopernicus:AFTER[Kopernicus]\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + baryName + "\n"
            "        cacheFile = InfiniteDiscoveries/Cache/" + baryName + ".bin" + "\n"
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
            "            description = The barycenter of the " + str(systemName) + " system.\n"
            "            sphereOfInfluence = 336413913169.9\n"
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
            "        Orbit:NEEDS[!Infinite_GalaxyMode]\n"
            "        {\n"
            "            referenceBody = Sun\n"
            "            color = " + starColors + ", 1\n"
            "            semiMajorAxis = " + str(baryDist) + "\n"
            "            inclination = " + str(random.randint(0,360)) + "\n"
            "            eccentricity = " + str(random.randint(0,500)/1000) + "\n"
            "            longitudeOfAscendingNode = 0\n"
            "            argumentOfPeriapsis = 0\n"
            "            meanAnomalyAtEpochD = " + str(random.randint(0,360)) + "\n"
            "            epoch = 0\n"
            "            mode = OFF\n"
            "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
            "        }\n"
            "        Orbit:NEEDS[Infinite_GalaxyMode]\n"
            "        {\n"
            "            referenceBody = Sun\n"
            "            color = " + starColors + ", 1\n"
            "            semiMajorAxis = " + str(baryDistG) + "\n"
            "            inclination = " + str(random.randint(0,10)) + "\n"
            "            eccentricity = " + str(random.randint(0,200)/1000) + "\n"
            "            longitudeOfAscendingNode = 0\n"
            "            argumentOfPeriapsis = 0\n"
            "            meanAnomalyAtEpochD = " + str(random.randint(0,360)) + "\n"
            "            epoch = 0\n"
            "            mode = OFF\n"
            "            iconTexture = InfiniteDiscoveries/Textures/Misc/starIcon.png\n"
            "        }\n"
            "        ScaledVersion\n"
            "        {\n"
            "            type = Star\n"
            "            invisible = True\n"
            "            Light\n"
            "            {\n"
            "                givesOffLight = false\n"
            "            }\n"
            "        }\n"
            "    }\n"
            "}\n"
        )

    def writeBodyCfg(planetCfg, planetName, planetRadius, planetMass, planetSMA, parentN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon):
        planetCfg.write(
            "@Kopernicus:AFTER[Kopernicus]\n"
            "{\n"
            "    Body\n"
            "    {\n"
            "        name = " + planetName + "\n"
            "        randomMainMenuBody = true\n"
            "        cacheFile = InfiniteDiscoveries/Cache/" + planetName + ".bin" + "\n"
            "        Template\n"
            "        {\n"
            "            name = " + templates[templ] + "\n"
            "            removeAllPQSMods = true\n"
            "        }\n"
            "        Properties\n"
            "        {\n"
            "            displayName = " + dispName + "^N" + "\n"
            "            radius = " + str(planetRadius) + "\n"
            "            geeASL = " + str(planetRadius/600000) + "\n"
            "            rotationPeriod = " + str(random.randint(360,360000)) + "\n"
        )
        if moon == True:
            planetCfg.write(
                "            tidallyLocked = true\n"
            )
        else:
            planetCfg.write(
                "            tidallyLocked = false\n"
            )
        if atmo == "Atmospheric":
            if life == True:
                planetCfg.write(
                    "            description = " + str(planetName) + " is a randomly generated world roughly " + str(round(planetRadius / 600000, 2)) + " times the size of Kerbin! This world has an oxygenated atmosphere and life!\n"
                )
            else:
                planetCfg.write(
                    "            description = " + str(planetName) + " is a randomly generated world roughly " + str(round(planetRadius / 600000, 2)) + " times the size of Kerbin! This world has an atmosphere with no oxygen.\n"
                )
        else:
            planetCfg.write(
                "            description = " + str(planetName) + " is a randomly generated world roughly " + str(round(planetRadius / 600000, 2)) + " times the size of Kerbin! This world has no atmosphere.\n"
            )
        planetCfg.write(
            "            ScienceValues\n"
            "            {\n"
            "                landedDataValue = 100\n"
            "                flyingLowDataValue = 20\n"
            "                flyingHighDataValue = 20\n"
            "                inSpaceLowDataValue = 20\n"
            "                inSpaceHighDataValue = 5\n"
            "                recoveryValue = 10\n"
            "                flyingAltitudeThreshold = 18000\n"
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
                "                    value = 1.0\n"
                "                    color = RGB(150,200,255)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Oceans\n"
                "                    displayName = Oceans\n"
                "                    value = 1.0\n"
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
                "                    value = 1.0\n"
                "                    color = RGB(255,0,0)\n"
                "                }\n"
                "                Biome\n"
                "                {\n"
                "                    name = Lava\n"
                "                    displayName = Lava\n"
                "                    value = 1.0\n"
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
            "        Orbit\n"
            "        {\n"
            "            referenceBody = " + parentN + "\n"
            "            color = RGBA(" + terrainClr + ")\n"
            "            semiMajorAxis = " + str(planetSMA) + "\n"
            "            inclination = " + str(random.randint(0,10)) + "\n"
            "            eccentricity = " + str(random.randint(0,200)/1000) + "\n"
            "            longitudeOfAscendingNode = 0\n"
            "            argumentOfPeriapsis = 0\n"
            "            meanAnomalyAtEpochD = " + str(random.randint(0,360)) + "\n"
            "            epoch = 0\n"
            "        }\n"
            "        ScaledVersion\n"
            "        {\n"
            "            type = " + atmo + "\n"
            "            Material\n"
            "            {\n"
        )
        if Settings.convertTexturesToDDS == True:
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
                "                specColor = 1, 1, 1, 1\n"
            )
        else:
            planetCfg.write(
                "                specColor = 0, 0, 0, 1\n"
            )
        planetCfg.write(
            "                shininess = 1\n"
            "\n"
            "                rimPower = 5\n"
            "		         rimBlend = 1\n"
            "                Gradient\n"
            "                {\n"
            "                    0.0 = RGBA(" + str(sctrClrR) + ", " + str(sctrClrG) + ", " + str(sctrClrB) + ", 100" + ")\n"
            "                    0.3 = RGBA(" + str(atmClrR) + ", " + str(atmClrG) + ", " + str(atmClrB) + ", 100" + ")\n"
            "                    0.6 = RGBA(" + str(atmClrR/2) + ", " + str(atmClrG/2) + ", " + str(atmClrB/2) + ", 100" + ")\n"
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
            "                tiles = 10\n"
            "                color = 1,1,1,1\n"
            "                unlit = false\n"
            "                useNewShader = true\n"
            "                penumbraMultiplier = 200\n"
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
            "            maxLevel = 6\n"
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
                "            ambientColor = RGBA(" + str(sctrClrR) + ", " + str(sctrClrG) + ", " + str(sctrClrB) + ", 100" + ")\n"
                "            altitude = " + str(atmoHeight) + "\n"
                "            pressureCurveIsNormalized = false\n"
                "            staticPressureASL = " + str(atmoPress) + "\n"
                "            temperatureSeaLevel = " + str(finalTemp) + "\n"
                "            pressureCurve\n"
                "            {\n"
                "                key = " + str(round(0)) + " " +               str(round(atmoPress))        + " -9.40053885714286E-03 -9.40053885714286E-03\n"
                "                key = " + str(round(atmoHeight/20.0)) + " " + str(round(atmoPress/1.289))  + " -9.06132071428572E-03 -9.06132071428572E-03\n"
                "                key = " + str(round(atmoHeight/10.0)) + " " + str(round(atmoPress/1.762))  + " -7.66193321571429E-03 -7.66193321571429E-03\n"
                "                key = " + str(round(atmoHeight/6.66)) + " " + str(round(atmoPress/2.440))  + " -5.75651121285714E-03 -5.75651121285714E-03\n"
                "                key = " + str(round(atmoHeight/5.00)) + " " + str(round(atmoPress/3.418))  + " -4.16994392857143E-03 -4.16994392857143E-03\n"
                "                key = " + str(round(atmoHeight/4.00)) + " " + str(round(atmoPress/4.746))  + " -2.90616120814286E-03 -2.90616100142857E-03\n"
                "                key = " + str(round(atmoHeight/3.33)) + " " + str(round(atmoPress/6.502))  + " -2.14383385714286E-03 -2.14383385714286E-03\n"
                "                key = " + str(round(atmoHeight/2.85)) + " " + str(round(atmoPress/9.229))  + " -1.57375037842857E-03 -1.57375037842857E-03\n"
                "                key = " + str(round(atmoHeight/2.50)) + " " + str(round(atmoPress/12.71))  + " -1.03374362157143E-03 -1.03374362157143E-03\n"
                "                key = " + str(round(atmoHeight/2.22)) + " " + str(round(atmoPress/16.95))  + " -7.27255171714286E-04 -7.27255171714286E-04\n"
                "                key = " + str(round(atmoHeight/2.00)) + " " + str(round(atmoPress/22.75))  + " -5.39731265282876E-04 -5.39731625876128E-04\n"
                "                key = " + str(round(atmoHeight/1.81)) + " " + str(round(atmoPress/30.09))  + " -4.01197907285714E-04 -4.01197907285714E-04\n"
                "                key = " + str(round(atmoHeight/1.66)) + " " + str(round(atmoPress/40.34))  + " -3.32120814571429E-04 -3.32120814571429E-04\n"
                "                key = " + str(round(atmoHeight/1.53)) + " " + str(round(atmoPress/57.58))  + " -2.57703878428571E-04 -2.57703878428571E-04\n"
                "                key = " + str(round(atmoHeight/1.42)) + " " + str(round(atmoPress/80.11))  + " -1.74466857142857E-04 -1.74466857142857E-04\n"
                "                key = " + str(round(atmoHeight/1.33)) + " " + str(round(atmoPress/110.6))  + " -1.36190255014286E-04 -1.36190255014286E-04\n"
                "                key = " + str(round(atmoHeight/1.25)) + " " + str(round(atmoPress/167.0))  + " -1.16655755014286E-04 -1.16655755014286E-04\n"
                "                key = " + str(round(atmoHeight/1.17)) + " " + str(round(atmoPress/288.0))  + " -9.19878571428571E-05 -9.19878571428571E-05\n"
                "                key = " + str(round(atmoHeight/1.11)) + " " + str(round(atmoPress/629.0))  + " -6.40814285714286E-05 -6.40814285714286E-05\n"
                "                key = " + str(round(atmoHeight/1.05)) + " " + str(round(atmoPress/2451))   + " -3.32465407285714E-05 -3.32465407285714E-05\n"
                "                key = " + str(round(atmoHeight/1.00)) + " " + str(round(0))          + " -1.70883816414286E-05 -1.70883816414286E-05\n"
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
            if planetRadius > 300000:
                planetCfg.write(
                    "            maxLevel = 9\n"
                )
            else:
                planetCfg.write(
                    "            maxLevel = 5\n"
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
                "                midTex = BUILTIN/tyloFloorDiffuse\n"
                "                midTexScale = 1,1\n"
                "                midTexOffset = 0,0\n"
                "                midTiling = 150000\n"
                "                midBumpMap = BUILTIN/tyloNRM\n"
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
                "                VertexHeightMap\n"
                "                {\n"
            )
            if Settings.convertTexturesToDDS == True:
                planetCfg.write(
                    "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_HGT" + ".dds" + "\n"
                )
            else:
                planetCfg.write(
                    "                    map = InfiniteDiscoveries/Textures/PluginData/" + planetName + "_HGT" + ".png" + "\n"
                )
            if ocean == True:
                planetCfg.write(
                    "                    offset = -1300\n"   
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
            if Settings.convertTexturesToDDS == True:
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
                "                VertexHeightNoiseVertHeightCurve2\n"
                "                {\n"
                "                    deformity = 2000\n"
                "                    ridgedAddFrequency = 32\n"
                "                    ridgedAddLacunarity = 2\n"
                "                    ridgedAddOctaves = 8\n"
                "                    ridgedAddSeed = 456352342\n"
                "                    ridgedMode = Low\n"
                "                    ridgedSubFrequency = 32\n"
                "                    ridgedSubLacunarity = 2\n"
                "                    ridgedSubOctaves = 8\n"
                "                    ridgedSubSeed = 234352\n"
                "                    simplexFrequency = 24\n"
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
        planetCfg.write(
            "    }\n"
            "}\n"
        )
        
    def GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, kpaASL, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano):
        albedoMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
        def convertToBiomeFeature(featureMap, colour, brighten1):
            biomeFeature = Image.new("RGBA", (4096,2048), colour)
            biomeFeature.putalpha(ImageEnhance.Brightness(ImageOps.posterize(ImageEnhance.Brightness((featureMap.getchannel("A"))).enhance(brighten1), 1)).enhance(2))
            biomeMap.paste(biomeFeature, (0,0), mask=biomeFeature)
        def add_Surface_Features(noiseImg, type, amount, alphaAdd, minMax, types, mean, std_dev, albedo=None):
            featureMap = Image.new("RGBA", (4096,2048), (0,0,0,0))
            minSize = minMax[0]
            maxSize = minMax[1]
            for i in range(0,amount):
                feature = Image.open(filepath + "/Presets/" + type + str(random.randint(1,types)) + ".png")
                featureSizeInt = int(np.random.normal(mean, std_dev))
                featureSize = max(minSize, min(maxSize, featureSizeInt))
                featurePreRes = feature.resize((featureSize,featureSize))
                featureA = featurePreRes.getchannel("A")
                alpha1 = Image.new("L", (featureSize, featureSize), (alphaAdd))
                featureA2 = ImageChops.multiply(alpha1,featureA)
                featurePreRes.putalpha(featureA2)

                print("Generating " + type + " " + str(i) + "...", end="\r")

                offs1 = random.randint(0,4096-featureSize)
                offs2 = random.randint(0,2048)
                #print(str(offs1) + " " + str(offs2))
                dist = (((offs2/2048)*2)*90)-90
                distCos = math.cos(math.radians(dist))
                featureRot = featurePreRes.rotate(random.randint(0,360))
                featureRes = featureRot.resize((featureSize,math.ceil(featureSize*distCos)))
                
                featureMap.paste(featureRes, (int(offs1),int(offs2-featureSize//2)), mask=featureRes)

                if not albedo == None:
                    albFeature = Image.open(filepath + "/Presets/" + albedo + str(random.randint(1,types)) + ".png")
                    albFeaturePreRes = albFeature.resize((featureSize,featureSize))
                    albFeatureA = albFeaturePreRes.getchannel("A")
                    albAlpha1 = Image.new("L", (featureSize, featureSize), (200))
                    albFeatureA2 = ImageChops.multiply(albAlpha1,albFeatureA)
                    albFeaturePreRes.putalpha(albFeatureA2)
                    albFeatureRot = albFeaturePreRes.rotate(random.randint(0,360))
                    albFeatureRes = albFeatureRot.resize((featureSize,math.ceil(featureSize*distCos)))
                    albedoMap.paste(albFeatureRes, (int(offs1),int(offs2-featureSize//2)), mask=albFeatureRes)
            noiseImg.paste(featureMap, (0,0), featureMap)
            if not albedo == None:
                return featureMap, albedoMap
            else:
                return featureMap

        print("Generating noise...")
        texStartTime = time.time()
        seed = random.randint(0,10000)
        size = 1024
        radius = 1.0
        octaves = Settings.noiseOctaves
        lacunarity = Settings.noiseLacunarity
        persistence = 0.5
        heightmap = np.zeros((size, size))
        freq_random = random.randint(Settings.noiseFrequencyMin,Settings.noiseFrequencyMax)/10
        for i in range(size):
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

        heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
        image = Image.fromarray((heightmap * 255).astype(np.uint8), mode='L')
        image90 = image.rotate(90)
        imageRes = image90.resize((4096,2048), resample=Image.Resampling.BICUBIC)
        brtAmount = random.randint(50,100)/100
        contrAmount = 1/brtAmount
        imageContr = ImageEnhance.Contrast(ImageEnhance.Brightness(imageRes).enhance(brtAmount)).enhance(contrAmount)
        texEndTime = time.time()
        noiseEndTime = texEndTime-texStartTime
        print("Finished generating noise. Time elapsed: " + str(noiseEndTime) + " seconds.")

        # For future me. The function (in order) takes the Original Image, decal name, amount, alpha, min/max size, variants, mean, standard deviation, and an optional albedo feature.
        if kpaASL < 35:
            if planetRadius < 50000 and planetRadius > 20000:
                large_craterMap = add_Surface_Features(imageContr, "crater", 100, 200, [200,800], 2, 200, 200)
            elif planetRadius > 50000:
                craterMap = add_Surface_Features(imageContr, "crater", 600, 150, [50,800], 2, 100, 100)
            if planetRadius > 75000 and ocean == False:
                ray_craterMap, ray_albedoMap = add_Surface_Features(imageContr, "rayCrater", 200, 150, [100,700], 1, 100, 200, "rayCrater_alb")
        if geoActive == True and planetRadius > 80000:
            volcanoMap = add_Surface_Features(imageContr, "volcano", 200, 200, [50,200], 1, 50, 100)
            if activeVolcano == True:
                activeVolcanoMap, lavaAlbedoMap = add_Surface_Features(imageContr, "volcano", 100, 200, [200,300], 1, 50, 100, "volcano_Lava")
            canyonMap = add_Surface_Features(imageContr, "canyon", 400, 125, [50,400], 2, 50, 100)
        if vacuum == False and planetRadius > 30000:
            mountainMap = add_Surface_Features(imageContr, "mountain", 400, 175, [50,600], 3, 50, 300)
        
        if icecaps == True:
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
            imageContr.paste(icecap_img, (0,0), mask=icecap_img)

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
        nrm_Patch = Image.open(filepath + "/Presets/" + "normalPatch.png")
        img_normalFilter.paste(nrm_Patch, (0,0), mask=nrm_Patch)
        texEndTime = time.time()
        nrmEndTime = texEndTime-texStartTime
        print("Finished generating normals. Time elapsed: " + str(nrmEndTime) + " seconds.")

        ImageResFilter = imageContr.filter(ImageFilter.SMOOTH_MORE)

        print("Generating color...")
        texStartTime = time.time()

        grayMap = ImageOps.grayscale(ImageResFilter)
        if life == True:
            randomB_R = plantColor[0]*255
            randomB_G = plantColor[1]*255
            randomB_B = plantColor[2]*255
            randomM_R = random.randint(Settings.LIFE_M_RedMin,Settings.LIFE_M_RedMax)
            randomM_G = random.randint(Settings.LIFE_M_GreenMin,Settings.LIFE_M_GreenMax)
            randomM_B = random.randint(Settings.LIFE_M_BlueMin,Settings.LIFE_M_BlueMax)
            randomW_R = random.randint(Settings.LIFE_W_RedMin,Settings.LIFE_W_RedMax)
            randomW_G = random.randint(Settings.LIFE_W_GreenMin,Settings.LIFE_W_GreenMax)
            randomW_B = random.randint(Settings.LIFE_W_BlueMin,Settings.LIFE_W_BlueMax)
        elif life == False and ocean == True:
            randomB_R = random.randint(Settings.OCEAN_B_RedMin,Settings.OCEAN_B_RedMax)
            randomB_G = random.randint(Settings.OCEAN_B_GreenMin,Settings.OCEAN_B_GreenMax)
            randomB_B = random.randint(Settings.OCEAN_B_BlueMin,Settings.OCEAN_B_BlueMax)
            randomM_R = random.randint(Settings.OCEAN_M_RedMin,Settings.OCEAN_M_RedMax)
            randomM_G = random.randint(Settings.OCEAN_M_GreenMin,Settings.OCEAN_M_GreenMax)
            randomM_B = random.randint(Settings.OCEAN_M_BlueMin,Settings.OCEAN_M_BlueMax)
            randomW_R = random.randint(Settings.OCEAN_W_RedMin,Settings.OCEAN_W_RedMax)
            randomW_G = random.randint(Settings.OCEAN_W_GreenMin,Settings.OCEAN_W_GreenMax)
            randomW_B = random.randint(Settings.OCEAN_W_BlueMin,Settings.OCEAN_W_BlueMax)
        else:
            randomB_R = random.randint(Settings.OTHER_B_RedMin,Settings.OTHER_B_RedMax)
            randomB_G = random.randint(Settings.OTHER_B_GreenMin,Settings.OTHER_B_GreenMax)
            randomB_B = random.randint(Settings.OTHER_B_BlueMin,Settings.OTHER_B_BlueMax)
            randomM_R = terrainR
            randomM_G = terrainG
            randomM_B = terrainB
            randomW_R = random.randint(Settings.OTHER_W_RedMin,Settings.OTHER_W_RedMax)
            randomW_G = random.randint(Settings.OTHER_W_GreenMin,Settings.OTHER_W_GreenMax)
            randomW_B = random.randint(Settings.OTHER_W_BlueMin,Settings.OTHER_W_BlueMax)
        print(str(randomB_R) + " " + str(randomB_G) + " " + str(randomB_B))
        print(str(randomM_R) + " " + str(randomM_G) + " " + str(randomM_B))
        print(str(randomW_R) + " " + str(randomW_G) + " " + str(randomW_B))
        if life == False:
            blackP = random.randint(0,85)
            midP = random.randint(85,150)
            whiteP = random.randint(150,200)
        else:
            blackP = random.randint(0,74)
            midP = random.randint(150,200)
            whiteP = random.randint(200,255)
        colorMap = ImageOps.colorize(grayMap, (randomB_R,randomB_G,randomB_B), (randomW_R,randomW_G,randomW_B), (randomM_R,randomM_G,randomM_B), blackpoint=blackP, midpoint=midP, whitepoint=whiteP)

        if ocean == True:
            brightFac = float(random.randint(1,500)/100)

            print("Ocean exists! Dryness factor is " + str(brightFac))

            brghtHeight = ImageEnhance.Brightness(ImageResFilter).enhance(brightFac)
            contrHeight = ImageEnhance.Contrast(brghtHeight).enhance(1000)
            posted = ImageOps.posterize(contrHeight.convert("RGB"),2)
            brightFinal = ImageEnhance.Brightness(posted).enhance(100)
            oceanRGBA = brightFinal.convert("RGBA")
            oceanInv = ImageOps.invert(brightFinal).convert("RGBA")
            ocInvL = oceanInv.convert("L")
            oceanRGBA.putalpha(ocInvL)
            oceanBlurA = oceanInv.filter(ImageFilter.GaussianBlur(5)).convert("L")
            heightOcean = Image.new("RGBA", (4096,2048), (0,0,0))
            heightOcean.putalpha(oceanBlurA)
            ImageResFilter.paste(heightOcean, (0,0), mask=heightOcean)

            normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
            normalOcean.putalpha(ocInvL)
            img_normalFilter.paste(normalOcean, (0,0), mask=ocInvL)

            beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
            beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
            beachColor.putalpha(beachMask)
            colorMap.paste(beachColor, (0,0), mask=beachColor)
            colorOcean = Image.new("RGBA", (4096,2048), (oceanR,oceanG,oceanB))
            colorOcean.putalpha(ocInvL)
            colorMap.paste(colorOcean, (0,0), mask=colorOcean)
            if icecaps == True:
                icecap_alph = icecap_img.getchannel("A")
                icecap_inv = ImageOps.invert(icecap_img.convert("RGB"))
                icecap_inv.putalpha(icecap_alph)
                ocInvL.paste(icecap_inv, (0,0), mask=icecap_inv)
                colorMap.paste(icecap_img, (0,0), mask=icecap_img)
                colorMap.putalpha(ocInvL)
            else:
                colorMap.putalpha(ocInvL)
        elif icecaps == True and ocean == False:
            colorMap.paste(icecap_img, (0,0), mask=icecap_img)

        nR,nG,nB,nA = img_normalFilter.convert("RGBA").split()
        nRinv = ImageOps.invert(nR)
        nRbl = Image.new("L", (4096,2048), (255))
        img_normal_Final = Image.merge("RGBA", (nRbl,nG,nB,nRinv))
        
        if life == False:
            colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.25)).enhance(1.5)
        else:
            colorMap_Filter = ImageEnhance.Brightness(ImageEnhance.Color(colorMap).enhance(0.75)).enhance(0.75)

        colorMap_Filter.paste(albedoMap, (0,0), mask=albedoMap)
        
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

        if Settings.convertTexturesToDDS == True:
            img_normal_FinalFlip = img_normal_Final.transpose(Image.FLIP_TOP_BOTTOM)
            ImageResFilterFlip = ImageResFilter.transpose(Image.FLIP_TOP_BOTTOM)
            colorMap_FilterFlip = colorMap_Filter.transpose(Image.FLIP_TOP_BOTTOM)

            biomeMap.save(filepath + "/Textures/PluginData/" + planetName + "_BIO" + ".png")
            img_normal_FinalFlip.save(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
            ImageResFilterFlip.save(filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")
            colorMap_FilterFlip.save(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
        else:
            biomeMap_Flip = biomeMap.transpose(Image.FLIP_TOP_BOTTOM)

            biomeMap_Flip.save(filepath + "/Textures/PluginData/" + planetName + "_BIO" + ".png")
            img_normal_Final.save(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
            ImageResFilter.save(filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")
            colorMap_Filter.save(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
        
        texEndTime = time.time()
        clrEndTime = texEndTime-texStartTime
        print("Finished generating colors. Time elapsed: " + str(clrEndTime) + " seconds.")

        print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime) + " seconds.")
        if Settings.convertTexturesToDDS == True:
            print("Converting maps to DDS for " + planetName + "...")
            texStartTime = time.time()

            #finalHeight2 = finalHeight.transpose(Image.FLIP_TOP_BOTTOM)
            hgtConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")
            hgtConv.options['dds:mipmaps'] = '0'
            hgtConv.compression = 'dxt5'
            hgtConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".dds")
            os.remove(filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")

            nrmConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
            #nrmConv.options['dds:mipmaps'] = '0'
            nrmConv.compression = 'dxt5'
            nrmConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".dds")
            os.remove(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")

            clrConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
            clrConv.options['dds:mipmaps'] = '0'
            clrConv.compression = 'dxt5'
            clrConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".dds")
            os.remove(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
            texEndTime = time.time()
            ddsEndTime = texEndTime-texStartTime
            print("Finished coverting maps to dds. Time elapsed: " + str(ddsEndTime) + " seconds.")

            print("Finished generating maps! Total time elapsed: " + str(noiseEndTime + nrmEndTime + clrEndTime + ddsEndTime) + " seconds.")

    def generateGasGiantMaps(terrainR, terrainG, terrainB, planetName):
        texStartTime = time.time()
        print("Generating noise...")
        texStartTime = time.time()
        seed = random.randint(0,1000)
        size = 1024
        radius = 1.0
        octaves = 1
        lacunarity = 2.0
        persistence = 0.5
        heightmap = np.zeros((size, size))
        for i in range(size):
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
                frequency = 10
                amplitude = 1.0
                for k in range(octaves):
                    noise_value += amplitude * noise.snoise4(x * frequency, y * frequency, z * frequency, seed)
                    frequency *= lacunarity
                    amplitude *= persistence

                # Store the noise value in the heightmap
                heightmap[i, j] = noise_value

        heightmap = (heightmap - heightmap.min()) / (heightmap.max() - heightmap.min())
        image = Image.fromarray((heightmap * 255).astype(np.uint8), mode='L')
        image90 = image.rotate(90)
        imageRes = image90.resize((4096,2048), resample=Image.Resampling.BICUBIC)
        noiseFinal = imageRes.convert("RGBA")
        
        print("Finished generating noise!                          ")

        mainImg = Image.new("RGBA", (4096,2048), (0,0,0,255))
        color = [terrainR,terrainG,terrainB]
        for i in range(0,1500):
            print("Adding band " + str(i), end="\r")
            mult = random.randint(66,133)/100
            bandSizeInt = int(np.random.normal(5, 25))
            rand = max(5, min(50, bandSizeInt))
            bar = Image.new("RGBA", (4096,rand), (int(color[0]*mult),int(color[1]*mult),int(color[2]*mult),255))
            mainImg.paste(bar, (0,random.randint(0,2048)), mask=bar)

        mainImgPreBlur = mainImg.filter(ImageFilter.GaussianBlur(1))

        blurred_map_img = noiseFinal.filter(ImageFilter.GaussianBlur(radius=2))
        # Get the pixel access objects for both images
        img_pixels = mainImgPreBlur.load()
        map_pixels = blurred_map_img.load()
        # Define the displacement amount (in pixels)
        displacement = 1
        # Loop through each pixel in the image
        for y in range(mainImgPreBlur.size[1]):
            print("Calculating deformity for pixel row " + str(y), end="\r")
            for x in range(mainImg.size[0]):
                # Get the displacement value from the map image
                map_value = map_pixels[x, y][0]  # Use the first channel of the map image

                # Calculate the new x-coordinate with the displacement value
                new_y = y + (map_value - 16) * displacement / 16

                # Get the pixel value from the original image at the new coordinates
                try:
                    pixel = img_pixels[x, new_y]
                except IndexError:
                    pixel = (color[0], color[1], color[2])

                # Set the pixel value in the displaced image
                img_pixels[x, y] = pixel
        print("Finished generating gas giant textures!             ")
        mainImgEnh = ImageEnhance.Sharpness(mainImgPreBlur).enhance(10)
        mainImgBlur = mainImgEnh.filter(ImageFilter.GaussianBlur(3))

        ggNrm = Image.new("RGBA", (4096,2048), (128,128,255))

        print("Added normals for gas giant " + planetName + "!")
        nR,nG,nB,nA = ggNrm.split()
        ggNrm.putalpha(nR)

        ggNrm.save(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
        mainImgBlur.save(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")

        if Settings.convertTexturesToDDS == True:
            print("Converting maps to dds for gas giant " + planetName + "...")

            nrmConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
            nrmConv.compression = 'dxt5'
            nrmConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".dds")
            os.remove(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")

            clrConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
            clrConv.options['dds:mipmaps'] = '0'
            clrConv.compression = 'dxt5'
            clrConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".dds")
            os.remove(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")

            print("Converted maps to dds for gas giant " + planetName + "!")

        texEndTime = time.time()
        print("Finished coverting maps to dds. Time elapsed: " + str(texEndTime-texStartTime) + " seconds.")

    def generateMoon(parentPlanet, moonsGenerated, parentRadius, gasGiantP, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, parentSMA, starRadius, parallaxCfg, subdfixCfg, binaryParents=None):
        print(moonsGenerated)
        planetName = parentPlanet + "-" + str(moonsGenerated)
        global totalMoonsGenerated
        totalMoonsGenerated = totalMoonsGenerated + 1
        print(planetName)
        if gasGiantP == True:
            planetRadius = random.randint(50,700)*1000
        else:
            planetRadius = (parentRadius*random.randint(5,10)/10)/2
        gasGiant = False
        planetMass = planetRadius * 8.8191931e+16
        planetSMA = (random.randint(3300000,5000000)*moonsGenerated)*(parentRadius/600000)
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
            atmoPress = random.randint(1,500)*((planetRadius/600000)*0.5)
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
        finalTemp = round(287*starLumMult*smaMult)
        if atmo == "Atmospheric":
            if gasGiant == False:
                if random.randint(1,3) == 1:
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

        if atmo == "Atmospheric":
            if finalTemp > 223 and finalTemp < 373 and gasGiant == False and ocean == True:
                life = True
                oxygen = True
                atmClrR = random.randint(100,200)
                atmClrG = random.randint(75,150)
                atmClrB = random.randint(0,50)
            else:
                oxygen = False
                life = False
                atmClrR = random.randint(0,200)
                atmClrG = random.randint(0,200)
                atmClrB = random.randint(0,200)
            sctrClrR = (atmClrR*-1)+255
            sctrClrG = (atmClrG*-1)+255
            sctrClrB = (atmClrB*-1)+255
        else:
            oxygen = False
            life = False

        if Settings.fantasyNames == True:
            if atmo == "Atmospheric":
                if finalTemp > 600:
                    dispName = generateName(0)
                elif finalTemp < 100:
                    dispName = generateName(1)
                elif ocean == True:
                    if life == True:
                        dispName = generateName(4)
                    else:
                        dispName = generateName(2)
                else:
                    dispName = generateName(5)
            else:
                dispName = generateName(3)
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

        oceanR = random.randint(10,75)
        oceanG = random.randint(10,75)
        oceanB = random.randint(10,75)

        moon = True

        terrainR = random.randint(50,175)
        terrainG = random.randint(50,175)
        terrainB = random.randint(50,175)

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

        if gasGiant == False:
            addSubdividerFix(subdfixCfg, planetName)
            addToParallaxCfg(parallaxCfg, planetName)

        terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"

        print("-------Physical Values-------")
        print("Radius: " + str(planetRadius))
        print("Mass: " + str(planetMass))
        print("Semimajor Axis: " + str(planetSMA))
        print("Terrain tint: " + str(terrainClr))
        if life == True:
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
        planetCfg = open(filepath + "/Configs/" + planetName + "-" + str(moonsGenerated) + ".cfg","x")
        if random.randint(1,2) == 1:
            geoActive = True
            if random.randint(1,2) == 1:
                activeVolcano = True
            else:
                activeVolcano = False
        else:
            geoActive = False
            activeVolcano = False
        GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, atmoPress, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano)

        ringInn = 2000
        ringOut = 2001
        rings = False

        atmoHeight = random.randint(50,90)*1000

        if ocean == True:
            addToOceanCfg(oceanCfg, oceanR, oceanG, oceanB, planetName)

        if atmo == "Atmospheric":
            addToAtmoCfg(atmoCfg, starN, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean)
            if binaryParents == None:
                addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound)
            else:
                addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound, binaryParents)
            if gasGiant == False:
                if ocean == True or random.randint(1,2) == 1:
                    cloudTexNum = random.randint(1,5)
                    addToEVECfg(eveCfg, cloudTexNum, planetName)

        writeBodyCfg(planetCfg, planetName, planetRadius, planetMass, planetSMA, parentPlanet, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon)

    def generate(starN,starRadius,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,Lum,parallaxCfg,subdfixCfg,evePQSCfg,binaryParents=None):
        print(planetsGenerated)
        moonsGenerated = 0
        global totalPlanetsGenerated
        totalPlanetsGenerated = totalPlanetsGenerated + 1
        if planetsGenerated > 1:
            moonAmount = math.floor(np.clip(scipy.stats.gamma.rvs(*Settings.moonDistributionArgs), Settings.minMoons, AmountOfMoonsToGenerate))
        else:
            moonAmount = 0
        planetName = starN + "-" + alphabet[planetsGenerated]
        print(planetName)
        print("Number Of Moons For " + planetName + ": " + str(moonAmount))
        #gasGiant = False
        if random.randint(1,3) == 1:
            planetRadius = random.randint(100,800)*10000
            gasGiant = True
        else:
            planetRadius = random.randint(50,800)*1000
            gasGiant = False
        planetMass = planetRadius * 8.8191931e+16
        planetSMA = (random.randint(4500000000,5500000000)*planetsGenerated)*(starRadius/261600000)
        
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
            atmoPress = random.randint(1,500)*((planetRadius/600000)*0.5)
        else:
            atmo = "Vacuum"
            vacuum = True
                
        starLum = Lum
        starLumMult = starLum/1360
        smaMult = 13599840256/planetSMA
        finalTemp = round(287*starLumMult*smaMult)
        if atmo == "Atmospheric":
            if gasGiant == False:
                if finalTemp > 100 and finalTemp < 600:
                    if random.randint(1,2) == 1:
                        ocean = True
                    else:
                        ocean = False
                else:
                    ocean = False
            else:
                ocean = False
        else:
            ocean = False

        if atmo == "Atmospheric":
            if finalTemp > 223 and finalTemp < 373 and gasGiant == False and ocean == True:
                life = True
                oxygen = True
                atmClrR = random.randint(100,200)
                atmClrG = random.randint(75,150)
                atmClrB = random.randint(0,50)
            else:
                oxygen = False
                life = False
                atmClrR = random.randint(0,200)
                atmClrG = random.randint(0,200)
                atmClrB = random.randint(0,200)
            sctrClrR = (atmClrR*-1)+255
            sctrClrG = (atmClrG*-1)+255
            sctrClrB = (atmClrB*-1)+255
        else:
            oxygen = False
            life = False

        if Settings.fantasyNames == True:
            if atmo == "Atmospheric":
                if finalTemp > 600:
                    dispName = generateName(0)
                elif finalTemp < 100:
                    dispName = generateName(1)
                elif ocean == True:
                    if life == True:
                        dispName = generateName(4)
                    else:
                        dispName = generateName(2)
                else:
                    dispName = generateName(5)
            else:
                dispName = generateName(3)
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

        oceanR = random.randint(10,75)
        oceanG = random.randint(10,75)
        oceanB = random.randint(10,75)

        moon = False
        
        if gasGiant == True:
            terrainR = random.randint(50,255)
            terrainG = random.randint(50,255)
            terrainB = random.randint(50,255)

            terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"
        else:
            terrainR = random.randint(50,175)
            terrainG = random.randint(50,175)
            terrainB = random.randint(50,175)

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

        print("-------Physical Values-------")
        print("Radius: " + str(planetRadius))
        print("Mass: " + str(planetMass))
        print("Semimajor Axis: " + str(planetSMA))
        print("Terrain tint: " + str(terrainClr))
        if life == True:
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

        if random.randint(1,2) == 1:
            geoActive = True
            if random.randint(1,2) == 1:
                activeVolcano = True
            else:
                activeVolcano = False
        else:
            geoActive = False
            activeVolcano = False

        planetCfg = open(filepath + "/Configs/" + planetName + ".cfg","x")
        if gasGiant == True:
            generateGasGiantMaps(terrainR, terrainG, terrainB, planetName)
        else:
            GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB, atmoPress, geoActive, icecaps, finalTemp, life, plantColor, planetRadius, anomaly, anLatLon, activeVolcano)
        
        if random.randint(1,3) == 1:
            print("RINGS!")
            print("-------------------------------")
            rings = True
            genRing(planetName)
            ringInn = random.randint(1000,4000)
            ringOut = ringInn + random.randint(100,3000)
        else:
            rings = False
            ringInn = 2000
            ringOut = 2001

        atmoHeight = random.randint(50,90)*1000

        if ocean == True:
            addToOceanCfg(oceanCfg, oceanR, oceanG, oceanB, planetName)

        if atmo == "Atmospheric":
            addToAtmoCfg(atmoCfg, starN, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean)
            if binaryParents == None:
                addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound)
            else:
                addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound, binaryParents)
            if gasGiant == False:
                if ocean == True or random.randint(1,2) == 1:
                    cloudTexNum = random.randint(1,5)
                    addToEVECfg(eveCfg, cloudTexNum, planetName)
                if atmoPress > 10:
                    auroraBright = random.randint(50,255)
                    addToEVEAurora(eveCfg, planetName, auroraBright)
            else:
                auroraBright = random.randint(50,255)
                addPQSFix(evePQSCfg, planetName)
                addToEVEAurora(eveCfg, planetName, auroraBright)

        if gasGiant == False:
            addSubdividerFix(subdfixCfg, planetName)
            addToParallaxCfg(parallaxCfg, planetName)

        writeBodyCfg(planetCfg, planetName, planetRadius, planetMass, planetSMA, starN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon)
        for a in range(moonAmount):
            moonsGenerated = moonsGenerated + 1
            if binaryParents == None:
                generateMoon(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg)
            else:
                generateMoon(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA, starRadius, parallaxCfg, subdfixCfg, binaryParents)

    def generateStar(AmountOfPlanetsToGenerate, systemName, parentBarycenter=None, binarySMA=None, binaryP=None, binaryRad=None, maaoD=None, baryOrder=None):
        print(parentBarycenter)
        if parentBarycenter == None:
            planetsNum = random.randint(Settings.minPlanets,AmountOfPlanetsToGenerate)
            global planetsGenerated
            planetsGenerated = 0
        print(binaryRad)
        global totalStarsGenerated
        totalStarsGenerated = totalStarsGenerated + 1
        if parentBarycenter == None:
            starName = str(alphabet[random.randint(0,len(alphabet)-1)]) + str(alphabet[random.randint(0,len(alphabet)-1)]) + "-" + str(random.randint(0,99999))
            print(starName)
            if Settings.fantasyNames == True:
                dispName = generateName(6)
                print("Display name for " + starName + " is " + dispName)
            else:
                dispName = starName
        else:
            starName = systemName + baryOrder
            print(starName)
            if Settings.fantasyNames == True:
                dispName = generateName(6)
                print("Display name for " + starName + " is " + dispName)
            else:
                dispName = starName
        if parentBarycenter == None:
            print("Number Of Planets For " + starName + ": " + str(planetsNum))
        min = Settings.minStarSize
        max = Settings.maxStarSize

        if parentBarycenter == None:
            starRadius = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
            starMass = starRadius * 6.7146251e+19
            starDist = random.randint(Settings.minStarDistance,Settings.maxStarDistance)
            starDistG = random.randint(Settings.minStarDistance/5,Settings.maxStarDistance)
        else:
            starRadius = binaryRad
            starMass = binaryRad * 6.7146251e+19
            starDist = binarySMA
            starDistG = binarySMA

        Mult = starRadius*10 / 261600000
        multRound = round(Mult)
        print(len(finalColors))
        print("Star color multiplier is " + str(Mult) + ".")
        print(str(starName) + "is " + str(starRadius / 261600000) + " times the size of Kerbol!")
        starColor = Color.get_rgb(finalColors[multRound-1])
        RGBfinal = str(starColor)[1:][:-1]

        Lum = 1360 * starRadius / 261600000

        print("Star color is: " + str(RGBfinal))

        colorsRound = (starColor[0] + starColor[1] + starColor[2])/3

        print(starColor)
        print(colorsRound)

        starCfg = open(filepath + "/Configs/" + starName + ".cfg","x")
        if parentBarycenter == None:
            writeStarCfg(starCfg, starName, starRadius, starMass, starDist, RGBfinal, starDistG, dispName)
        else:
            writeStarCfg(starCfg, starName, starRadius, starMass, starDist, RGBfinal, starDistG, dispName, parentBarycenter, binaryP, maaoD)

        if parentBarycenter == None:
            listCfg = open(filepath + "/Visuals/Scatterer/" + starName + "_ScattererList" + ".cfg","x")
            listCfg.write(
                "@Scatterer_planetsList:FINAL\n"
                "{\n"
                "    @scattererCelestialBodies\n"
                "    {\n"
            )
            atmoCfg = open(filepath + "/Visuals/Scatterer/" + starName + "_ScattererAtmo" + ".cfg","x")
            atmoCfg.write(
                "Scatterer_atmosphere\n"
                "{\n"
            )
            oceanCfg = open(filepath + "/Visuals/Scatterer/" + starName + "_ScattererOcean" + ".cfg","x")
            oceanCfg.write(
                "Scatterer_ocean\n"
                "{\n"
            )
            eveCfg = open(filepath + "/Visuals/EVE/Configs/" + starName + "_EVE" + ".cfg","x")
            eveCfg.write(
                "EVE_CLOUDS\n"
                "{\n"
            )
            evePQSCfg = open(filepath + "/Visuals/EVE/Configs/" + starName + "_PQSFIX" + ".cfg","x")
            evePQSCfg.write(
                "PQS_MANAGER\n"
                "{\n"
            )
            parallaxCfg = open(filepath + "/Visuals/Parallax/Configs/" + starName + "_PARALLAX" + ".cfg","x")
            parallaxCfg.write(
                "Parallax\n"
                "{\n"
            )
            parallax_subd_Cfg = open(filepath + "/Visuals/Parallax/Configs/" + starName + "_PARALLAX_SUBDFIX" + ".cfg","x")
            parallax_subd_Cfg.write(
                "@Kopernicus:FOR[ParallaxStock]:NEEDS[Parallax]\n"
                "{\n"
            )

            sunfCfg = open(filepath + "/Visuals/Scatterer/" + starName + "_ScattererSunflare" + ".cfg","x")
            addSunflareCfg(sunfCfg, starColor, starName)

            for x in range(planetsNum):
                planetsGenerated = planetsGenerated + 1
                generate(starName,starRadius,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,Lum,parallaxCfg,parallax_subd_Cfg,evePQSCfg)
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
            evePQSCfg.write(
                "}\n"
            )
            parallaxCfg.write(
                "}\n"
            )
            parallax_subd_Cfg.write(
                "}\n"
            )
        return starColor, starName, dispName

    def generateBarycenter(AmountOfPlanetsToGenerate):
        planetsNum = math.floor(np.clip(scipy.stats.gamma.rvs(*Settings.planetDistributionArgs), Settings.minMoons, AmountOfPlanetsToGenerate))
        global planetsGenerated
        planetsGenerated = 0
        systemName = str(alphabet[random.randint(0,len(alphabet)-1)]) + str(alphabet[random.randint(0,len(alphabet)-1)]) + "-" + str(random.randint(0,99999))

        print(systemName)
        print("Number Of Planets For " + systemName + ": " + str(planetsNum))
        min = Settings.minStarSize
        max = Settings.maxStarSize

        star1Radius = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
        star1Mass = star1Radius * 6.7146251e+19
        star2Radius = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
        star2Mass = star2Radius * 6.7146251e+19

        barycenterMass = star1Mass + star2Mass
        barycenterRadius = (star1Radius + star2Radius) / 2
        barycenterDist = random.randint(Settings.minStarDistance,Settings.maxStarDistance)
        barycenterDistG = random.randint(Settings.minStarDistance/5,Settings.maxStarDistance)
        if star1Mass > star2Mass:
            ML = star1Mass # Larger object mass.
            MS = star2Mass # Smaller object mass.
        else:
            ML = star2Mass # Larger object mass.
            MS = star1Mass # Smaller object mass.
        gSMA = random.randint(300000000,900000000) # Distance between both bodies in meters.
        diff = ML/MS
        # math lol
        gSMA_km = gSMA/1000
        distL = gSMA_km * 1/(1+diff)
        distS = gSMA_km * diff/(1+diff)
        pi = math.pi
        Period = 2 * pi * math.sqrt(gSMA**3 / (6.67408E-11*(ML + MS)))

        binarySMA1 = distL * 1000
        binarySMA2 = distS * 1000

        listCfg = open(filepath + "/Visuals/Scatterer/" + systemName + "_ScattererList" + ".cfg","x")
        listCfg.write(
            "@Scatterer_planetsList:FINAL\n"
            "{\n"
            "    @scattererCelestialBodies\n"
            "    {\n"
        )
        atmoCfg = open(filepath + "/Visuals/Scatterer/" + systemName + "_ScattererAtmo" + ".cfg","x")
        atmoCfg.write(
            "Scatterer_atmosphere\n"
            "{\n"
        )
        oceanCfg = open(filepath + "/Visuals/Scatterer/" + systemName + "_ScattererOcean" + ".cfg","x")
        oceanCfg.write(
            "Scatterer_ocean\n"
            "{\n"
        )
        eveCfg = open(filepath + "/Visuals/EVE/Configs/" + systemName + "_EVE" + ".cfg","x")
        eveCfg.write(
            "EVE_CLOUDS\n"
            "{\n"
        )
        evePQSCfg = open(filepath + "/Visuals/EVE/Configs/" + systemName + "_PQSFIX" + ".cfg","x")
        evePQSCfg.write(
            "PQS_MANAGER\n"
            "{\n"
        )
        parallaxCfg = open(filepath + "/Visuals/Parallax/Configs/" + systemName + "_PARALLAX" + ".cfg","x")
        parallaxCfg.write(
            "Parallax\n"
            "{\n"
        )
        parallax_subd_Cfg = open(filepath + "/Visuals/Parallax/Configs/" + systemName + "_PARALLAX_SUBDFIX" + ".cfg","x")
        parallax_subd_Cfg.write(
            "@Kopernicus:FOR[ParallaxStock]:NEEDS[Parallax]\n"
            "{\n"
        )

        if star1Mass > star2Mass:
            star1Color, star1Name, dispName1 = generateStar(AmountOfPlanetsToGenerate, systemName, systemName, binarySMA1, Period, star1Radius, 0, "-1")
            star2Color, star2Name, dispName2 = generateStar(AmountOfPlanetsToGenerate, systemName, systemName, binarySMA2, Period, star2Radius, 180, "-2")
        else:
            star1Color, star1Name, dispName1 = generateStar(AmountOfPlanetsToGenerate, systemName, systemName, binarySMA1, Period, star2Radius, 0, "-1")
            star2Color, star2Name, dispName2 = generateStar(AmountOfPlanetsToGenerate, systemName, systemName, binarySMA2, Period, star1Radius, 180, "-2")
        baryCfg = open(filepath + "/Configs/" + systemName + ".cfg","x")
        if star1Mass > star2Mass:
            starColors = star1Color
        else:
            starColors = star2Color
        RGBfinal = str(starColors)[1:][:-1]
        baryDispName = dispName1 + "-" + dispName2 + " Barycenter"
        writeBarycenterCfg(baryCfg, systemName, barycenterRadius, barycenterMass, barycenterDist, systemName, RGBfinal, barycenterDistG, baryDispName)

        print(star1Color)
        colorsRound = (star1Color[0] + star1Color[1] + star1Color[2])/3
        Lum1 = 1360 * star1Radius / 261600000
        Lum2 = 1360 * star2Radius / 261600000
        Lum = (Lum1 + Lum2)/2

        sunfCfg = open(filepath + "/Visuals/Scatterer/" + systemName + "_ScattererSunflare" + ".cfg","x")
        addSunflareCfg(sunfCfg, star1Color, star1Name)
        addSunflareCfg(sunfCfg, star2Color, star2Name)
        binaryParents = [star1Name,star2Name]
        for x in range(planetsNum):
            planetsGenerated = planetsGenerated + 1
            generate(systemName,barycenterRadius,star1Color,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,Lum,parallaxCfg,parallax_subd_Cfg,evePQSCfg,binaryParents)
        
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
        evePQSCfg.write(
            "}\n"
        )
        parallaxCfg.write(
            "}\n"
        )
        parallax_subd_Cfg.write(
            "}\n"
        )

    def testNum(Numer):
        try:
            val = int(Numer)
        except ValueError:
            print("That's not an number!")
            exit()
            
    print("---------------------------------------------------------------")
    print("Infinite-Discoveries Version 0.9.7 (beta!)")
    print("---------------------------------------------------------------")
    print("WARNING: Generating a large amount of stars will take longer to... generate! The more stars you generate, the more it has to generate. You can find a settings file in the mod directory if you want to adjust some parameters.")
    print("---------------------------------------------------------------")

    StarAmount = int(input("Amount of stars to generate: "))
    testNum(StarAmount)

    print("---------------------------------------------------------------")
    print("If you happened to input a very high number just now, it's recommended to lower the amount of planets per star to reduce KSP loading times.")
    print("---------------------------------------------------------------")
    AmountOfPlanetsToGenerate = int(input("Maximum number of planets to add around stars: "))
    testNum(AmountOfPlanetsToGenerate)
    print("---------------------------------------------------------------")
    print("Last thing to input before you can generate! Please input the maximum number of moons to add around a planet.")
    print("---------------------------------------------------------------")
    AmountOfMoonsToGenerate = int(input("Maximum number of moons per planet: "))
    testNum(AmountOfMoonsToGenerate)
    print("---------------------------------------------------------------")
    estTime = ((AmountOfPlanetsToGenerate * AmountOfMoonsToGenerate) * StarAmount)*15
    print("The generator should take AT MOST " + str(round((estTime/60),2)) + " minutes.")
    print("---------------------------------------------------------------")
    input("Type anything or press enter to continue: ")
    planetsGenerated = 0
    startTime = time.time()
    for i in range(0,StarAmount):
        if random.randint(0,1) == 0:
            barycenter = True
            generateBarycenter(AmountOfPlanetsToGenerate)
        else:
            barycenter = False
            generateStar(AmountOfPlanetsToGenerate, barycenter)
        
    print("All done!")
    print("---------------------------------------------------------------")
    print("Total number of stars generated: " + str(totalStarsGenerated))
    print("Total number of planets generated: " + str(totalPlanetsGenerated))
    print("Total number of moons generated: " + str(totalMoonsGenerated))
    print("---------------------------------------------------------------")
    print("Total objects generated: " + str(totalStarsGenerated + totalPlanetsGenerated + totalMoonsGenerated))
    print("---------------------------------------------------------------")
    print("Now it's REALLY all done!")
    print("---------------------------------------------------------------")
    print("Make sure to delete the GenerateSystem folder so that KSP can load!")
    endTime = time.time()
    elapsedTime = endTime - startTime
    if elapsedTime > 60:
        print("Time elapsed: " + str(round(elapsedTime/60,2)) + " minutes.")
    elif elapsedTime < 60:
        print("Time elapsed: " + str(round(elapsedTime,2)) + " seconds.")

    input("Type anything or press enter to close: ")
except Exception:
    logging.error(traceback.format_exc())
    print(traceback.format_exc())
    input("Type anything or press enter to close: ")