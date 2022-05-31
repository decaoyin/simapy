# This an autogenerated file
# 
# Generated with WorkflowTest
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.workflowtest import WorkflowTestBlueprint
from typing import Dict
from sima.doc.comparisonassertion import ComparisonAssertion
from sima.doc.duration import Duration
from sima.doc.outputnodevalueassertion import OutputNodeValueAssertion
from sima.doc.test import Test
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.workflow.workflow import Workflow

class WorkflowTest(Test):
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
    disabled : bool
         If disabled, the test will not be run in a continuous integration environment(default False)
    duration : Duration
    assertions : List[OutputNodeValueAssertion]
    comparisons : List[ComparisonAssertion]
    workflow : Workflow
    """

    def __init__(self , name="", description="", _id="", disabled=False, duration=Duration.MEDIUM, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.disabled = disabled
        self.duration = duration
        self.assertions = list()
        self.comparisons = list()
        self.workflow = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WorkflowTestBlueprint()


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
    def disabled(self) -> bool:
        """If disabled, the test will not be run in a continuous integration environment"""
        return self.__disabled

    @disabled.setter
    def disabled(self, value: bool):
        """Set disabled"""
        self.__disabled = bool(value)

    @property
    def duration(self) -> Duration:
        """"""
        return self.__duration

    @duration.setter
    def duration(self, value: Duration):
        """Set duration"""
        self.__duration = value

    @property
    def assertions(self) -> List[OutputNodeValueAssertion]:
        """"""
        return self.__assertions

    @assertions.setter
    def assertions(self, value: List[OutputNodeValueAssertion]):
        """Set assertions"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__assertions = value

    @property
    def comparisons(self) -> List[ComparisonAssertion]:
        """"""
        return self.__comparisons

    @comparisons.setter
    def comparisons(self, value: List[ComparisonAssertion]):
        """Set comparisons"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__comparisons = value

    @property
    def workflow(self) -> Workflow:
        """"""
        return self.__workflow

    @workflow.setter
    def workflow(self, value: Workflow):
        """Set workflow"""
        self.__workflow = value
