# This an autogenerated file
# 
# Generated with PhysicalConstants
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.physicalconstants import PhysicalConstantsBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class PhysicalConstants(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    waterDensity : float
         Water density - rho water(default 1025.0)
    accOfGravity : float
         Acceleration of gravity - g(default 9.81)
    """

    def __init__(self , description="", waterDensity=1025.0, accOfGravity=9.81, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.waterDensity = waterDensity
        self.accOfGravity = accOfGravity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PhysicalConstantsBlueprint()


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
    def waterDensity(self) -> float:
        """Water density - rho water"""
        return self.__waterDensity

    @waterDensity.setter
    def waterDensity(self, value: float):
        """Set waterDensity"""
        self.__waterDensity = float(value)

    @property
    def accOfGravity(self) -> float:
        """Acceleration of gravity - g"""
        return self.__accOfGravity

    @accOfGravity.setter
    def accOfGravity(self, value: float):
        """Set accOfGravity"""
        self.__accOfGravity = float(value)