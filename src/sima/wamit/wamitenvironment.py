# This an autogenerated file
# 
# Generated with WamitEnvironment
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wamitenvironment import WamitEnvironmentBlueprint
from typing import Dict
from sima.sima.conditionselectable import ConditionSelectable
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.wamit.wamitwave import WamitWave

class WamitEnvironment(NamedObject,ConditionSelectable):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    wave : WamitWave
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.wave = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WamitEnvironmentBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def wave(self) -> WamitWave:
        """"""
        return self.__wave

    @wave.setter
    def wave(self, value: WamitWave):
        """Set wave"""
        self.__wave = value
