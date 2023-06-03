# This an autogenerated file
# 
# Generated with SectorExtreme
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.sectorextreme import SectorExtremeBlueprint
from typing import Dict
from .extremevalue import ExtremeValue
from sima.sima import MOAO
from sima.sima import ScriptableValue

class SectorExtreme(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    sector : float
         (default 0.0)
    probability : float
         (default 0.0)
    extremeValues : List[ExtremeValue]
    """

    def __init__(self , description="", sector=0.0, probability=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.sector = sector
        self.probability = probability
        self.extremeValues = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SectorExtremeBlueprint()


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
    def sector(self) -> float:
        """"""
        return self.__sector

    @sector.setter
    def sector(self, value: float):
        """Set sector"""
        self.__sector = float(value)

    @property
    def probability(self) -> float:
        """"""
        return self.__probability

    @probability.setter
    def probability(self, value: float):
        """Set probability"""
        self.__probability = float(value)

    @property
    def extremeValues(self) -> List[ExtremeValue]:
        """"""
        return self.__extremeValues

    @extremeValues.setter
    def extremeValues(self, value: List[ExtremeValue]):
        """Set extremeValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__extremeValues = value
