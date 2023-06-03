# This an autogenerated file
# 
# Generated with ExtremeValue
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.extremevalue import ExtremeValueBlueprint
from typing import Dict
from sima.sima import MOAO
from sima.sima import ScriptableValue

class ExtremeValue(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    extreme : float
         (default 0.0)
    returnPeriod : float
         (default 0.0)
    """

    def __init__(self , description="", extreme=0.0, returnPeriod=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.extreme = extreme
        self.returnPeriod = returnPeriod
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExtremeValueBlueprint()


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
    def extreme(self) -> float:
        """"""
        return self.__extreme

    @extreme.setter
    def extreme(self, value: float):
        """Set extreme"""
        self.__extreme = float(value)

    @property
    def returnPeriod(self) -> float:
        """"""
        return self.__returnPeriod

    @returnPeriod.setter
    def returnPeriod(self, value: float):
        """Set returnPeriod"""
        self.__returnPeriod = float(value)
