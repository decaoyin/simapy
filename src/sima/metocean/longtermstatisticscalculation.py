# This an autogenerated file
# 
# Generated with LongTermStatisticsCalculation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.longtermstatisticscalculation import LongTermStatisticsCalculationBlueprint
from typing import Dict
from sima.metocean.inputreferencesystem import InputReferenceSystem
from sima.metocean.longtermstatisticscurrentcalculation import LongTermStatisticsCurrentCalculation
from sima.metocean.longtermstatisticswavecalculation import LongTermStatisticsWaveCalculation
from sima.metocean.longtermstatisticswindcalculation import LongTermStatisticsWindCalculation
from sima.sima.conditionselectable import ConditionSelectable
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.metocean.longtermstatistics import LongTermStatistics
    from sima.metocean.longtermstatisticsperiod import LongTermStatisticsPeriod

class LongTermStatisticsCalculation(NamedObject,ConditionSelectable):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    relativeCompassAngle : float
         Relative angle between analysis x-axis and north direction in anti-clockwise direction.\nShould match the angle given in the recieving SIMA task location.(default 0.0)
    inputReferenceSystem : InputReferenceSystem
         Defines the input reference system of the data.\nIf the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated
    applyNorsok : bool
          Apply NORSOK N-006(default True)
    longTermStatistics : LongTermStatistics
    period : LongTermStatisticsPeriod
    waveCalculation : LongTermStatisticsWaveCalculation
    windCalculation : LongTermStatisticsWindCalculation
    currentCalculation : LongTermStatisticsCurrentCalculation
    """

    def __init__(self , _id="", name="", relativeCompassAngle=0.0, inputReferenceSystem=InputReferenceSystem.METOCEAN, applyNorsok=True, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.relativeCompassAngle = relativeCompassAngle
        self.inputReferenceSystem = inputReferenceSystem
        self.applyNorsok = applyNorsok
        self.longTermStatistics = None
        self.period = None
        self.waveCalculation = None
        self.windCalculation = None
        self.currentCalculation = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LongTermStatisticsCalculationBlueprint()


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
    def relativeCompassAngle(self) -> float:
        """Relative angle between analysis x-axis and north direction in anti-clockwise direction.
Should match the angle given in the recieving SIMA task location."""
        return self.__relativeCompassAngle

    @relativeCompassAngle.setter
    def relativeCompassAngle(self, value: float):
        """Set relativeCompassAngle"""
        self.__relativeCompassAngle = float(value)

    @property
    def inputReferenceSystem(self) -> InputReferenceSystem:
        """Defines the input reference system of the data.
If the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated"""
        return self.__inputReferenceSystem

    @inputReferenceSystem.setter
    def inputReferenceSystem(self, value: InputReferenceSystem):
        """Set inputReferenceSystem"""
        self.__inputReferenceSystem = value

    @property
    def applyNorsok(self) -> bool:
        """ Apply NORSOK N-006"""
        return self.__applyNorsok

    @applyNorsok.setter
    def applyNorsok(self, value: bool):
        """Set applyNorsok"""
        self.__applyNorsok = bool(value)

    @property
    def longTermStatistics(self) -> LongTermStatistics:
        """"""
        return self.__longTermStatistics

    @longTermStatistics.setter
    def longTermStatistics(self, value: LongTermStatistics):
        """Set longTermStatistics"""
        self.__longTermStatistics = value

    @property
    def period(self) -> LongTermStatisticsPeriod:
        """"""
        return self.__period

    @period.setter
    def period(self, value: LongTermStatisticsPeriod):
        """Set period"""
        self.__period = value

    @property
    def waveCalculation(self) -> LongTermStatisticsWaveCalculation:
        """"""
        return self.__waveCalculation

    @waveCalculation.setter
    def waveCalculation(self, value: LongTermStatisticsWaveCalculation):
        """Set waveCalculation"""
        self.__waveCalculation = value

    @property
    def windCalculation(self) -> LongTermStatisticsWindCalculation:
        """"""
        return self.__windCalculation

    @windCalculation.setter
    def windCalculation(self, value: LongTermStatisticsWindCalculation):
        """Set windCalculation"""
        self.__windCalculation = value

    @property
    def currentCalculation(self) -> LongTermStatisticsCurrentCalculation:
        """"""
        return self.__currentCalculation

    @currentCalculation.setter
    def currentCalculation(self, value: LongTermStatisticsCurrentCalculation):
        """Set currentCalculation"""
        self.__currentCalculation = value
