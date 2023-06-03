# This an autogenerated file
# 
# Generated with PressureVariationItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.pressurevariationitem import PressureVariationItemBlueprint
from typing import Dict
from sima.sima import MOAO
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .mainriserline import MainRiserLine

class PressureVariationItem(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    mainRiserLine : MainRiserLine
         Main riser line
    inletPressure : float
         Final pressure at inlet end(default 0.0)
    pressureDrop : float
         Final pressure drop(default 0.0)
    fluidVelocity : float
         Final fluid velocity(default 0.0)
    """

    def __init__(self , description="", inletPressure=0.0, pressureDrop=0.0, fluidVelocity=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.mainRiserLine = None
        self.inletPressure = inletPressure
        self.pressureDrop = pressureDrop
        self.fluidVelocity = fluidVelocity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PressureVariationItemBlueprint()


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
    def mainRiserLine(self) -> MainRiserLine:
        """Main riser line"""
        return self.__mainRiserLine

    @mainRiserLine.setter
    def mainRiserLine(self, value: MainRiserLine):
        """Set mainRiserLine"""
        self.__mainRiserLine = value

    @property
    def inletPressure(self) -> float:
        """Final pressure at inlet end"""
        return self.__inletPressure

    @inletPressure.setter
    def inletPressure(self, value: float):
        """Set inletPressure"""
        self.__inletPressure = float(value)

    @property
    def pressureDrop(self) -> float:
        """Final pressure drop"""
        return self.__pressureDrop

    @pressureDrop.setter
    def pressureDrop(self, value: float):
        """Set pressureDrop"""
        self.__pressureDrop = float(value)

    @property
    def fluidVelocity(self) -> float:
        """Final fluid velocity"""
        return self.__fluidVelocity

    @fluidVelocity.setter
    def fluidVelocity(self, value: float):
        """Set fluidVelocity"""
        self.__fluidVelocity = float(value)
