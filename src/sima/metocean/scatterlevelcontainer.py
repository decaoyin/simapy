# This an autogenerated file
# 
# Generated with ScatterLevelContainer
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scatterlevelcontainer import ScatterLevelContainerBlueprint
from typing import Dict
from sima.metocean.scatterlevel import ScatterLevel
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ScatterLevelContainer(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    levels : List[ScatterLevel]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.levels = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScatterLevelContainerBlueprint()


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
    def levels(self) -> List[ScatterLevel]:
        """"""
        return self.__levels

    @levels.setter
    def levels(self, value: List[ScatterLevel]):
        """Set levels"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__levels = value
