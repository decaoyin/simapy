# This an autogenerated file
# 
# Generated with HLAPipeRoute
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hlapiperoute import HLAPipeRouteBlueprint
from typing import Dict
from sima.hla.hlaobject import HLAObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.simacolor import SIMAColor

class HLAPipeRoute(HLAObject):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    routeFile : str
         (default "")
    coordsUTM : str
         (default 'no')
    mapOnTerrain : str
         (default 'auto')
    routeWidth : float
         (default 0.0)
    color : SIMAColor
    routeWidthColor : SIMAColor
    """

    def __init__(self , _id="", name="", routeFile="", coordsUTM='no', mapOnTerrain='auto', routeWidth=0.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.routeFile = routeFile
        self.coordsUTM = coordsUTM
        self.mapOnTerrain = mapOnTerrain
        self.routeWidth = routeWidth
        self.color = None
        self.routeWidthColor = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLAPipeRouteBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def routeFile(self) -> str:
        """"""
        return self.__routeFile

    @routeFile.setter
    def routeFile(self, value: str):
        """Set routeFile"""
        self.__routeFile = str(value)

    @property
    def coordsUTM(self) -> str:
        """"""
        return self.__coordsUTM

    @coordsUTM.setter
    def coordsUTM(self, value: str):
        """Set coordsUTM"""
        self.__coordsUTM = str(value)

    @property
    def mapOnTerrain(self) -> str:
        """"""
        return self.__mapOnTerrain

    @mapOnTerrain.setter
    def mapOnTerrain(self, value: str):
        """Set mapOnTerrain"""
        self.__mapOnTerrain = str(value)

    @property
    def routeWidth(self) -> float:
        """"""
        return self.__routeWidth

    @routeWidth.setter
    def routeWidth(self, value: float):
        """Set routeWidth"""
        self.__routeWidth = float(value)

    @property
    def color(self) -> SIMAColor:
        """"""
        return self.__color

    @color.setter
    def color(self, value: SIMAColor):
        """Set color"""
        self.__color = value

    @property
    def routeWidthColor(self) -> SIMAColor:
        """"""
        return self.__routeWidthColor

    @routeWidthColor.setter
    def routeWidthColor(self, value: SIMAColor):
        """Set routeWidthColor"""
        self.__routeWidthColor = value
