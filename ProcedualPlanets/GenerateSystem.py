import random
import string
import os
from PIL import Image, ImageEnhance, ImageChops, ImageOps, ImageFilter
from colour import Color
import sys
from wand import image as wImage
import time
import math
#Variables lamo
templates = ["Dres", "Duna", "Laythe", "Mun", "Jool"]
planetsGenerated = 0
alphabet = list(string.ascii_uppercase)

#Star Colors
red = Color("#eb0000")
colors1 = list(red.range_to(Color("#f7e297"),10))
yellow = Color("#f7e297")
colors2 = list(yellow.range_to(Color("#f7f9fa"),25))
white = Color("#f7f9fa")
colors3 = list(white.range_to(Color("#0051ff"),65))
finalColors = colors1 + colors2 + colors3
filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
totalStarsGenerated = 0
totalPlanetsGenerated = 0
totalMoonsGenerated = 0

print("Starting generator...")
print(filepath)

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
        "                value = ProcedualPlanets/Presets/Clouds" + str(cloudTexNum) + "\n"
        "            }\n"
        "            _DetailTex\n"
        "            {\n"
        "                value = ProcedualPlanets/Visuals/EVE/detail1\n"
        "            }\n"
        "            _UVNoiseTex\n"
        "            {\n"
        "                value = ProcedualPlanets/Visuals/EVE/uvnoise1\n"
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
        "                _BumpMap = ProcedualPlanets/Visuals/EVE/particle/particle_NRM\n"
        "                _Opacity = 0.5\n"
        "                _MinScatter = 0.5\n"
        "                _Tex\n"
        "                {\n"
        "                    value = ProcedualPlanets/Visuals/EVE/particle/rgb\n"
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

def addToScattererList(scattererCfg, starName, planetName, starColor, ocean, colorsRound):
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
        "            sunColor = " + str(colorsRound) + str(colorsRound) + str(colorsRound) + "\n"
        "            sunsUseIntensityCurves = False\n"
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

