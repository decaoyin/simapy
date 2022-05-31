# This an autogenerated file
# 
# Generated with SNCurveItem
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.sncurveitem import SNCurveItemBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class SNCurveItem(MOAO):
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
    negativeInverseSlope : float
         Negative inverse slope of S-N curve(default 0.0)
    transitionPointLog : float
         log10 of number of cycles at transition point between preceding curve segment and this curve segment(default 0.0)
    """

    def __init__(self , name="", description="", _id="", negativeInverseSlope=0.0, transitionPointLog=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.negativeInverseSlope = negativeInverseSlope
        self.transitionPointLog = transitionPointLog
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SNCurveItemBlueprint()


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
    def negativeInverseSlope(self) -> float:
        """Negative inverse slope of S-N curve"""
        return self.__negativeInverseSlope

    @negativeInverseSlope.setter
    def negativeInverseSlope(self, value: float):
        """Set negativeInverseSlope"""
        self.__negativeInverseSlope = float(value)

    @property
    def transitionPointLog(self) -> float:
        """log10 of number of cycles at transition point between preceding curve segment and this curve segment"""
        return self.__transitionPointLog

    @transitionPointLog.setter
    def transitionPointLog(self, value: float):
        """Set transitionPointLog"""
        self.__transitionPointLog = float(value)
