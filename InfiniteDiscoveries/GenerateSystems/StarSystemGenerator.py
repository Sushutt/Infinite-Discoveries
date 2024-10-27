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

def GenerateStar(seed, barycenter = None):
    systemRNG = random.Random()
    systemRNG.seed = seed
    newStar = CelestialClasses.star(
        Parent = "Sun",
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