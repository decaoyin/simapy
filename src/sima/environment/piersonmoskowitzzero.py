# This an autogenerated file
# 
# Generated with PiersonMoskowitzZero
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.piersonmoskowitzzero import PiersonMoskowitzZeroBlueprint
from typing import Dict
from sima.environment.piersonmoskowitz import PiersonMoskowitz
from sima.environment.wavespreadingtype import WaveSpreadingType
from sima.sima.scriptablevalue import ScriptableValue

class PiersonMoskowitzZero(PiersonMoskowitz):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Average wave propagation direction(default 0.0)
    spreadingExponent : float
         Exponent  η in cos spreading function(default 2.0)
    numDirections : int
         Number of directions in spreading function, must be odd(default 11)
    spreadingType : WaveSpreadingType
         Wave spreading code
    significantWaveHeight : float
         Significant wave height(default 0.0)
    zeroCrossingPeriod : float
         Zero-crossing wave period(default 0.0)
    """

    def __init__(self , description="", direction=0.0, spreadingExponent=2.0, numDirections=11, spreadingType=WaveSpreadingType.UNIDIRECTIONAL, significantWaveHeight=0.0, zeroCrossingPeriod=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.direction = direction
        self.spreadingExponent = spreadingExponent
        self.numDirections = numDirections
        self.spreadingType = spreadingType
        self.significantWaveHeight = significantWaveHeight
        self.zeroCrossingPeriod = zeroCrossingPeriod
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PiersonMoskowitzZeroBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def direction(self) -> float:
        """Average wave propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def spreadingExponent(self) -> float:
        """Exponent  η in cos spreading function"""
        return self.__spreadingExponent

    @spreadingExponent.setter
    def spreadingExponent(self, value: float):
        """Set spreadingExponent"""
        self.__spreadingExponent = float(value)

    @property
    def numDirections(self) -> int:
        """Number of directions in spreading function, must be odd"""
        return self.__numDirections

    @numDirections.setter
    def numDirections(self, value: int):
        """Set numDirections"""
        self.__numDirections = int(value)

    @property
    def spreadingType(self) -> WaveSpreadingType:
        """Wave spreading code"""
        return self.__spreadingType

    @spreadingType.setter
    def spreadingType(self, value: WaveSpreadingType):
        """Set spreadingType"""
        self.__spreadingType = value

    @property
    def significantWaveHeight(self) -> float:
        """Significant wave height"""
        return self.__significantWaveHeight

    @significantWaveHeight.setter
    def significantWaveHeight(self, value: float):
        """Set significantWaveHeight"""
        self.__significantWaveHeight = float(value)

    @property
    def zeroCrossingPeriod(self) -> float:
        """Zero-crossing wave period"""
        return self.__zeroCrossingPeriod

    @zeroCrossingPeriod.setter
    def zeroCrossingPeriod(self, value: float):
        """Set zeroCrossingPeriod"""
        self.__zeroCrossingPeriod = float(value)
