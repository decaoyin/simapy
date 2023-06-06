# This an autogenerated file
# 
# Generated with SIMOModel
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simomodel import SIMOModelBlueprint
from typing import Dict
from ..environment import Environment
from ..environment import EnvironmentsContainer
from ..sima import ScriptableValue
from ..windturbine import Airfoil
from .advancedbumper import AdvancedBumper
from .bumpergroup import BumperGroup
from .dockingcone import DockingCone
from .fibreropemodel import FibreRopeModel
from .fixedelongationcoupling import FixedElongationCoupling
from .hydrodynamiccoupling import HydrodynamicCoupling
from .liftlinecoupling import LiftLineCoupling
from .momentcoupling import MomentCoupling
from .multiplewirecoupling import MultipleWireCoupling
from .pointfender import PointFender
from .ratchetcoupling import RatchetCoupling
from .rollerfender import RollerFender
from .simobody import SIMOBody
from .simodynamiccalculationparameters import SIMODynamicCalculationParameters
from .simofrequencydomaincalculation import SIMOFrequencyDomainCalculation
from .simolocation import SIMOLocation
from .simostaticcalculationparameters import SIMOStaticCalculationParameters
from .simplewirecoupling import SimpleWireCoupling
from .stabilitycalculationparameters import StabilityCalculationParameters

