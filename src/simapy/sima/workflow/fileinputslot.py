# This an autogenerated file
# 
# Generated with FileInputSlot
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fileinputslot import FileInputSlotBlueprint
from typing import Dict
from ..post import InputSlot
from ..post import SignalProperties
from ..post import SignalPropertiesContainer
from ..sima import ScriptableValue

class FileInputSlot(InputSlot,SignalPropertiesContainer):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[SignalProperties]
    filename : str
         Name of file to be imported(default None)
    specifyAdditionalProperties : bool
         Specify additional properties in the file root(default False)
    """

    def __init__(self , description="", specifyAdditionalProperties=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.filename = None
        self.specifyAdditionalProperties = specifyAdditionalProperties
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FileInputSlotBlueprint()


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
    def filename(self) -> str:
        """Name of file to be imported"""
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        """Set filename"""
        self.__filename = value

    @property
    def specifyAdditionalProperties(self) -> bool:
        """Specify additional properties in the file root"""
        return self.__specifyAdditionalProperties

    @specifyAdditionalProperties.setter
    def specifyAdditionalProperties(self, value: bool):
        """Set specifyAdditionalProperties"""
        self.__specifyAdditionalProperties = bool(value)
