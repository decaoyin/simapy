# This an autogenerated file
# 
# Generated with StrouhalConstantNumberProperty
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.strouhalconstantnumberproperty import StrouhalConstantNumberPropertyBlueprint
from typing import Dict
from sima.riflex.strouhalspecificationproperty import StrouhalSpecificationProperty
from sima.sima.scriptablevalue import ScriptableValue

class StrouhalConstantNumberProperty(StrouhalSpecificationProperty):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    fixedStrouhalNumber : float
         Fixed Strouhal number(default 0.19)
    """

    def __init__(self , description="", fixedStrouhalNumber=0.19, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.fixedStrouhalNumber = fixedStrouhalNumber
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StrouhalConstantNumberPropertyBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def fixedStrouhalNumber(self) -> float:
        """Fixed Strouhal number"""
        return self.__fixedStrouhalNumber

    @fixedStrouhalNumber.setter
    def fixedStrouhalNumber(self, value: float):
        """Set fixedStrouhalNumber"""
        self.__fixedStrouhalNumber = float(value)