def writeStarCfg(starCfg, starName, starRadius, starMass, starDist, RGBfinal):
    starCfg.write(
        "@Kopernicus:AFTER[Kopernicus]\n"
        "{\n"
        "    Body\n"
        "    {\n"
        "        name = " + starName + "\n"
        "        cacheFile = ProcedualPlanets/Cache/" + starName + ".bin" + "\n"
        "        Template\n"
        "        {\n"
        "            name = Sun\n"
        "        }\n"
        "        Properties\n"
        "        {\n"
        "            displayName = " + starName + "^N" + "\n"
        "            radius = " + str(starRadius) + "\n"
        "            mass = " + str(starMass) + "\n"
        "            rotationPeriod = 106300.6069891\n"
        "            tidallyLocked = false\n"
        "            description = " + str(starName) + " is a randomly generated star roughly " + str(round(starRadius / 261600000, 2)) + " times the size of Kerbol!" + "\n"
        "            sphereOfInfluence = 736413913169.9\n"
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
        "            inclination = " + str(random.randint(0,360)) + "\n"
        "            eccentricity = " + str(random.randint(0,500)/1000) + "\n"
        "            longitudeOfAscendingNode = 0\n"
        "            argumentOfPeriapsis = 0\n"
        "            meanAnomalyAtEpochD = " + str(random.randint(0,360)) + "\n"
        "            epoch = 0\n"
        "            mode = OFF\n"
        "            iconTexture = ProcedualPlanets/Textures/Misc/starIcon.png\n"
        "        }\n"
        "        ScaledVersion\n"
        "        {\n"
        "            type = Star\n"
        "            Light\n"
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
        "                        texture = ProcedualPlanets/Textures/Misc/None.dds\n"
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

def writeBodyCfg(planetCfg, planetName, planetRadius, planetMass, planetSMA, parentN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen):
    planetCfg.write(
        "@Kopernicus:AFTER[Kopernicus]\n"
        "{\n"
        "    Body\n"
        "    {\n"
        "        name = " + planetName + "\n"
        "        cacheFile = ProcedualPlanets/Cache/" + planetName + ".bin" + "\n"
        "        Template\n"
        "        {\n"
        "            name = " + templates[templ] + "\n"
        "            removeAllPQSMods = true\n"
        "        }\n"
        "        Properties\n"
        "        {\n"
        "            displayName = " + planetName + "^N" + "\n"
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
        if oxygen == True:
            planetCfg.write(
                "            description = " + str(planetName) + " is a randomly generated world roughly " + str(round(planetRadius / 600000, 2)) + " times the size of Kerbin! This world has an oxygenated atmosphere!\n"
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
        "                texture = ProcedualPlanets/Textures/PluginData/" + planetName + "_CLR" + ".dds" + "\n"
        "                normals = ProcedualPlanets/Textures/PluginData/" + planetName + "_NRM" + ".dds" + "\n"
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
        "                texture = ProcedualPlanets/Textures/PluginData/" + planetName + "_RINGS" + ".png\n"
        )
    else:
        planetCfg.write(
        "                innerRadius = 2000\n"
        "                outerRadius = 2001\n"
        "                texture = ProcedualPlanets/Presets/RingNone.png\n"
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
            "            maxLevel = 9\n"
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
            "                    map = ProcedualPlanets/Textures/PluginData/" + planetName + "_HGT" + ".dds" + "\n"
        )
        if ocean == True:
            planetCfg.write(
                "                    offset = -4000\n"   
            )
        else:
            planetCfg.write(
                "                    offset = 0\n"   
            )
        planetCfg.write(
            "                    deformity = 8000\n"
            "                    scaleDeformityByRadius = False\n"
            "                    order = 10\n"
            "                    enabled = True\n"
            "                }\n"
            "                VertexColorMap\n"
            "                {\n"
            "                   map = ProcedualPlanets/Textures/PluginData/" + planetName + "_CLR" + ".dds" + "\n"
            "                   order = 20\n"
            "                   enabled = true\n"
            "                }\n"
            "                VertexHeightNoiseVertHeightCurve2\n"
            "                {\n"
            "                    deformity = 4000\n"
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
    
def GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB):
    chosenImgs = []
    for i in range(0,3):
        randomNum = random.randint(1,6)
        if vacuum == True:
            chosenImgs.append("Vacuum" + str(randomNum))
        else:
            chosenImgs.append("Atmo" + str(randomNum))


    print(chosenImgs)

    srcBase = Image.open(filepath + "/Presets/GeneralNoise1.png")

    src1 = Image.open(filepath + "/Presets/" + chosenImgs[0] + ".png")
    src2 = Image.open(filepath + "/Presets/" + chosenImgs[1] + ".png")
    src3 = Image.open(filepath + "/Presets/" + chosenImgs[2] + ".png")

    print("Generating height map for " + planetName + "...")
    srcBase.putalpha(64)
    src1.putalpha(128)
    src2.putalpha(128)
    src3.putalpha(64)

    baseContr = ImageEnhance.Contrast(srcBase)
    baseFinl = baseContr.enhance(1.1)

    OffsetB = random.randint(0,4096)
    Offset1 = random.randint(0,4096)
    Offset2 = random.randint(0,4096)
    Offset3 = random.randint(0,4096)

    finalImg = Image.new("RGBA", (4096,2048), (128,128,128))
    baseOff = ImageChops.offset(baseFinl, OffsetB,0)
    imOff1 = ImageChops.offset(src1, Offset1,0)
    imOff2 = ImageChops.offset(src2, Offset2,0)
    imOff3 = ImageChops.offset(src3, Offset3,0)
    finalImg.paste(imOff1, (0,0), mask=imOff1)
    finalImg.paste(imOff2, (0,0), mask=imOff2)
    finalImg.paste(imOff3, (0,0), mask=imOff3)
    finalImg.paste(baseOff, (0,0), mask=baseOff)
    contraster = ImageEnhance.Contrast(finalImg)
    contrasted = contraster.enhance(2)
    brightener = ImageEnhance.Brightness(contrasted)
    brightened = brightener.enhance(1.5)
    finalHeight = brightened
    #finalHeight.show()

    print("Generated height map for " + planetName + "!")
    #time.sleep(1)
    print("Generating normal map for " + planetName + "...")
    srcNRMBase = Image.open(filepath + "/Presets/GeneralNoise1NRM.png")

    srcNRM1 = Image.open(filepath + "/Presets/" + chosenImgs[0] + "NRM" + ".png")
    srcNRM2 = Image.open(filepath + "/Presets/" + chosenImgs[1] + "NRM" + ".png")
    srcNRM3 = Image.open(filepath + "/Presets/" + chosenImgs[2] + "NRM" + ".png")

    srcNRMBase.putalpha(64)
    srcNRM1.putalpha(128)
    srcNRM2.putalpha(128)
    srcNRM3.putalpha(64)

    finalImgNRM = Image.new("RGBA", (4096,2048), (255,255,255))
    baseNrmOff = ImageChops.offset(srcNRMBase, OffsetB,0)
    nrOff1 = ImageChops.offset(srcNRM1, Offset1,0)
    nrOff2 = ImageChops.offset(srcNRM2, Offset2,0)
    nrOff3 = ImageChops.offset(srcNRM3, Offset3,0)
    finalImgNRM.paste(nrOff1, (0,0), mask=nrOff1)
    finalImgNRM.paste(nrOff2, (0,0), mask=nrOff2)
    finalImgNRM.paste(nrOff3, (0,0), mask=nrOff3)
    finalImgNRM.paste(baseNrmOff, (0,0), mask=baseNrmOff)

    OceanPre1 = random.randint(1,3)

    
    #nrmFINAL = ImageOps.grayscale(nrmBrted)

    #nrmBrted.show()
    print("Generated normal map for " + planetName + "!")

    print("Generating color map for " + planetName + "...")

    heightColor = ImageEnhance.Contrast(ImageEnhance.Brightness(finalHeight).enhance(0.5)).enhance(2)
    colorMapBlur = heightColor.filter(ImageFilter.GaussianBlur(1))
    colorMap = ImageOps.colorize(ImageOps.grayscale(colorMapBlur), ((random.randint(0,32)),(random.randint(0,32)),(random.randint(0,32))), (terrainR,terrainG,terrainB))

    nrmContr = ImageEnhance.Contrast(finalImgNRM)
    nrmContred = nrmContr.enhance(1.1)
    nrmBrt = ImageEnhance.Contrast(nrmContred)
    nrmBrted = nrmBrt.enhance(2)

    if ocean == True:
        brightFac = float(random.randint(100,200)/100)

        print("Ocean exists! Dryness factor is " + str(brightFac))

        brghtHeight = ImageEnhance.Brightness(finalHeight).enhance(brightFac)
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
        finalHeight.paste(heightOcean, (0,0), mask=heightOcean)

        normalOcean = Image.new("RGBA", (4096,2048), (128,128,255))
        normalOcean.putalpha(ocInvL)
        nrmBrted.paste(normalOcean, (0,0), mask=ocInvL)

        beachColor = Image.new("RGBA", (4096,2048), (171,160,111))
        beachMask = oceanInv.filter(ImageFilter.GaussianBlur(3)).convert("L")
        beachColor.putalpha(beachMask)
        colorMap.paste(beachColor, (0,0), mask=beachColor)
        colorOcean = Image.new("RGBA", (4096,2048), (oceanR,oceanG,oceanB))
        colorOcean.putalpha(ocInvL)
        colorMap.paste(colorOcean, (0,0), mask=colorOcean)
        colorMap.putalpha(ocInvL)

    gray = ImageOps.grayscale(finalHeight)

    #colorMap.show()

    print("Generated color map for " + planetName + "!")
    print("Converting maps to DDS for " + planetName + "...")

    #finalHeight2 = finalHeight.transpose(Image.FLIP_TOP_BOTTOM)
    gray.save(filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")
    hgtConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")
    hgtConv.options['dds:mipmaps'] = '0'
    hgtConv.compression = 'dxt5'
    hgtConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".dds")
    os.remove(filepath + "/Textures/PluginData/" + planetName + "_HGT" + ".png")

    nR,nG,nB,nA = nrmBrted.convert("RGBA").split()
    nrmBrted.putalpha(nR)

    nrmBrted.save(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
    nrmConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
    #nrmConv.options['dds:mipmaps'] = '0'
    nrmConv.compression = 'dxt5'
    nrmConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".dds")
    os.remove(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")

    colorMap.save(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
    clrConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
    clrConv.options['dds:mipmaps'] = '0'
    clrConv.compression = 'dxt5'
    clrConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".dds")
    os.remove(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
   
    print("Converted maps to DDS for " + planetName + "!")

def generateGasGiantMaps(terrainR, terrainG, terrainB, planetName):
    gg1 = Image.open(filepath + "/Presets/" + "GasGiant" + str(random.randint(1,3)) + ".png")
    gg2 = Image.open(filepath + "/Presets/" + "GasGiant" + str(random.randint(1,3)) + ".png")
    gg3 = Image.open(filepath + "/Presets/" + "GasGiant" + str(random.randint(1,3)) + ".png")

    print("Generating color map for gas giant " + planetName + "...")

    ggClr1 = ImageOps.colorize(ImageOps.grayscale(gg1),(128,128,128),(random.randint(0,255),random.randint(0,255),random.randint(0,255))).convert("RGBA")
    ggClr2 = ImageOps.colorize(ImageOps.grayscale(gg2),(128,128,128),(random.randint(0,255),random.randint(0,255),random.randint(0,255))).convert("RGBA")
    ggClr3 = ImageOps.colorize(ImageOps.grayscale(gg3),(128,128,128),(terrainR,terrainG,terrainB)).convert("RGBA")

    ggCnt1 = ImageEnhance.Contrast(ggClr1).enhance(random.randint(0,10))
    ggCnt2 = ImageEnhance.Contrast(ggClr2).enhance(random.randint(0,10))
    ggCnt3 = ImageEnhance.Contrast(ggClr3).enhance(random.randint(0,10))

    ggCnt1.putalpha(128)
    ggCnt2.putalpha(64)
    ggCnt3.putalpha(32)

    Offset1 = random.randint(0,2048)
    Offset2 = random.randint(0,2048)
    Offset3 = random.randint(0,2048)

    #gg1.show()
    #gg2.show()
    #gg3.show()

    ggOffs1 = ImageChops.offset(ggCnt1, 0,Offset1)
    ggOffs2 = ImageChops.offset(ggCnt2, 0,Offset2)
    ggOffs3 = ImageChops.offset(ggCnt3, 0,Offset3)

    finalImg = Image.new("RGBA", (4096,2048), (128,128,128))
    finalImg.paste(ggOffs1, (0,0), mask=ggOffs1)
    finalImg.paste(ggOffs2, (0,0), mask=ggOffs2)
    finalImg.paste(ggOffs3, (0,0), mask=ggOffs3)

    print("Generated color map for gas giant " + planetName + "!")

    ggNrm = Image.new("RGBA", (4096,2048), (128,128,255))

    print("Added normals for gas giant " + planetName + "!")
    nR,nG,nB,nA = ggNrm.split()
    ggNrm.putalpha(nR)

    print("Converting maps to dds for gas giant " + planetName + "...")

    ggNrm.save(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
    nrmConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")
    nrmConv.compression = 'dxt5'
    nrmConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".dds")
    os.remove(filepath + "/Textures/PluginData/" + planetName + "_NRM" + ".png")

    finalImg.save(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
    clrConv = wImage.Image(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")
    clrConv.options['dds:mipmaps'] = '0'
    clrConv.compression = 'dxt5'
    clrConv.save(filename= filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".dds")
    os.remove(filepath + "/Textures/PluginData/" + planetName + "_CLR" + ".png")

    print("Converted maps to dds for gas giant " + planetName + "!")

def generateMoon(parentPlanet, moonsGenerated, parentRadius, gasGiantP, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, parentSMA):
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
    planetSMA = (random.randint(5000000,20000000)*moonsGenerated)*(parentRadius/600000)
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
        atmClrR = random.randint(0,150)
        atmClrG = random.randint(0,150)
        atmClrB = random.randint(0,150)
        sctrClrR = (atmClrR*-1)+255
        sctrClrG = (atmClrG*-1)+255
        sctrClrB = (atmClrB*-1)+255
    else:
        atmo = "Vacuum"
        vacuum = True
    
    if atmo == "Atmospheric":
        templ = 1
    elif atmo == "Vacuum":
        templ = 0
    
    starLum = Lum
    starLumMult = starLum/1360
    smaMult = 13599840256/planetSMA
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
        if random.randint(1,4) == 1:
            if finalTemp > 54 and finalTemp < 1000: 
                oxygen = True
            else:
                oxygen = False
        else:
            oxygen = False
    else:
        oxygen = False

    oceanR = random.randint(50,100)
    oceanG = random.randint(50,100)
    oceanB = random.randint(50,100)

    moon = True

    terrainR = random.randint(100,255)
    terrainG = random.randint(100,255)
    terrainB = random.randint(100,255)

    terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"

    print("-------Physical Values-------")
    print("Radius: " + str(planetRadius))
    print("Mass: " + str(planetMass))
    print("Semimajor Axis: " + str(planetSMA))
    print("Terrain tint: " + str(terrainClr))

    print("-------Atmosphere Values-------")
    if atmo == "Atmospheric":
        print("Atmosphere scattering color: " + str(atmClrR) + " " + str(atmClrG) + " " + str(atmClrB))
        print("Atmosphere main color: " + str(sctrClrR) + " " + str(sctrClrG) + " " + str(sctrClrB))
        print("kPa at sea level: " + str(atmoPress))
    else:
        print("No atmosphere!")

    print("-------------------------------")
    planetCfg = open(filepath + "/Configs/" + planetName + "-" + str(moonsGenerated) + ".cfg","x")
    GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB)

    ringInn = 2000
    ringOut = 2001
    rings = False

    atmoHeight = random.randint(50,90)*1000

    if ocean == True:
        addToOceanCfg(oceanCfg, oceanR, oceanG, oceanB, planetName)

    if atmo == "Atmospheric":
        addToAtmoCfg(atmoCfg, starN, planetName, starColor, sctrClrR, sctrClrG, sctrClrB, ocean)
        addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound)
        if gasGiant == False:
            if random.randint(1,2) == 1:
                cloudTexNum = random.randint(1,5)
                addToEVECfg(eveCfg, cloudTexNum, planetName)

    writeBodyCfg(planetCfg, planetName, planetRadius, planetMass, planetSMA, parentPlanet, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen)

def generate(starN,starRadius,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,Lum):
    print(planetsGenerated)
    moonsGenerated = 0
    global totalPlanetsGenerated
    totalPlanetsGenerated = totalPlanetsGenerated + 1
    if planetsGenerated > 1:
        moonAmount = random.randint(0,AmountOfMoonsToGenerate)
    else:
        moonAmount = 0
    planetName = starN + "-" + alphabet[planetsGenerated]
    print(planetName)
    print("Number Of Moons For " + planetName + ": " + str(moonAmount))
    #gasGiant = False
    if random.randint(1,3) == 1:
        planetRadius = random.randint(100,1000)*10000
        gasGiant = True
    else:
        planetRadius = random.randint(50,800)*1000
        gasGiant = False
    planetMass = planetRadius * 8.8191931e+16
    planetSMA = (random.randint(3000000000,7000000000)*planetsGenerated)*(starRadius/261600000)
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
        atmClrR = random.randint(0,150)
        atmClrG = random.randint(0,150)
        atmClrB = random.randint(0,150)
        sctrClrR = (atmClrR*-1)+255
        sctrClrG = (atmClrG*-1)+255
        sctrClrB = (atmClrB*-1)+255
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
        if random.randint(1,3) == 1:
            if finalTemp > 54 and finalTemp < 1000: 
                oxygen = True
            else:
                oxygen = False
        else:
            oxygen = False
    else:
        oxygen = False

    oceanR = random.randint(50,100)
    oceanG = random.randint(50,100)
    oceanB = random.randint(50,100)

    moon = False
    
    if gasGiant == True:
        terrainR = random.randint(100,255)
        terrainG = random.randint(100,255)
        terrainB = random.randint(100,255)

        terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"
    else:
        terrainR = random.randint(0,255)
        terrainG = random.randint(0,255)
        terrainB = random.randint(0,255)

        terrainClr = "RGBA(" + str(terrainR) + ", " + str(terrainG) + ", " + str(terrainB) + ", 100)"

    if atmo == "Atmospheric" and gasGiant == False:
        templ = 1
    elif atmo == "Atmospheric" and gasGiant == True:
        templ = 4
    elif atmo == "Vacuum":
        templ = 0

    print("-------Physical Values-------")
    print("Radius: " + str(planetRadius))
    print("Mass: " + str(planetMass))
    print("Semimajor Axis: " + str(planetSMA))
    print("Terrain tint: " + str(terrainClr))

    print("-------Atmosphere Values-------")
    if atmo == "Atmospheric":
        print("Atmosphere scattering color: " + str(atmClrR) + " " + str(atmClrG) + " " + str(atmClrB))
        print("Atmosphere main color: " + str(sctrClrR) + " " + str(sctrClrG) + " " + str(sctrClrB))
        print("kPa at sea level: " + str(atmoPress))
        if oxygen == True:
            print("Oxygenated!")
    else:
        print("No atmosphere!")

    print("-------------------------------")
    planetCfg = open(filepath + "/Configs/" + planetName + ".cfg","x")
    if gasGiant == True:
        generateGasGiantMaps(terrainR, terrainG, terrainB, planetName)
    else:
        GeneratePlanetMaps(vacuum, terrainR, terrainG, terrainB, planetName, ocean, oceanR, oceanG, oceanB)
    
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
        addToScattererList(listCfg, starN, planetName, starColor, ocean, colorsRound)
        if gasGiant == False:
            if random.randint(1,2) == 1:
                cloudTexNum = random.randint(1,5)
                addToEVECfg(eveCfg, cloudTexNum, planetName)

    writeBodyCfg(planetCfg, planetName, planetRadius, planetMass, planetSMA, starN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen)
    for a in range(moonAmount):
        moonsGenerated = moonsGenerated + 1
        generateMoon(planetName, moonsGenerated, planetRadius, gasGiant, atmoCfg, starN, starColor, listCfg, colorsRound, oceanCfg, eveCfg, Lum, planetSMA)

def generateStar(AmountOfPlanetsToGenerate):
    global planetsGenerated
    planetsGenerated = 0
    global totalStarsGenerated
    totalStarsGenerated = totalStarsGenerated + 1
    starName = str(alphabet[random.randint(0,len(alphabet)-1)]) + str(alphabet[random.randint(0,len(alphabet)-1)]) + "-" + str(random.randint(0,99999))
    planetsNum = random.randint(0,AmountOfPlanetsToGenerate)
    print(starName)
    print("Number Of Planets For " + starName + ": " + str(planetsNum))
    min = 56160000
    max = 1316000000
    starRadius = math.floor(abs(random.random() - random.random()) * (10 + max - min) + min)
    starRadius = starRadius
    starMass = starRadius * 6.7146251e+19
    starDist = random.randint(10000000000000,50000000000000)
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

    listCfg = open(filepath + "/Visuals/Scatterer/" + starName + "_ScattererList" + ".cfg","x")
    listCfg.write(
        "@Scatterer_planetsList\n"
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

    sunfCfg = open(filepath + "/Visuals/Scatterer/" + starName + "_ScattererSunflare" + ".cfg","x")
    addSunflareCfg(sunfCfg, starColor, starName)

    starCfg = open(filepath + "/Configs/" + starName + ".cfg","x")
    writeStarCfg(starCfg, starName, starRadius, starMass, starDist, RGBfinal)

    for x in range(planetsNum):
        planetsGenerated = planetsGenerated + 1
        generate(starName,starRadius,starColor,atmoCfg,listCfg,colorsRound,oceanCfg,eveCfg,Lum)
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

def testNum(Numer):
    try:
        val = int(Numer)
    except ValueError:
        print("That's not an number!")
        exit()
        
print("Welcome! This generator requires you to input a few values in order to work.")
print("---------------------------------------------------------------")
print("Infinite-Discoveries Version 0.9 (alpha!)")
print("---------------------------------------------------------------")
print("WARNING: Generating a large amount of stars will take longer to... generate! The more stars you generate, the more it has to generate. Insightful, I know.")
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
startTime = time.time()
for i in range(0,StarAmount):
    generateStar(AmountOfPlanetsToGenerate)
print("All done!")
print("---------------------------------------------------------------")
print("Total number of stars generated: " + str(totalStarsGenerated))
print("Total number of planets generated: " + str(totalPlanetsGenerated))
print("Total number of moons generated: " + str(totalMoonsGenerated))
print("---------------------------------------------------------------")
print("Total objects generated: " + str(totalStarsGenerated + totalPlanetsGenerated + totalMoonsGenerated))
print("---------------------------------------------------------------")
print("Now it's REALLY all done!")

endTime = time.time()
elapsedTime = endTime - startTime
if elapsedTime > 60:
    print("Time elapsed: " + str(round(elapsedTime/60,2)) + " minutes.")
elif elapsedTime < 60:
    print("Time elapsed: " + str(round(elapsedTime,2)) + " seconds.")