# This an autogenerated file
# 
# Generated with RegularWaveAnalaysis
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.regularwaveanalaysis import RegularWaveAnalaysisBlueprint
from typing import Dict
from sima.riflex.platformmotion import PlatformMotion
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class RegularWaveAnalaysis(MOAO):
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
    periods : int
         Number of periods for regular wave analysis, referring to wave or motion periods (of first vessel)(default 1)
    timeSteps : int
         Number of integration time steps per period, recommended value: 50-120(default 80)
    waveActing : bool
         Whether there is a wave acting or not (in which case motions must be present)(default True)
    platformMotion : PlatformMotion
         Platform motion options:
    """

    def __init__(self , name="", description="", _id="", periods=1, timeSteps=80, waveActing=True, platformMotion=PlatformMotion.GENERATED, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.periods = periods
        self.timeSteps = timeSteps
        self.waveActing = waveActing
        self.platformMotion = platformMotion
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RegularWaveAnalaysisBlueprint()


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
    def periods(self) -> int:
        """Number of periods for regular wave analysis, referring to wave or motion periods (of first vessel)"""
        return self.__periods

    @periods.setter
    def periods(self, value: int):
        """Set periods"""
        self.__periods = int(value)

    @property
    def timeSteps(self) -> int:
        """Number of integration time steps per period, recommended value: 50-120"""
        return self.__timeSteps

    @timeSteps.setter
    def timeSteps(self, value: int):
        """Set timeSteps"""
        self.__timeSteps = int(value)

    @property
    def waveActing(self) -> bool:
        """Whether there is a wave acting or not (in which case motions must be present)"""
        return self.__waveActing

    @waveActing.setter
    def waveActing(self, value: bool):
        """Set waveActing"""
        self.__waveActing = bool(value)

    @property
    def platformMotion(self) -> PlatformMotion:
        """Platform motion options:"""
        return self.__platformMotion

    @platformMotion.setter
    def platformMotion(self, value: PlatformMotion):
        """Set platformMotion"""
        self.__platformMotion = value
