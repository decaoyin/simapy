# This an autogenerated file
# 
# Generated with NonLinearForceModel
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.nonlinearforcemodel import NonLinearForceModelBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .dampingmatrixcalculationoption import DampingMatrixCalculationOption
from .hydrodynamicforceindicator import HydrodynamicForceIndicator
from .slugforcespecification import SlugForceSpecification

class NonLinearForceModel(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    internalSlugFlow : bool
         Indicator for modelling forces from internal slug flow(default False)
    hydrodynamicForce : HydrodynamicForceIndicator
         Indicator for hydrodynamic force model
    maxHit : int
         Maximum number of load iterations (linear analysis). A negative value gives print of convergence for each step.(default 5)
    forceIterationConvergence : float
         Convergence control parameter for force iteration(default 0.01)
    startUpDuration : float
         Duration of start-up procedure(default 10.0)
    ruptureRelease : bool
         Indicator for rupture / release(default False)
    connectorNumber : int
         Global ball-joint connector ID in the RIFLEX FEM model(default 0)
    timeStepNumForRelease : int
         Time step number for release (nonlinear analysis only). In linear analysis the connector will be released at the first step.(default 0)
    dampingMatrixCalculation : DampingMatrixCalculationOption
         Option for calculation of proportional damping matrix in nonlinear analysis. Irrelevant for linear analysis.
    slugForceSpecification : SlugForceSpecification
    """

    def __init__(self , description="", internalSlugFlow=False, hydrodynamicForce=HydrodynamicForceIndicator.NO_FORCE_ITERATION_VELOCITIES, maxHit=5, forceIterationConvergence=0.01, startUpDuration=10.0, ruptureRelease=False, connectorNumber=0, timeStepNumForRelease=0, dampingMatrixCalculation=DampingMatrixCalculationOption.CONSTANT_PROPORTIONAL, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.internalSlugFlow = internalSlugFlow
        self.hydrodynamicForce = hydrodynamicForce
        self.maxHit = maxHit
        self.forceIterationConvergence = forceIterationConvergence
        self.startUpDuration = startUpDuration
        self.ruptureRelease = ruptureRelease
        self.connectorNumber = connectorNumber
        self.timeStepNumForRelease = timeStepNumForRelease
        self.dampingMatrixCalculation = dampingMatrixCalculation
        self.slugForceSpecification = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return NonLinearForceModelBlueprint()


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
    def internalSlugFlow(self) -> bool:
        """Indicator for modelling forces from internal slug flow"""
        return self.__internalSlugFlow

    @internalSlugFlow.setter
    def internalSlugFlow(self, value: bool):
        """Set internalSlugFlow"""
        self.__internalSlugFlow = bool(value)

    @property
    def hydrodynamicForce(self) -> HydrodynamicForceIndicator:
        """Indicator for hydrodynamic force model"""
        return self.__hydrodynamicForce

    @hydrodynamicForce.setter
    def hydrodynamicForce(self, value: HydrodynamicForceIndicator):
        """Set hydrodynamicForce"""
        self.__hydrodynamicForce = value

    @property
    def maxHit(self) -> int:
        """Maximum number of load iterations (linear analysis). A negative value gives print of convergence for each step."""
        return self.__maxHit

    @maxHit.setter
    def maxHit(self, value: int):
        """Set maxHit"""
        self.__maxHit = int(value)

    @property
    def forceIterationConvergence(self) -> float:
        """Convergence control parameter for force iteration"""
        return self.__forceIterationConvergence

    @forceIterationConvergence.setter
    def forceIterationConvergence(self, value: float):
        """Set forceIterationConvergence"""
        self.__forceIterationConvergence = float(value)

    @property
    def startUpDuration(self) -> float:
        """Duration of start-up procedure"""
        return self.__startUpDuration

    @startUpDuration.setter
    def startUpDuration(self, value: float):
        """Set startUpDuration"""
        self.__startUpDuration = float(value)

    @property
    def ruptureRelease(self) -> bool:
        """Indicator for rupture / release"""
        return self.__ruptureRelease

    @ruptureRelease.setter
    def ruptureRelease(self, value: bool):
        """Set ruptureRelease"""
        self.__ruptureRelease = bool(value)

    @property
    def connectorNumber(self) -> int:
        """Global ball-joint connector ID in the RIFLEX FEM model"""
        return self.__connectorNumber

    @connectorNumber.setter
    def connectorNumber(self, value: int):
        """Set connectorNumber"""
        self.__connectorNumber = int(value)

    @property
    def timeStepNumForRelease(self) -> int:
        """Time step number for release (nonlinear analysis only). In linear analysis the connector will be released at the first step."""
        return self.__timeStepNumForRelease

    @timeStepNumForRelease.setter
    def timeStepNumForRelease(self, value: int):
        """Set timeStepNumForRelease"""
        self.__timeStepNumForRelease = int(value)

    @property
    def dampingMatrixCalculation(self) -> DampingMatrixCalculationOption:
        """Option for calculation of proportional damping matrix in nonlinear analysis. Irrelevant for linear analysis."""
        return self.__dampingMatrixCalculation

    @dampingMatrixCalculation.setter
    def dampingMatrixCalculation(self, value: DampingMatrixCalculationOption):
        """Set dampingMatrixCalculation"""
        self.__dampingMatrixCalculation = value

    @property
    def slugForceSpecification(self) -> SlugForceSpecification:
        """"""
        return self.__slugForceSpecification

    @slugForceSpecification.setter
    def slugForceSpecification(self, value: SlugForceSpecification):
        """Set slugForceSpecification"""
        self.__slugForceSpecification = value