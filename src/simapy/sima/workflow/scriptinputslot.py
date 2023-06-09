# This an autogenerated file
# 
# Generated with ScriptInputSlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scriptinputslot import ScriptInputSlotBlueprint
from typing import Dict
from ..post import InputSlot
from ..post import SignalProperties
from ..post import SignalPropertiesContainer
from ..sima import ScriptableValue

class ScriptInputSlot(InputSlot,SignalPropertiesContainer):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[SignalProperties]
    inputSignals : bool
         If checked the input will be imported directly as signals in an array with name as specified.(default False)
    """

    def __init__(self , description="", inputSignals=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.inputSignals = inputSignals
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScriptInputSlotBlueprint()


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
    def inputSignals(self) -> bool:
        """If checked the input will be imported directly as signals in an array with name as specified."""
        return self.__inputSignals

    @inputSignals.setter
    def inputSignals(self, value: bool):
        """Set inputSignals"""
        self.__inputSignals = bool(value)