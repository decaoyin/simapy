# This an autogenerated file
# 
# Generated with StrouhalUserDefinedProperty
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.strouhaluserdefinedproperty import StrouhalUserDefinedPropertyBlueprint
from typing import Dict
from .reynoldstrouhalnumberitem import ReynoldStrouhalNumberItem
from .strouhalspecificationproperty import StrouhalSpecificationProperty
from sima.sima import ScriptableValue

class StrouhalUserDefinedProperty(StrouhalSpecificationProperty):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    reynoldStrouhalProperties : List[ReynoldStrouhalNumberItem]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.reynoldStrouhalProperties = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StrouhalUserDefinedPropertyBlueprint()


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
    def reynoldStrouhalProperties(self) -> List[ReynoldStrouhalNumberItem]:
        """"""
        return self.__reynoldStrouhalProperties

    @reynoldStrouhalProperties.setter
    def reynoldStrouhalProperties(self, value: List[ReynoldStrouhalNumberItem]):
        """Set reynoldStrouhalProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__reynoldStrouhalProperties = value
