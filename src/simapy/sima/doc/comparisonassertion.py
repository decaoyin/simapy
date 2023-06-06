# This an autogenerated file
# 
# Generated with ComparisonAssertion
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.comparisonassertion import ComparisonAssertionBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from ..sima import Severity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..post import OutputNode

class ComparisonAssertion(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    severity : Severity
    message : str
         (default None)
    outputNode : OutputNode
    path : str
         (default None)
    read : bool
         If the path points to a file, the file will be read(default False)
    expectedOutput : str
         Expected output represented by the content of this file(default None)
    """

    def __init__(self , description="", severity=Severity.WARNING, read=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.severity = severity
        self.message = None
        self.outputNode = None
        self.path = None
        self.read = read
        self.expectedOutput = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ComparisonAssertionBlueprint()


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
    def severity(self) -> Severity:
        """"""
        return self.__severity

    @severity.setter
    def severity(self, value: Severity):
        """Set severity"""
        self.__severity = value

    @property
    def message(self) -> str:
        """"""
        return self.__message

    @message.setter
    def message(self, value: str):
        """Set message"""
        self.__message = value

    @property
    def outputNode(self) -> OutputNode:
        """"""
        return self.__outputNode

    @outputNode.setter
    def outputNode(self, value: OutputNode):
        """Set outputNode"""
        self.__outputNode = value

    @property
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value

    @property
    def read(self) -> bool:
        """If the path points to a file, the file will be read"""
        return self.__read

    @read.setter
    def read(self, value: bool):
        """Set read"""
        self.__read = bool(value)

    @property
    def expectedOutput(self) -> str:
        """Expected output represented by the content of this file"""
        return self.__expectedOutput

    @expectedOutput.setter
    def expectedOutput(self, value: str):
        """Set expectedOutput"""
        self.__expectedOutput = value
