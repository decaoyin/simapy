# This an autogenerated file
# 
# Generated with DynamicPressureVariationItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dynamicpressurevariationitem import DynamicPressureVariationItemBlueprint
from typing import Dict
from sima.riflex.pressurevariationitem import PressureVariationItem
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.mainriserline import MainRiserLine

class DynamicPressureVariationItem(PressureVariationItem):
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
    mainRiserLine : MainRiserLine
         Main riser line
    inletPressure : float
         Final pressure at inlet end(default 0.0)
    pressureDrop : float
         Final pressure drop(default 0.0)
    fluidVelocity : float
         Final fluid velocity(default 0.0)
    startTime : float
         Start time for pressure variation(default 0.0)
    endTime : float
         End time for pressure variation(default 0.0)
    """

    def __init__(self , name="", description="", _id="", inletPressure=0.0, pressureDrop=0.0, fluidVelocity=0.0, startTime=0.0, endTime=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.mainRiserLine = None
        self.inletPressure = inletPressure
        self.pressureDrop = pressureDrop
        self.fluidVelocity = fluidVelocity
        self.startTime = startTime
        self.endTime = endTime
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicPressureVariationItemBlueprint()


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

    @property
    def startTime(self) -> float:
        """Start time for pressure variation"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def endTime(self) -> float:
        """End time for pressure variation"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: float):
        """Set endTime"""
        self.__endTime = float(value)
