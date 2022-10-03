# This an autogenerated file
# 
# Generated with VariableInputItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.variableinputitem import VariableInputItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.singleparameter import SingleParameter

class VariableInputItem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    parameter : SingleParameter
    variation : str
         (default "")
    """

    def __init__(self , _id="", variation="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.parameter = None
        self.variation = variation
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VariableInputItemBlueprint()


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
    def parameter(self) -> SingleParameter:
        """"""
        return self.__parameter

    @parameter.setter
    def parameter(self, value: SingleParameter):
        """Set parameter"""
        self.__parameter = value

    @property
    def variation(self) -> str:
        """"""
        return self.__variation

    @variation.setter
    def variation(self, value: str):
        """Set variation"""
        self.__variation = str(value)
