# This an autogenerated file
# 
# Generated with DNV_OS_F201CombinedLoading
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dnv_os_f201combinedloading import DNV_OS_F201CombinedLoadingBlueprint
from typing import Dict
from ..post import LimitStateCategory
from ..post import SafetyClass
from ..sima import ScriptableValue
from .combinedloading import CombinedLoading
from .combinedloadingapproach import CombinedLoadingApproach
from .combinedloadingproperties import CombinedLoadingProperties

class DNV_OS_F201CombinedLoading(CombinedLoading):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    refPointPressure : float
         Internal design pressure at vertical reference position(default 0.0)
    referencePoint : float
         Vertical reference position for internal pressure. \nGiven as the Z coordinate in global coordinate system.(default 0.0)
    limitTimeInterval : bool
         Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time(default False)
    startTime : float
         (default 0.0)
    endTime : float
         (default 0.0)
    addIntermediateResults : bool
         Add intermediate element results to the output(default False)
    properties : List[CombinedLoadingProperties]
         Specification of nodes for displacement storage
    useDistributionFitting : bool
         Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting(default False)
    seastateReturnPeriod : float
         Return period used for estimating the characteristic extreme value(default 3.0)
    percentile : float
         Specify percentile in extreme value distribution. \nThe value 0.57038 corresponds to the expected extreme, and 0.9 corresponds to 90% estimate of the extreme response(default 0.57038)
    approach : CombinedLoadingApproach
    customSafetyClassResistanceFactor : float
         Safety class resistance factor (ɣ SC)(default 0.0)
    customLoadEffectFactorForEnvironmentalLoads : float
         Load effect factor for environmental loads (ɣ E)(default 0.0)
    customLoadEffectFactorForFunctionalLoads : float
         Load effect factor for functional loads (ɣ F)(default 0.0)
    customLoadFactorForAccidentalLoads : float
         Load factor for accidental loads (ɣ A)(default 0.0)
    customMaterialResistanceFactor : float
         Material resistance factor (ɣ m)(default 0.0)
    fabricationFactor : float
         Fabrication factor (α fab)(default 0.85)
    safetyClass : SafetyClass
    limitStateCategory : LimitStateCategory
    lastFunctionalLoadGroup : int
         Number of the last load group in static calculation parameter that is part of the functional load(default 0)
    """

    def __init__(self , description="", refPointPressure=0.0, referencePoint=0.0, limitTimeInterval=False, startTime=0.0, endTime=0.0, addIntermediateResults=False, useDistributionFitting=False, seastateReturnPeriod=3.0, percentile=0.57038, approach=CombinedLoadingApproach.LRFD, customSafetyClassResistanceFactor=0.0, customLoadEffectFactorForEnvironmentalLoads=0.0, customLoadEffectFactorForFunctionalLoads=0.0, customLoadFactorForAccidentalLoads=0.0, customMaterialResistanceFactor=0.0, fabricationFactor=0.85, safetyClass=SafetyClass.LOW, limitStateCategory=LimitStateCategory.SLS, lastFunctionalLoadGroup=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.refPointPressure = refPointPressure
        self.referencePoint = referencePoint
        self.limitTimeInterval = limitTimeInterval
        self.startTime = startTime
        self.endTime = endTime
        self.addIntermediateResults = addIntermediateResults
        self.properties = list()
        self.useDistributionFitting = useDistributionFitting
        self.seastateReturnPeriod = seastateReturnPeriod
        self.percentile = percentile
        self.approach = approach
        self.customSafetyClassResistanceFactor = customSafetyClassResistanceFactor
        self.customLoadEffectFactorForEnvironmentalLoads = customLoadEffectFactorForEnvironmentalLoads
        self.customLoadEffectFactorForFunctionalLoads = customLoadEffectFactorForFunctionalLoads
        self.customLoadFactorForAccidentalLoads = customLoadFactorForAccidentalLoads
        self.customMaterialResistanceFactor = customMaterialResistanceFactor
        self.fabricationFactor = fabricationFactor
        self.safetyClass = safetyClass
        self.limitStateCategory = limitStateCategory
        self.lastFunctionalLoadGroup = lastFunctionalLoadGroup
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DNV_OS_F201CombinedLoadingBlueprint()


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
    def refPointPressure(self) -> float:
        """Internal design pressure at vertical reference position"""
        return self.__refPointPressure

    @refPointPressure.setter
    def refPointPressure(self, value: float):
        """Set refPointPressure"""
        self.__refPointPressure = float(value)

    @property
    def referencePoint(self) -> float:
        """Vertical reference position for internal pressure. 
