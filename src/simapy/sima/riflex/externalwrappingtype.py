# This an autogenerated file
# 
# Generated with ExternalWrappingType
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.externalwrappingtype import ExternalWrappingTypeBlueprint
from typing import Dict
from ..sima import NamedObject
from ..sima import ScriptableValue

class ExternalWrappingType(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    mass : float
         Mass per unit length(default 0.0)
    buoyancy : float
         Buoyancy volume/length(default 0.0)
    gyrationRadius : float
         Radius of gyration around x-axis(default 0.0)
    coveredFraction : float
         Fraction of the segment that is covered. 0 < FRAC < 1.0.(default 0.0)
    wrappingItemLength : float
         Length of wrapping item. Only used for graphics.(default 1.0)
    tangentialDrag : float
         Drag force coefficient in tangential direction(default 0.0)
    normalDrag : float
         Drag force coefficient in normal direction(default 0.0)
    tangentialAddedMass : float
         Added mass per length in tangential direction(default 0.0)
    normalAddedMass : float
         Added mass per length in normal direction(default 0.0)
    tangentialLinearDrag : float
         Linear drag force coefficients in tangential direction(default 0.0)
    normalLinearDrag : float
         Linear drag force coefficients in tangential direction(default 0.0)
    """

    def __init__(self , description="", mass=0.0, buoyancy=0.0, gyrationRadius=0.0, coveredFraction=0.0, wrappingItemLength=1.0, tangentialDrag=0.0, normalDrag=0.0, tangentialAddedMass=0.0, normalAddedMass=0.0, tangentialLinearDrag=0.0, normalLinearDrag=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.mass = mass
        self.buoyancy = buoyancy
        self.gyrationRadius = gyrationRadius
        self.coveredFraction = coveredFraction
        self.wrappingItemLength = wrappingItemLength
        self.tangentialDrag = tangentialDrag
        self.normalDrag = normalDrag
        self.tangentialAddedMass = tangentialAddedMass
        self.normalAddedMass = normalAddedMass
        self.tangentialLinearDrag = tangentialLinearDrag
        self.normalLinearDrag = normalLinearDrag
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ExternalWrappingTypeBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def mass(self) -> float:
        """Mass per unit length"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def buoyancy(self) -> float:
        """Buoyancy volume/length"""
        return self.__buoyancy

    @buoyancy.setter
    def buoyancy(self, value: float):
        """Set buoyancy"""
        self.__buoyancy = float(value)

    @property
    def gyrationRadius(self) -> float:
        """Radius of gyration around x-axis"""
        return self.__gyrationRadius

    @gyrationRadius.setter
    def gyrationRadius(self, value: float):
        """Set gyrationRadius"""
        self.__gyrationRadius = float(value)

    @property
    def coveredFraction(self) -> float:
        """Fraction of the segment that is covered. 0 < FRAC < 1.0."""
        return self.__coveredFraction

    @coveredFraction.setter
    def coveredFraction(self, value: float):
        """Set coveredFraction"""
        self.__coveredFraction = float(value)

    @property
    def wrappingItemLength(self) -> float:
        """Length of wrapping item. Only used for graphics."""
        return self.__wrappingItemLength

    @wrappingItemLength.setter
    def wrappingItemLength(self, value: float):
        """Set wrappingItemLength"""
        self.__wrappingItemLength = float(value)

    @property
    def tangentialDrag(self) -> float:
        """Drag force coefficient in tangential direction"""
        return self.__tangentialDrag

    @tangentialDrag.setter
    def tangentialDrag(self, value: float):
        """Set tangentialDrag"""
        self.__tangentialDrag = float(value)

    @property
    def normalDrag(self) -> float:
        """Drag force coefficient in normal direction"""
        return self.__normalDrag

    @normalDrag.setter
    def normalDrag(self, value: float):
        """Set normalDrag"""
        self.__normalDrag = float(value)

    @property
    def tangentialAddedMass(self) -> float:
        """Added mass per length in tangential direction"""
        return self.__tangentialAddedMass

    @tangentialAddedMass.setter
    def tangentialAddedMass(self, value: float):
        """Set tangentialAddedMass"""
        self.__tangentialAddedMass = float(value)

    @property
    def normalAddedMass(self) -> float:
        """Added mass per length in normal direction"""
        return self.__normalAddedMass

    @normalAddedMass.setter
    def normalAddedMass(self, value: float):
        """Set normalAddedMass"""
        self.__normalAddedMass = float(value)

    @property
    def tangentialLinearDrag(self) -> float:
        """Linear drag force coefficients in tangential direction"""
        return self.__tangentialLinearDrag

    @tangentialLinearDrag.setter
    def tangentialLinearDrag(self, value: float):
        """Set tangentialLinearDrag"""
        self.__tangentialLinearDrag = float(value)

    @property
    def normalLinearDrag(self) -> float:
        """Linear drag force coefficients in tangential direction"""
        return self.__normalLinearDrag

    @normalLinearDrag.setter
    def normalLinearDrag(self, value: float):
        """Set normalLinearDrag"""
        self.__normalLinearDrag = float(value)
