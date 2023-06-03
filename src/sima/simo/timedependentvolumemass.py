# This an autogenerated file
# 
# Generated with TimeDependentVolumeMass
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.timedependentvolumemass import TimeDependentVolumeMassBlueprint
from typing import Dict
from .flowrateitem import FlowRateItem
from .volumemassportion import VolumeMassPortion
from sima.sima import NamedObject
from sima.sima import Point3
from sima.sima import ScriptableValue
from sima.sima import Vector3

class TimeDependentVolumeMass(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    point : Point3
         Mass point (local coordinates).
    flowRates : List[FlowRateItem]
    vol0 : float
         Volume of liquid at t=0(default 0.0)
    volMax : float
         Maximum allowable volume(default 0.0)
    volMin : float
         Minimum allowable volume(default 0.0)
    volRateMax : float
         Maximum allowable volume rate (HLA only)(default 0.0)
    volRateMin : float
         Minimum allowable volume rate (HLA only)(default 0.0)
    density : float
         Density of liquid in tank(default 0.0)
    vectorZ : Vector3
         Vector defining portion z-axis in local system
    vectorXZ : Vector3
         Vector in local xz-plane def. portion x-axis
    portions : List[VolumeMassPortion]
    """

    def __init__(self , description="", vol0=0.0, volMax=0.0, volMin=0.0, volRateMax=0.0, volRateMin=0.0, density=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.point = None
        self.flowRates = list()
        self.vol0 = vol0
        self.volMax = volMax
        self.volMin = volMin
        self.volRateMax = volRateMax
        self.volRateMin = volRateMin
        self.density = density
        self.vectorZ = None
        self.vectorXZ = None
        self.portions = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TimeDependentVolumeMassBlueprint()


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
    def point(self) -> Point3:
        """Mass point (local coordinates)."""
        return self.__point

    @point.setter
    def point(self, value: Point3):
        """Set point"""
        self.__point = value

    @property
    def flowRates(self) -> List[FlowRateItem]:
        """"""
        return self.__flowRates

    @flowRates.setter
    def flowRates(self, value: List[FlowRateItem]):
        """Set flowRates"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__flowRates = value

    @property
    def vol0(self) -> float:
        """Volume of liquid at t=0"""
        return self.__vol0

    @vol0.setter
    def vol0(self, value: float):
        """Set vol0"""
        self.__vol0 = float(value)

    @property
    def volMax(self) -> float:
        """Maximum allowable volume"""
        return self.__volMax

    @volMax.setter
    def volMax(self, value: float):
        """Set volMax"""
        self.__volMax = float(value)

    @property
    def volMin(self) -> float:
        """Minimum allowable volume"""
        return self.__volMin

    @volMin.setter
    def volMin(self, value: float):
        """Set volMin"""
        self.__volMin = float(value)

    @property
    def volRateMax(self) -> float:
        """Maximum allowable volume rate (HLA only)"""
        return self.__volRateMax

    @volRateMax.setter
    def volRateMax(self, value: float):
        """Set volRateMax"""
        self.__volRateMax = float(value)

    @property
    def volRateMin(self) -> float:
        """Minimum allowable volume rate (HLA only)"""
        return self.__volRateMin

    @volRateMin.setter
    def volRateMin(self, value: float):
        """Set volRateMin"""
        self.__volRateMin = float(value)

    @property
    def density(self) -> float:
        """Density of liquid in tank"""
        return self.__density

    @density.setter
    def density(self, value: float):
        """Set density"""
        self.__density = float(value)

    @property
    def vectorZ(self) -> Vector3:
        """Vector defining portion z-axis in local system"""
        return self.__vectorZ

    @vectorZ.setter
    def vectorZ(self, value: Vector3):
        """Set vectorZ"""
        self.__vectorZ = value

    @property
    def vectorXZ(self) -> Vector3:
        """Vector in local xz-plane def. portion x-axis"""
        return self.__vectorXZ

    @vectorXZ.setter
    def vectorXZ(self, value: Vector3):
        """Set vectorXZ"""
        self.__vectorXZ = value

    @property
    def portions(self) -> List[VolumeMassPortion]:
        """"""
        return self.__portions

    @portions.setter
    def portions(self, value: List[VolumeMassPortion]):
        """Set portions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__portions = value
