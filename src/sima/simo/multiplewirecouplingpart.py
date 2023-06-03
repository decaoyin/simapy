# This an autogenerated file
# 
# Generated with MultipleWireCouplingPart
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.multiplewirecouplingpart import MultipleWireCouplingPartBlueprint
from typing import Dict
from .failuremode import FailureMode
from sima.sima import NamedObject
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simobodypoint import SIMOBodyPoint

class MultipleWireCouplingPart(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    endPoint : SIMOBodyPoint
    ea : float
         Wire cross section stiffness(default 0.0)
    length : float
         Initial, unstretched wire length(default 0.0)
    damping : float
         Material damping(default 0.0)
    flexibility : float
         Connection flexibility(default 0.0)
    failureMode : FailureMode
         Failure mode of coupling element
    failureTime : float
         Earliest possible time of failure(default 0.0)
    breakingStrength : float
         Breaking strength(default 0.0)
    """

    def __init__(self , description="", ea=0.0, length=0.0, damping=0.0, flexibility=0.0, failureMode=FailureMode.NONE, failureTime=0.0, breakingStrength=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.endPoint = None
        self.ea = ea
        self.length = length
        self.damping = damping
        self.flexibility = flexibility
        self.failureMode = failureMode
        self.failureTime = failureTime
        self.breakingStrength = breakingStrength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MultipleWireCouplingPartBlueprint()


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
    def endPoint(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint

    @endPoint.setter
    def endPoint(self, value: SIMOBodyPoint):
        """Set endPoint"""
        self.__endPoint = value

    @property
    def ea(self) -> float:
        """Wire cross section stiffness"""
        return self.__ea

    @ea.setter
    def ea(self, value: float):
        """Set ea"""
        self.__ea = float(value)

    @property
    def length(self) -> float:
        """Initial, unstretched wire length"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def damping(self) -> float:
        """Material damping"""
        return self.__damping

    @damping.setter
    def damping(self, value: float):
        """Set damping"""
        self.__damping = float(value)

    @property
    def flexibility(self) -> float:
        """Connection flexibility"""
        return self.__flexibility

    @flexibility.setter
    def flexibility(self, value: float):
        """Set flexibility"""
        self.__flexibility = float(value)

    @property
    def failureMode(self) -> FailureMode:
        """Failure mode of coupling element"""
        return self.__failureMode

    @failureMode.setter
    def failureMode(self, value: FailureMode):
        """Set failureMode"""
        self.__failureMode = value

    @property
    def failureTime(self) -> float:
        """Earliest possible time of failure"""
        return self.__failureTime

    @failureTime.setter
    def failureTime(self, value: float):
        """Set failureTime"""
        self.__failureTime = float(value)

    @property
    def breakingStrength(self) -> float:
        """Breaking strength"""
        return self.__breakingStrength

    @breakingStrength.setter
    def breakingStrength(self, value: float):
        """Set breakingStrength"""
        self.__breakingStrength = float(value)
