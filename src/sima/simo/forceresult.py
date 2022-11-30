# This an autogenerated file
# 
# Generated with ForceResult
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.forceresult import ForceResultBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class ForceResult(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         Force name(default None)
    fx : float
         Statically calculated force(default 0.0)
    fy : float
         Statically calculated force(default 0.0)
    fz : float
         Statically calculated force(default 0.0)
    mx : float
         Statically calculated moment(default 0.0)
    my : float
         Statically calculated moment(default 0.0)
    mz : float
         Statically calculated moment(default 0.0)
    mass : float
         Mass of object(default 0.0)
    """

    def __init__(self , description="", fx=0.0, fy=0.0, fz=0.0, mx=0.0, my=0.0, mz=0.0, mass=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.mx = mx
        self.my = my
        self.mz = mz
        self.mass = mass
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ForceResultBlueprint()


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
        """Force name"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def fx(self) -> float:
        """Statically calculated force"""
        return self.__fx

    @fx.setter
    def fx(self, value: float):
        """Set fx"""
        self.__fx = float(value)

    @property
    def fy(self) -> float:
        """Statically calculated force"""
        return self.__fy

    @fy.setter
    def fy(self, value: float):
        """Set fy"""
        self.__fy = float(value)

    @property
    def fz(self) -> float:
        """Statically calculated force"""
        return self.__fz

    @fz.setter
    def fz(self, value: float):
        """Set fz"""
        self.__fz = float(value)

    @property
    def mx(self) -> float:
        """Statically calculated moment"""
        return self.__mx

    @mx.setter
    def mx(self, value: float):
        """Set mx"""
        self.__mx = float(value)

    @property
    def my(self) -> float:
        """Statically calculated moment"""
        return self.__my

    @my.setter
    def my(self, value: float):
        """Set my"""
        self.__my = float(value)

    @property
    def mz(self) -> float:
        """Statically calculated moment"""
        return self.__mz

    @mz.setter
    def mz(self, value: float):
        """Set mz"""
        self.__mz = float(value)

    @property
    def mass(self) -> float:
        """Mass of object"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)
