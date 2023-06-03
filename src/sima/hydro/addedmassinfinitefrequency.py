# This an autogenerated file
# 
# Generated with AddedMassInfiniteFrequency
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.addedmassinfinitefrequency import AddedMassInfiniteFrequencyBlueprint
from numpy import ndarray,asarray
from .matrix6 import Matrix6
from sima.sima import ScriptableValue

class AddedMassInfiniteFrequency(Matrix6):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    values : ndarray of float
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.values = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AddedMassInfiniteFrequencyBlueprint()


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
    def values(self) -> ndarray:
        """"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        array = asarray(value, dtype=float)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__values = array
