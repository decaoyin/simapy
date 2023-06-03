# This an autogenerated file
# 
# Generated with ExcitationZoneProperty
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.excitationzoneproperty import ExcitationZonePropertyBlueprint
from typing import Dict
from sima.sima import NamedObject
from sima.sima import ScriptableValue

class ExcitationZoneProperty(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    min : float
         Minimum non dimensional frequency limit(default 0.125)
    max : float
         Minimum non dimensional frequency limit(default 0.2)
    """

    def __init__(self , description="", min=0.125, max=0.2, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.min = min
        self.max = max
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExcitationZonePropertyBlueprint()


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
    def min(self) -> float:
        """Minimum non dimensional frequency limit"""
        return self.__min

    @min.setter
    def min(self, value: float):
        """Set min"""
        self.__min = float(value)

    @property
    def max(self) -> float:
        """Minimum non dimensional frequency limit"""
        return self.__max

    @max.setter
    def max(self, value: float):
        """Set max"""
        self.__max = float(value)
