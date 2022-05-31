# This an autogenerated file
# 
# Generated with HLADataTable
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.hladatatable import HLADataTableBlueprint
from typing import Dict
from sima.hla.hlasignal import HLASignal
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class HLADataTable(MOAO):
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
    signals : List[HLASignal]
    showHorisontalTable : bool
         (default False)
    """

    def __init__(self , name="", description="", _id="", showHorisontalTable=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.signals = list()
        self.showHorisontalTable = showHorisontalTable
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLADataTableBlueprint()


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
    def signals(self) -> List[HLASignal]:
        """"""
        return self.__signals

    @signals.setter
    def signals(self, value: List[HLASignal]):
        """Set signals"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__signals = value

    @property
    def showHorisontalTable(self) -> bool:
        """"""
        return self.__showHorisontalTable

    @showHorisontalTable.setter
    def showHorisontalTable(self, value: bool):
        """Set showHorisontalTable"""
        self.__showHorisontalTable = bool(value)
