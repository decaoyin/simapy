# This an autogenerated file
# 
# Generated with WorkflowSetItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowsetitem import WorkflowSetItemBlueprint
from numpy import ndarray,asarray
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class WorkflowSetItem(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    parameterId : str
         (default "")
    values : ndarray
    """

    def __init__(self , _id="", parameterId="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.parameterId = parameterId
        self.values = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowSetItemBlueprint()


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
    def parameterId(self) -> str:
        """"""
        return self.__parameterId

    @parameterId.setter
    def parameterId(self, value: str):
        """Set parameterId"""
        self.__parameterId = str(value)

    @property
    def values(self) -> ndarray:
        """"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        self.__values = asarray(value)
