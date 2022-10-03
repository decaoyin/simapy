# This an autogenerated file
# 
# Generated with NonLinearHydrostaticStiffness
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.nonlinearhydrostaticstiffness import NonLinearHydrostaticStiffnessBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.position import Position
from sima.sima.scriptablevalue import ScriptableValue

class NonLinearHydrostaticStiffness(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    geometryPosition : Position
    geometryFile : str
         Geometry definition file(default "")
    transparency : float
         Geometry transparency, [0-1], where 1 is full transparency.(default 0.0)
    """

    def __init__(self , _id="", geometryFile="", transparency=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.geometryPosition = None
        self.geometryFile = geometryFile
        self.transparency = transparency
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NonLinearHydrostaticStiffnessBlueprint()


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
    def geometryPosition(self) -> Position:
        """"""
        return self.__geometryPosition

    @geometryPosition.setter
    def geometryPosition(self, value: Position):
        """Set geometryPosition"""
        self.__geometryPosition = value

    @property
    def geometryFile(self) -> str:
        """Geometry definition file"""
        return self.__geometryFile

    @geometryFile.setter
    def geometryFile(self, value: str):
        """Set geometryFile"""
        self.__geometryFile = str(value)

    @property
    def transparency(self) -> float:
        """Geometry transparency, [0-1], where 1 is full transparency."""
        return self.__transparency

    @transparency.setter
    def transparency(self, value: float):
        """Set transparency"""
        self.__transparency = float(value)
