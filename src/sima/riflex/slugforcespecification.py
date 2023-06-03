# This an autogenerated file
# 
# Generated with SlugForceSpecification
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.slugforcespecification import SlugForceSpecificationBlueprint
from typing import Dict
from .slugforcedensitycontrol import SlugForceDensityControl
from .slugforceinterruption import SlugForceInterruption
from .slugforcevelocitycontrol import SlugForceVelocityControl
from sima.sima import MOAO
from sima.sima import ScriptableValue

class SlugForceSpecification(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    enterTime : float
         Time when slug enters first end of main riser line(default 0.0)
    interruption : SlugForceInterruption
         Interruption parameter
    length : float
         Initial slug length(default 0.0)
    mass : float
         Slug mass(default 0.0)
    velocity : float
         Initial slug velocity(default 0.0)
    densityControl : SlugForceDensityControl
         Control parameter density
    velocityControl : SlugForceVelocityControl
         Control parameter velocity
    cycles : int
         Number of slug cycles(default 1)
    cycleTime : float
         Slug cycle time(default 0.0)
    secondPosition : float
         Second vertical position for the slug unit mass(default 0.0)
    massAtSecondPosition : float
         Slug unit mass at second vertical position(default 0.0)
    referenceDepth : float
         Reference depth(default 0.0)
    velocitySpecification : float
         Velocity specification(default 0.0)
    velocityExponent : float
         Exponent for velocity(default 0.0)
    importFlow : bool
         Import internal flow data from file(default False)
    flowFile : str
         Internal flow data specification(default None)
    addedFlow : bool
         Specified flow is in addition to that given on main riser line (default is replacement)(default False)
    """

    def __init__(self , description="", enterTime=0.0, interruption=SlugForceInterruption.SLUG, length=0.0, mass=0.0, velocity=0.0, densityControl=SlugForceDensityControl.CONSTANT, velocityControl=SlugForceVelocityControl.CONSTANT, cycles=1, cycleTime=0.0, secondPosition=0.0, massAtSecondPosition=0.0, referenceDepth=0.0, velocitySpecification=0.0, velocityExponent=0.0, importFlow=False, addedFlow=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.enterTime = enterTime
        self.interruption = interruption
        self.length = length
        self.mass = mass
        self.velocity = velocity
        self.densityControl = densityControl
        self.velocityControl = velocityControl
        self.cycles = cycles
        self.cycleTime = cycleTime
        self.secondPosition = secondPosition
        self.massAtSecondPosition = massAtSecondPosition
        self.referenceDepth = referenceDepth
        self.velocitySpecification = velocitySpecification
        self.velocityExponent = velocityExponent
        self.importFlow = importFlow
        self.flowFile = None
        self.addedFlow = addedFlow
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SlugForceSpecificationBlueprint()


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
    def enterTime(self) -> float:
        """Time when slug enters first end of main riser line"""
        return self.__enterTime

    @enterTime.setter
    def enterTime(self, value: float):
        """Set enterTime"""
        self.__enterTime = float(value)

    @property
    def interruption(self) -> SlugForceInterruption:
        """Interruption parameter"""
        return self.__interruption

    @interruption.setter
    def interruption(self, value: SlugForceInterruption):
        """Set interruption"""
        self.__interruption = value

    @property
    def length(self) -> float:
        """Initial slug length"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def mass(self) -> float:
        """Slug mass"""
        return self.__mass

    @mass.setter
    def mass(self, value: float):
        """Set mass"""
        self.__mass = float(value)

    @property
    def velocity(self) -> float:
        """Initial slug velocity"""
        return self.__velocity

    @velocity.setter
    def velocity(self, value: float):
        """Set velocity"""
        self.__velocity = float(value)

    @property
    def densityControl(self) -> SlugForceDensityControl:
        """Control parameter density"""
        return self.__densityControl

    @densityControl.setter
    def densityControl(self, value: SlugForceDensityControl):
        """Set densityControl"""
        self.__densityControl = value

    @property
    def velocityControl(self) -> SlugForceVelocityControl:
        """Control parameter velocity"""
        return self.__velocityControl

    @velocityControl.setter
    def velocityControl(self, value: SlugForceVelocityControl):
        """Set velocityControl"""
        self.__velocityControl = value

    @property
    def cycles(self) -> int:
        """Number of slug cycles"""
        return self.__cycles

    @cycles.setter
    def cycles(self, value: int):
        """Set cycles"""
        self.__cycles = int(value)

    @property
    def cycleTime(self) -> float:
        """Slug cycle time"""
        return self.__cycleTime

    @cycleTime.setter
    def cycleTime(self, value: float):
        """Set cycleTime"""
        self.__cycleTime = float(value)

    @property
    def secondPosition(self) -> float:
        """Second vertical position for the slug unit mass"""
        return self.__secondPosition

    @secondPosition.setter
    def secondPosition(self, value: float):
        """Set secondPosition"""
        self.__secondPosition = float(value)

    @property
    def massAtSecondPosition(self) -> float:
        """Slug unit mass at second vertical position"""
        return self.__massAtSecondPosition

    @massAtSecondPosition.setter
    def massAtSecondPosition(self, value: float):
        """Set massAtSecondPosition"""
        self.__massAtSecondPosition = float(value)

    @property
    def referenceDepth(self) -> float:
        """Reference depth"""
        return self.__referenceDepth

    @referenceDepth.setter
    def referenceDepth(self, value: float):
        """Set referenceDepth"""
        self.__referenceDepth = float(value)

    @property
    def velocitySpecification(self) -> float:
        """Velocity specification"""
        return self.__velocitySpecification

    @velocitySpecification.setter
    def velocitySpecification(self, value: float):
        """Set velocitySpecification"""
        self.__velocitySpecification = float(value)

    @property
    def velocityExponent(self) -> float:
        """Exponent for velocity"""
        return self.__velocityExponent

    @velocityExponent.setter
    def velocityExponent(self, value: float):
        """Set velocityExponent"""
        self.__velocityExponent = float(value)

    @property
    def importFlow(self) -> bool:
        """Import internal flow data from file"""
        return self.__importFlow

    @importFlow.setter
    def importFlow(self, value: bool):
        """Set importFlow"""
        self.__importFlow = bool(value)

    @property
    def flowFile(self) -> str:
        """Internal flow data specification"""
        return self.__flowFile

    @flowFile.setter
    def flowFile(self, value: str):
        """Set flowFile"""
        self.__flowFile = value

    @property
    def addedFlow(self) -> bool:
        """Specified flow is in addition to that given on main riser line (default is replacement)"""
        return self.__addedFlow

    @addedFlow.setter
    def addedFlow(self, value: bool):
        """Set addedFlow"""
        self.__addedFlow = bool(value)
