# This an autogenerated file
# 
# Generated with DynamicWindChange
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.dynamicwindchange import DynamicWindChangeBlueprint
from typing import Dict
from .iec2005windeventtype import IEC2005WindEventType
from .iec2005windturbineclass import IEC2005WindTurbineClass
from .winddirection import WindDirection
from sima.sima import MOAO
from sima.sima import ScriptableValue

class DynamicWindChange(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    include : bool
         (default False)
    eventType : IEC2005WindEventType
    eventStartTime : float
         Time for event to start(default 0.0)
    direction : WindDirection
    turbineClass : IEC2005WindTurbineClass
    vref : float
         Reference wind speed average over 10 minutes(default 0.0)
    iref : float
         Expected value of the turbulence intensity at 15 m/s(default 0.0)
    velocityChange : float
         (default 0.0)
    directionChange : float
         (default 0.0)
    durationOfEvent : float
         (default 0.0)
    gustMagnitude : float
         (default 0.0)
    """

    def __init__(self , description="", include=False, eventType=IEC2005WindEventType.ECD, eventStartTime=0.0, direction=WindDirection.POSITIVE, turbineClass=IEC2005WindTurbineClass.NONE, vref=0.0, iref=0.0, velocityChange=0.0, directionChange=0.0, durationOfEvent=0.0, gustMagnitude=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.include = include
        self.eventType = eventType
        self.eventStartTime = eventStartTime
        self.direction = direction
        self.turbineClass = turbineClass
        self.vref = vref
        self.iref = iref
        self.velocityChange = velocityChange
        self.directionChange = directionChange
        self.durationOfEvent = durationOfEvent
        self.gustMagnitude = gustMagnitude
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DynamicWindChangeBlueprint()


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
    def include(self) -> bool:
        """"""
        return self.__include

    @include.setter
    def include(self, value: bool):
        """Set include"""
        self.__include = bool(value)

    @property
    def eventType(self) -> IEC2005WindEventType:
        """"""
        return self.__eventType

    @eventType.setter
    def eventType(self, value: IEC2005WindEventType):
        """Set eventType"""
        self.__eventType = value

    @property
    def eventStartTime(self) -> float:
        """Time for event to start"""
        return self.__eventStartTime

    @eventStartTime.setter
    def eventStartTime(self, value: float):
        """Set eventStartTime"""
        self.__eventStartTime = float(value)

    @property
    def direction(self) -> WindDirection:
        """"""
        return self.__direction

    @direction.setter
    def direction(self, value: WindDirection):
        """Set direction"""
        self.__direction = value

    @property
    def turbineClass(self) -> IEC2005WindTurbineClass:
        """"""
        return self.__turbineClass

    @turbineClass.setter
    def turbineClass(self, value: IEC2005WindTurbineClass):
        """Set turbineClass"""
        self.__turbineClass = value

    @property
    def vref(self) -> float:
        """Reference wind speed average over 10 minutes"""
        return self.__vref

    @vref.setter
    def vref(self, value: float):
        """Set vref"""
        self.__vref = float(value)

    @property
    def iref(self) -> float:
        """Expected value of the turbulence intensity at 15 m/s"""
        return self.__iref

    @iref.setter
    def iref(self, value: float):
        """Set iref"""
        self.__iref = float(value)

    @property
    def velocityChange(self) -> float:
        """"""
        return self.__velocityChange

    @velocityChange.setter
    def velocityChange(self, value: float):
        """Set velocityChange"""
        self.__velocityChange = float(value)

    @property
    def directionChange(self) -> float:
        """"""
        return self.__directionChange

    @directionChange.setter
    def directionChange(self, value: float):
        """Set directionChange"""
        self.__directionChange = float(value)

    @property
    def durationOfEvent(self) -> float:
        """"""
        return self.__durationOfEvent

    @durationOfEvent.setter
    def durationOfEvent(self, value: float):
        """Set durationOfEvent"""
        self.__durationOfEvent = float(value)

    @property
    def gustMagnitude(self) -> float:
        """"""
        return self.__gustMagnitude

    @gustMagnitude.setter
    def gustMagnitude(self, value: float):
        """Set gustMagnitude"""
        self.__gustMagnitude = float(value)
