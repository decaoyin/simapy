# This an autogenerated file
# 
# Generated with ContourDataPoint
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.contourdatapoint import ContourDataPointBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class ContourDataPoint(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    peakPeriod : float
         (default 0.0)
    significantWaveHeight : float
         (default 0.0)
    """

    def __init__(self , description="", peakPeriod=0.0, significantWaveHeight=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.peakPeriod = peakPeriod
        self.significantWaveHeight = significantWaveHeight
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ContourDataPointBlueprint()


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
    def peakPeriod(self) -> float:
        """"""
        return self.__peakPeriod

    @peakPeriod.setter
    def peakPeriod(self, value: float):
        """Set peakPeriod"""
        self.__peakPeriod = float(value)

    @property
    def significantWaveHeight(self) -> float:
        """"""
        return self.__significantWaveHeight

    @significantWaveHeight.setter
    def significantWaveHeight(self, value: float):
        """Set significantWaveHeight"""
        self.__significantWaveHeight = float(value)
