# This an autogenerated file
# 
# Generated with FluctuatingWindVelocityProfile
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.fluctuatingwindvelocityprofile import FluctuatingWindVelocityProfileBlueprint
from typing import Dict
from sima.environment.windvelocityprofile import WindVelocityProfile
from sima.sima.scriptablevalue import ScriptableValue

class FluctuatingWindVelocityProfile(WindVelocityProfile):
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
    verticalCoordinate : float
         Vertical coordinate of profile level(default 0.0)
    longitudinalVelocityFactor : float
         Wind speed scaling factor for fluctuating part of the longitudinal wind(default 0.0)
    lateralVelocityFactor : float
         Wind speed scaling factor for the lateral wind velocity(default 0.0)
    verticalVelocityFactor : float
         Wind speed scaling factor for the vertical wind velocity(default 0.0)
    meanSpeedFactor : float
         Wind speed scaling factor for the mean wind speed(default 0.0)
    """

    def __init__(self , name="", description="", _id="", verticalCoordinate=0.0, longitudinalVelocityFactor=0.0, lateralVelocityFactor=0.0, verticalVelocityFactor=0.0, meanSpeedFactor=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.verticalCoordinate = verticalCoordinate
        self.longitudinalVelocityFactor = longitudinalVelocityFactor
        self.lateralVelocityFactor = lateralVelocityFactor
        self.verticalVelocityFactor = verticalVelocityFactor
        self.meanSpeedFactor = meanSpeedFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FluctuatingWindVelocityProfileBlueprint()


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
    def verticalCoordinate(self) -> float:
        """Vertical coordinate of profile level"""
        return self.__verticalCoordinate

    @verticalCoordinate.setter
    def verticalCoordinate(self, value: float):
        """Set verticalCoordinate"""
        self.__verticalCoordinate = float(value)

    @property
    def longitudinalVelocityFactor(self) -> float:
        """Wind speed scaling factor for fluctuating part of the longitudinal wind"""
        return self.__longitudinalVelocityFactor

    @longitudinalVelocityFactor.setter
    def longitudinalVelocityFactor(self, value: float):
        """Set longitudinalVelocityFactor"""
        self.__longitudinalVelocityFactor = float(value)

    @property
    def lateralVelocityFactor(self) -> float:
        """Wind speed scaling factor for the lateral wind velocity"""
        return self.__lateralVelocityFactor

    @lateralVelocityFactor.setter
    def lateralVelocityFactor(self, value: float):
        """Set lateralVelocityFactor"""
        self.__lateralVelocityFactor = float(value)

    @property
    def verticalVelocityFactor(self) -> float:
        """Wind speed scaling factor for the vertical wind velocity"""
        return self.__verticalVelocityFactor

    @verticalVelocityFactor.setter
    def verticalVelocityFactor(self, value: float):
        """Set verticalVelocityFactor"""
        self.__verticalVelocityFactor = float(value)

    @property
    def meanSpeedFactor(self) -> float:
        """Wind speed scaling factor for the mean wind speed"""
        return self.__meanSpeedFactor

    @meanSpeedFactor.setter
    def meanSpeedFactor(self, value: float):
        """Set meanSpeedFactor"""
        self.__meanSpeedFactor = float(value)
