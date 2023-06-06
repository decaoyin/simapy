# This an autogenerated file
# 
# Generated with FoilPoint
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.foilpoint import FoilPointBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue

class FoilPoint(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    x : float
         Foil point in x-axis(default 0.0)
    y : float
         Foil point in y-axis(default 0.0)
    """

    def __init__(self , description="", x=0.0, y=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.x = x
        self.y = y
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FoilPointBlueprint()


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
    def x(self) -> float:
        """Foil point in x-axis"""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """Foil point in y-axis"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)
