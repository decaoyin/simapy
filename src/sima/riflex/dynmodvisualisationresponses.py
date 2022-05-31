# This an autogenerated file
# 
# Generated with DynmodVisualisationResponses
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.dynmodvisualisationresponses import DynmodVisualisationResponsesBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class DynmodVisualisationResponses(MOAO):
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
    startTime : float
         Start time for export(default 0.0)
    endTime : float
         End time for export(default 512.0)
    timeIncrement : float
         Time increment for export(default 0.5)
    storeVisualisationResponses : bool
         Visualisation responses indicator(default False)
    storeVTF : bool
         Visualisation responses indicator(default False)
    """

    def __init__(self , name="", description="", _id="", startTime=0.0, endTime=512.0, timeIncrement=0.5, storeVisualisationResponses=False, storeVTF=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.startTime = startTime
        self.endTime = endTime
        self.timeIncrement = timeIncrement
        self.storeVisualisationResponses = storeVisualisationResponses
        self.storeVTF = storeVTF
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynmodVisualisationResponsesBlueprint()


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
    def startTime(self) -> float:
        """Start time for export"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def endTime(self) -> float:
        """End time for export"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: float):
        """Set endTime"""
        self.__endTime = float(value)

    @property
    def timeIncrement(self) -> float:
        """Time increment for export"""
        return self.__timeIncrement

    @timeIncrement.setter
    def timeIncrement(self, value: float):
        """Set timeIncrement"""
        self.__timeIncrement = float(value)

    @property
    def storeVisualisationResponses(self) -> bool:
        """Visualisation responses indicator"""
        return self.__storeVisualisationResponses

    @storeVisualisationResponses.setter
    def storeVisualisationResponses(self, value: bool):
        """Set storeVisualisationResponses"""
        self.__storeVisualisationResponses = bool(value)

    @property
    def storeVTF(self) -> bool:
        """Visualisation responses indicator"""
        return self.__storeVTF

    @storeVTF.setter
    def storeVTF(self, value: bool):
        """Set storeVTF"""
        self.__storeVTF = bool(value)
