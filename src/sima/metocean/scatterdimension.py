# This an autogenerated file
# 
# Generated with ScatterDimension
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scatterdimension import ScatterDimensionBlueprint
from numpy import ndarray,asarray
from sima.sima import MOAO
from sima.sima import ScriptableValue

class ScatterDimension(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    nValues : int
         (default 0)
    values : ndarray of float
         Scatter values
    """

    def __init__(self , description="", nValues=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.nValues = nValues
        self.values = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScatterDimensionBlueprint()


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
    def nValues(self) -> int:
        """"""
        return self.__nValues

    @nValues.setter
    def nValues(self, value: int):
        """Set nValues"""
        self.__nValues = int(value)

    @property
    def values(self) -> ndarray:
        """Scatter values"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__values = array
