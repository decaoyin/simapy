# This an autogenerated file
# 
# Generated with Vector3
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.vector3 import Vector3Blueprint
from typing import Dict
from .moao import MOAO
from .scriptablevalue import ScriptableValue

class Vector3(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    x : float
         X component(default 0.0)
    y : float
         Y component(default 0.0)
    z : float
         Z component(default 0.0)
    """

    def __init__(self , description="", x=0.0, y=0.0, z=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.x = x
        self.y = y
        self.z = z
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return Vector3Blueprint()


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
    def x(self) -> float:
        """X component"""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """Y component"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def z(self) -> float:
        """Z component"""
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)
