# This an autogenerated file
# 
# Generated with ParameterLines
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.parameterlines import ParameterLinesBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ParameterLines(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    entityName : str
         (default "")
    floatIndex : int
         (default 0)
    value : float
         (default 0.0)
    """

    def __init__(self , _id="", entityName="", floatIndex=0, value=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.entityName = entityName
        self.floatIndex = floatIndex
        self.value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ParameterLinesBlueprint()


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
    def entityName(self) -> str:
        """"""
        return self.__entityName

    @entityName.setter
    def entityName(self, value: str):
        """Set entityName"""
        self.__entityName = str(value)

    @property
    def floatIndex(self) -> int:
        """"""
        return self.__floatIndex

    @floatIndex.setter
    def floatIndex(self, value: int):
        """Set floatIndex"""
        self.__floatIndex = int(value)

    @property
    def value(self) -> float:
        """"""
        return self.__value

    @value.setter
    def value(self, value: float):
        """Set value"""
        self.__value = float(value)
