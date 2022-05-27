# This an autogenerated file
# 
# Generated with BiasBladePitchFaultItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.biasbladepitchfaultitem import BiasBladePitchFaultItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class BiasBladePitchFaultItem(MOAO):
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
    startTime : float
         Start time for blade pitch fault(default 0.0)
    line : ARLine
    pitchDeviation : float
         Pitch deviation from required pitch(default 0.0)
    rampDuration : float
         Ramp duration to full pitch deviation(default 0.0)
    """

    def __init__(self , name="", description="", _id="", startTime=0.0, pitchDeviation=0.0, rampDuration=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.startTime = startTime
        self.line = None
        self.pitchDeviation = pitchDeviation
        self.rampDuration = rampDuration
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BiasBladePitchFaultItemBlueprint()


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
    def startTime(self) -> float:
        """Start time for blade pitch fault"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def line(self) -> ARLine:
        """"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def pitchDeviation(self) -> float:
        """Pitch deviation from required pitch"""
        return self.__pitchDeviation

    @pitchDeviation.setter
    def pitchDeviation(self, value: float):
        """Set pitchDeviation"""
        self.__pitchDeviation = float(value)

    @property
    def rampDuration(self) -> float:
        """Ramp duration to full pitch deviation"""
        return self.__rampDuration

    @rampDuration.setter
    def rampDuration(self, value: float):
        """Set rampDuration"""
        self.__rampDuration = float(value)
