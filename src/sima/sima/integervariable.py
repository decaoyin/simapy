# This an autogenerated file
# 
# Generated with IntegerVariable
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.integervariable import IntegerVariableBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.variable import Variable

class IntegerVariable(Variable):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    value : int
         The current value for the variable(default 0)
    """

    def __init__(self , name="", description="", _id="", value=0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.value = value
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return IntegerVariableBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

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
    def value(self) -> int:
        """The current value for the variable"""
        return self.__value

    @value.setter
    def value(self, value: int):
        """Set value"""
        self.__value = int(value)
