# This an autogenerated file
# 
# Generated with StringValue
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.stringvalue import StringValueBlueprint
from numpy import ndarray,asarray
from ..sima import ScriptableValue
from ..sima import SingleParameter
from .generatorsignal import GeneratorSignal
from .signalproperties import SignalProperties

class StringValue(GeneratorSignal,SingleParameter):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    properties : List[SignalProperties]
    name : str
         (default None)
    array : bool
         (default False)
    value : str
         Value of the String constant(default None)
    values : ndarray of str
         Value of the String constant
    """

    def __init__(self , description="", array=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.properties = list()
        self.name = None
        self.array = array
        self.value = None
        self.values = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StringValueBlueprint()


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
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def array(self) -> bool:
        """"""
        return self.__array

    @array.setter
    def array(self, value: bool):
        """Set array"""
        self.__array = bool(value)

    @property
    def value(self) -> str:
        """Value of the String constant"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = value

    @property
    def values(self) -> ndarray:
        """Value of the String constant"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        array = asarray(value, dtype=str)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__values = array