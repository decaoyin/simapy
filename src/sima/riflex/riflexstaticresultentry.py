# This an autogenerated file
# 
# Generated with RIFLEXStaticResultEntry
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexstaticresultentry import RIFLEXStaticResultEntryBlueprint
from typing import Dict
from .resfile import ResFile
from sima.sima import Property
from sima.sima import Result
from sima.sima import ResultEntry
from sima.sima import ScriptableValue
from sima.simo import LisFile
from sima.simo import SIMOStaticResultEntry
from sima.simo import StaticResult

class RIFLEXStaticResultEntry(SIMOStaticResultEntry):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    properties : List[Property]
    resource : str
         (default None)
    relative : bool
         (default False)
    changeNumber : int
         (default 0)
    results : List[Result]
    entries : List[ResultEntry]
    lisFile : LisFile
    simoLDAT : Result
    staticResult : StaticResult
    riflexLDAT : Result
    inpmodResFile : ResFile
    stamodResFile : ResFile
    """

    def __init__(self , description="", relative=False, changeNumber=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.properties = list()
        self.resource = None
        self.relative = relative
        self.changeNumber = changeNumber
        self.results = list()
        self.entries = list()
        self.lisFile = None
        self.simoLDAT = None
        self.staticResult = None
        self.riflexLDAT = None
        self.inpmodResFile = None
        self.stamodResFile = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXStaticResultEntryBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def properties(self) -> List[Property]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[Property]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def resource(self) -> str:
        """"""
        return self.__resource

    @resource.setter
    def resource(self, value: str):
        """Set resource"""
        self.__resource = value

    @property
    def relative(self) -> bool:
        """"""
        return self.__relative

    @relative.setter
    def relative(self, value: bool):
        """Set relative"""
        self.__relative = bool(value)

    @property
    def changeNumber(self) -> int:
        """"""
        return self.__changeNumber

    @changeNumber.setter
    def changeNumber(self, value: int):
        """Set changeNumber"""
        self.__changeNumber = int(value)

    @property
    def results(self) -> List[Result]:
        """"""
        return self.__results

    @results.setter
    def results(self, value: List[Result]):
        """Set results"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__results = value

    @property
    def entries(self) -> List[ResultEntry]:
        """"""
        return self.__entries

    @entries.setter
    def entries(self, value: List[ResultEntry]):
        """Set entries"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__entries = value

    @property
    def lisFile(self) -> LisFile:
        """"""
        return self.__lisFile

    @lisFile.setter
    def lisFile(self, value: LisFile):
        """Set lisFile"""
        self.__lisFile = value

    @property
    def simoLDAT(self) -> Result:
        """"""
        return self.__simoLDAT

    @simoLDAT.setter
    def simoLDAT(self, value: Result):
        """Set simoLDAT"""
        self.__simoLDAT = value

    @property
    def staticResult(self) -> StaticResult:
        """"""
        return self.__staticResult

    @staticResult.setter
    def staticResult(self, value: StaticResult):
        """Set staticResult"""
        self.__staticResult = value

    @property
    def riflexLDAT(self) -> Result:
        """"""
        return self.__riflexLDAT

    @riflexLDAT.setter
    def riflexLDAT(self, value: Result):
        """Set riflexLDAT"""
        self.__riflexLDAT = value

    @property
    def inpmodResFile(self) -> ResFile:
        """"""
        return self.__inpmodResFile

    @inpmodResFile.setter
    def inpmodResFile(self, value: ResFile):
        """Set inpmodResFile"""
        self.__inpmodResFile = value

    @property
    def stamodResFile(self) -> ResFile:
        """"""
        return self.__stamodResFile

    @stamodResFile.setter
    def stamodResFile(self, value: ResFile):
        """Set stamodResFile"""
        self.__stamodResFile = value
