# This an autogenerated file
# 
# Generated with SNCurve
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.sncurve import SNCurveBlueprint
from typing import Dict
from sima.riflex.fatiguelimitindicator import FatigueLimitIndicator
from sima.riflex.sncurveitem import SNCurveItem
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class SNCurve(NamedObject):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    fatigueLimitIndicator : FatigueLimitIndicator
         Fatigue limit indicator
    fatigueLimit : float
         Point where SN curve becomes horizontal. Stresses below this line will not contribute to fatigue damage.(default 0.0)
    referenceThickness : float
         Reference thickness for thickness correction. A value of zero will give no thickness correction.(default 0.0)
    thicknessCorrectionExponent : float
         Exponent for thickness correction(default 0.0)
    firstSlope : float
         Slope of the SN curve - m(default 0.0)
    constant : float
         Constant defining the SN curve. First segment or total curve - logC (for a SN-curve given in MPa)(default 0.0)
    curveItems : List[SNCurveItem]
    """

    def __init__(self , description="", fatigueLimitIndicator=FatigueLimitIndicator.NO_LIMIT, fatigueLimit=0.0, referenceThickness=0.0, thicknessCorrectionExponent=0.0, firstSlope=0.0, constant=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.fatigueLimitIndicator = fatigueLimitIndicator
        self.fatigueLimit = fatigueLimit
        self.referenceThickness = referenceThickness
        self.thicknessCorrectionExponent = thicknessCorrectionExponent
        self.firstSlope = firstSlope
        self.constant = constant
        self.curveItems = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SNCurveBlueprint()


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
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def fatigueLimitIndicator(self) -> FatigueLimitIndicator:
        """Fatigue limit indicator"""
        return self.__fatigueLimitIndicator

    @fatigueLimitIndicator.setter
    def fatigueLimitIndicator(self, value: FatigueLimitIndicator):
        """Set fatigueLimitIndicator"""
        self.__fatigueLimitIndicator = value

    @property
    def fatigueLimit(self) -> float:
        """Point where SN curve becomes horizontal. Stresses below this line will not contribute to fatigue damage."""
        return self.__fatigueLimit

    @fatigueLimit.setter
    def fatigueLimit(self, value: float):
        """Set fatigueLimit"""
        self.__fatigueLimit = float(value)

    @property
    def referenceThickness(self) -> float:
        """Reference thickness for thickness correction. A value of zero will give no thickness correction."""
        return self.__referenceThickness

    @referenceThickness.setter
    def referenceThickness(self, value: float):
        """Set referenceThickness"""
        self.__referenceThickness = float(value)

    @property
    def thicknessCorrectionExponent(self) -> float:
        """Exponent for thickness correction"""
        return self.__thicknessCorrectionExponent

    @thicknessCorrectionExponent.setter
    def thicknessCorrectionExponent(self, value: float):
        """Set thicknessCorrectionExponent"""
        self.__thicknessCorrectionExponent = float(value)

    @property
    def firstSlope(self) -> float:
        """Slope of the SN curve - m"""
        return self.__firstSlope

    @firstSlope.setter
    def firstSlope(self, value: float):
        """Set firstSlope"""
        self.__firstSlope = float(value)

    @property
    def constant(self) -> float:
        """Constant defining the SN curve. First segment or total curve - logC (for a SN-curve given in MPa)"""
        return self.__constant

    @constant.setter
    def constant(self, value: float):
        """Set constant"""
        self.__constant = float(value)

    @property
    def curveItems(self) -> List[SNCurveItem]:
        """"""
        return self.__curveItems

    @curveItems.setter
    def curveItems(self, value: List[SNCurveItem]):
        """Set curveItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__curveItems = value
