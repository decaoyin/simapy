# This an autogenerated file
# 
# Generated with ContourData
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.contourdata import ContourDataBlueprint
from typing import Dict
from sima.metocean.contourdatapoint import ContourDataPoint
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ContourData(MOAO):
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
    returnPeriod : float
         (default 0.0)
    contourDataPoints : List[ContourDataPoint]
    """

    def __init__(self , name="", description="", _id="", returnPeriod=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.returnPeriod = returnPeriod
        self.contourDataPoints = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ContourDataBlueprint()


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
    def returnPeriod(self) -> float:
        """"""
        return self.__returnPeriod

    @returnPeriod.setter
    def returnPeriod(self, value: float):
        """Set returnPeriod"""
        self.__returnPeriod = float(value)

    @property
    def contourDataPoints(self) -> List[ContourDataPoint]:
        """"""
        return self.__contourDataPoints

    @contourDataPoints.setter
    def contourDataPoints(self, value: List[ContourDataPoint]):
        """Set contourDataPoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__contourDataPoints = value
