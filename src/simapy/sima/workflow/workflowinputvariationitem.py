# This an autogenerated file
# 
# Generated with WorkflowInputVariationItem
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowinputvariationitem import WorkflowInputVariationItemBlueprint
from numpy import ndarray,asarray
from ..sima import ScriptableValue
from .workflowlinkitem import WorkflowLinkItem

class WorkflowInputVariationItem(WorkflowLinkItem):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    fromId : str
         (default None)
    toId : str
         (default None)
    runRoots : ndarray of str
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.fromId = None
        self.toId = None
        self.runRoots = []
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowInputVariationItemBlueprint()


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
    def fromId(self) -> str:
        """"""
        return self.__fromId

    @fromId.setter
    def fromId(self, value: str):
        """Set fromId"""
        self.__fromId = value

    @property
    def toId(self) -> str:
        """"""
        return self.__toId

    @toId.setter
    def toId(self, value: str):
        """Set toId"""
        self.__toId = value

    @property
    def runRoots(self) -> ndarray:
        """"""
        return self.__runRoots

    @runRoots.setter
    def runRoots(self, value: ndarray):
        """Set runRoots"""
        array = asarray(value, dtype=str)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__runRoots = array