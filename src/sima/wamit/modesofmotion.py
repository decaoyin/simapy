# This an autogenerated file
# 
# Generated with ModesOfMotion
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.modesofmotion import ModesOfMotionBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ModesOfMotion(MOAO):
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
    surge : bool
         (default True)
    sway : bool
         (default True)
    heave : bool
         (default True)
    roll : bool
         (default True)
    pitch : bool
         (default True)
    yaw : bool
         (default True)
    """

    def __init__(self , name="", description="", _id="", surge=True, sway=True, heave=True, roll=True, pitch=True, yaw=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.surge = surge
        self.sway = sway
        self.heave = heave
        self.roll = roll
        self.pitch = pitch
        self.yaw = yaw
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ModesOfMotionBlueprint()


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
    def surge(self) -> bool:
        """"""
        return self.__surge

    @surge.setter
    def surge(self, value: bool):
        """Set surge"""
        self.__surge = bool(value)

    @property
    def sway(self) -> bool:
        """"""
        return self.__sway

    @sway.setter
    def sway(self, value: bool):
        """Set sway"""
        self.__sway = bool(value)

    @property
    def heave(self) -> bool:
        """"""
        return self.__heave

    @heave.setter
    def heave(self, value: bool):
        """Set heave"""
        self.__heave = bool(value)

    @property
    def roll(self) -> bool:
        """"""
        return self.__roll

    @roll.setter
    def roll(self, value: bool):
        """Set roll"""
        self.__roll = bool(value)

    @property
    def pitch(self) -> bool:
        """"""
        return self.__pitch

    @pitch.setter
    def pitch(self, value: bool):
        """Set pitch"""
        self.__pitch = bool(value)

    @property
    def yaw(self) -> bool:
        """"""
        return self.__yaw

    @yaw.setter
    def yaw(self, value: bool):
        """Set yaw"""
        self.__yaw = bool(value)
