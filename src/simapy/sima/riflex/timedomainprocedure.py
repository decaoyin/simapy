# This an autogenerated file
# 
# Generated with TimeDomainProcedure
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.timedomainprocedure import TimeDomainProcedureBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .methodindicator import MethodIndicator
from .nonlinearforcemodel import NonLinearForceModel
from .nonlinearintegrationprocedure import NonLinearIntegrationProcedure
from .procedureindicator import ProcedureIndicator
from .rayleighdamping import RayleighDamping

class TimeDomainProcedure(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    method : MethodIndicator
         Method indicator
    procedure : ProcedureIndicator
         Procedure indicator
    displacementStorage : bool
         Displacement storage indicator(default False)
    forceResultStorage : bool
         Force response storage indicator(default False)
    sumForceResponseStorage : bool
         Sum force response storage indicator(default False)
    curvatureResponseStorage : bool
         Curvature response storage indicator(default False)
    envelopeCurveSpecification : bool
         Envelope curve specification indicator(default False)
    inverseBeta : float
         Inverse value of the beta-parameter.(default 4.0)
    gamma : float
         Value of the parameter gamma of the Newmark operators (usually equal to 0.5)(default 0.5)
    theta : float
         Value of the parameter theta in Wilson`s integration method(default 1.0)
    dampingOption : RayleighDamping
         Stiffness proportional damping options
    globalMassDampingFactor : float
         Global mass proportional damping factor(default 0.0)
    globalStiffnessDampingFactor : float
         Global stiffness proportional damping factor(default 0.0)
    localMassTensionDamping : float
         Local mass proportional damping factor for tension(default 0.0)
    localMassTorsionDamping : float
         Local mass proportional damping factor for torsion(default 0.0)
    localMassBendingDamping : float
         Local mass proportional damping factor for bending(default 0.0)
    localStiffnessTensionDamping : float
         Local stiffness proportional damping factor for tension(default 0.0)
    localStiffnessTorsionDamping : float
         Local stiffness proportional damping factor for torsion(default 0.0)
    localStiffnessBendingDamping : float
         Local stiffness proportional damping factor for bending(default 0.0)
    nonLinearForceModel : NonLinearForceModel
    nonLinearIntegrationProcedure : NonLinearIntegrationProcedure
    """

    def __init__(self , description="", method=MethodIndicator.NONLINEAR, procedure=ProcedureIndicator.NEWMARK, displacementStorage=False, forceResultStorage=False, sumForceResponseStorage=False, curvatureResponseStorage=False, envelopeCurveSpecification=False, inverseBeta=4.0, gamma=0.5, theta=1.0, dampingOption=RayleighDamping.TOTAL, globalMassDampingFactor=0.0, globalStiffnessDampingFactor=0.0, localMassTensionDamping=0.0, localMassTorsionDamping=0.0, localMassBendingDamping=0.0, localStiffnessTensionDamping=0.0, localStiffnessTorsionDamping=0.0, localStiffnessBendingDamping=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.method = method
        self.procedure = procedure
        self.displacementStorage = displacementStorage
        self.forceResultStorage = forceResultStorage
        self.sumForceResponseStorage = sumForceResponseStorage
        self.curvatureResponseStorage = curvatureResponseStorage
        self.envelopeCurveSpecification = envelopeCurveSpecification
        self.inverseBeta = inverseBeta
        self.gamma = gamma
        self.theta = theta
        self.dampingOption = dampingOption
        self.globalMassDampingFactor = globalMassDampingFactor
        self.globalStiffnessDampingFactor = globalStiffnessDampingFactor
        self.localMassTensionDamping = localMassTensionDamping
        self.localMassTorsionDamping = localMassTorsionDamping
        self.localMassBendingDamping = localMassBendingDamping
        self.localStiffnessTensionDamping = localStiffnessTensionDamping
        self.localStiffnessTorsionDamping = localStiffnessTorsionDamping
        self.localStiffnessBendingDamping = localStiffnessBendingDamping
        self.nonLinearForceModel = None
        self.nonLinearIntegrationProcedure = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TimeDomainProcedureBlueprint()


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
    def method(self) -> MethodIndicator:
        """Method indicator"""
        return self.__method

    @method.setter
    def method(self, value: MethodIndicator):
        """Set method"""
        self.__method = value

    @property
    def procedure(self) -> ProcedureIndicator:
        """Procedure indicator"""
        return self.__procedure

    @procedure.setter
    def procedure(self, value: ProcedureIndicator):
        """Set procedure"""
        self.__procedure = value

    @property
    def displacementStorage(self) -> bool:
        """Displacement storage indicator"""
        return self.__displacementStorage

    @displacementStorage.setter
    def displacementStorage(self, value: bool):
        """Set displacementStorage"""
        self.__displacementStorage = bool(value)

    @property
    def forceResultStorage(self) -> bool:
        """Force response storage indicator"""
        return self.__forceResultStorage

    @forceResultStorage.setter
    def forceResultStorage(self, value: bool):
        """Set forceResultStorage"""
        self.__forceResultStorage = bool(value)

    @property
    def sumForceResponseStorage(self) -> bool:
        """Sum force response storage indicator"""
        return self.__sumForceResponseStorage

    @sumForceResponseStorage.setter
    def sumForceResponseStorage(self, value: bool):
        """Set sumForceResponseStorage"""
        self.__sumForceResponseStorage = bool(value)

    @property
    def curvatureResponseStorage(self) -> bool:
        """Curvature response storage indicator"""
        return self.__curvatureResponseStorage

    @curvatureResponseStorage.setter
    def curvatureResponseStorage(self, value: bool):
        """Set curvatureResponseStorage"""
        self.__curvatureResponseStorage = bool(value)

    @property
    def envelopeCurveSpecification(self) -> bool:
        """Envelope curve specification indicator"""
        return self.__envelopeCurveSpecification

    @envelopeCurveSpecification.setter
    def envelopeCurveSpecification(self, value: bool):
        """Set envelopeCurveSpecification"""
        self.__envelopeCurveSpecification = bool(value)

    @property
    def inverseBeta(self) -> float:
        """Inverse value of the beta-parameter."""
        return self.__inverseBeta

    @inverseBeta.setter
    def inverseBeta(self, value: float):
        """Set inverseBeta"""
        self.__inverseBeta = float(value)

    @property
    def gamma(self) -> float:
        """Value of the parameter gamma of the Newmark operators (usually equal to 0.5)"""
        return self.__gamma

    @gamma.setter
    def gamma(self, value: float):
        """Set gamma"""
        self.__gamma = float(value)

    @property
    def theta(self) -> float:
        """Value of the parameter theta in Wilson`s integration method"""
        return self.__theta

    @theta.setter
    def theta(self, value: float):
        """Set theta"""
        self.__theta = float(value)

    @property
    def dampingOption(self) -> RayleighDamping:
        """Stiffness proportional damping options"""
        return self.__dampingOption

    @dampingOption.setter
    def dampingOption(self, value: RayleighDamping):
        """Set dampingOption"""
        self.__dampingOption = value

    @property
    def globalMassDampingFactor(self) -> float:
        """Global mass proportional damping factor"""
        return self.__globalMassDampingFactor

    @globalMassDampingFactor.setter
    def globalMassDampingFactor(self, value: float):
        """Set globalMassDampingFactor"""
        self.__globalMassDampingFactor = float(value)

    @property
    def globalStiffnessDampingFactor(self) -> float:
        """Global stiffness proportional damping factor"""
        return self.__globalStiffnessDampingFactor

    @globalStiffnessDampingFactor.setter
    def globalStiffnessDampingFactor(self, value: float):
        """Set globalStiffnessDampingFactor"""
        self.__globalStiffnessDampingFactor = float(value)

    @property
    def localMassTensionDamping(self) -> float:
        """Local mass proportional damping factor for tension"""
        return self.__localMassTensionDamping

    @localMassTensionDamping.setter
    def localMassTensionDamping(self, value: float):
        """Set localMassTensionDamping"""
        self.__localMassTensionDamping = float(value)

    @property
    def localMassTorsionDamping(self) -> float:
        """Local mass proportional damping factor for torsion"""
        return self.__localMassTorsionDamping

    @localMassTorsionDamping.setter
    def localMassTorsionDamping(self, value: float):
        """Set localMassTorsionDamping"""
        self.__localMassTorsionDamping = float(value)

    @property
    def localMassBendingDamping(self) -> float:
        """Local mass proportional damping factor for bending"""
        return self.__localMassBendingDamping

    @localMassBendingDamping.setter
    def localMassBendingDamping(self, value: float):
        """Set localMassBendingDamping"""
        self.__localMassBendingDamping = float(value)

    @property
    def localStiffnessTensionDamping(self) -> float:
        """Local stiffness proportional damping factor for tension"""
        return self.__localStiffnessTensionDamping

    @localStiffnessTensionDamping.setter
    def localStiffnessTensionDamping(self, value: float):
        """Set localStiffnessTensionDamping"""
        self.__localStiffnessTensionDamping = float(value)

    @property
    def localStiffnessTorsionDamping(self) -> float:
        """Local stiffness proportional damping factor for torsion"""
        return self.__localStiffnessTorsionDamping

    @localStiffnessTorsionDamping.setter
    def localStiffnessTorsionDamping(self, value: float):
        """Set localStiffnessTorsionDamping"""
        self.__localStiffnessTorsionDamping = float(value)

    @property
    def localStiffnessBendingDamping(self) -> float:
        """Local stiffness proportional damping factor for bending"""
        return self.__localStiffnessBendingDamping

    @localStiffnessBendingDamping.setter
    def localStiffnessBendingDamping(self, value: float):
        """Set localStiffnessBendingDamping"""
        self.__localStiffnessBendingDamping = float(value)

    @property
    def nonLinearForceModel(self) -> NonLinearForceModel:
        """"""
        return self.__nonLinearForceModel

    @nonLinearForceModel.setter
    def nonLinearForceModel(self, value: NonLinearForceModel):
        """Set nonLinearForceModel"""
        self.__nonLinearForceModel = value

    @property
    def nonLinearIntegrationProcedure(self) -> NonLinearIntegrationProcedure:
        """"""
        return self.__nonLinearIntegrationProcedure

    @nonLinearIntegrationProcedure.setter
    def nonLinearIntegrationProcedure(self, value: NonLinearIntegrationProcedure):
        """Set nonLinearIntegrationProcedure"""
        self.__nonLinearIntegrationProcedure = value
