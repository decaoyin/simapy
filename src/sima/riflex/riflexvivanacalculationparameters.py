# This an autogenerated file
# 
# Generated with RIFLEXVivanaCalculationParameters
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.riflexvivanacalculationparameters import RIFLEXVivanaCalculationParametersBlueprint
from typing import Dict
from .addedmassfrequencydependency import AddedMassFrequencyDependency
from .addedmassproperty import AddedMassProperty
from .dampingfactorproperty import DampingFactorProperty
from .eigenvalueanalysisparameters import EigenvalueAnalysisParameters
from .excitationcoefficientsproperty import ExcitationCoefficientsProperty
from .excitationzoneproperty import ExcitationZoneProperty
from .fatigueproperties import FatigueProperties
from .hydrodynamiccrosssectionproperties import HydrodynamicCrossSectionProperties
from .responseanalysisparameters import ResponseAnalysisParameters
from .strouhalspecificationproperty import StrouhalSpecificationProperty
from .vivloadtype import VIVLoadType
from sima.sima import MOAO
from sima.sima import ScriptableValue
from sima.simo import RandomGenerator

class RIFLEXVivanaCalculationParameters(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    eigenvalueAnalysisParameters : EigenvalueAnalysisParameters
    responseAnalysisParameters : ResponseAnalysisParameters
    fatigueProperties : FatigueProperties
    vivLoadType : VIVLoadType
         Option for type of VIV loads to be applied
    waterTemperature : float
         Water temperature(default 4.0)
    randomGenerator : RandomGenerator
    hydrodynamicCrossSectionProperties : List[HydrodynamicCrossSectionProperties]
    excitationZoneProperties : List[ExcitationZoneProperty]
    addedMassProperties : List[AddedMassProperty]
    excitationCoefficientProperties : List[ExcitationCoefficientsProperty]
    dampingFactorProperties : List[DampingFactorProperty]
    strouhalSpecificationProperties : List[StrouhalSpecificationProperty]
    addedMassFirstModeNumber : int
         First mode number in the active VIV direction for which the constant still-water added mass will be used.(default 1000000)
    addedMassLastModeNumber : int
         Last mode number in the active VIV direction for which the full frequency-dependent added mass curves will be used.(default 1000000)
    addedMassFrequencyDependence : AddedMassFrequencyDependency
    """

    def __init__(self , description="", vivLoadType=VIVLoadType.CROSS_FLOW, waterTemperature=4.0, randomGenerator=RandomGenerator.MERSENNE, addedMassFirstModeNumber=1000000, addedMassLastModeNumber=1000000, addedMassFrequencyDependence=AddedMassFrequencyDependency.FREQUENCY_ADDED_MASS, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.eigenvalueAnalysisParameters = None
        self.responseAnalysisParameters = None
        self.fatigueProperties = None
        self.vivLoadType = vivLoadType
        self.waterTemperature = waterTemperature
        self.randomGenerator = randomGenerator
        self.hydrodynamicCrossSectionProperties = list()
        self.excitationZoneProperties = list()
        self.addedMassProperties = list()
        self.excitationCoefficientProperties = list()
        self.dampingFactorProperties = list()
        self.strouhalSpecificationProperties = list()
        self.addedMassFirstModeNumber = addedMassFirstModeNumber
        self.addedMassLastModeNumber = addedMassLastModeNumber
        self.addedMassFrequencyDependence = addedMassFrequencyDependence
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXVivanaCalculationParametersBlueprint()


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
    def eigenvalueAnalysisParameters(self) -> EigenvalueAnalysisParameters:
        """"""
        return self.__eigenvalueAnalysisParameters

    @eigenvalueAnalysisParameters.setter
    def eigenvalueAnalysisParameters(self, value: EigenvalueAnalysisParameters):
        """Set eigenvalueAnalysisParameters"""
        self.__eigenvalueAnalysisParameters = value

    @property
    def responseAnalysisParameters(self) -> ResponseAnalysisParameters:
        """"""
        return self.__responseAnalysisParameters

    @responseAnalysisParameters.setter
    def responseAnalysisParameters(self, value: ResponseAnalysisParameters):
        """Set responseAnalysisParameters"""
        self.__responseAnalysisParameters = value

    @property
    def fatigueProperties(self) -> FatigueProperties:
        """"""
        return self.__fatigueProperties

    @fatigueProperties.setter
    def fatigueProperties(self, value: FatigueProperties):
        """Set fatigueProperties"""
        self.__fatigueProperties = value

    @property
    def vivLoadType(self) -> VIVLoadType:
        """Option for type of VIV loads to be applied"""
        return self.__vivLoadType

    @vivLoadType.setter
    def vivLoadType(self, value: VIVLoadType):
        """Set vivLoadType"""
        self.__vivLoadType = value

    @property
    def waterTemperature(self) -> float:
        """Water temperature"""
        return self.__waterTemperature

    @waterTemperature.setter
    def waterTemperature(self, value: float):
        """Set waterTemperature"""
        self.__waterTemperature = float(value)

    @property
    def randomGenerator(self) -> RandomGenerator:
        """"""
        return self.__randomGenerator

    @randomGenerator.setter
    def randomGenerator(self, value: RandomGenerator):
        """Set randomGenerator"""
        self.__randomGenerator = value

    @property
    def hydrodynamicCrossSectionProperties(self) -> List[HydrodynamicCrossSectionProperties]:
        """"""
        return self.__hydrodynamicCrossSectionProperties

    @hydrodynamicCrossSectionProperties.setter
    def hydrodynamicCrossSectionProperties(self, value: List[HydrodynamicCrossSectionProperties]):
        """Set hydrodynamicCrossSectionProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__hydrodynamicCrossSectionProperties = value

    @property
    def excitationZoneProperties(self) -> List[ExcitationZoneProperty]:
        """"""
        return self.__excitationZoneProperties

    @excitationZoneProperties.setter
    def excitationZoneProperties(self, value: List[ExcitationZoneProperty]):
        """Set excitationZoneProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__excitationZoneProperties = value

    @property
    def addedMassProperties(self) -> List[AddedMassProperty]:
        """"""
        return self.__addedMassProperties

    @addedMassProperties.setter
    def addedMassProperties(self, value: List[AddedMassProperty]):
        """Set addedMassProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__addedMassProperties = value

    @property
    def excitationCoefficientProperties(self) -> List[ExcitationCoefficientsProperty]:
        """"""
        return self.__excitationCoefficientProperties

    @excitationCoefficientProperties.setter
    def excitationCoefficientProperties(self, value: List[ExcitationCoefficientsProperty]):
        """Set excitationCoefficientProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__excitationCoefficientProperties = value

    @property
    def dampingFactorProperties(self) -> List[DampingFactorProperty]:
        """"""
        return self.__dampingFactorProperties

    @dampingFactorProperties.setter
    def dampingFactorProperties(self, value: List[DampingFactorProperty]):
        """Set dampingFactorProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__dampingFactorProperties = value

    @property
    def strouhalSpecificationProperties(self) -> List[StrouhalSpecificationProperty]:
        """"""
        return self.__strouhalSpecificationProperties

    @strouhalSpecificationProperties.setter
    def strouhalSpecificationProperties(self, value: List[StrouhalSpecificationProperty]):
        """Set strouhalSpecificationProperties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__strouhalSpecificationProperties = value

    @property
    def addedMassFirstModeNumber(self) -> int:
        """First mode number in the active VIV direction for which the constant still-water added mass will be used."""
        return self.__addedMassFirstModeNumber

    @addedMassFirstModeNumber.setter
    def addedMassFirstModeNumber(self, value: int):
        """Set addedMassFirstModeNumber"""
        self.__addedMassFirstModeNumber = int(value)

    @property
    def addedMassLastModeNumber(self) -> int:
        """Last mode number in the active VIV direction for which the full frequency-dependent added mass curves will be used."""
        return self.__addedMassLastModeNumber

    @addedMassLastModeNumber.setter
    def addedMassLastModeNumber(self, value: int):
        """Set addedMassLastModeNumber"""
        self.__addedMassLastModeNumber = int(value)

    @property
    def addedMassFrequencyDependence(self) -> AddedMassFrequencyDependency:
        """"""
        return self.__addedMassFrequencyDependence

    @addedMassFrequencyDependence.setter
    def addedMassFrequencyDependence(self, value: AddedMassFrequencyDependency):
        """Set addedMassFrequencyDependence"""
        self.__addedMassFrequencyDependence = value
