# This an autogenerated file
# 
# Generated with DerbyshireScott
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.derbyshirescott import DerbyshireScottBlueprint
from typing import Dict
from sima.environment.wave import Wave
from sima.environment.wavespreadingtype import WaveSpreadingType
from sima.sima.scriptablevalue import ScriptableValue

class DerbyshireScott(Wave):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
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
    spectrumA : float
         Spectrum parameter, a(default 0.214)
    spectrumB : float
         Spectrum parameter, b(default 0.065)
    spectrumD : float
         Spectrum parameter, d(default 0.26)
    waveHeight : float
         Significant wave height(default 0.0)
    wavePeriod : float
         Average wave period(default 0.0)
    lowerTrunc : float
         Lower truncation parameter(default 0.0414)
    upperTrunc : float
         Upper truncation parameter(default 10.367)
    """

    def __init__(self , name="", description="", _id="", direction=0.0, spreadingExponent=2.0, numDirections=11, spreadingType=WaveSpreadingType.UNIDIRECTIONAL, spectrumA=0.214, spectrumB=0.065, spectrumD=0.26, waveHeight=0.0, wavePeriod=0.0, lowerTrunc=0.0414, upperTrunc=10.367, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.direction = direction
        self.spreadingExponent = spreadingExponent
        self.numDirections = numDirections
        self.spreadingType = spreadingType
        self.spectrumA = spectrumA
        self.spectrumB = spectrumB
        self.spectrumD = spectrumD
        self.waveHeight = waveHeight
        self.wavePeriod = wavePeriod
        self.lowerTrunc = lowerTrunc
        self.upperTrunc = upperTrunc
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DerbyshireScottBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

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
    def spectrumA(self) -> float:
        """Spectrum parameter, a"""
        return self.__spectrumA

    @spectrumA.setter
    def spectrumA(self, value: float):
        """Set spectrumA"""
        self.__spectrumA = float(value)

    @property
    def spectrumB(self) -> float:
        """Spectrum parameter, b"""
        return self.__spectrumB

    @spectrumB.setter
    def spectrumB(self, value: float):
        """Set spectrumB"""
        self.__spectrumB = float(value)

    @property
    def spectrumD(self) -> float:
        """Spectrum parameter, d"""
        return self.__spectrumD

    @spectrumD.setter
    def spectrumD(self, value: float):
        """Set spectrumD"""
        self.__spectrumD = float(value)

    @property
    def waveHeight(self) -> float:
        """Significant wave height"""
        return self.__waveHeight

    @waveHeight.setter
    def waveHeight(self, value: float):
        """Set waveHeight"""
        self.__waveHeight = float(value)

    @property
    def wavePeriod(self) -> float:
        """Average wave period"""
        return self.__wavePeriod

    @wavePeriod.setter
    def wavePeriod(self, value: float):
        """Set wavePeriod"""
        self.__wavePeriod = float(value)

    @property
    def lowerTrunc(self) -> float:
        """Lower truncation parameter"""
        return self.__lowerTrunc

    @lowerTrunc.setter
    def lowerTrunc(self, value: float):
        """Set lowerTrunc"""
        self.__lowerTrunc = float(value)

    @property
    def upperTrunc(self) -> float:
        """Upper truncation parameter"""
        return self.__upperTrunc

    @upperTrunc.setter
    def upperTrunc(self, value: float):
        """Set upperTrunc"""
        self.__upperTrunc = float(value)
