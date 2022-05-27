# This an autogenerated file
# 
# Generated with WorkflowRouting
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.workflowrouting import WorkflowRoutingBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.workflowinputvariationitem import WorkflowInputVariationItem
from sima.workflow.workflowlinkitem import WorkflowLinkItem
from sima.workflow.workflowsetitem import WorkflowSetItem

class WorkflowRouting(MOAO):
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
    workflowSetInputs : List[WorkflowSetItem]
    workflowInputVariations : List[WorkflowInputVariationItem]
    inputs : List[WorkflowLinkItem]
    outputs : List[WorkflowLinkItem]
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
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
    def workflowSetInputs(self) -> List[WorkflowSetItem]:
        """"""
        return self.__workflowSetInputs

    @workflowSetInputs.setter
    def workflowSetInputs(self, value: List[WorkflowSetItem]):
        """Set workflowSetInputs"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__workflowSetInputs = value

    @property
    def workflowInputVariations(self) -> List[WorkflowInputVariationItem]:
        """"""
        return self.__workflowInputVariations

    @workflowInputVariations.setter
    def workflowInputVariations(self, value: List[WorkflowInputVariationItem]):
        """Set workflowInputVariations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__workflowInputVariations = value

    @property
    def inputs(self) -> List[WorkflowLinkItem]:
        """"""
        return self.__inputs

    @inputs.setter
    def inputs(self, value: List[WorkflowLinkItem]):
        """Set inputs"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__inputs = value

    @property
    def outputs(self) -> List[WorkflowLinkItem]:
        """"""
        return self.__outputs

    @outputs.setter
    def outputs(self, value: List[WorkflowLinkItem]):
        """Set outputs"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__outputs = value
