# This an autogenerated file
# 
# Generated with BooleanArray
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.booleanarray import BooleanArrayBlueprint
from numpy import ndarray,asarray
from marmo.containers.attribute import Attribute
from marmo.containers.signal import Signal

class BooleanArray(Signal):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    attributes : List[Attribute]
    value : ndarray
    """

    def __init__(self , name:str="", description:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.__attributes = list()
        self.__value = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BooleanArrayBlueprint()


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
    def attributes(self) -> List[Attribute]:
        """"""
        return self.__attributes

    @attributes.setter
    def attributes(self, value: List[Attribute]):
        """Set attributes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__attributes = value

    @property
    def value(self) -> ndarray:
        """"""
        return self.__value

    @value.setter
    def value(self, value: ndarray):
        """Set value"""
        self.__value = asarray(value)
