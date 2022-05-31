# This an autogenerated file
# 
# Generated with StaticEquilibriumBody
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.staticequilibriumbody import StaticEquilibriumBodyBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.simobody import SIMOBody

class StaticEquilibriumBody(MOAO):
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
    body : SIMOBody
         Selected body to compute equilibrium for
    x : float
         Excursion along global X axis(default 1.0)
    y : float
         Excursion along global Y axis(default 1.0)
    z : float
         Excursion along global Z axis(default 1.0)
    rx : float
         Excursion of rotation about global X axis(default 1.0)
    ry : float
         Excursion of rotation about global Y axis(default 1.0)
    rz : float
         Excursion of rotation about global Z axis(default 1.0)
    """

    def __init__(self , name="", description="", _id="", x=1.0, y=1.0, z=1.0, rx=1.0, ry=1.0, rz=1.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.body = None
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return StaticEquilibriumBodyBlueprint()


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
    def body(self) -> SIMOBody:
        """Selected body to compute equilibrium for"""
        return self.__body

    @body.setter
    def body(self, value: SIMOBody):
        """Set body"""
        self.__body = value

    @property
    def x(self) -> float:
        """Excursion along global X axis"""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set x"""
        self.__x = float(value)

    @property
    def y(self) -> float:
        """Excursion along global Y axis"""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set y"""
        self.__y = float(value)

    @property
    def z(self) -> float:
        """Excursion along global Z axis"""
        return self.__z

    @z.setter
    def z(self, value: float):
        """Set z"""
        self.__z = float(value)

    @property
    def rx(self) -> float:
        """Excursion of rotation about global X axis"""
        return self.__rx

    @rx.setter
    def rx(self, value: float):
        """Set rx"""
        self.__rx = float(value)

    @property
    def ry(self) -> float:
        """Excursion of rotation about global Y axis"""
        return self.__ry

    @ry.setter
    def ry(self, value: float):
        """Set ry"""
        self.__ry = float(value)

    @property
    def rz(self) -> float:
        """Excursion of rotation about global Z axis"""
        return self.__rz

    @rz.setter
    def rz(self, value: float):
        """Set rz"""
        self.__rz = float(value)
