# This an autogenerated file
# 
# Generated with WFMotionTimeSeries
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.wfmotiontimeseries import WFMotionTimeSeriesBlueprint
from typing import Dict
from .fileformatascistarnone import FileFormatAsciStarNone
from .motiontimeseriestype import MotionTimeSeriesType
from .rotationunit import RotationUnit
from sima.sima import MOAO
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .supportvessel import SupportVessel

class WFMotionTimeSeries(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    timeSeriesFile : bool
         (default False)
    supportVessel : SupportVessel
    fileName : str
         Motion time series file(default None)
    fileFormat : FileFormatAsciStarNone
         Motion time series file format
    motionTimeSeriesType : MotionTimeSeriesType
         Kind of motion time series input
    rotationUnit : RotationUnit
         Rotation unit
    timeColumnNum : int
         Column number for time (Does not apply to STAR files)(default 1)
    xMotionColumn : int
         Column or time series number for global dynamic x-motion(default 0)
    xMotionVersion : int
         Startimes version number for global dynamic x-motion(default 0)
    yMotionColumn : int
         Column or time series number for global dynamic y-motion(default 0)
    yMotionVersion : int
         Startimes version number for global dynamic y-motion(default 0)
    zRotationColumn : int
         Column or time series number for global dynamic z-rotation(default 0)
    zRotationVersion : int
         Startimes version number for global dynamic z-rotation(default 0)
    zMotionColumn : int
         Column or time series number for global dynamic z-motion(default 0)
    zMotionVersion : int
         Startimes version number for global dynamic z-motion(default 0)
    xRotationColumn : int
         Column or time series number for global dynamic x-rotation(default 0)
    xRotationVersion : int
         Startimes version number for global dynamic x-rotation(default 0)
    yRotationColumn : int
         Column or time series number for global dynamic y-rotation(default 0)
    yRotationVersion : int
         Startimes version number for global dynamic y-rotation(default 0)
    """

    def __init__(self , description="", timeSeriesFile=False, fileFormat=FileFormatAsciStarNone.ASCII, motionTimeSeriesType=MotionTimeSeriesType.POSI, rotationUnit=RotationUnit.DEGR, timeColumnNum=1, xMotionColumn=0, xMotionVersion=0, yMotionColumn=0, yMotionVersion=0, zRotationColumn=0, zRotationVersion=0, zMotionColumn=0, zMotionVersion=0, xRotationColumn=0, xRotationVersion=0, yRotationColumn=0, yRotationVersion=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.timeSeriesFile = timeSeriesFile
        self.supportVessel = None
        self.fileName = None
        self.fileFormat = fileFormat
        self.motionTimeSeriesType = motionTimeSeriesType
        self.rotationUnit = rotationUnit
        self.timeColumnNum = timeColumnNum
        self.xMotionColumn = xMotionColumn
        self.xMotionVersion = xMotionVersion
        self.yMotionColumn = yMotionColumn
        self.yMotionVersion = yMotionVersion
        self.zRotationColumn = zRotationColumn
        self.zRotationVersion = zRotationVersion
        self.zMotionColumn = zMotionColumn
        self.zMotionVersion = zMotionVersion
        self.xRotationColumn = xRotationColumn
        self.xRotationVersion = xRotationVersion
        self.yRotationColumn = yRotationColumn
        self.yRotationVersion = yRotationVersion
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WFMotionTimeSeriesBlueprint()


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
    def timeSeriesFile(self) -> bool:
        """"""
        return self.__timeSeriesFile

    @timeSeriesFile.setter
    def timeSeriesFile(self, value: bool):
        """Set timeSeriesFile"""
        self.__timeSeriesFile = bool(value)

    @property
    def supportVessel(self) -> SupportVessel:
        """"""
        return self.__supportVessel

    @supportVessel.setter
    def supportVessel(self, value: SupportVessel):
        """Set supportVessel"""
        self.__supportVessel = value

    @property
    def fileName(self) -> str:
        """Motion time series file"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = value

    @property
    def fileFormat(self) -> FileFormatAsciStarNone:
        """Motion time series file format"""
        return self.__fileFormat

    @fileFormat.setter
    def fileFormat(self, value: FileFormatAsciStarNone):
        """Set fileFormat"""
        self.__fileFormat = value

    @property
    def motionTimeSeriesType(self) -> MotionTimeSeriesType:
        """Kind of motion time series input"""
        return self.__motionTimeSeriesType

    @motionTimeSeriesType.setter
    def motionTimeSeriesType(self, value: MotionTimeSeriesType):
        """Set motionTimeSeriesType"""
        self.__motionTimeSeriesType = value

    @property
    def rotationUnit(self) -> RotationUnit:
        """Rotation unit"""
        return self.__rotationUnit

    @rotationUnit.setter
    def rotationUnit(self, value: RotationUnit):
        """Set rotationUnit"""
        self.__rotationUnit = value

    @property
    def timeColumnNum(self) -> int:
        """Column number for time (Does not apply to STAR files)"""
        return self.__timeColumnNum

    @timeColumnNum.setter
    def timeColumnNum(self, value: int):
        """Set timeColumnNum"""
        self.__timeColumnNum = int(value)

    @property
    def xMotionColumn(self) -> int:
        """Column or time series number for global dynamic x-motion"""
        return self.__xMotionColumn

    @xMotionColumn.setter
    def xMotionColumn(self, value: int):
        """Set xMotionColumn"""
        self.__xMotionColumn = int(value)

    @property
    def xMotionVersion(self) -> int:
        """Startimes version number for global dynamic x-motion"""
        return self.__xMotionVersion

    @xMotionVersion.setter
    def xMotionVersion(self, value: int):
        """Set xMotionVersion"""
        self.__xMotionVersion = int(value)

    @property
    def yMotionColumn(self) -> int:
        """Column or time series number for global dynamic y-motion"""
        return self.__yMotionColumn

    @yMotionColumn.setter
    def yMotionColumn(self, value: int):
        """Set yMotionColumn"""
        self.__yMotionColumn = int(value)

    @property
    def yMotionVersion(self) -> int:
        """Startimes version number for global dynamic y-motion"""
        return self.__yMotionVersion

    @yMotionVersion.setter
    def yMotionVersion(self, value: int):
        """Set yMotionVersion"""
        self.__yMotionVersion = int(value)

    @property
    def zRotationColumn(self) -> int:
        """Column or time series number for global dynamic z-rotation"""
        return self.__zRotationColumn

    @zRotationColumn.setter
    def zRotationColumn(self, value: int):
        """Set zRotationColumn"""
        self.__zRotationColumn = int(value)

    @property
    def zRotationVersion(self) -> int:
        """Startimes version number for global dynamic z-rotation"""
        return self.__zRotationVersion

    @zRotationVersion.setter
    def zRotationVersion(self, value: int):
        """Set zRotationVersion"""
        self.__zRotationVersion = int(value)

    @property
    def zMotionColumn(self) -> int:
        """Column or time series number for global dynamic z-motion"""
        return self.__zMotionColumn

    @zMotionColumn.setter
    def zMotionColumn(self, value: int):
        """Set zMotionColumn"""
        self.__zMotionColumn = int(value)

    @property
    def zMotionVersion(self) -> int:
        """Startimes version number for global dynamic z-motion"""
        return self.__zMotionVersion

    @zMotionVersion.setter
    def zMotionVersion(self, value: int):
        """Set zMotionVersion"""
        self.__zMotionVersion = int(value)

    @property
    def xRotationColumn(self) -> int:
        """Column or time series number for global dynamic x-rotation"""
        return self.__xRotationColumn

    @xRotationColumn.setter
    def xRotationColumn(self, value: int):
        """Set xRotationColumn"""
        self.__xRotationColumn = int(value)

    @property
    def xRotationVersion(self) -> int:
        """Startimes version number for global dynamic x-rotation"""
        return self.__xRotationVersion

    @xRotationVersion.setter
    def xRotationVersion(self, value: int):
        """Set xRotationVersion"""
        self.__xRotationVersion = int(value)

    @property
    def yRotationColumn(self) -> int:
        """Column or time series number for global dynamic y-rotation"""
        return self.__yRotationColumn

    @yRotationColumn.setter
    def yRotationColumn(self, value: int):
        """Set yRotationColumn"""
        self.__yRotationColumn = int(value)

    @property
    def yRotationVersion(self) -> int:
        """Startimes version number for global dynamic y-rotation"""
        return self.__yRotationVersion

    @yRotationVersion.setter
    def yRotationVersion(self, value: int):
        """Set yRotationVersion"""
        self.__yRotationVersion = int(value)
