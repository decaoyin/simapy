# This an autogenerated file
# 
# Generated with TraceConfiguration
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.traceconfiguration import TraceConfigurationBlueprint
from typing import Dict
from .linestyle import LineStyle
from .pathspecification import PathSpecification
from .pointstyle import PointStyle
from sima.sima import SIMAColor
from sima.sima import ScriptableValue

class TraceConfiguration(PathSpecification):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    path : str
         (default None)
    name : str
         (default None)
    label : str
         (default None)
    color : SIMAColor
    lineStyle : LineStyle
    lineWidth : int
         (default 1)
    pointStyle : PointStyle
    showStatistics : bool
         (default True)
    pointSize : int
         (default 1)
    specifyPath : bool
         (default False)
    """

    def __init__(self , description="", lineStyle=LineStyle.SOLID, lineWidth=1, pointStyle=PointStyle.NONE, showStatistics=True, pointSize=1, specifyPath=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.path = None
        self.name = None
        self.label = None
        self.color = None
        self.lineStyle = lineStyle
        self.lineWidth = lineWidth
        self.pointStyle = pointStyle
        self.showStatistics = showStatistics
        self.pointSize = pointSize
        self.specifyPath = specifyPath
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TraceConfigurationBlueprint()


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
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = value

    @property
    def color(self) -> SIMAColor:
        """"""
        return self.__color

    @color.setter
    def color(self, value: SIMAColor):
        """Set color"""
        self.__color = value

    @property
    def lineStyle(self) -> LineStyle:
        """"""
        return self.__lineStyle

    @lineStyle.setter
    def lineStyle(self, value: LineStyle):
        """Set lineStyle"""
        self.__lineStyle = value

    @property
    def lineWidth(self) -> int:
        """"""
        return self.__lineWidth

    @lineWidth.setter
    def lineWidth(self, value: int):
        """Set lineWidth"""
        self.__lineWidth = int(value)

    @property
    def pointStyle(self) -> PointStyle:
        """"""
        return self.__pointStyle

    @pointStyle.setter
    def pointStyle(self, value: PointStyle):
        """Set pointStyle"""
        self.__pointStyle = value

    @property
    def showStatistics(self) -> bool:
        """"""
        return self.__showStatistics

    @showStatistics.setter
    def showStatistics(self, value: bool):
        """Set showStatistics"""
        self.__showStatistics = bool(value)

    @property
    def pointSize(self) -> int:
        """"""
        return self.__pointSize

    @pointSize.setter
    def pointSize(self, value: int):
        """Set pointSize"""
        self.__pointSize = int(value)

    @property
    def specifyPath(self) -> bool:
        """"""
        return self.__specifyPath

    @specifyPath.setter
    def specifyPath(self, value: bool):
        """Set specifyPath"""
        self.__specifyPath = bool(value)
