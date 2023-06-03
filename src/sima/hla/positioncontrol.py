# This an autogenerated file
# 
# Generated with PositionControl
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.positioncontrol import PositionControlBlueprint
from typing import Dict
from sima.custom import CustomComponent
from sima.sima import Position
from sima.sima import ScriptableValue

class PositionControl(CustomComponent):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    hlaObjectId : str
         (default None)
    reference : Position
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.hlaObjectId = None
        self.reference = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PositionControlBlueprint()


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
    def hlaObjectId(self) -> str:
        """"""
        return self.__hlaObjectId

    @hlaObjectId.setter
    def hlaObjectId(self, value: str):
        """Set hlaObjectId"""
        self.__hlaObjectId = value

    @property
    def reference(self) -> Position:
        """"""
        return self.__reference

    @reference.setter
    def reference(self, value: Position):
        """Set reference"""
        self.__reference = value
