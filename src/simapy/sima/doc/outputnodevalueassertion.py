# This an autogenerated file
# 
# Generated with OutputNodeValueAssertion
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.outputnodevalueassertion import OutputNodeValueAssertionBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from ..sima import Severity
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..post import OutputNode

class OutputNodeValueAssertion(MOAO):
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
    expectedValue : str
         When expected value is a number, the number of significant digits will be used as a tolerance level(default None)
    tolerance : float
         When set, will be used instead of the implicit toleranse based on significant digits(default 0.0)
    """

    def __init__(self , description="", severity=Severity.WARNING, tolerance=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.severity = severity
        self.message = None
        self.outputNode = None
        self.path = None
        self.expectedValue = None
        self.tolerance = tolerance
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OutputNodeValueAssertionBlueprint()


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
    def expectedValue(self) -> str:
        """When expected value is a number, the number of significant digits will be used as a tolerance level"""
        return self.__expectedValue

    @expectedValue.setter
    def expectedValue(self, value: str):
        """Set expectedValue"""
        self.__expectedValue = value

    @property
    def tolerance(self) -> float:
        """When set, will be used instead of the implicit toleranse based on significant digits"""
        return self.__tolerance

    @tolerance.setter
    def tolerance(self, value: float):
        """Set tolerance"""
        self.__tolerance = float(value)
