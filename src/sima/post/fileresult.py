# This an autogenerated file
# 
# Generated with FileResult
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fileresult import FileResultBlueprint
from typing import Dict
from .signalstorage import SignalStorage
from sima.sima import ScriptableValue

class FileResult(SignalStorage):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    filename : str
         (default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.filename = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FileResultBlueprint()


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
    def filename(self) -> str:
        """"""
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        """Set filename"""
        self.__filename = value
