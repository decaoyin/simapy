# This an autogenerated file
# 
# Generated with ContourDataPoint
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.contourdatapoint import ContourDataPointBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ContourDataPoint(MOAO):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    peakPeriod : float
         (default 0.0)
    significantWaveHeight : float
         (default 0.0)
    """

    def __init__(self , name="", description="", _id="", peakPeriod=0.0, significantWaveHeight=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

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
