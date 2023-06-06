# This an autogenerated file
# 
# Generated with DirectionDependentComplexValues
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.directiondependentcomplexvalues import DirectionDependentComplexValuesBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .complexvalues import ComplexValues

class DirectionDependentComplexValues(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    directionalValues : List[ComplexValues]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.directionalValues = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DirectionDependentComplexValuesBlueprint()


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
    def directionalValues(self) -> List[ComplexValues]:
        """"""
        return self.__directionalValues

    @directionalValues.setter
    def directionalValues(self, value: List[ComplexValues]):
        """Set directionalValues"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__directionalValues = value
