# This an autogenerated file
# 
# Generated with RIFLEXFederate
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexfederate import RIFLEXFederateBlueprint
from typing import Dict
from ..sima import ScriptableValue
from ..simo import SIMOFederate
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..condition import ConditionTask

class RIFLEXFederate(SIMOFederate):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    timeStep : float
         (default 0.0)
    task : ConditionTask
    """

    def __init__(self , description="", timeStep=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.timeStep = timeStep
        self.task = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXFederateBlueprint()


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
    def timeStep(self) -> float:
        """"""
        return self.__timeStep

    @timeStep.setter
    def timeStep(self, value: float):
        """Set timeStep"""
        self.__timeStep = float(value)

    @property
    def task(self) -> ConditionTask:
        """"""
        return self.__task

    @task.setter
    def task(self, value: ConditionTask):
        """Set task"""
        self.__task = value
