# This an autogenerated file
# 
# Generated with WorkflowRouting
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.workflowrouting import WorkflowRoutingBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .workflowinputvariationitem import WorkflowInputVariationItem
from .workflowlinkitem import WorkflowLinkItem
from .workflowsetitem import WorkflowSetItem

class WorkflowRouting(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    workflowSetInputs : List[WorkflowSetItem]
    workflowInputVariations : List[WorkflowInputVariationItem]
    inputs : List[WorkflowLinkItem]
    outputs : List[WorkflowLinkItem]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.workflowSetInputs = list()
        self.workflowInputVariations = list()
        self.inputs = list()
        self.outputs = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowRoutingBlueprint()


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
    def workflowSetInputs(self) -> List[WorkflowSetItem]:
        """"""
        return self.__workflowSetInputs

    @workflowSetInputs.setter
    def workflowSetInputs(self, value: List[WorkflowSetItem]):
        """Set workflowSetInputs"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__workflowSetInputs = value

    @property
    def workflowInputVariations(self) -> List[WorkflowInputVariationItem]:
        """"""
        return self.__workflowInputVariations

    @workflowInputVariations.setter
    def workflowInputVariations(self, value: List[WorkflowInputVariationItem]):
        """Set workflowInputVariations"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__workflowInputVariations = value

    @property
    def inputs(self) -> List[WorkflowLinkItem]:
        """"""
        return self.__inputs

    @inputs.setter
    def inputs(self, value: List[WorkflowLinkItem]):
        """Set inputs"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__inputs = value

    @property
    def outputs(self) -> List[WorkflowLinkItem]:
        """"""
        return self.__outputs

    @outputs.setter
    def outputs(self, value: List[WorkflowLinkItem]):
        """Set outputs"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__outputs = value