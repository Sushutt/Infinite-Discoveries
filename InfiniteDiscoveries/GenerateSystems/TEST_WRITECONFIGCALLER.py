import CelestialClasses
import WriteConfigs

import os
print(os.getcwd())

orbitParams = CelestialClasses.orbitParams(
    SMA=25874234,
    Period=None,
    Inclination=34,
    Eccentricity=0.1,
    MeanAnomalyAtEpochD=3,
    IconTexture="yeah/who/okay/icon.png"
    )

atmoParams = CelestialClasses.atmo(70000, 101.1,(104,201,54),(54,201,104),True)
ringParams = CelestialClasses.rings(1043,2049)
oceanParams = CelestialClasses.ocean((2,6,53), 5000)

newPlanet = CelestialClasses.nonStarCelestialBody(
    Parent="AJ-012391",
    Name="AJ-012391-P",
    DisplayName="absolute fucking nightmare",
    Description="poopygoopy is a planet in the poopy goopy nebula in the zoopy sector",
    Seed=42,
    Number=3,
    Tag="InfD_Planet",
    Template="Laythe",
    Radius=600000,
    GeeASL=1,
    RotationPeriod=2104,
    TidallyLocked=False,
    Temperature=290,
    TerrainClr=(255,0,0),
    BodyType="terrestrial",
    Orbit=orbitParams,
    Ocean=oceanParams,
    Atmo=atmoParams,
    Rings=ringParams,
    Life=None,
    SciVal=10,

    #ColourMap="map/path/to/AJ-012391-P_CLR.png",
    #NormalMap="map/path/to/AJ-012391-P_NRM.png",
    #HeightMap="map/path/to/AJ-012391-P_HGT.png",
    #BiomesMap="map/path/to/AJ-012391-P_BIO.png",
    )

WriteConfigs.WriteBodyCfg(newPlanet)