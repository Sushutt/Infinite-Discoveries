import CelestialClasses
import Constants
import random
import scipy
import numpy
import matplotlib.pyplot as plt

def weightedRandom(seed,minValue,maxValue,power):
    systemRNG = random.Random()
    systemRNG.seed = seed
    initialVal = maxValue + (minValue - maxValue) * pow(systemRNG.random(), power)

    return initialVal

def RandomStarMass(seed, minValue,maxValue,power,multiplyChance=100):
    systemRNG = random.Random()
    systemRNG.seed = seed
    #initialVal = maxValue + (minValue - maxValue) * pow(systemRNG.random(), power)
    initialVal = weightedRandom(seed+1,minValue,maxValue,power)
    # the endless fight against probability
    if (systemRNG.randint(0,100) < multiplyChance):
        initialVal *= (systemRNG.randint(100,3000)/100)
    return initialVal

def GeneratePlanet(seed,index,parentStar: CelestialClasses.star):
    #------------------------------------------------------------
    #   Planet Orbit Calculations
    #
    semimajorAxis = int(((planetRNG.randint(4500000000,5500000000)*currentPlanetNum)*(parentStar.Mass/Constants.kerbolMass)))
    inclination = random.randint(-10,10)
    eccentricity = random.randint(0,2000)/10000
    meanAnomalyAtEpochD = random.randint(0,360)
    orbitParams = CelestialClasses.orbitParams(
        SMA=semimajorAxis,
        Period=None,
        Inclination=inclination,
        Eccentricity=eccentricity,
        MeanAnomalyAtEpochD=meanAnomalyAtEpochD,
        IconTexture="yeah/who/okay/icon.png" # Evil
    )
    #
    #
    #------------------------------------------------------------
    newPlanet = CelestialClasses.nonStarCelestialBody(
        Parent="AJ-012391",
        Children=[],
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
        Ocean=None,
        Atmo=None,
        Rings=None,
        Life=None,
        SciVal=10,

        #ColourMap="map/path/to/AJ-012391-P_CLR.png",
        #NormalMap="map/path/to/AJ-012391-P_NRM.png",
        #HeightMap="map/path/to/AJ-012391-P_HGT.png",
        #BiomesMap="map/path/to/AJ-012391-P_BIO.png",
    )
    return newPlanet

def GeneratePlanets(seed,count,parent):
    planets = []
    for i in range(0,count):
        planet = GeneratePlanet(seed,i,parent)
        planets.append(planet)
    return planets

def GenerateStar(seed, barycenter = None):
    systemRNG = random.Random()
    systemRNG.seed = seed
    newStar = CelestialClasses.star(
        Parent = "Sun",
        Children = GeneratePlanets(seed,5),
        Mass = RandomStarMass(seed+1, Constants.kerbolMass/100,Constants.kerbolMass*40,0.03,multiplyChance=50),
        Age = weightedRandom(seed,0,10000000000,0.07), #systemRNG.randint(0,10000000000), #Constants.kerbolAge * (systemRNG.randint(1000,100000)/10000),
        Orbit = CelestialClasses.orbitParams(
            SMA = systemRNG.randint(4.73e+15,9.461e+16),
            Period = 1000000000000,
            Inclination = systemRNG.randint(-180,180),
            Eccentricity = 0,
            MeanAnomalyAtEpochD = systemRNG.randint(-180,180)
        )
    )
    newStar.CalculateStarParameters()
    print(newStar.Children)

def GenerateBarycenter(systemRNG):
    newBary = CelestialClasses.barycenter(
        Parent="Sun",
        Orbit= CelestialClasses.orbitParams(
            SMA = systemRNG.randint(4.73e+15,9.461e+16),
            Period = 1000000000000,
            Inclination = systemRNG.randint(-180,180),
            Eccentricity = 0,
            MeanAnomalyAtEpochD = systemRNG.randint(-180,180)
        )
    )

def GenerateSystem(Seed):
    GenerateStar(Seed)

# Test call!
for i in range(0,10000):
    GenerateSystem(i)

#for i in range(0,1000):
    #print((10000 + (0 - 10000) * pow(random.random(), 0.1))/100<2)
    #print((Constants.kerbolMass*10 + (Constants.kerbolMass/10 - Constants.kerbolMass*10) * pow(random.random(), 0.1)))


#x = numpy.linspace(0, 10)

#y = scipy.stats.gamma.pdf(x, a=1, scale=1)

#for i in range(0,1):
#    print(scipy.stats.gamma.rvs(1,1))

#plt.plot(x, y)
#plt.show()