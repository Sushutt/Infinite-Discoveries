import Constants

class ocean:
    def __init__(self, Colour, Height) -> None:
        self.Colour = Colour
        self.Height = Height

class atmo:
    def __init__(self, Height, Press, MainClr, SctrClr, Oxygen) -> None:
        self.Height = Height
        self.Press = Press
        self.MainClr = MainClr
        self.SctrClr = SctrClr
        self.Oxygen = Oxygen

class rings:
    def __init__(self, RingsInn, RingsOut) -> None:
        self.RingsInn = RingsInn
        self.RingsOut = RingsOut

class orbitParams:
    def __init__(self,
                SMA: float,
                Period: float,
                Inclination : float,
                Eccentricity : float,
                MeanAnomalyAtEpochD : float,
                IconTexture : str = None
                ) -> None:
        
        self.SMA = SMA
        self.Period = Period
        self.Inclination = Inclination
        self.Eccentricity = Eccentricity
        self.MeanAnomalyAtEpochD = MeanAnomalyAtEpochD
        self.IconTexture = IconTexture

class star:
    def __init__(self,
                 Parent: str,
                 Children: list,
                 Mass: float,
                 Age: float,
                 Orbit: orbitParams,
                 ) -> None:
        
        self.Parent = Parent # can either be kerbol (center of the universe) or a barycenter or literally anything else idc lol
        self.Children = Children # list of things oribitng this planet i guess idk
        self.Mass = Mass
        self.Age = Age
        self.Orbit = Orbit

    def CalculateStarParameters(self):
        self.Radius = self.Mass
        self.Luminosity = 1*(self.Mass/Constants.kerbolMass)**3.5 #(self.Mass / Constants.kerbolMass)**2
        self.Lifetime = 10**10*(Constants.kerbolMass/self.Mass)**2.5 # SUPER big approximation but this is used to determine the star type AFTER creating its properties
        
        # Checks what type of star this is by its mass and such (may not use due to finnicky behaviour!!)
        if self.Age > self.Lifetime + self.Lifetime/5:
            if (self.Mass/Constants.kerbolMass) < 8:
                # white dwarf
                print("White Dwarf")
            elif (self.Mass/Constants.kerbolMass) < 30:
                # neutron star
                print("Neutron Star")
            else:
                # black hole
                print("Black Hole")
        elif self.Age > self.Lifetime:
            self.Radius *= 10
            self.Luminosity *= 10
            print("Red Giant")
        else:
            print("Main Sequence")

class barycenter:
    def __init__(self,
                 Parent: str,
                 Orbit: orbitParams, # here's the real magic, THIS can be anything too! We can now have as many stars in one system as we want!
                 Mass0: float,
                 Mass1: float, 
                 Seperation: float,
                 ) -> None:
        
        self.Parent = Parent
        self.Orbit = Orbit
        self.Mass0 = Mass0
        self.Mass1 = Mass1
        self.Mass = Mass0 + Mass1
        self.Seperation = Seperation

    def CalculateBinaryParams():
        gSMA_km = self.Seperation/1000
        distL = gSMA_km * 1/(1+diff)
        distS = gSMA_km * diff/(1+diff)
        pi = math.pi
        Period = 2 * pi * math.sqrt(gSMA**3 / (6.67408E-11*(ML + MS)))

        self.BinarySMA1 = distL * 1000
        self.BinarySMA2 = distS * 1000

class nonStarCelestialBody:
    def __init__(self,
                Parent: str, # Anything lol
                Children: list,
                Name: str,
                DisplayName: str,
                Description: str,
                Seed: int,
                Number: int,
                Tag: str,
                Template: str,
                Radius: float,
                GeeASL: float,
                RotationPeriod: float,
                TidallyLocked: bool,
                Temperature: float,
                #Mass: float,
                TerrainClr: tuple,
                BodyType: str,
                Orbit: orbitParams,
                Ocean: ocean,
                Atmo: atmo,
                Rings: rings,
                Life: str,
                SciVal: float,
                # lotsa maps
                #ColourMap: str,
                #NormalMap: str,
                #HeightMap: str,
                #BiomesMap: str,
                ) -> None:
        # Need all these:
        # planetCfgSeed, planetCfg, planetName, planetRadius, planetMass, planetSMA, parentN, atmo, atmoPress, templ, atmClrR, atmClrG, atmClrB, sctrClrR, sctrClrG, sctrClrB, terrainClr, moon, gasGiant, rings, ringInn, ringOut, ocean, oceanR, oceanG, oceanB, atmoHeight, finalTemp, oxygen, life, dispName, anomaly, anLatLon, Tag, Lava, tidallyLocked, oceanFactor, isAsteroid, icy, inclinationLimits, sciValue
        
        # Identification IG
        self.Parent = Parent
        self.Children = Children # list of things oribitng this planet i guess idk
        self.Name = Name
        self.DisplayName = DisplayName
        self.Description = Description
        self.Seed = Seed
        self.Number = Number
        self.Tag = Tag
        self.template = Template

        # Physical properties
        self.Radius = Radius
        self.GeeASL = GeeASL
        self.RotationPeriod = RotationPeriod
        self.TidallyLocked = TidallyLocked
        #self.Mass = Mass
        self.Orbit = Orbit # A class
        self.terrainClr = TerrainClr
        self.bodyType = BodyType # asteroid, terrestrial, gaseous,
        self.ocean = Ocean # Now a class on its own.
        self.temperature = Temperature
        self.atmo = Atmo # Now a class on its own.
        self.rings = Rings # Now a class on its own.
        
        # Life.
        self.life = Life

        # Value
        self.SciVal = SciVal

        # Maps
        #self.ColourMap = ColourMap
        #self.NormalMap = NormalMap
        #self.HeightMap = HeightMap
        #self.BiomesMap = BiomesMap