# This an autogenerated file
# 
# Generated with ConditionTaskCondition
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.conditiontaskcondition import ConditionTaskConditionBlueprint
from typing import Dict
from sima.sima.condition import Condition
from sima.sima.scriptablevalue import ScriptableValue

class ConditionTaskCondition(Condition):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    """

    def __init__(self , _id="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ConditionTaskConditionBlueprint()


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
