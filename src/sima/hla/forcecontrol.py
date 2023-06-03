# This an autogenerated file
# 
# Generated with ForceControl
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.forcecontrol import ForceControlBlueprint
from typing import Dict
from sima.custom import CustomComponent
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .hlaforce import HLAForce

class ForceControl(CustomComponent):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    force : HLAForce
    fx : float
         (default 0.0)
    fy : float
         (default 0.0)
    fz : float
         (default 0.0)
    mx : float
         (default 0.0)
    my : float
         (default 0.0)
    mz : float
         (default 0.0)
    """

    def __init__(self , description="", fx=0.0, fy=0.0, fz=0.0, mx=0.0, my=0.0, mz=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.force = None
        self.fx = fx
        self.fy = fy
        self.fz = fz
        self.mx = mx
        self.my = my
        self.mz = mz
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ForceControlBlueprint()


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
    def force(self) -> HLAForce:
        """"""
        return self.__force

    @force.setter
    def force(self, value: HLAForce):
        """Set force"""
        self.__force = value

    @property
    def fx(self) -> float:
        """"""
        return self.__fx

    @fx.setter
    def fx(self, value: float):
        """Set fx"""
        self.__fx = float(value)

    @property
    def fy(self) -> float:
        """"""
        return self.__fy

    @fy.setter
    def fy(self, value: float):
        """Set fy"""
        self.__fy = float(value)

    @property
    def fz(self) -> float:
        """"""
        return self.__fz

    @fz.setter
    def fz(self, value: float):
        """Set fz"""
        self.__fz = float(value)

    @property
    def mx(self) -> float:
        """"""
        return self.__mx

    @mx.setter
    def mx(self, value: float):
        """Set mx"""
        self.__mx = float(value)

    @property
    def my(self) -> float:
        """"""
        return self.__my

    @my.setter
    def my(self, value: float):
        """Set my"""
        self.__my = float(value)

    @property
    def mz(self) -> float:
        """"""
        return self.__mz

    @mz.setter
    def mz(self, value: float):
        """Set mz"""
        self.__mz = float(value)
