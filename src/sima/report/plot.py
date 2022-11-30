# This an autogenerated file
# 
# Generated with Plot
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.plot import PlotBlueprint
from typing import Dict
from sima.report.reportitem import ReportItem
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class Plot(ReportItem):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    object : MOAO
    caption : str
         Caption(default None)
    mergeSeries : bool
         Merge all series in one plot(default False)
    xLabel : str
         (default None)
    yLabel : str
         (default None)
    """

    def __init__(self , description="", mergeSeries=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.object = None
        self.caption = None
        self.mergeSeries = mergeSeries
        self.xLabel = None
        self.yLabel = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PlotBlueprint()


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
    def object(self) -> MOAO:
        """"""
        return self.__object

    @object.setter
    def object(self, value: MOAO):
        """Set object"""
        self.__object = value

    @property
    def caption(self) -> str:
        """Caption"""
        return self.__caption

    @caption.setter
    def caption(self, value: str):
        """Set caption"""
        self.__caption = value

    @property
    def mergeSeries(self) -> bool:
        """Merge all series in one plot"""
        return self.__mergeSeries

    @mergeSeries.setter
    def mergeSeries(self, value: bool):
        """Set mergeSeries"""
        self.__mergeSeries = bool(value)

    @property
    def xLabel(self) -> str:
        """"""
        return self.__xLabel

    @xLabel.setter
    def xLabel(self, value: str):
        """Set xLabel"""
        self.__xLabel = value

    @property
    def yLabel(self) -> str:
        """"""
        return self.__yLabel

    @yLabel.setter
    def yLabel(self, value: str):
        """Set yLabel"""
        self.__yLabel = value
