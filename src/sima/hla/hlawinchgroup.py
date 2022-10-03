# This an autogenerated file
# 
# Generated with HLAWinchGroup
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hlawinchgroup import HLAWinchGroupBlueprint
from typing import Dict
from sima.hla.hlaobject import HLAObject
from sima.hla.hlawinchcontrolconfiguration import HLAWinchControlConfiguration
from sima.sima.scriptablevalue import ScriptableValue

class HLAWinchGroup(HLAObject):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    winchConfigurations : List[HLAWinchControlConfiguration]
    """

    def __init__(self , _id="", name="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.winchConfigurations = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLAWinchGroupBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def winchConfigurations(self) -> List[HLAWinchControlConfiguration]:
        """"""
        return self.__winchConfigurations

    @winchConfigurations.setter
    def winchConfigurations(self, value: List[HLAWinchControlConfiguration]):
        """Set winchConfigurations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__winchConfigurations = value
