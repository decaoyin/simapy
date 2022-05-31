# This an autogenerated file
# 
# Generated with CombinedLoadingProperties
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.combinedloadingproperties import CombinedLoadingPropertiesBlueprint
from typing import Dict
from sima.riflex.elementreference import ElementReference
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class CombinedLoadingProperties(ElementReference):
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
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    elementNumber : int
         Local element number on actual segment(default 1)
    allElements : bool
         All elements(default False)
    youngsFactor : float
         Young's modulus(default 210000000000.0)
    poissonsRatio : float
         Poisson's ratio for pipe wall material(default 0.3)
    yieldStrength : float
         Yield strength to be used in design(default 400000000.0)
    tensileStrength : float
         Tensile strength to be used in design(default 700000000.0)
    ovality : float
         Ovality(default 0.005)
    internalCorrosion : float
         Internal corrosion allowance(default 0.001)
    externalCorrosion : float
         External corrosion allowance(default 0.002)
    nominalDiameter : float
         Nominal outer diameter (D). If not set the value will be taken from the model(default 0.0)
    nominalThickness : float
         Nominal wall thickness (t_nom) of pipe (uncorroded), as specified on the drawing/specification (default 0.0)
    """

    def __init__(self , name="", description="", _id="", segment=1, allSegments=False, elementNumber=1, allElements=False, youngsFactor=210000000000.0, poissonsRatio=0.3, yieldStrength=400000000.0, tensileStrength=700000000.0, ovality=0.005, internalCorrosion=0.001, externalCorrosion=0.002, nominalDiameter=0.0, nominalThickness=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.elementNumber = elementNumber
        self.allElements = allElements
        self.youngsFactor = youngsFactor
        self.poissonsRatio = poissonsRatio
        self.yieldStrength = yieldStrength
        self.tensileStrength = tensileStrength
        self.ovality = ovality
        self.internalCorrosion = internalCorrosion
        self.externalCorrosion = externalCorrosion
        self.nominalDiameter = nominalDiameter
        self.nominalThickness = nominalThickness
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CombinedLoadingPropertiesBlueprint()


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
    def line(self) -> ARLine:
        """Line"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def segment(self) -> int:
        """Segment on given line"""
        return self.__segment

    @segment.setter
    def segment(self, value: int):
        """Set segment"""
        self.__segment = int(value)

    @property
    def allSegments(self) -> bool:
        """All segments"""
        return self.__allSegments

    @allSegments.setter
    def allSegments(self, value: bool):
        """Set allSegments"""
        self.__allSegments = bool(value)

    @property
    def elementNumber(self) -> int:
        """Local element number on actual segment"""
        return self.__elementNumber

    @elementNumber.setter
    def elementNumber(self, value: int):
        """Set elementNumber"""
        self.__elementNumber = int(value)

    @property
    def allElements(self) -> bool:
        """All elements"""
        return self.__allElements

    @allElements.setter
    def allElements(self, value: bool):
        """Set allElements"""
        self.__allElements = bool(value)

    @property
    def youngsFactor(self) -> float:
        """Young's modulus"""
        return self.__youngsFactor

    @youngsFactor.setter
    def youngsFactor(self, value: float):
        """Set youngsFactor"""
        self.__youngsFactor = float(value)

    @property
    def poissonsRatio(self) -> float:
        """Poisson's ratio for pipe wall material"""
        return self.__poissonsRatio

    @poissonsRatio.setter
    def poissonsRatio(self, value: float):
        """Set poissonsRatio"""
        self.__poissonsRatio = float(value)

    @property
    def yieldStrength(self) -> float:
        """Yield strength to be used in design"""
        return self.__yieldStrength

    @yieldStrength.setter
    def yieldStrength(self, value: float):
        """Set yieldStrength"""
        self.__yieldStrength = float(value)

    @property
    def tensileStrength(self) -> float:
        """Tensile strength to be used in design"""
        return self.__tensileStrength

    @tensileStrength.setter
    def tensileStrength(self, value: float):
        """Set tensileStrength"""
        self.__tensileStrength = float(value)

    @property
    def ovality(self) -> float:
        """Ovality"""
        return self.__ovality

    @ovality.setter
    def ovality(self, value: float):
        """Set ovality"""
        self.__ovality = float(value)

    @property
    def internalCorrosion(self) -> float:
        """Internal corrosion allowance"""
        return self.__internalCorrosion

    @internalCorrosion.setter
    def internalCorrosion(self, value: float):
        """Set internalCorrosion"""
        self.__internalCorrosion = float(value)

    @property
    def externalCorrosion(self) -> float:
        """External corrosion allowance"""
        return self.__externalCorrosion

    @externalCorrosion.setter
    def externalCorrosion(self, value: float):
        """Set externalCorrosion"""
        self.__externalCorrosion = float(value)

    @property
    def nominalDiameter(self) -> float:
        """Nominal outer diameter (D). If not set the value will be taken from the model"""
        return self.__nominalDiameter

    @nominalDiameter.setter
    def nominalDiameter(self, value: float):
        """Set nominalDiameter"""
        self.__nominalDiameter = float(value)

    @property
    def nominalThickness(self) -> float:
        """Nominal wall thickness (t_nom) of pipe (uncorroded), as specified on the drawing/specification """
        return self.__nominalThickness

    @nominalThickness.setter
    def nominalThickness(self, value: float):
        """Set nominalThickness"""
        self.__nominalThickness = float(value)
