# This an autogenerated file
# 
# Generated with CustomModelReference
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.custommodelreference import CustomModelReferenceBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.workflow.modelreferenceinput import ModelReferenceInput

class CustomModelReference(CustomComponent):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    label : str
         (default "")
    tooltip : str
         (default "")
    modelReference : ModelReferenceInput
    """

    def __init__(self , _id="", label="", tooltip="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.label = label
        self.tooltip = tooltip
        self.modelReference = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomModelReferenceBlueprint()


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
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = str(value)

    @property
    def modelReference(self) -> ModelReferenceInput:
        """"""
        return self.__modelReference

    @modelReference.setter
    def modelReference(self, value: ModelReferenceInput):
        """Set modelReference"""
        self.__modelReference = value
