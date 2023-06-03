# This an autogenerated file
# 
# Generated with GeneratorSignal
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.generatorsignal import GeneratorSignalBlueprint
from typing import Dict
from .signalproperties import SignalProperties
from .signalpropertiescontainer import SignalPropertiesContainer
from sima.sima import Named
from sima.sima import ScriptableValue

class GeneratorSignal(SignalPropertiesContainer,Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    properties : List[SignalProperties]
    name : str
         (default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.properties = list()
        self.name = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeneratorSignalBlueprint()


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
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value
