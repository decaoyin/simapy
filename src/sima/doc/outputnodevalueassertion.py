# This an autogenerated file
# 
# Generated with OutputNodeValueAssertion
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.outputnodevalueassertion import OutputNodeValueAssertionBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.severity import Severity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.post.outputnode import OutputNode

class OutputNodeValueAssertion(MOAO):
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
    severity : Severity
    message : str
         (default "")
    outputNode : OutputNode
    path : str
         (default "")
    expectedValue : str
         (default "")
    """

    def __init__(self , name="", description="", _id="", severity=Severity.WARNING, message="", path="", expectedValue="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.severity = severity
        self.message = message
        self.outputNode = None
        self.path = path
        self.expectedValue = expectedValue
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OutputNodeValueAssertionBlueprint()


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
        self.__message = str(value)

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
        self.__path = str(value)

    @property
    def expectedValue(self) -> str:
        """"""
        return self.__expectedValue

    @expectedValue.setter
    def expectedValue(self, value: str):
        """Set expectedValue"""
        self.__expectedValue = str(value)
