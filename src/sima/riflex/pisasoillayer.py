# This an autogenerated file
# 
# Generated with PisaSoilLayer
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.pisasoillayer import PisaSoilLayerBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.soiltype import SoilType

class PisaSoilLayer(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    soilType : SoilType
    deltaZ : float
         Height of soil layer(default 0.0)
    shearModulusTop : float
         Shear modulus at top of soil layer(default 0.0)
    shearModulusBottom : float
         Shear modulus at bottom of soil layer(default 0.0)
    effectiveWeightTop : float
         Effective soil weight (gamma) at top of soil layer(default 0.0)
    effectiveWeightBottom : float
         Effective soil weight (gamma) at bottom of soil layer(default 0.0)
    undrainedShearStrengthTop : float
         Undrained shear strength (Su) at top of soil layer. Applies for clay only.(default 0.0)
    undrainedShearStrengthBottom : float
         Undrained shear strength (Su) at bottom of soil layer. Applies for clay only.(default 0.0)
    relativeDensity : float
         Relative density used for scaling soil curve. Applies for Dunkirk sand only.(default 100.0)
    """

    def __init__(self , description="", deltaZ=0.0, shearModulusTop=0.0, shearModulusBottom=0.0, effectiveWeightTop=0.0, effectiveWeightBottom=0.0, undrainedShearStrengthTop=0.0, undrainedShearStrengthBottom=0.0, relativeDensity=100.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.soilType = None
        self.deltaZ = deltaZ
        self.shearModulusTop = shearModulusTop
        self.shearModulusBottom = shearModulusBottom
        self.effectiveWeightTop = effectiveWeightTop
        self.effectiveWeightBottom = effectiveWeightBottom
        self.undrainedShearStrengthTop = undrainedShearStrengthTop
        self.undrainedShearStrengthBottom = undrainedShearStrengthBottom
        self.relativeDensity = relativeDensity
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PisaSoilLayerBlueprint()


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
    def soilType(self) -> SoilType:
        """"""
        return self.__soilType

    @soilType.setter
    def soilType(self, value: SoilType):
        """Set soilType"""
        self.__soilType = value

    @property
    def deltaZ(self) -> float:
        """Height of soil layer"""
        return self.__deltaZ

    @deltaZ.setter
    def deltaZ(self, value: float):
        """Set deltaZ"""
        self.__deltaZ = float(value)

    @property
    def shearModulusTop(self) -> float:
        """Shear modulus at top of soil layer"""
        return self.__shearModulusTop

    @shearModulusTop.setter
    def shearModulusTop(self, value: float):
        """Set shearModulusTop"""
        self.__shearModulusTop = float(value)

    @property
    def shearModulusBottom(self) -> float:
        """Shear modulus at bottom of soil layer"""
        return self.__shearModulusBottom

    @shearModulusBottom.setter
    def shearModulusBottom(self, value: float):
        """Set shearModulusBottom"""
        self.__shearModulusBottom = float(value)

    @property
    def effectiveWeightTop(self) -> float:
        """Effective soil weight (gamma) at top of soil layer"""
        return self.__effectiveWeightTop

    @effectiveWeightTop.setter
    def effectiveWeightTop(self, value: float):
        """Set effectiveWeightTop"""
        self.__effectiveWeightTop = float(value)

    @property
    def effectiveWeightBottom(self) -> float:
        """Effective soil weight (gamma) at bottom of soil layer"""
        return self.__effectiveWeightBottom

    @effectiveWeightBottom.setter
    def effectiveWeightBottom(self, value: float):
        """Set effectiveWeightBottom"""
        self.__effectiveWeightBottom = float(value)

    @property
    def undrainedShearStrengthTop(self) -> float:
        """Undrained shear strength (Su) at top of soil layer. Applies for clay only."""
        return self.__undrainedShearStrengthTop

    @undrainedShearStrengthTop.setter
    def undrainedShearStrengthTop(self, value: float):
        """Set undrainedShearStrengthTop"""
        self.__undrainedShearStrengthTop = float(value)

    @property
    def undrainedShearStrengthBottom(self) -> float:
        """Undrained shear strength (Su) at bottom of soil layer. Applies for clay only."""
        return self.__undrainedShearStrengthBottom

    @undrainedShearStrengthBottom.setter
    def undrainedShearStrengthBottom(self, value: float):
        """Set undrainedShearStrengthBottom"""
        self.__undrainedShearStrengthBottom = float(value)

    @property
    def relativeDensity(self) -> float:
        """Relative density used for scaling soil curve. Applies for Dunkirk sand only."""
        return self.__relativeDensity

    @relativeDensity.setter
    def relativeDensity(self, value: float):
        """Set relativeDensity"""
        self.__relativeDensity = float(value)
