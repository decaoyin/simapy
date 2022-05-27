# This an autogenerated file
# 
# Generated with BumperGroup
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.bumpergroup import BumperGroupBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.bumperpart import BumperPart
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobody import SIMOBody

class BumperGroup(NamedObject):
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
    body1 : SIMOBody
    body2 : SIMOBody
    velocityLimit : float
         Velocity limit for friction force (Damping Exponent = 0)(default 0.0)
    body1Bumpers : List[BumperPart]
    body2Bumpers : List[BumperPart]
    """

    def __init__(self , name="", description="", _id="", velocityLimit=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.body1 = None
        self.body2 = None
        self.velocityLimit = velocityLimit
        self.body1Bumpers = list()
        self.body2Bumpers = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BumperGroupBlueprint()


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
    def body1(self) -> SIMOBody:
        """"""
        return self.__body1

    @body1.setter
    def body1(self, value: SIMOBody):
        """Set body1"""
        self.__body1 = value

    @property
    def body2(self) -> SIMOBody:
        """"""
        return self.__body2

    @body2.setter
    def body2(self, value: SIMOBody):
        """Set body2"""
        self.__body2 = value

    @property
    def velocityLimit(self) -> float:
        """Velocity limit for friction force (Damping Exponent = 0)"""
        return self.__velocityLimit

    @velocityLimit.setter
    def velocityLimit(self, value: float):
        """Set velocityLimit"""
        self.__velocityLimit = float(value)

    @property
    def body1Bumpers(self) -> List[BumperPart]:
        """"""
        return self.__body1Bumpers

    @body1Bumpers.setter
    def body1Bumpers(self, value: List[BumperPart]):
        """Set body1Bumpers"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__body1Bumpers = value

    @property
    def body2Bumpers(self) -> List[BumperPart]:
        """"""
        return self.__body2Bumpers

    @body2Bumpers.setter
    def body2Bumpers(self, value: List[BumperPart]):
        """Set body2Bumpers"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__body2Bumpers = value
