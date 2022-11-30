# This an autogenerated file
# 
# Generated with CurrentVariationItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.currentvariationitem import CurrentVariationItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CurrentVariationItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    velocityIncrement : float
         Current velocity increment(default 0.0)
    directionIncrement : float
         Current direction increment(default 0.0)
    """

    def __init__(self , description="", velocityIncrement=0.0, directionIncrement=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.velocityIncrement = velocityIncrement
        self.directionIncrement = directionIncrement
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CurrentVariationItemBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def velocityIncrement(self) -> float:
        """Current velocity increment"""
        return self.__velocityIncrement

    @velocityIncrement.setter
    def velocityIncrement(self, value: float):
        """Set velocityIncrement"""
        self.__velocityIncrement = float(value)

    @property
    def directionIncrement(self) -> float:
        """Current direction increment"""
        return self.__directionIncrement

    @directionIncrement.setter
    def directionIncrement(self, value: float):
        """Set directionIncrement"""
        self.__directionIncrement = float(value)
