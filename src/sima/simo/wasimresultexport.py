# This an autogenerated file
# 
# Generated with WasimResultExport
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.wasimresultexport import WasimResultExportBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.bodyforcecomponentreference import BodyForceComponentReference
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobody import SIMOBody

class WasimResultExport(MOAO):
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
    floaterBody : SIMOBody
    pointForces : List[BodyForceComponentReference]
    maxNumberOfWaveComponents : int
         Limit the number of wave components exported to file(default 0)
    """

    def __init__(self , name="", description="", _id="", maxNumberOfWaveComponents=0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.floaterBody = None
        self.pointForces = list()
        self.maxNumberOfWaveComponents = maxNumberOfWaveComponents
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WasimResultExportBlueprint()


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
    def floaterBody(self) -> SIMOBody:
        """"""
        return self.__floaterBody

    @floaterBody.setter
    def floaterBody(self, value: SIMOBody):
        """Set floaterBody"""
        self.__floaterBody = value

    @property
    def pointForces(self) -> List[BodyForceComponentReference]:
        """"""
        return self.__pointForces

    @pointForces.setter
    def pointForces(self, value: List[BodyForceComponentReference]):
        """Set pointForces"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__pointForces = value

    @property
    def maxNumberOfWaveComponents(self) -> int:
        """Limit the number of wave components exported to file"""
        return self.__maxNumberOfWaveComponents

    @maxNumberOfWaveComponents.setter
    def maxNumberOfWaveComponents(self, value: int):
        """Set maxNumberOfWaveComponents"""
        self.__maxNumberOfWaveComponents = int(value)
