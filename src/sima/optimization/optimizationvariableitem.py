# This an autogenerated file
# 
# Generated with OptimizationVariableItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.optimizationvariableitem import OptimizationVariableItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.workflow.realnumberinput import RealNumberInput

class OptimizationVariableItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    start : float
         Starting value for the optimization variable(default 0.0)
    min : float
         Lower bound for the optimization variable(default 0.0)
    max : float
         Upper bound for the optimization variable(default 0.0)
    delta : float
         Delta for the optimization variable to be used in calculation of gradients(default 0.0)
    variable : RealNumberInput
         Optimization variable
    """

    def __init__(self , description="", start=0.0, min=0.0, max=0.0, delta=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.start = start
        self.min = min
        self.max = max
        self.delta = delta
        self.variable = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return OptimizationVariableItemBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def start(self) -> float:
        """Starting value for the optimization variable"""
        return self.__start

    @start.setter
    def start(self, value: float):
        """Set start"""
        self.__start = float(value)

    @property
    def min(self) -> float:
        """Lower bound for the optimization variable"""
        return self.__min

    @min.setter
    def min(self, value: float):
        """Set min"""
        self.__min = float(value)

    @property
    def max(self) -> float:
        """Upper bound for the optimization variable"""
        return self.__max

    @max.setter
    def max(self, value: float):
        """Set max"""
        self.__max = float(value)

    @property
    def delta(self) -> float:
        """Delta for the optimization variable to be used in calculation of gradients"""
        return self.__delta

    @delta.setter
    def delta(self, value: float):
        """Set delta"""
        self.__delta = float(value)

    @property
    def variable(self) -> RealNumberInput:
        """Optimization variable"""
        return self.__variable

    @variable.setter
    def variable(self, value: RealNumberInput):
        """Set variable"""
        self.__variable = value
