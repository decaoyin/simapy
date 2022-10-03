# This an autogenerated file
# 
# Generated with FatigueProperties
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fatigueproperties import FatiguePropertiesBlueprint
from typing import Dict
from sima.riflex.crosssectionreference import CrossSectionReference
from sima.riflex.fatiguecalculationoption import FatigueCalculationOption
from sima.riflex.resultprintoption import ResultPrintOption
from sima.riflex.sncurvereference import SNCurveReference
from sima.riflex.timeseriesprintoption import TimeSeriesPrintOption
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class FatigueProperties(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    calculationOption : FatigueCalculationOption
    numCrossSectionPoints : int
         Number of points around cross-section where fatigue is(default 0)
    resultPrintOption : ResultPrintOption
    timeSeriesPrintOption : TimeSeriesPrintOption
    timeSeriesLength : float
         Length of stress time series to be generated for fatigue calculation(default 0.0)
    timeStep : float
         Time step to be used in the stress time series(default 0.0)
    seed : int
         Seed for generating random phase angles(default 31415)
    axialFactor : float
         Default stress concentration factor for axial force contribution(default 1.0)
    myFactor : float
         Default stress concentration factor for bending about Yaxis(default 1.0)
    mzFactor : float
         Default stress concentration factor for bending about Zaxis(default 1.0)
    crossSectionArea : float
         Optional cross-section area.(default 0.0)
    sectionModulus : float
         Optional cross-section modulus.(default 0.0)
    wallThickness : float
         Optional wall thickness(default 0.0)
    snCurves : List[SNCurveReference]
    includeAllSNCurves : bool
         Include all SNCurves in fatigue analysis(default False)
    crossSectionReferences : List[CrossSectionReference]
    relativeDuration : float
         Relative duration / probability of the current condition(default 0.0)
    scaledContributions : bool
         (default False)
    """

    def __init__(self , _id="", calculationOption=FatigueCalculationOption.DEFAULT, numCrossSectionPoints=0, resultPrintOption=ResultPrintOption.MOST_CRITICAL_POINT, timeSeriesPrintOption=TimeSeriesPrintOption.NO_PRINT, timeSeriesLength=0.0, timeStep=0.0, seed=31415, axialFactor=1.0, myFactor=1.0, mzFactor=1.0, crossSectionArea=0.0, sectionModulus=0.0, wallThickness=0.0, includeAllSNCurves=False, relativeDuration=0.0, scaledContributions=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.calculationOption = calculationOption
        self.numCrossSectionPoints = numCrossSectionPoints
        self.resultPrintOption = resultPrintOption
        self.timeSeriesPrintOption = timeSeriesPrintOption
        self.timeSeriesLength = timeSeriesLength
        self.timeStep = timeStep
        self.seed = seed
        self.axialFactor = axialFactor
        self.myFactor = myFactor
        self.mzFactor = mzFactor
        self.crossSectionArea = crossSectionArea
        self.sectionModulus = sectionModulus
        self.wallThickness = wallThickness
        self.snCurves = list()
        self.includeAllSNCurves = includeAllSNCurves
        self.crossSectionReferences = list()
        self.relativeDuration = relativeDuration
        self.scaledContributions = scaledContributions
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FatiguePropertiesBlueprint()


    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

    @property
    def scriptableValues(self) -> List[ScriptableValue]:
        """"""
        return self.__scriptableValues

    @scriptableValues.setter
    def scriptableValues(self, value: List[ScriptableValue]):
        """Set scriptableValues"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def calculationOption(self) -> FatigueCalculationOption:
        """"""
        return self.__calculationOption

    @calculationOption.setter
    def calculationOption(self, value: FatigueCalculationOption):
        """Set calculationOption"""
        self.__calculationOption = value

    @property
    def numCrossSectionPoints(self) -> int:
        """Number of points around cross-section where fatigue is"""
        return self.__numCrossSectionPoints

    @numCrossSectionPoints.setter
    def numCrossSectionPoints(self, value: int):
        """Set numCrossSectionPoints"""
        self.__numCrossSectionPoints = int(value)

    @property
    def resultPrintOption(self) -> ResultPrintOption:
        """"""
        return self.__resultPrintOption

    @resultPrintOption.setter
    def resultPrintOption(self, value: ResultPrintOption):
        """Set resultPrintOption"""
        self.__resultPrintOption = value

    @property
    def timeSeriesPrintOption(self) -> TimeSeriesPrintOption:
        """"""
        return self.__timeSeriesPrintOption

    @timeSeriesPrintOption.setter
    def timeSeriesPrintOption(self, value: TimeSeriesPrintOption):
        """Set timeSeriesPrintOption"""
        self.__timeSeriesPrintOption = value

    @property
    def timeSeriesLength(self) -> float:
        """Length of stress time series to be generated for fatigue calculation"""
        return self.__timeSeriesLength

    @timeSeriesLength.setter
    def timeSeriesLength(self, value: float):
        """Set timeSeriesLength"""
        self.__timeSeriesLength = float(value)

    @property
    def timeStep(self) -> float:
        """Time step to be used in the stress time series"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def seed(self) -> int:
        """Seed for generating random phase angles"""
        return self.__seed

    @seed.setter
    def seed(self, value: int):
        """Set seed"""
        self.__seed = int(value)

    @property
    def axialFactor(self) -> float:
        """Default stress concentration factor for axial force contribution"""
        return self.__axialFactor

    @axialFactor.setter
    def axialFactor(self, value: float):
        """Set axialFactor"""
        self.__axialFactor = float(value)

    @property
    def myFactor(self) -> float:
        """Default stress concentration factor for bending about Yaxis"""
        return self.__myFactor

    @myFactor.setter
    def myFactor(self, value: float):
        """Set myFactor"""
        self.__myFactor = float(value)

    @property
    def mzFactor(self) -> float:
        """Default stress concentration factor for bending about Zaxis"""
        return self.__mzFactor

    @mzFactor.setter
    def mzFactor(self, value: float):
        """Set mzFactor"""
        self.__mzFactor = float(value)

    @property
    def crossSectionArea(self) -> float:
        """Optional cross-section area."""
        return self.__crossSectionArea

    @crossSectionArea.setter
    def crossSectionArea(self, value: float):
        """Set crossSectionArea"""
        self.__crossSectionArea = float(value)

    @property
    def sectionModulus(self) -> float:
        """Optional cross-section modulus."""
        return self.__sectionModulus

    @sectionModulus.setter
    def sectionModulus(self, value: float):
        """Set sectionModulus"""
        self.__sectionModulus = float(value)

    @property
    def wallThickness(self) -> float:
        """Optional wall thickness"""
        return self.__wallThickness

    @wallThickness.setter
    def wallThickness(self, value: float):
        """Set wallThickness"""
        self.__wallThickness = float(value)

    @property
    def snCurves(self) -> List[SNCurveReference]:
        """"""
        return self.__snCurves

    @snCurves.setter
    def snCurves(self, value: List[SNCurveReference]):
        """Set snCurves"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__snCurves = value

    @property
    def includeAllSNCurves(self) -> bool:
        """Include all SNCurves in fatigue analysis"""
        return self.__includeAllSNCurves

    @includeAllSNCurves.setter
    def includeAllSNCurves(self, value: bool):
        """Set includeAllSNCurves"""
        self.__includeAllSNCurves = bool(value)

    @property
    def crossSectionReferences(self) -> List[CrossSectionReference]:
        """"""
        return self.__crossSectionReferences

    @crossSectionReferences.setter
    def crossSectionReferences(self, value: List[CrossSectionReference]):
        """Set crossSectionReferences"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__crossSectionReferences = value

    @property
    def relativeDuration(self) -> float:
        """Relative duration / probability of the current condition"""
        return self.__relativeDuration

    @relativeDuration.setter
    def relativeDuration(self, value: float):
        """Set relativeDuration"""
        self.__relativeDuration = float(value)

    @property
    def scaledContributions(self) -> bool:
        """"""
        return self.__scaledContributions

    @scaledContributions.setter
    def scaledContributions(self, value: bool):
        """Set scaledContributions"""
        self.__scaledContributions = bool(value)
