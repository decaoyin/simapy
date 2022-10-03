# This an autogenerated file
# 
# Generated with ControlSystem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.controlsystem import ControlSystemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.allocationsystem import AllocationSystem
from sima.simo.controlreference import ControlReference
from sima.simo.dofcontrolconfiguration import DOFControlConfiguration
from sima.simo.estimator import Estimator
from sima.simo.guidancesystem import GuidanceSystem
from sima.simo.windmeasurement import WindMeasurement
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobody import SIMOBody

class ControlSystem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    relativeBody : SIMOBody
    xRef : float
         X-coordinate of wanted position(default 0.0)
    yRef : float
         Y-coordinate of wanted position(default 0.0)
    dirRef : float
         Wanted heading(default 0.0)
    circleXRef : float
         X-coordinate of circle center(default 0.0)
    circleYRef : float
         Y-coordinate of circle center (default 0.0)
    circleRadius : float
         Radius of the circle(default 0.0)
    xLocal : float
         X-coordinate of the point on the body which shall be positioned at the secified reference(default 0.0)
    yLocal : float
         Y-coordinate of the point on the body which shall be positioned at the specified reference(default 0.0)
    controlReference : ControlReference
         Control Reference:\n Global:              Global position\n Body Relative:  Relative to another body\n Waypoint:        Wayoint reference
    xyRelative : bool
         follow body position(default True)
    dirRelative : bool
         Follow body heading(default True)
    referenceCutOff : float
         Cut-off time in low-pass filter for position measurement of body to follow(default 0.0)
    controlConfigurations : List[DOFControlConfiguration]
    estimator : Estimator
    intialXForce : float
         Initial x value on non-measured external forces acting on the body(default 0.0)
    intialYForce : float
         Initial y value on non-measured external forces acting on the body(default 0.0)
    intialMoment : float
         Initial value on non-measured external moment acting on the body(default 0.0)
    windCutOff : float
         Cut-off time in low-pass filter for wind measurements(default 0.0)
    windMeasurement : WindMeasurement
         Flag for measurement of wind forces to be included in the controller
    allocationSystem : AllocationSystem
    guidanceSystem : GuidanceSystem
    """

    def __init__(self , _id="", xRef=0.0, yRef=0.0, dirRef=0.0, circleXRef=0.0, circleYRef=0.0, circleRadius=0.0, xLocal=0.0, yLocal=0.0, controlReference=ControlReference.GLOBAL, xyRelative=True, dirRelative=True, referenceCutOff=0.0, intialXForce=0.0, intialYForce=0.0, intialMoment=0.0, windCutOff=0.0, windMeasurement=WindMeasurement.NO, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.relativeBody = None
        self.xRef = xRef
        self.yRef = yRef
        self.dirRef = dirRef
        self.circleXRef = circleXRef
        self.circleYRef = circleYRef
        self.circleRadius = circleRadius
        self.xLocal = xLocal
        self.yLocal = yLocal
        self.controlReference = controlReference
        self.xyRelative = xyRelative
        self.dirRelative = dirRelative
        self.referenceCutOff = referenceCutOff
        self.controlConfigurations = list()
        self.estimator = None
        self.intialXForce = intialXForce
        self.intialYForce = intialYForce
        self.intialMoment = intialMoment
        self.windCutOff = windCutOff
        self.windMeasurement = windMeasurement
        self.allocationSystem = None
        self.guidanceSystem = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ControlSystemBlueprint()


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
    def relativeBody(self) -> SIMOBody:
        """"""
        return self.__relativeBody

    @relativeBody.setter
    def relativeBody(self, value: SIMOBody):
        """Set relativeBody"""
        self.__relativeBody = value

    @property
    def xRef(self) -> float:
        """X-coordinate of wanted position"""
        return self.__xRef

    @xRef.setter
    def xRef(self, value: float):
        """Set xRef"""
        self.__xRef = float(value)

    @property
    def yRef(self) -> float:
        """Y-coordinate of wanted position"""
        return self.__yRef

    @yRef.setter
    def yRef(self, value: float):
        """Set yRef"""
        self.__yRef = float(value)

    @property
    def dirRef(self) -> float:
        """Wanted heading"""
        return self.__dirRef

    @dirRef.setter
    def dirRef(self, value: float):
        """Set dirRef"""
        self.__dirRef = float(value)

    @property
    def circleXRef(self) -> float:
        """X-coordinate of circle center"""
        return self.__circleXRef

    @circleXRef.setter
    def circleXRef(self, value: float):
        """Set circleXRef"""
        self.__circleXRef = float(value)

    @property
    def circleYRef(self) -> float:
        """Y-coordinate of circle center """
        return self.__circleYRef

    @circleYRef.setter
    def circleYRef(self, value: float):
        """Set circleYRef"""
        self.__circleYRef = float(value)

    @property
    def circleRadius(self) -> float:
        """Radius of the circle"""
        return self.__circleRadius

    @circleRadius.setter
    def circleRadius(self, value: float):
        """Set circleRadius"""
        self.__circleRadius = float(value)

    @property
    def xLocal(self) -> float:
        """X-coordinate of the point on the body which shall be positioned at the secified reference"""
        return self.__xLocal

    @xLocal.setter
    def xLocal(self, value: float):
        """Set xLocal"""
        self.__xLocal = float(value)

    @property
    def yLocal(self) -> float:
        """Y-coordinate of the point on the body which shall be positioned at the specified reference"""
        return self.__yLocal

    @yLocal.setter
    def yLocal(self, value: float):
        """Set yLocal"""
        self.__yLocal = float(value)

    @property
    def controlReference(self) -> ControlReference:
        """Control Reference:
 Global:              Global position
 Body Relative:  Relative to another body
 Waypoint:        Wayoint reference"""
        return self.__controlReference

    @controlReference.setter
    def controlReference(self, value: ControlReference):
        """Set controlReference"""
        self.__controlReference = value

    @property
    def xyRelative(self) -> bool:
        """follow body position"""
        return self.__xyRelative

    @xyRelative.setter
    def xyRelative(self, value: bool):
        """Set xyRelative"""
        self.__xyRelative = bool(value)

    @property
    def dirRelative(self) -> bool:
        """Follow body heading"""
        return self.__dirRelative

    @dirRelative.setter
    def dirRelative(self, value: bool):
        """Set dirRelative"""
        self.__dirRelative = bool(value)

    @property
    def referenceCutOff(self) -> float:
        """Cut-off time in low-pass filter for position measurement of body to follow"""
        return self.__referenceCutOff

    @referenceCutOff.setter
    def referenceCutOff(self, value: float):
        """Set referenceCutOff"""
        self.__referenceCutOff = float(value)

    @property
    def controlConfigurations(self) -> List[DOFControlConfiguration]:
        """"""
        return self.__controlConfigurations

    @controlConfigurations.setter
    def controlConfigurations(self, value: List[DOFControlConfiguration]):
        """Set controlConfigurations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlConfigurations = value

    @property
    def estimator(self) -> Estimator:
        """"""
        return self.__estimator

    @estimator.setter
    def estimator(self, value: Estimator):
        """Set estimator"""
        self.__estimator = value

    @property
    def intialXForce(self) -> float:
        """Initial x value on non-measured external forces acting on the body"""
        return self.__intialXForce

    @intialXForce.setter
    def intialXForce(self, value: float):
        """Set intialXForce"""
        self.__intialXForce = float(value)

    @property
    def intialYForce(self) -> float:
        """Initial y value on non-measured external forces acting on the body"""
        return self.__intialYForce

    @intialYForce.setter
    def intialYForce(self, value: float):
        """Set intialYForce"""
        self.__intialYForce = float(value)

    @property
    def intialMoment(self) -> float:
        """Initial value on non-measured external moment acting on the body"""
        return self.__intialMoment

    @intialMoment.setter
    def intialMoment(self, value: float):
        """Set intialMoment"""
        self.__intialMoment = float(value)

    @property
    def windCutOff(self) -> float:
        """Cut-off time in low-pass filter for wind measurements"""
        return self.__windCutOff

    @windCutOff.setter
    def windCutOff(self, value: float):
        """Set windCutOff"""
        self.__windCutOff = float(value)

    @property
    def windMeasurement(self) -> WindMeasurement:
        """Flag for measurement of wind forces to be included in the controller"""
        return self.__windMeasurement

    @windMeasurement.setter
    def windMeasurement(self, value: WindMeasurement):
        """Set windMeasurement"""
        self.__windMeasurement = value

    @property
    def allocationSystem(self) -> AllocationSystem:
        """"""
        return self.__allocationSystem

    @allocationSystem.setter
    def allocationSystem(self, value: AllocationSystem):
        """Set allocationSystem"""
        self.__allocationSystem = value

    @property
    def guidanceSystem(self) -> GuidanceSystem:
        """"""
        return self.__guidanceSystem

    @guidanceSystem.setter
    def guidanceSystem(self, value: GuidanceSystem):
        """Set guidanceSystem"""
        self.__guidanceSystem = value
