# This an autogenerated file
# 
# Generated with SignalGeneratorContainer
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.signalgeneratorcontainer import SignalGeneratorContainerBlueprint
from typing import Dict
from .generatorsignal import GeneratorSignal
from .signalproperties import SignalProperties
from .signalpropertiescontainer import SignalPropertiesContainer
from sima.sima import Named
from sima.sima import ScriptableValue

class SignalGeneratorContainer(SignalPropertiesContainer,Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    properties : List[SignalProperties]
    name : str
         (default None)
    signals : List[GeneratorSignal]
    children : List[SignalGeneratorContainer]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.properties = list()
        self.name = None
        self.signals = list()
        self.children = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SignalGeneratorContainerBlueprint()


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

    @property
    def signals(self) -> List[GeneratorSignal]:
        """"""
        return self.__signals

    @signals.setter
    def signals(self, value: List[GeneratorSignal]):
        """Set signals"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__signals = value

    @property
    def children(self) -> List[SignalGeneratorContainer]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[SignalGeneratorContainer]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__children = value
