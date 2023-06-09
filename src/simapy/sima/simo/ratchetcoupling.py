# This an autogenerated file
# 
# Generated with RatchetCoupling
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.ratchetcoupling import RatchetCouplingBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue
from .failuremode import FailureMode
from .ratchettype import RatchetType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simobodypoint import SIMOBodyPoint

class RatchetCoupling(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    endPoint1 : SIMOBodyPoint
    endPoint2 : SIMOBodyPoint
    _type : RatchetType
         Ratchet type
    staticForce : float
         Static force in element(default 0.0)
    stiffness : float
         Element stiffness(default 0.0)
    startTime : float
         Time when dynamics in element will be activated(default 0.0)
    dampingCoefficient : float
         Damping coefficient(default 0.0)
    exponent : float
         Exponent in damping(default 0.0)
    minVelocity : float
         Velocity limit for damping force(default 0.0)
    failureMode : FailureMode
         Failure mode of coupling element
    failureTime : float
         Earliest possible time of failure(default 0.0)
    maximumForce : float
         Maximum force(default 0.0)
    """

    def __init__(self , description="", _type=RatchetType.TENSION, staticForce=0.0, stiffness=0.0, startTime=0.0, dampingCoefficient=0.0, exponent=0.0, minVelocity=0.0, failureMode=FailureMode.NONE, failureTime=0.0, maximumForce=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.endPoint1 = None
        self.endPoint2 = None
        self._type = _type
        self.staticForce = staticForce
        self.stiffness = stiffness
        self.startTime = startTime
        self.dampingCoefficient = dampingCoefficient
        self.exponent = exponent
        self.minVelocity = minVelocity
        self.failureMode = failureMode
        self.failureTime = failureTime
        self.maximumForce = maximumForce
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RatchetCouplingBlueprint()


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
    def endPoint1(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint1

    @endPoint1.setter
    def endPoint1(self, value: SIMOBodyPoint):
        """Set endPoint1"""
        self.__endPoint1 = value

    @property
    def endPoint2(self) -> SIMOBodyPoint:
        """"""
        return self.__endPoint2

    @endPoint2.setter
    def endPoint2(self, value: SIMOBodyPoint):
        """Set endPoint2"""
        self.__endPoint2 = value

    @property
    def _type(self) -> RatchetType:
        """Ratchet type"""
        return self.___type

    @_type.setter
    def _type(self, value: RatchetType):
        """Set _type"""
        self.___type = value

    @property
    def staticForce(self) -> float:
        """Static force in element"""
        return self.__staticForce

    @staticForce.setter
    def staticForce(self, value: float):
        """Set staticForce"""
        self.__staticForce = float(value)

    @property
    def stiffness(self) -> float:
        """Element stiffness"""
        return self.__stiffness

    @stiffness.setter
    def stiffness(self, value: float):
        """Set stiffness"""
        self.__stiffness = float(value)

    @property
    def startTime(self) -> float:
        """Time when dynamics in element will be activated"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def dampingCoefficient(self) -> float:
        """Damping coefficient"""
        return self.__dampingCoefficient

    @dampingCoefficient.setter
    def dampingCoefficient(self, value: float):
        """Set dampingCoefficient"""
        self.__dampingCoefficient = float(value)

    @property
    def exponent(self) -> float:
        """Exponent in damping"""
        return self.__exponent

    @exponent.setter
    def exponent(self, value: float):
        """Set exponent"""
        self.__exponent = float(value)

    @property
    def minVelocity(self) -> float:
        """Velocity limit for damping force"""
        return self.__minVelocity

    @minVelocity.setter
    def minVelocity(self, value: float):
        """Set minVelocity"""
        self.__minVelocity = float(value)

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
    def maximumForce(self) -> float:
        """Maximum force"""
        return self.__maximumForce

    @maximumForce.setter
    def maximumForce(self, value: float):
        """Set maximumForce"""
        self.__maximumForce = float(value)