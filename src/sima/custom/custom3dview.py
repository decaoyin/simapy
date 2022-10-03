# This an autogenerated file
# 
# Generated with Custom3DView
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.custom3dview import Custom3DViewBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class Custom3DView(CustomComponent):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    model : MOAO
    result : str
         (default "")
    _type : str
         (default "")
    """

    def __init__(self , _id="", result="", _type="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.model = None
        self.result = result
        self._type = _type
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return Custom3DViewBlueprint()


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
    def model(self) -> MOAO:
        """"""
        return self.__model

    @model.setter
    def model(self, value: MOAO):
        """Set model"""
        self.__model = value

    @property
    def result(self) -> str:
        """"""
        return self.__result

    @result.setter
    def result(self, value: str):
        """Set result"""
        self.__result = str(value)

    @property
    def _type(self) -> str:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: str):
        """Set _type"""
        self.___type = str(value)
