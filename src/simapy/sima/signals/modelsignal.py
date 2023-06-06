# This an autogenerated file
# 
# Generated with ModelSignal
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.modelsignal import ModelSignalBlueprint
from typing import Dict
from ..sima import MOAO
from .attribute import Attribute
from .signal import Signal

class ModelSignal(Signal):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    name : str
         (default None)
    attributes : List[Attribute]
    value : MOAO
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.name = None
        self.attributes = list()
        self.value = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ModelSignalBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def attributes(self) -> List[Attribute]:
        """"""
        return self.__attributes

    @attributes.setter
    def attributes(self, value: List[Attribute]):
        """Set attributes"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__attributes = value

    @property
    def value(self) -> MOAO:
        """"""
        return self.__value

    @value.setter
    def value(self, value: MOAO):
        """Set value"""
        self.__value = value
