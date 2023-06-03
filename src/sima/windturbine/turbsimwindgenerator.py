# This an autogenerated file
# 
# Generated with TurbSimWindGenerator
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.turbsimwindgenerator import TurbSimWindGeneratorBlueprint
from typing import Dict
from .iecstandard import IECStandard
from .iecturbulencecharacteristics import IECTurbulenceCharacteristics
from .iecwindprofiletype import IECWindProfileType
from .iecwindtype import IECWindType
from .randomseedgeneration import RandomSeedGeneration
from .turbulencemodel import TurbulenceModel
from sima.sima import ConditionSelectable
from sima.sima import NamedObject
from sima.sima import ScriptableValue

class TurbSimWindGenerator(NamedObject,ConditionSelectable):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    randSeed1 : int
         First random seed (-2147483648 to 2147483647)(default 0)
    seedGeneration : RandomSeedGeneration
    randSeed2 : int
         Second random seed (-2147483648 to 2147483647) for intrinsic pRNG, or an alternative pRNG: 'RanLux' or 'RNSNLW'(default 0)
    gridPointsZ : int
         Vertical grid-point matrix dimension(default 0)
    gridPointsY : int
          Horizontal grid-point matrix dimension(default 0)
    timeStep : float
         (default 0.0)
    analysisTime : float
         Length of analysis time series (program will add time if necessary: AnalysisTime = MAX(AnalysisTime, UsableTime+GridWidth/MeanHHWS) )(default 0.0)
    usableTime : float
         Usable length of output time series (program will add GridWidth/MeanHHWS seconds). Default value is analysis time for Turbsim v1, otherwise ALL(default 0.0)
    hubHeight : float
         Hub height (should be > 0.5*GridHeight)(default 0.0)
    gridHeight : float
         (default 0.0)
    gridWidth : float
         Grid width (should be >= 2*(RotorRadius+ShaftLength))(default 0.0)
    turbulenceModel : TurbulenceModel
    iecStandard : IECStandard
    turbulenceCharacteristics : IECTurbulenceCharacteristics
    turbulencePercentage : float
         Turbulence intensity in percent(default 0.0)
    windType : IECWindType
    etmC : float
          IEC ETM 'c' parameter(default 0.0)
    windProfileType : IECWindProfileType
    referenceHeight : float
         Height of the reference wind speed(default 0.0)
    meanWindSpeed : float
         Mean (total) wind speed at the reference height(default 0.0)
    powerLawExponent : float
         Power law exponent (or 'default')(default 0.0)
    surfaceRoughnessLength : float
         Surface roughness length (or 'default')(default 0.0)
    """

    def __init__(self , description="", randSeed1=0, seedGeneration=RandomSeedGeneration.INTRINSIC, randSeed2=0, gridPointsZ=0, gridPointsY=0, timeStep=0.0, analysisTime=0.0, usableTime=0.0, hubHeight=0.0, gridHeight=0.0, gridWidth=0.0, turbulenceModel=TurbulenceModel.IECKAI, iecStandard=IECStandard.IEC_61400_1, turbulenceCharacteristics=IECTurbulenceCharacteristics.A, turbulencePercentage=0.0, windType=IECWindType.NTM, etmC=0.0, windProfileType=IECWindProfileType.LOG, referenceHeight=0.0, meanWindSpeed=0.0, powerLawExponent=0.0, surfaceRoughnessLength=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.randSeed1 = randSeed1
        self.seedGeneration = seedGeneration
        self.randSeed2 = randSeed2
        self.gridPointsZ = gridPointsZ
        self.gridPointsY = gridPointsY
        self.timeStep = timeStep
        self.analysisTime = analysisTime
        self.usableTime = usableTime
        self.hubHeight = hubHeight
        self.gridHeight = gridHeight
        self.gridWidth = gridWidth
        self.turbulenceModel = turbulenceModel
        self.iecStandard = iecStandard
        self.turbulenceCharacteristics = turbulenceCharacteristics
        self.turbulencePercentage = turbulencePercentage
        self.windType = windType
        self.etmC = etmC
        self.windProfileType = windProfileType
        self.referenceHeight = referenceHeight
        self.meanWindSpeed = meanWindSpeed
        self.powerLawExponent = powerLawExponent
        self.surfaceRoughnessLength = surfaceRoughnessLength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TurbSimWindGeneratorBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def randSeed1(self) -> int:
        """First random seed (-2147483648 to 2147483647)"""
        return self.__randSeed1

    @randSeed1.setter
    def randSeed1(self, value: int):
        """Set randSeed1"""
        self.__randSeed1 = int(value)

    @property
    def seedGeneration(self) -> RandomSeedGeneration:
        """"""
        return self.__seedGeneration

    @seedGeneration.setter
    def seedGeneration(self, value: RandomSeedGeneration):
        """Set seedGeneration"""
        self.__seedGeneration = value

    @property
    def randSeed2(self) -> int:
        """Second random seed (-2147483648 to 2147483647) for intrinsic pRNG, or an alternative pRNG: 'RanLux' or 'RNSNLW'"""
        return self.__randSeed2

    @randSeed2.setter
    def randSeed2(self, value: int):
        """Set randSeed2"""
        self.__randSeed2 = int(value)

    @property
    def gridPointsZ(self) -> int:
        """Vertical grid-point matrix dimension"""
        return self.__gridPointsZ

    @gridPointsZ.setter
    def gridPointsZ(self, value: int):
        """Set gridPointsZ"""
        self.__gridPointsZ = int(value)

    @property
    def gridPointsY(self) -> int:
        """ Horizontal grid-point matrix dimension"""
        return self.__gridPointsY

    @gridPointsY.setter
    def gridPointsY(self, value: int):
        """Set gridPointsY"""
        self.__gridPointsY = int(value)

    @property
    def timeStep(self) -> float:
        """"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def analysisTime(self) -> float:
        """Length of analysis time series (program will add time if necessary: AnalysisTime = MAX(AnalysisTime, UsableTime+GridWidth/MeanHHWS) )"""
        return self.__analysisTime

    @analysisTime.setter
    def analysisTime(self, value: float):
        """Set analysisTime"""
        self.__analysisTime = float(value)

    @property
    def usableTime(self) -> float:
        """Usable length of output time series (program will add GridWidth/MeanHHWS seconds). Default value is analysis time for Turbsim v1, otherwise ALL"""
        return self.__usableTime

    @usableTime.setter
    def usableTime(self, value: float):
        """Set usableTime"""
        self.__usableTime = float(value)

    @property
    def hubHeight(self) -> float:
        """Hub height (should be > 0.5*GridHeight)"""
        return self.__hubHeight

    @hubHeight.setter
    def hubHeight(self, value: float):
        """Set hubHeight"""
        self.__hubHeight = float(value)

    @property
    def gridHeight(self) -> float:
        """"""
        return self.__gridHeight

    @gridHeight.setter
    def gridHeight(self, value: float):
        """Set gridHeight"""
        self.__gridHeight = float(value)

    @property
    def gridWidth(self) -> float:
        """Grid width (should be >= 2*(RotorRadius+ShaftLength))"""
        return self.__gridWidth

    @gridWidth.setter
    def gridWidth(self, value: float):
        """Set gridWidth"""
        self.__gridWidth = float(value)

    @property
    def turbulenceModel(self) -> TurbulenceModel:
        """"""
        return self.__turbulenceModel

    @turbulenceModel.setter
    def turbulenceModel(self, value: TurbulenceModel):
        """Set turbulenceModel"""
        self.__turbulenceModel = value

    @property
    def iecStandard(self) -> IECStandard:
        """"""
        return self.__iecStandard

    @iecStandard.setter
    def iecStandard(self, value: IECStandard):
        """Set iecStandard"""
        self.__iecStandard = value

    @property
    def turbulenceCharacteristics(self) -> IECTurbulenceCharacteristics:
        """"""
        return self.__turbulenceCharacteristics

    @turbulenceCharacteristics.setter
    def turbulenceCharacteristics(self, value: IECTurbulenceCharacteristics):
        """Set turbulenceCharacteristics"""
        self.__turbulenceCharacteristics = value

    @property
    def turbulencePercentage(self) -> float:
        """Turbulence intensity in percent"""
        return self.__turbulencePercentage

    @turbulencePercentage.setter
    def turbulencePercentage(self, value: float):
        """Set turbulencePercentage"""
        self.__turbulencePercentage = float(value)

    @property
    def windType(self) -> IECWindType:
        """"""
        return self.__windType

    @windType.setter
    def windType(self, value: IECWindType):
        """Set windType"""
        self.__windType = value

    @property
    def etmC(self) -> float:
        """ IEC ETM 'c' parameter"""
        return self.__etmC

    @etmC.setter
    def etmC(self, value: float):
        """Set etmC"""
        self.__etmC = float(value)

    @property
    def windProfileType(self) -> IECWindProfileType:
        """"""
        return self.__windProfileType

    @windProfileType.setter
    def windProfileType(self, value: IECWindProfileType):
        """Set windProfileType"""
        self.__windProfileType = value

    @property
    def referenceHeight(self) -> float:
        """Height of the reference wind speed"""
        return self.__referenceHeight

    @referenceHeight.setter
    def referenceHeight(self, value: float):
        """Set referenceHeight"""
        self.__referenceHeight = float(value)

    @property
    def meanWindSpeed(self) -> float:
        """Mean (total) wind speed at the reference height"""
        return self.__meanWindSpeed

    @meanWindSpeed.setter
    def meanWindSpeed(self, value: float):
        """Set meanWindSpeed"""
        self.__meanWindSpeed = float(value)

    @property
    def powerLawExponent(self) -> float:
        """Power law exponent (or 'default')"""
        return self.__powerLawExponent

    @powerLawExponent.setter
    def powerLawExponent(self, value: float):
        """Set powerLawExponent"""
        self.__powerLawExponent = float(value)

    @property
    def surfaceRoughnessLength(self) -> float:
        """Surface roughness length (or 'default')"""
        return self.__surfaceRoughnessLength

    @surfaceRoughnessLength.setter
    def surfaceRoughnessLength(self, value: float):
        """Set surfaceRoughnessLength"""
        self.__surfaceRoughnessLength = float(value)
