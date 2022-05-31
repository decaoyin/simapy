# This an autogenerated file
# 
# Generated with CommonSoilCoefficients
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.commonsoilcoefficients import CommonSoilCoefficientsBlueprint
from typing import Dict
from sima.riflex.commonsoilcoefficientsitem import CommonSoilCoefficientsItem
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CommonSoilCoefficients(MOAO):
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
    xu : CommonSoilCoefficientsItem
    k : CommonSoilCoefficientsItem
    n : CommonSoilCoefficientsItem
    yu : CommonSoilCoefficientsItem
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.xu = None
        self.k = None
        self.n = None
        self.yu = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CommonSoilCoefficientsBlueprint()


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
    def xu(self) -> CommonSoilCoefficientsItem:
        """"""
        return self.__xu

    @xu.setter
    def xu(self, value: CommonSoilCoefficientsItem):
        """Set xu"""
        self.__xu = value

    @property
    def k(self) -> CommonSoilCoefficientsItem:
        """"""
        return self.__k

    @k.setter
    def k(self, value: CommonSoilCoefficientsItem):
        """Set k"""
        self.__k = value

    @property
    def n(self) -> CommonSoilCoefficientsItem:
        """"""
        return self.__n

    @n.setter
    def n(self, value: CommonSoilCoefficientsItem):
        """Set n"""
        self.__n = value

    @property
    def yu(self) -> CommonSoilCoefficientsItem:
        """"""
        return self.__yu

    @yu.setter
    def yu(self, value: CommonSoilCoefficientsItem):
        """Set yu"""
        self.__yu = value
