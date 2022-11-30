# This an autogenerated file
# 
# Generated with IrregularWaveProcedure
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.irregularwaveprocedure import IrregularWaveProcedureBlueprint
from typing import Dict
from sima.riflex.kinematicsinwavezone import KinematicsInWaveZone
from sima.riflex.kinematicspositions import KinematicsPositions
from sima.riflex.storagetype import StorageType
from sima.riflex.wavekinematicsdiffpoint import WaveKinematicsDiffPoint
from sima.riflex.wavekinematicsnodepoint import WaveKinematicsNodePoint
from sima.riflex.wavekinematicstimeseriesreference import WaveKinematicsTimeSeriesReference
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class IrregularWaveProcedure(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    kinematicsPosition : KinematicsPositions
         Kinematic positions
    kinematicsInWaveZone : KinematicsInWaveZone
         Type of kinematics in wave zone
    defaultProcedureOn : bool
         If chosen the default kinematics points procedure is run in RIFLEX. If not chosen the default procedure is not run in RIFLEX. In both cases additional detailed specification of wave kinematics points are run if present.(default True)
    nodeStep : int
         Wave kinematics is calculated for every 'Node Step' node between Z Lower\nand Z Upper(default 1)
    zLower : float
         Z-coordinate indicating lowest node position for which wave kinematics are calculated(default 0.0)
    zUpper : float
         Upper limit for wave kinematics(default 0.0)
    applyDiffractedWaves : bool
         Whether diffracted wave points are to be specified(default False)
    waveKinematicDiffPoints : List[WaveKinematicsDiffPoint]
    waveKinematicNodePoints : List[WaveKinematicsNodePoint]
    waveKinematicsFile : bool
         Whether wave kinematics time series should be read from file or not(default False)
    waveKinematicsFileName : str
         Reference to a wave kinematics file(default None)
    waveKinematicsTimeSeriesReferences : List[WaveKinematicsTimeSeriesReference]
    waveKinematicsMaxColumns : int
         Maximum number of columns in the wave kinematics time series file(default 0)
    waveKinematicsTimeColumn : int
         Column number for time in the wave kinematics time series file(default 0)
    waveKinematicsStorage : bool
         Wave kinematics storage indicator(default False)
    fileFormat : StorageType
    """

    def __init__(self , description="", kinematicsPosition=KinematicsPositions.STATIC, kinematicsInWaveZone=KinematicsInWaveZone.MEAN_WATER_LEVEL, defaultProcedureOn=True, nodeStep=1, zLower=0.0, zUpper=0.0, applyDiffractedWaves=False, waveKinematicsFile=False, waveKinematicsMaxColumns=0, waveKinematicsTimeColumn=0, waveKinematicsStorage=False, fileFormat=StorageType.BINARY, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.kinematicsPosition = kinematicsPosition
        self.kinematicsInWaveZone = kinematicsInWaveZone
        self.defaultProcedureOn = defaultProcedureOn
        self.nodeStep = nodeStep
        self.zLower = zLower
        self.zUpper = zUpper
        self.applyDiffractedWaves = applyDiffractedWaves
        self.waveKinematicDiffPoints = list()
        self.waveKinematicNodePoints = list()
        self.waveKinematicsFile = waveKinematicsFile
        self.waveKinematicsFileName = None
        self.waveKinematicsTimeSeriesReferences = list()
        self.waveKinematicsMaxColumns = waveKinematicsMaxColumns
        self.waveKinematicsTimeColumn = waveKinematicsTimeColumn
        self.waveKinematicsStorage = waveKinematicsStorage
        self.fileFormat = fileFormat
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return IrregularWaveProcedureBlueprint()


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
    def kinematicsPosition(self) -> KinematicsPositions:
        """Kinematic positions"""
        return self.__kinematicsPosition

    @kinematicsPosition.setter
    def kinematicsPosition(self, value: KinematicsPositions):
        """Set kinematicsPosition"""
        self.__kinematicsPosition = value

    @property
    def kinematicsInWaveZone(self) -> KinematicsInWaveZone:
        """Type of kinematics in wave zone"""
        return self.__kinematicsInWaveZone

    @kinematicsInWaveZone.setter
    def kinematicsInWaveZone(self, value: KinematicsInWaveZone):
        """Set kinematicsInWaveZone"""
        self.__kinematicsInWaveZone = value

    @property
    def defaultProcedureOn(self) -> bool:
        """If chosen the default kinematics points procedure is run in RIFLEX. If not chosen the default procedure is not run in RIFLEX. In both cases additional detailed specification of wave kinematics points are run if present."""
        return self.__defaultProcedureOn

    @defaultProcedureOn.setter
    def defaultProcedureOn(self, value: bool):
        """Set defaultProcedureOn"""
        self.__defaultProcedureOn = bool(value)

    @property
    def nodeStep(self) -> int:
        """Wave kinematics is calculated for every 'Node Step' node between Z Lower
and Z Upper"""
        return self.__nodeStep

    @nodeStep.setter
    def nodeStep(self, value: int):
        """Set nodeStep"""
        self.__nodeStep = int(value)

    @property
    def zLower(self) -> float:
        """Z-coordinate indicating lowest node position for which wave kinematics are calculated"""
        return self.__zLower

    @zLower.setter
    def zLower(self, value: float):
        """Set zLower"""
        self.__zLower = float(value)

    @property
    def zUpper(self) -> float:
        """Upper limit for wave kinematics"""
        return self.__zUpper

    @zUpper.setter
    def zUpper(self, value: float):
        """Set zUpper"""
        self.__zUpper = float(value)

    @property
    def applyDiffractedWaves(self) -> bool:
        """Whether diffracted wave points are to be specified"""
        return self.__applyDiffractedWaves

    @applyDiffractedWaves.setter
    def applyDiffractedWaves(self, value: bool):
        """Set applyDiffractedWaves"""
        self.__applyDiffractedWaves = bool(value)

    @property
    def waveKinematicDiffPoints(self) -> List[WaveKinematicsDiffPoint]:
        """"""
        return self.__waveKinematicDiffPoints

    @waveKinematicDiffPoints.setter
    def waveKinematicDiffPoints(self, value: List[WaveKinematicsDiffPoint]):
        """Set waveKinematicDiffPoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__waveKinematicDiffPoints = value

    @property
    def waveKinematicNodePoints(self) -> List[WaveKinematicsNodePoint]:
        """"""
        return self.__waveKinematicNodePoints

    @waveKinematicNodePoints.setter
    def waveKinematicNodePoints(self, value: List[WaveKinematicsNodePoint]):
        """Set waveKinematicNodePoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__waveKinematicNodePoints = value

    @property
    def waveKinematicsFile(self) -> bool:
        """Whether wave kinematics time series should be read from file or not"""
        return self.__waveKinematicsFile

    @waveKinematicsFile.setter
    def waveKinematicsFile(self, value: bool):
        """Set waveKinematicsFile"""
        self.__waveKinematicsFile = bool(value)

    @property
    def waveKinematicsFileName(self) -> str:
        """Reference to a wave kinematics file"""
        return self.__waveKinematicsFileName

    @waveKinematicsFileName.setter
    def waveKinematicsFileName(self, value: str):
        """Set waveKinematicsFileName"""
        self.__waveKinematicsFileName = value

    @property
    def waveKinematicsTimeSeriesReferences(self) -> List[WaveKinematicsTimeSeriesReference]:
        """"""
        return self.__waveKinematicsTimeSeriesReferences

    @waveKinematicsTimeSeriesReferences.setter
    def waveKinematicsTimeSeriesReferences(self, value: List[WaveKinematicsTimeSeriesReference]):
        """Set waveKinematicsTimeSeriesReferences"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__waveKinematicsTimeSeriesReferences = value

    @property
    def waveKinematicsMaxColumns(self) -> int:
        """Maximum number of columns in the wave kinematics time series file"""
        return self.__waveKinematicsMaxColumns

    @waveKinematicsMaxColumns.setter
    def waveKinematicsMaxColumns(self, value: int):
        """Set waveKinematicsMaxColumns"""
        self.__waveKinematicsMaxColumns = int(value)

    @property
    def waveKinematicsTimeColumn(self) -> int:
        """Column number for time in the wave kinematics time series file"""
        return self.__waveKinematicsTimeColumn

    @waveKinematicsTimeColumn.setter
    def waveKinematicsTimeColumn(self, value: int):
        """Set waveKinematicsTimeColumn"""
        self.__waveKinematicsTimeColumn = int(value)

    @property
    def waveKinematicsStorage(self) -> bool:
        """Wave kinematics storage indicator"""
        return self.__waveKinematicsStorage

    @waveKinematicsStorage.setter
    def waveKinematicsStorage(self, value: bool):
        """Set waveKinematicsStorage"""
        self.__waveKinematicsStorage = bool(value)

    @property
    def fileFormat(self) -> StorageType:
        """"""
        return self.__fileFormat

    @fileFormat.setter
    def fileFormat(self, value: StorageType):
        """Set fileFormat"""
        self.__fileFormat = value
