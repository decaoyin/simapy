# This an autogenerated file
# 
# Generated with StaticConditionResult
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.staticconditionresult import StaticConditionResultBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.bodyresult import BodyResult

class StaticConditionResult(MOAO):
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
    bodyResults : List[BodyResult]
    header : str
         (default "")
    dateTag : str
         (default "")
    filepart : str
         (default "")
    globalForces : bool
         (default True)
    """

    def __init__(self , name="", description="", _id="", header="", dateTag="", filepart="", globalForces=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.bodyResults = list()
        self.header = header
        self.dateTag = dateTag
        self.filepart = filepart
        self.globalForces = globalForces
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StaticConditionResultBlueprint()


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
    def bodyResults(self) -> List[BodyResult]:
        """"""
        return self.__bodyResults

    @bodyResults.setter
    def bodyResults(self, value: List[BodyResult]):
        """Set bodyResults"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__bodyResults = value

    @property
    def header(self) -> str:
        """"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = str(value)

    @property
    def dateTag(self) -> str:
        """"""
        return self.__dateTag

    @dateTag.setter
    def dateTag(self, value: str):
        """Set dateTag"""
        self.__dateTag = str(value)

    @property
    def filepart(self) -> str:
        """"""
        return self.__filepart

    @filepart.setter
    def filepart(self, value: str):
        """Set filepart"""
        self.__filepart = str(value)

    @property
    def globalForces(self) -> bool:
        """"""
        return self.__globalForces

    @globalForces.setter
    def globalForces(self, value: bool):
        """Set globalForces"""
        self.__globalForces = bool(value)
