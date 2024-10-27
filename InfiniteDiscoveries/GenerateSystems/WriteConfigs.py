# Writes the whole config for planets. Now CLEAN! :D
import CelestialClasses

import os

filepath = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")
configTemplates = filepath + "/ConfigTemplates"

bodyTemplate = open(configTemplates + "/MainBody.txt").read()
propertiesTemplate = open(configTemplates + "/Properties.txt").read()
orbitTemplate = open(configTemplates + "/Orbit.txt").read()
scaledTemplate = open(configTemplates + "/ScaledVersion.txt").read()
scaledAtmoTemplate = open(configTemplates + "/ScaledVersion_AtmoExtension.txt").read()
ringsTemplate = open(configTemplates + "/Rings.txt").read()
atmoTemplate = open(configTemplates + "/Atmosphere.txt").read()
oceanTemplate =  open(configTemplates + "/Ocean.txt").read()
pqsTemplate =  open(configTemplates + "/PQS.txt").read()

def WriteBodyCfg(planet: CelestialClasses.nonStarCelestialBody):
    CFG_ScaledTypeValue = "Vacuum"
    CFG_ScaledAtmo = "// No atmosphere!"
    if planet.atmo != None:
        CFG_ScaledTypeValue = "Atmospheric"
        CFG_ScaledAtmo = f"{scaledAtmoTemplate}".format(
            atmoR = planet.atmo.MainClr[0],
            atmoG = planet.atmo.MainClr[1],
            atmoB = planet.atmo.MainClr[2],

            sctrR = planet.atmo.SctrClr[0],
            sctrG = planet.atmo.SctrClr[1],
            sctrB = planet.atmo.SctrClr[2],
        )

    CFG_Rings = "// No rings!"
    if planet.rings != None:
        CFG_Rings = f"{ringsTemplate}".format(
            InnerRadius = planet.rings.RingsInn,
            OuterRadius = planet.rings.RingsOut
        )

    CFG_Atmo = "// No atmosphere!"
    if planet.atmo != None:
        CFG_Atmo = f"{atmoTemplate}".format(
            hasOxygen = planet.atmo.Oxygen,
            waveR = planet.atmo.SctrClr[0],
            waveG = planet.atmo.SctrClr[1],
            waveB = planet.atmo.SctrClr[2],
            waveR_02 = planet.atmo.SctrClr[0]/2,
            waveG_02 = planet.atmo.SctrClr[1]/2,
            waveB_02 = planet.atmo.SctrClr[2]/2,

            atmoHeight_1 = planet.atmo.Height,
            atmoHeight_075 = planet.atmo.Height*0.75,
            atmoHeight_05 = planet.atmo.Height*0.5,
            atmoHeight_025 = planet.atmo.Height*0.25,

            atmoPress_1 = planet.atmo.Press,
            atmoPress_005 = planet.atmo.Press*0.05,

            curve1 = str((-8E-05*planet.atmo.Press)/(planet.atmo.Height/70000)),
            curve2 = str((-5E-06*planet.atmo.Press)/(planet.atmo.Height/70000)),
            curve3 = str((-5E-06*planet.atmo.Press)/(planet.atmo.Height/70000)),

            temp1 = str(planet.temperature),
            temp2 = str(planet.temperature/1.3),
            temp3 = str(planet.temperature/1.1),
            temp4 = str(planet.temperature/1.5)
        )

    CFG_Ocean = "// No ocean!"
    if planet.ocean != None:
        CFG_Ocean = f"{oceanTemplate}".format(
            oceanR = planet.ocean.Colour[0],
            oceanG = planet.ocean.Colour[1],
            oceanB = planet.ocean.Colour[2]
        )

    # buncha weird shit
    seaHeight = 0
    vertClrDooDad = "//"
    if planet.ocean != None:
        seaHeight = planet.ocean.Height
        vertClrDooDad = ""

    CFG_PQS = "// No land!"
    if planet.bodyType != "gaseous":
        CFG_PQS = f"{pqsTemplate}".format(
            planetName = planet.Name,
            format = "dds",
            oceanHeight = seaHeight,
            vertClrMapComm = vertClrDooDad
        )

    CFG_Properties = f"{propertiesTemplate}".format(
        displayName= planet.DisplayName,
        radius = planet.Radius,
        geeASL = planet.GeeASL,
        rotationPeriod = planet.RotationPeriod,
        tidallyLocked = planet.TidallyLocked,
        description = planet.Description,
        scienceValues = "// SCIENCE VALUES LATER AHAHAHA",
        biomeMap_PATH = "path/to/awesome/"+planet.Name+"_BIO.png",
    )

    CFG_Orbit = f"{orbitTemplate}".format(
        parent = planet.Parent,
        orbitR = planet.terrainClr[0],
        orbitG = planet.terrainClr[1],
        orbitB = planet.terrainClr[2],
        SMA = planet.Orbit.SMA,
        inclination = planet.Orbit.Inclination,
        eccentricity = planet.Orbit.Eccentricity,
        meanAnomalyAtEpochD = planet.Orbit.MeanAnomalyAtEpochD,
        iconFilepath = planet.Orbit.IconTexture
    ) 

    CFG_Scaled = f"{scaledTemplate}".format(
        scaledType = CFG_ScaledTypeValue,
        internalName = planet.Name,
        AtmoGradient = CFG_ScaledAtmo
    )

    CFG_Body = f"{bodyTemplate}".format(
        internalName = planet.Name,
        tag = planet.Tag,
        templateName = planet.template,

        Properties = CFG_Properties,
        Orbit = CFG_Orbit,
        ScaledVersion = CFG_Scaled,
        Rings = CFG_Rings,
        Atmosphere = CFG_Atmo,
        Ocean = CFG_Ocean,
        PQS = CFG_PQS,
        HazardousBody = "//hazard"
    )

    planetCFG = open(filepath + "/asbestor.cfg", "w")
    planetCFG.write(CFG_Body)