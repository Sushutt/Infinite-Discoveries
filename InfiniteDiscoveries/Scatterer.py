import os
from colour import Color
import random
red = Color("#eb0000")
colors1 = list(red.range_to(Color("#fad348"),10))
yellow = Color("#fad348")
colors2 = list(yellow.range_to(Color("#f7f9fa"),25))
white = Color("#f7f9fa")
colors3 = list(white.range_to(Color("#0051ff"),65))
finalColors = colors1 + colors2 + colors3

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

def addToScattererList(scattererCfg, starName, planetName, starColor):
    scattererCfg.write(
        "       Item\n"
        "       {\n"
        "            celestialBodyName = " + planetName + "\n"
        "            transformName = " + planetName + "\n"
        "            loadDistance = 100000000\n"
        "            unloadDistance = 200000000\n"
        "            hasOcean = True\n"
        "            flatScaledSpaceModel = True\n"
        "            usesCloudIntegration = True\n"
        "            cloudIntegrationUsesScattererSunColors = False\n"
        "            mainSunCelestialBody = " + starName + "\n"
        "            sunColor = " + str(starColor[0]) + "," + str(starColor[1]) + "," + str(starColor[2]) + "\n"
        "            sunsUseIntensityCurves = False\n"
        "        }\n"
    )



def addToAtmoCfg(atmoCfg, starName, planetName, starColor, sctrClrR, sctrClrG, sctrClrB):
    atmoCfg.write(
    "    Atmo\n"
    "    {\n"
    "        name = " + planetName + "\n"
    "        atmosphereStartRadiusScale = 1\n"
    "        HR = 7.5\n"
    "        HM = 1.79999995\n"
    "        m_betaR = " + str((sctrClrR/256)/100) + "," + str((sctrClrG/256)/100) + "," + str((sctrClrB/256)/100) + "\n"
    "        BETA_MSca = 0.0150000000,0.0150000000,0.0150000000\n"
    "        m_mieG = 0.850000024\n"
    "        averageGroundReflectance = 0.5\n"
    "        multipleScattering = True\n"
    "        godrayStrength = 0.5\n"
    "        flattenScaledSpaceMesh = 0.600000024\n"
    "        rimBlend = 1\n"
    "        rimpower = 5\n"
    "        specR = 100\n"
    "        specG = 100\n"
    "        specB = 100\n"
    "        shininess = 100\n"
    "        cloudColorMultiplier = 3\n"
    "        cloudScatteringMultiplier = 0.200000003\n"
    "        cloudSkyIrradianceMultiplier = 0.0500000007\n"
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

scattererCfg = open(filepath + "/Visuals/Scatterer/" + "testScatterer" + ".cfg","x")
scattererCfg.write(
    "@Scatterer_planetsList\n"
    "{\n"
    "    @scattererCelestialBodies\n"
    "    {\n"
)
atmoCfg = open(filepath + "/Visuals/Scatterer/" + "testAtmo" + ".cfg","x")
atmoCfg.write(
    "Scatterer_atmosphere\n"
    "{\n"
)
planetName = "blunkus"
starName = "blonker"
starRadius = random.choices(range(261,2616000), weights=range(261,2616000))
starRadius = starRadius[0]*175
Mult = starRadius*10 / 261600000
multRound = round(Mult)
starColor = Color.get_rgb(finalColors[multRound-1])

atmClrR = random.randint(0,150)
atmClrG = random.randint(0,150)
atmClrB = random.randint(0,150)
sctrClrR = (atmClrR*-1)+255
sctrClrG = (atmClrG*-1)+255
sctrClrB = (atmClrB*-1)+255

addToAtmoCfg(atmoCfg, starName, planetName, starColor, sctrClrR, sctrClrG, sctrClrB)
addToScattererList(scattererCfg, starName, planetName, starColor)