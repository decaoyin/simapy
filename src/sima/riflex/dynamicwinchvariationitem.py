# This an autogenerated file
# 
# Generated with DynamicWinchVariationItem
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dynamicwinchvariationitem import DynamicWinchVariationItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arwinch import ARWinch

class DynamicWinchVariationItem(MOAO):
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
    winch : ARWinch
    startTime : float
         Start time for winching(default 0.0)
    endTime : float
         End time for winching(default 0.0)
    velocity : float
         Winch velocity(default 0.0)
    """

    def __init__(self , name="", description="", _id="", startTime=0.0, endTime=0.0, velocity=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.winch = None
        self.startTime = startTime
        self.endTime = endTime
        self.velocity = velocity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicWinchVariationItemBlueprint()


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
    def winch(self) -> ARWinch:
        """"""
        return self.__winch

    @winch.setter
    def winch(self, value: ARWinch):
        """Set winch"""
        self.__winch = value

    @property
    def startTime(self) -> float:
        """Start time for winching"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def endTime(self) -> float:
        """End time for winching"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: float):
        """Set endTime"""
        self.__endTime = float(value)

    @property
    def velocity(self) -> float:
        """Winch velocity"""
        return self.__velocity

    @velocity.setter
    def velocity(self, value: float):
        """Set velocity"""
        self.__velocity = float(value)