class SIMOModel(EnvironmentsContainer):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    environments : List[Environment]
    airfoils : List[Airfoil]
    location : SIMOLocation
    bodies : List[SIMOBody]
    hydrodynamicCouplings : List[HydrodynamicCoupling]
    simpleWireCouplings : List[SimpleWireCoupling]
    fixedElongationCouplings : List[FixedElongationCoupling]
    dockingCones : List[DockingCone]
    pointFenders : List[PointFender]
    rollerFenders : List[RollerFender]
    ratchets : List[RatchetCoupling]
    multipleWireCouplings : List[MultipleWireCoupling]
    bumperGroups : List[BumperGroup]
    advancedBumpers : List[AdvancedBumper]
    liftLineCouplings : List[LiftLineCoupling]
    momentCouplings : List[MomentCoupling]
    sIMOStaticCalculationParameters : SIMOStaticCalculationParameters
    sIMODynamicCalculationParameters : SIMODynamicCalculationParameters
    stabilityCalculationParameters : StabilityCalculationParameters
    simoFrequencyDomainCalculation : SIMOFrequencyDomainCalculation
    fibreRopeModels : List[FibreRopeModel]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.environments = list()
        self.airfoils = list()
        self.location = None
        self.bodies = list()
        self.hydrodynamicCouplings = list()
        self.simpleWireCouplings = list()
        self.fixedElongationCouplings = list()
        self.dockingCones = list()
        self.pointFenders = list()
        self.rollerFenders = list()
        self.ratchets = list()
        self.multipleWireCouplings = list()
        self.bumperGroups = list()
        self.advancedBumpers = list()
        self.liftLineCouplings = list()
        self.momentCouplings = list()
        self.sIMOStaticCalculationParameters = None
        self.sIMODynamicCalculationParameters = None
        self.stabilityCalculationParameters = None
        self.simoFrequencyDomainCalculation = None
        self.fibreRopeModels = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMOModelBlueprint()


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
    def environments(self) -> List[Environment]:
        """"""
        return self.__environments

    @environments.setter
    def environments(self, value: List[Environment]):
        """Set environments"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__environments = value

    @property
    def airfoils(self) -> List[Airfoil]:
        """"""
        return self.__airfoils

    @airfoils.setter
    def airfoils(self, value: List[Airfoil]):
        """Set airfoils"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__airfoils = value

    @property
    def location(self) -> SIMOLocation:
        """"""
        return self.__location

    @location.setter
    def location(self, value: SIMOLocation):
        """Set location"""
        self.__location = value

    @property
    def bodies(self) -> List[SIMOBody]:
        """"""
        return self.__bodies

    @bodies.setter
    def bodies(self, value: List[SIMOBody]):
        """Set bodies"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__bodies = value

    @property
    def hydrodynamicCouplings(self) -> List[HydrodynamicCoupling]:
        """"""
        return self.__hydrodynamicCouplings

    @hydrodynamicCouplings.setter
    def hydrodynamicCouplings(self, value: List[HydrodynamicCoupling]):
        """Set hydrodynamicCouplings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__hydrodynamicCouplings = value

    @property
    def simpleWireCouplings(self) -> List[SimpleWireCoupling]:
        """"""
        return self.__simpleWireCouplings

    @simpleWireCouplings.setter
    def simpleWireCouplings(self, value: List[SimpleWireCoupling]):
        """Set simpleWireCouplings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__simpleWireCouplings = value

    @property
    def fixedElongationCouplings(self) -> List[FixedElongationCoupling]:
        """"""
        return self.__fixedElongationCouplings

    @fixedElongationCouplings.setter
    def fixedElongationCouplings(self, value: List[FixedElongationCoupling]):
        """Set fixedElongationCouplings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__fixedElongationCouplings = value

    @property
    def dockingCones(self) -> List[DockingCone]:
        """"""
        return self.__dockingCones

    @dockingCones.setter
    def dockingCones(self, value: List[DockingCone]):
        """Set dockingCones"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__dockingCones = value

    @property
    def pointFenders(self) -> List[PointFender]:
        """"""
        return self.__pointFenders

    @pointFenders.setter
    def pointFenders(self, value: List[PointFender]):
        """Set pointFenders"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__pointFenders = value

    @property
    def rollerFenders(self) -> List[RollerFender]:
        """"""
        return self.__rollerFenders

    @rollerFenders.setter
    def rollerFenders(self, value: List[RollerFender]):
        """Set rollerFenders"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__rollerFenders = value

    @property
    def ratchets(self) -> List[RatchetCoupling]:
        """"""
        return self.__ratchets

    @ratchets.setter
    def ratchets(self, value: List[RatchetCoupling]):
        """Set ratchets"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__ratchets = value

    @property
    def multipleWireCouplings(self) -> List[MultipleWireCoupling]:
        """"""
        return self.__multipleWireCouplings

    @multipleWireCouplings.setter
    def multipleWireCouplings(self, value: List[MultipleWireCoupling]):
        """Set multipleWireCouplings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__multipleWireCouplings = value

    @property
    def bumperGroups(self) -> List[BumperGroup]:
        """"""
        return self.__bumperGroups

    @bumperGroups.setter
    def bumperGroups(self, value: List[BumperGroup]):
        """Set bumperGroups"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__bumperGroups = value

    @property
    def advancedBumpers(self) -> List[AdvancedBumper]:
        """"""
        return self.__advancedBumpers

    @advancedBumpers.setter
    def advancedBumpers(self, value: List[AdvancedBumper]):
        """Set advancedBumpers"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__advancedBumpers = value

    @property
    def liftLineCouplings(self) -> List[LiftLineCoupling]:
        """"""
        return self.__liftLineCouplings

    @liftLineCouplings.setter
    def liftLineCouplings(self, value: List[LiftLineCoupling]):
        """Set liftLineCouplings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__liftLineCouplings = value

    @property
    def momentCouplings(self) -> List[MomentCoupling]:
        """"""
        return self.__momentCouplings

    @momentCouplings.setter
    def momentCouplings(self, value: List[MomentCoupling]):
        """Set momentCouplings"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__momentCouplings = value

    @property
    def sIMOStaticCalculationParameters(self) -> SIMOStaticCalculationParameters:
        """"""
        return self.__sIMOStaticCalculationParameters

    @sIMOStaticCalculationParameters.setter
    def sIMOStaticCalculationParameters(self, value: SIMOStaticCalculationParameters):
        """Set sIMOStaticCalculationParameters"""
        self.__sIMOStaticCalculationParameters = value

    @property
    def sIMODynamicCalculationParameters(self) -> SIMODynamicCalculationParameters:
        """"""
        return self.__sIMODynamicCalculationParameters

    @sIMODynamicCalculationParameters.setter
    def sIMODynamicCalculationParameters(self, value: SIMODynamicCalculationParameters):
        """Set sIMODynamicCalculationParameters"""
        self.__sIMODynamicCalculationParameters = value

    @property
    def stabilityCalculationParameters(self) -> StabilityCalculationParameters:
        """"""
        return self.__stabilityCalculationParameters

    @stabilityCalculationParameters.setter
    def stabilityCalculationParameters(self, value: StabilityCalculationParameters):
        """Set stabilityCalculationParameters"""
        self.__stabilityCalculationParameters = value

    @property
    def simoFrequencyDomainCalculation(self) -> SIMOFrequencyDomainCalculation:
        """"""
        return self.__simoFrequencyDomainCalculation

    @simoFrequencyDomainCalculation.setter
    def simoFrequencyDomainCalculation(self, value: SIMOFrequencyDomainCalculation):
        """Set simoFrequencyDomainCalculation"""
        self.__simoFrequencyDomainCalculation = value

    @property
    def fibreRopeModels(self) -> List[FibreRopeModel]:
        """"""
        return self.__fibreRopeModels

    @fibreRopeModels.setter
    def fibreRopeModels(self, value: List[FibreRopeModel]):
        """Set fibreRopeModels"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__fibreRopeModels = value
