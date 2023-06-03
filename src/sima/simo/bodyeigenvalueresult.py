# This an autogenerated file
# 
# Generated with BodyEigenvalueResult
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.bodyeigenvalueresult import BodyEigenvalueResultBlueprint
from typing import Dict
from .periodeigenvalueresult import PeriodEigenvalueResult
from sima.sima import MOAO
from sima.sima import ScriptableValue

class BodyEigenvalueResult(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    body : str
         Result body(default None)
    surgeExcursion : float
         Excursion in surge(default 0.0)
    swayExcursion : float
         Excursion in sway(default 0.0)
    heaveExcursion : float
         Excursion in heave(default 0.0)
    rollExcursion : float
         Excursion in roll(default 0.0)
    pitchExcursion : float
         Excursion in pitch(default 0.0)
    yawExcursion : float
         Excursion in yaw(default 0.0)
    periodResults : List[PeriodEigenvalueResult]
    """

    def __init__(self , description="", surgeExcursion=0.0, swayExcursion=0.0, heaveExcursion=0.0, rollExcursion=0.0, pitchExcursion=0.0, yawExcursion=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.body = None
        self.surgeExcursion = surgeExcursion
        self.swayExcursion = swayExcursion
        self.heaveExcursion = heaveExcursion
        self.rollExcursion = rollExcursion
        self.pitchExcursion = pitchExcursion
        self.yawExcursion = yawExcursion
        self.periodResults = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BodyEigenvalueResultBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def body(self) -> str:
        """Result body"""
        return self.__body

    @body.setter
    def body(self, value: str):
        """Set body"""
        self.__body = value

    @property
    def surgeExcursion(self) -> float:
        """Excursion in surge"""
        return self.__surgeExcursion

    @surgeExcursion.setter
    def surgeExcursion(self, value: float):
        """Set surgeExcursion"""
        self.__surgeExcursion = float(value)

    @property
    def swayExcursion(self) -> float:
        """Excursion in sway"""
        return self.__swayExcursion

    @swayExcursion.setter
    def swayExcursion(self, value: float):
        """Set swayExcursion"""
        self.__swayExcursion = float(value)

    @property
    def heaveExcursion(self) -> float:
        """Excursion in heave"""
        return self.__heaveExcursion

    @heaveExcursion.setter
    def heaveExcursion(self, value: float):
        """Set heaveExcursion"""
        self.__heaveExcursion = float(value)

    @property
    def rollExcursion(self) -> float:
        """Excursion in roll"""
        return self.__rollExcursion

    @rollExcursion.setter
    def rollExcursion(self, value: float):
        """Set rollExcursion"""
        self.__rollExcursion = float(value)

    @property
    def pitchExcursion(self) -> float:
        """Excursion in pitch"""
        return self.__pitchExcursion

    @pitchExcursion.setter
    def pitchExcursion(self, value: float):
        """Set pitchExcursion"""
        self.__pitchExcursion = float(value)

    @property
    def yawExcursion(self) -> float:
        """Excursion in yaw"""
        return self.__yawExcursion

    @yawExcursion.setter
    def yawExcursion(self, value: float):
        """Set yawExcursion"""
        self.__yawExcursion = float(value)

    @property
    def periodResults(self) -> List[PeriodEigenvalueResult]:
        """"""
        return self.__periodResults

    @periodResults.setter
    def periodResults(self, value: List[PeriodEigenvalueResult]):
        """Set periodResults"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__periodResults = value
