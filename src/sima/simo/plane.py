# This an autogenerated file
# 
# Generated with Plane
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.plane import PlaneBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.vector3 import Vector3

class Plane(MOAO):
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
    unlimited : bool
         Whether the fender plane is limited to a restricted sector(default False)
    width : float
         Width of plane(default 0.0)
    length : float
         Length of plane(default 0.0)
    point : Point3
    normalVector : Vector3
    parallelVector : Vector3
    """

    def __init__(self , name="", description="", _id="", unlimited=False, width=0.0, length=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.unlimited = unlimited
        self.width = width
        self.length = length
        self.point = None
        self.normalVector = None
        self.parallelVector = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PlaneBlueprint()


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
    def unlimited(self) -> bool:
        """Whether the fender plane is limited to a restricted sector"""
        return self.__unlimited

    @unlimited.setter
    def unlimited(self, value: bool):
        """Set unlimited"""
        self.__unlimited = bool(value)

    @property
    def width(self) -> float:
        """Width of plane"""
        return self.__width

    @width.setter
    def width(self, value: float):
        """Set width"""
        self.__width = float(value)

    @property
    def length(self) -> float:
        """Length of plane"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def point(self) -> Point3:
        """"""
        return self.__point

    @point.setter
    def point(self, value: Point3):
        """Set point"""
        self.__point = value

    @property
    def normalVector(self) -> Vector3:
        """"""
        return self.__normalVector

    @normalVector.setter
    def normalVector(self, value: Vector3):
        """Set normalVector"""
        self.__normalVector = value

    @property
    def parallelVector(self) -> Vector3:
        """"""
        return self.__parallelVector

    @parallelVector.setter
    def parallelVector(self, value: Vector3):
        """Set parallelVector"""
        self.__parallelVector = value
