# This an autogenerated file
# 
# Generated with CatenaryLine
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.catenaryline import CatenaryLineBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.failuremode import FailureMode
from sima.simo.inputmethodtype import InputMethodType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobodypoint import SIMOBodyPoint
    from sima.simo.linetype import LineType

class CatenaryLine(NamedObject):
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
    attachmentPoint : SIMOBodyPoint
    direction : float
         Direction of line in horizontal plane(default 0.0)
    xglobal : float
         X-coordinate of the anchor in global coordinate\nsystem(default 0.0)
    yglobal : float
         Y-coordinate of the anchor in global coordinate\nsystem(default 0.0)
    xwinch : float
         Run length of winch(default 0.0)
    xhor : float
         Horizontal distance from attachment point\nto anchor(default 0.0)
    pretension : float
         Pretension(default 0.0)
    lineType : LineType
    inputMethod : InputMethodType
         Method for initialization of line
    failureMode : FailureMode
         Failure mode of positioning element
    failureTime : float
         Earliest possible time of failure(default 0.0)
    breakingStrength : float
         Breaking strength(default 0.0)
    """

    def __init__(self , name="", description="", _id="", direction=0.0, xglobal=0.0, yglobal=0.0, xwinch=0.0, xhor=0.0, pretension=0.0, inputMethod=InputMethodType.TENSION, failureMode=FailureMode.NONE, failureTime=0.0, breakingStrength=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.attachmentPoint = None
        self.direction = direction
        self.xglobal = xglobal
        self.yglobal = yglobal
        self.xwinch = xwinch
        self.xhor = xhor
        self.pretension = pretension
        self.lineType = None
        self.inputMethod = inputMethod
        self.failureMode = failureMode
        self.failureTime = failureTime
        self.breakingStrength = breakingStrength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CatenaryLineBlueprint()


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
    def attachmentPoint(self) -> SIMOBodyPoint:
        """"""
        return self.__attachmentPoint

    @attachmentPoint.setter
    def attachmentPoint(self, value: SIMOBodyPoint):
        """Set attachmentPoint"""
        self.__attachmentPoint = value

    @property
    def direction(self) -> float:
        """Direction of line in horizontal plane"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def xglobal(self) -> float:
        """X-coordinate of the anchor in global coordinate
system"""
        return self.__xglobal

    @xglobal.setter
    def xglobal(self, value: float):
        """Set xglobal"""
        self.__xglobal = float(value)

    @property
    def yglobal(self) -> float:
        """Y-coordinate of the anchor in global coordinate
system"""
        return self.__yglobal

    @yglobal.setter
    def yglobal(self, value: float):
        """Set yglobal"""
        self.__yglobal = float(value)

    @property
    def xwinch(self) -> float:
        """Run length of winch"""
        return self.__xwinch

    @xwinch.setter
    def xwinch(self, value: float):
        """Set xwinch"""
        self.__xwinch = float(value)

    @property
    def xhor(self) -> float:
        """Horizontal distance from attachment point
to anchor"""
        return self.__xhor

    @xhor.setter
    def xhor(self, value: float):
        """Set xhor"""
        self.__xhor = float(value)

    @property
    def pretension(self) -> float:
        """Pretension"""
        return self.__pretension

    @pretension.setter
    def pretension(self, value: float):
        """Set pretension"""
        self.__pretension = float(value)

    @property
    def lineType(self) -> LineType:
        """"""
        return self.__lineType

    @lineType.setter
    def lineType(self, value: LineType):
        """Set lineType"""
        self.__lineType = value

    @property
    def inputMethod(self) -> InputMethodType:
        """Method for initialization of line"""
        return self.__inputMethod

    @inputMethod.setter
    def inputMethod(self, value: InputMethodType):
        """Set inputMethod"""
        self.__inputMethod = value

    @property
    def failureMode(self) -> FailureMode:
        """Failure mode of positioning element"""
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