Given as the Z coordinate in global coordinate system."""
        return self.__referencePoint

    @referencePoint.setter
    def referencePoint(self, value: float):
        """Set referencePoint"""
        self.__referencePoint = float(value)

    @property
    def limitTimeInterval(self) -> bool:
        """Specify time window to be applied for assessment of utilization. In case 'end time' exceeds the time series duration, the end of the time series will be used as the end time"""
        return self.__limitTimeInterval

    @limitTimeInterval.setter
    def limitTimeInterval(self, value: bool):
        """Set limitTimeInterval"""
        self.__limitTimeInterval = bool(value)

    @property
    def startTime(self) -> float:
        """"""
        return self.__startTime

    @startTime.setter
    def startTime(self, value: float):
        """Set startTime"""
        self.__startTime = float(value)

    @property
    def endTime(self) -> float:
        """"""
        return self.__endTime

    @endTime.setter
    def endTime(self, value: float):
        """Set endTime"""
        self.__endTime = float(value)

    @property
    def addIntermediateResults(self) -> bool:
        """Add intermediate element results to the output"""
        return self.__addIntermediateResults

    @addIntermediateResults.setter
    def addIntermediateResults(self, value: bool):
        """Set addIntermediateResults"""
        self.__addIntermediateResults = bool(value)

    @property
    def properties(self) -> List[CombinedLoadingProperties]:
        """Specification of nodes for displacement storage"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[CombinedLoadingProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def useDistributionFitting(self) -> bool:
        """Calculate characteristic extreme values of utilization factors using Gumbel distribution fitting"""
        return self.__useDistributionFitting

    @useDistributionFitting.setter
    def useDistributionFitting(self, value: bool):
        """Set useDistributionFitting"""
        self.__useDistributionFitting = bool(value)

    @property
    def seastateReturnPeriod(self) -> float:
        """Return period used for estimating the characteristic extreme value"""
        return self.__seastateReturnPeriod

    @seastateReturnPeriod.setter
    def seastateReturnPeriod(self, value: float):
        """Set seastateReturnPeriod"""
        self.__seastateReturnPeriod = float(value)

    @property
    def percentile(self) -> float:
        """Specify percentile in extreme value distribution. 
The value 0.57038 corresponds to the expected extreme, and 0.9 corresponds to 90% estimate of the extreme response"""
        return self.__percentile

    @percentile.setter
    def percentile(self, value: float):
        """Set percentile"""
        self.__percentile = float(value)

    @property
    def approach(self) -> CombinedLoadingApproach:
        """"""
        return self.__approach

    @approach.setter
    def approach(self, value: CombinedLoadingApproach):
        """Set approach"""
        self.__approach = value

    @property
    def customSafetyClassResistanceFactor(self) -> float:
        """Safety class resistance factor (ɣ SC)"""
        return self.__customSafetyClassResistanceFactor

    @customSafetyClassResistanceFactor.setter
    def customSafetyClassResistanceFactor(self, value: float):
        """Set customSafetyClassResistanceFactor"""
        self.__customSafetyClassResistanceFactor = float(value)

    @property
    def customLoadEffectFactorForEnvironmentalLoads(self) -> float:
        """Load effect factor for environmental loads (ɣ E)"""
        return self.__customLoadEffectFactorForEnvironmentalLoads

    @customLoadEffectFactorForEnvironmentalLoads.setter
    def customLoadEffectFactorForEnvironmentalLoads(self, value: float):
        """Set customLoadEffectFactorForEnvironmentalLoads"""
        self.__customLoadEffectFactorForEnvironmentalLoads = float(value)

    @property
    def customLoadEffectFactorForFunctionalLoads(self) -> float:
        """Load effect factor for functional loads (ɣ F)"""
        return self.__customLoadEffectFactorForFunctionalLoads

    @customLoadEffectFactorForFunctionalLoads.setter
    def customLoadEffectFactorForFunctionalLoads(self, value: float):
        """Set customLoadEffectFactorForFunctionalLoads"""
        self.__customLoadEffectFactorForFunctionalLoads = float(value)

    @property
    def customLoadFactorForAccidentalLoads(self) -> float:
        """Load factor for accidental loads (ɣ A)"""
        return self.__customLoadFactorForAccidentalLoads

    @customLoadFactorForAccidentalLoads.setter
    def customLoadFactorForAccidentalLoads(self, value: float):
        """Set customLoadFactorForAccidentalLoads"""
        self.__customLoadFactorForAccidentalLoads = float(value)

    @property
    def customMaterialResistanceFactor(self) -> float:
        """Material resistance factor (ɣ m)"""
        return self.__customMaterialResistanceFactor

    @customMaterialResistanceFactor.setter
    def customMaterialResistanceFactor(self, value: float):
        """Set customMaterialResistanceFactor"""
        self.__customMaterialResistanceFactor = float(value)

    @property
    def fabricationFactor(self) -> float:
        """Fabrication factor (α fab)"""
        return self.__fabricationFactor

    @fabricationFactor.setter
    def fabricationFactor(self, value: float):
        """Set fabricationFactor"""
        self.__fabricationFactor = float(value)

    @property
    def safetyClass(self) -> SafetyClass:
        """"""
        return self.__safetyClass

    @safetyClass.setter
    def safetyClass(self, value: SafetyClass):
        """Set safetyClass"""
        self.__safetyClass = value

    @property
    def limitStateCategory(self) -> LimitStateCategory:
        """"""
        return self.__limitStateCategory

    @limitStateCategory.setter
    def limitStateCategory(self, value: LimitStateCategory):
        """Set limitStateCategory"""
        self.__limitStateCategory = value

    @property
    def lastFunctionalLoadGroup(self) -> int:
        """Number of the last load group in static calculation parameter that is part of the functional load"""
        return self.__lastFunctionalLoadGroup

    @lastFunctionalLoadGroup.setter
    def lastFunctionalLoadGroup(self, value: int):
        """Set lastFunctionalLoadGroup"""
        self.__lastFunctionalLoadGroup = int(value)