# This an autogenerated file
# 
# Generated with LFMotionTimeSeries
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.lfmotiontimeseries import LFMotionTimeSeriesBlueprint
from typing import Dict
from sima.riflex.fileformatascistarnone import FileFormatAsciStarNone
from sima.riflex.motiontimeseriestype import MotionTimeSeriesType
from sima.riflex.rotationunit import RotationUnit
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.supportvessel import SupportVessel

class LFMotionTimeSeries(MOAO):
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
    timeSeriesFile : bool
         (default False)
    supportVessel : SupportVessel
    fileName : str
         Motion time series file(default "")
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
    """

    def __init__(self , name="", description="", _id="", timeSeriesFile=False, fileName="", fileFormat=FileFormatAsciStarNone.ASCII, motionTimeSeriesType=MotionTimeSeriesType.POSI, rotationUnit=RotationUnit.DEGR, timeColumnNum=1, xMotionColumn=0, xMotionVersion=0, yMotionColumn=0, yMotionVersion=0, zRotationColumn=0, zRotationVersion=0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.timeSeriesFile = timeSeriesFile
        self.supportVessel = None
        self.fileName = fileName
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
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LFMotionTimeSeriesBlueprint()


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
        self.__fileName = str(value)

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
