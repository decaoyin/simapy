# This an autogenerated file
# 
# Generated with Appearance
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.appearance import AppearanceBlueprint
from typing import Dict
from .geomrepresentationtype import GeomRepresentationType
from .moao import MOAO
from .scriptablevalue import ScriptableValue
from .simacolor import SIMAColor
from .symmetry import Symmetry
from .vector3 import Vector3

class Appearance(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    graphicsfile : str
         Graphics file(default None)
    translation : Vector3
    rotation : Vector3
    scaling : Vector3
    color : SIMAColor
    geomRepresentationType : GeomRepresentationType
         Geometry representation type
    radius : float
         (default 1.0)
    transparency : float
         Transparency of geometry. No transparancy=0, Full transparency=1(default 0.0)
    symmetry : Symmetry
         Symmetric properties of the geometry
    """

    def __init__(self , description="", geomRepresentationType=GeomRepresentationType.DEFAULT_BOX, radius=1.0, transparency=0.0, symmetry=Symmetry.NONE, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.graphicsfile = None
        self.translation = None
        self.rotation = None
        self.scaling = None
        self.color = None
        self.geomRepresentationType = geomRepresentationType
        self.radius = radius
        self.transparency = transparency
        self.symmetry = symmetry
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AppearanceBlueprint()


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
    def graphicsfile(self) -> str:
        """Graphics file"""
        return self.__graphicsfile

    @graphicsfile.setter
    def graphicsfile(self, value: str):
        """Set graphicsfile"""
        self.__graphicsfile = value

    @property
    def translation(self) -> Vector3:
        """"""
        return self.__translation

    @translation.setter
    def translation(self, value: Vector3):
        """Set translation"""
        self.__translation = value

    @property
    def rotation(self) -> Vector3:
        """"""
        return self.__rotation

    @rotation.setter
    def rotation(self, value: Vector3):
        """Set rotation"""
        self.__rotation = value

    @property
    def scaling(self) -> Vector3:
        """"""
        return self.__scaling

    @scaling.setter
    def scaling(self, value: Vector3):
        """Set scaling"""
        self.__scaling = value

    @property
    def color(self) -> SIMAColor:
        """"""
        return self.__color

    @color.setter
    def color(self, value: SIMAColor):
        """Set color"""
        self.__color = value

    @property
    def geomRepresentationType(self) -> GeomRepresentationType:
        """Geometry representation type"""
        return self.__geomRepresentationType

    @geomRepresentationType.setter
    def geomRepresentationType(self, value: GeomRepresentationType):
        """Set geomRepresentationType"""
        self.__geomRepresentationType = value

    @property
    def radius(self) -> float:
        """"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def transparency(self) -> float:
        """Transparency of geometry. No transparancy=0, Full transparency=1"""
        return self.__transparency

    @transparency.setter
    def transparency(self, value: float):
        """Set transparency"""
        self.__transparency = float(value)

    @property
    def symmetry(self) -> Symmetry:
        """Symmetric properties of the geometry"""
        return self.__symmetry

    @symmetry.setter
    def symmetry(self, value: Symmetry):
        """Set symmetry"""
        self.__symmetry = value
