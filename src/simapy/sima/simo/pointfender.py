# This an autogenerated file
# 
# Generated with PointFender
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.pointfender import PointFenderBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import Point3
from ..sima import ScriptableValue
from .forcedampingcharacteristic import ForceDampingCharacteristic
from .plane import Plane
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .simobody import SIMOBody

class PointFender(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    dynamicFriction : float
         Dynamic friction coefficient, sliding(default 0.0)
    staticFriction : float
         Friction coefficient, when not sliding (stiction)(default 0.0)
    shearStiffnes : float
         Shear stiffness associated with friction(default 0.0)
    velocityLimit : float
         Velocity limit for normal friction force(default 0.0)
    contactPlane : Plane
    characteristic : ForceDampingCharacteristic
    pointBody : SIMOBody
    planeBody : SIMOBody
    contactPoints : List[Point3]
    """

    def __init__(self , description="", dynamicFriction=0.0, staticFriction=0.0, shearStiffnes=0.0, velocityLimit=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.dynamicFriction = dynamicFriction
        self.staticFriction = staticFriction
        self.shearStiffnes = shearStiffnes
        self.velocityLimit = velocityLimit
        self.contactPlane = None
        self.characteristic = None
        self.pointBody = None
        self.planeBody = None
        self.contactPoints = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PointFenderBlueprint()


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
    def dynamicFriction(self) -> float:
        """Dynamic friction coefficient, sliding"""
        return self.__dynamicFriction

    @dynamicFriction.setter
    def dynamicFriction(self, value: float):
        """Set dynamicFriction"""
        self.__dynamicFriction = float(value)

    @property
    def staticFriction(self) -> float:
        """Friction coefficient, when not sliding (stiction)"""
        return self.__staticFriction

    @staticFriction.setter
    def staticFriction(self, value: float):
        """Set staticFriction"""
        self.__staticFriction = float(value)

    @property
    def shearStiffnes(self) -> float:
        """Shear stiffness associated with friction"""
        return self.__shearStiffnes

    @shearStiffnes.setter
    def shearStiffnes(self, value: float):
        """Set shearStiffnes"""
        self.__shearStiffnes = float(value)

    @property
    def velocityLimit(self) -> float:
        """Velocity limit for normal friction force"""
        return self.__velocityLimit

    @velocityLimit.setter
    def velocityLimit(self, value: float):
        """Set velocityLimit"""
        self.__velocityLimit = float(value)

    @property
    def contactPlane(self) -> Plane:
        """"""
        return self.__contactPlane

    @contactPlane.setter
    def contactPlane(self, value: Plane):
        """Set contactPlane"""
        self.__contactPlane = value

    @property
    def characteristic(self) -> ForceDampingCharacteristic:
        """"""
        return self.__characteristic

    @characteristic.setter
    def characteristic(self, value: ForceDampingCharacteristic):
        """Set characteristic"""
        self.__characteristic = value

    @property
    def pointBody(self) -> SIMOBody:
        """"""
        return self.__pointBody

    @pointBody.setter
    def pointBody(self, value: SIMOBody):
        """Set pointBody"""
        self.__pointBody = value

    @property
    def planeBody(self) -> SIMOBody:
        """"""
        return self.__planeBody

    @planeBody.setter
    def planeBody(self, value: SIMOBody):
        """Set planeBody"""
        self.__planeBody = value

    @property
    def contactPoints(self) -> List[Point3]:
        """"""
        return self.__contactPoints

    @contactPoints.setter
    def contactPoints(self, value: List[Point3]):
        """Set contactPoints"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__contactPoints = value
