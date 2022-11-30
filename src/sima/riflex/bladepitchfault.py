# This an autogenerated file
# 
# Generated with BladePitchFault
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.bladepitchfault import BladePitchFaultBlueprint
from typing import Dict
from sima.riflex.biasbladepitchfaultitem import BiasBladePitchFaultItem
from sima.riflex.runawaybladepitchfaultitem import RunawayBladePitchFaultItem
from sima.riflex.seizebladepitchfaultitem import SeizeBladePitchFaultItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class BladePitchFault(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    seizeFaults : List[SeizeBladePitchFaultItem]
    runawayFaults : List[RunawayBladePitchFaultItem]
    biasFaults : List[BiasBladePitchFaultItem]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.seizeFaults = list()
        self.runawayFaults = list()
        self.biasFaults = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BladePitchFaultBlueprint()


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
    def seizeFaults(self) -> List[SeizeBladePitchFaultItem]:
        """"""
        return self.__seizeFaults

    @seizeFaults.setter
    def seizeFaults(self, value: List[SeizeBladePitchFaultItem]):
        """Set seizeFaults"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__seizeFaults = value

    @property
    def runawayFaults(self) -> List[RunawayBladePitchFaultItem]:
        """"""
        return self.__runawayFaults

    @runawayFaults.setter
    def runawayFaults(self, value: List[RunawayBladePitchFaultItem]):
        """Set runawayFaults"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__runawayFaults = value

    @property
    def biasFaults(self) -> List[BiasBladePitchFaultItem]:
        """"""
        return self.__biasFaults

    @biasFaults.setter
    def biasFaults(self, value: List[BiasBladePitchFaultItem]):
        """Set biasFaults"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__biasFaults = value
