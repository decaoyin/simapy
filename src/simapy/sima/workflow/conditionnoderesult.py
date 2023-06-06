# This an autogenerated file
# 
# Generated with ConditionNodeResult
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.conditionnoderesult import ConditionNodeResultBlueprint
from numpy import ndarray,asarray
from ..post import SignalStorage
from ..sima import ResultContainer
from ..sima import ScriptableValue

class ConditionNodeResult(SignalStorage):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    resultContainer : ResultContainer
    filenames : ndarray of str
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.resultContainer = None
        self.filenames = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ConditionNodeResultBlueprint()


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
    def resultContainer(self) -> ResultContainer:
        """"""
        return self.__resultContainer

    @resultContainer.setter
    def resultContainer(self, value: ResultContainer):
        """Set resultContainer"""
        self.__resultContainer = value

    @property
    def filenames(self) -> ndarray:
        """"""
        return self.__filenames

    @filenames.setter
    def filenames(self, value: ndarray):
        """Set filenames"""
        array = asarray(value, dtype=str)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__filenames = array
