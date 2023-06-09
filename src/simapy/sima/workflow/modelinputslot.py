# This an autogenerated file
# 
# Generated with ModelInputSlot
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.modelinputslot import ModelInputSlotBlueprint
from typing import Dict
from ..post import InputSlot
from ..sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..sima import ModelReferenceVariable

class ModelInputSlot(InputSlot):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    reference : ModelReferenceVariable
         Model reference to be replaced
    replaceChildren : bool
         If checked the children of the reference will replaced(default False)
    """

    def __init__(self , description="", replaceChildren=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.reference = None
        self.replaceChildren = replaceChildren
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ModelInputSlotBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def reference(self) -> ModelReferenceVariable:
        """Model reference to be replaced"""
        return self.__reference

    @reference.setter
    def reference(self, value: ModelReferenceVariable):
        """Set reference"""
        self.__reference = value

    @property
    def replaceChildren(self) -> bool:
        """If checked the children of the reference will replaced"""
        return self.__replaceChildren

    @replaceChildren.setter
    def replaceChildren(self, value: bool):
        """Set replaceChildren"""
        self.__replaceChildren = bool(value)