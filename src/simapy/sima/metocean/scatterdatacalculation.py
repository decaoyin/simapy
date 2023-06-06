# This an autogenerated file
# 
# Generated with ScatterDataCalculation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scatterdatacalculation import ScatterDataCalculationBlueprint
from typing import Dict
from ..sima import ConditionSelectable
from ..sima import NamedObject
from ..sima import ScriptableValue
from .calculationdirection import CalculationDirection
from .calculationlevel import CalculationLevel
from .currentmodel import CurrentModel
from .inputreferencesystem import InputReferenceSystem
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .profile import Profile
    from .scatterdata import ScatterData

class ScatterDataCalculation(NamedObject,ConditionSelectable):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    currentModel : CurrentModel
    kfactor : float
         (default 1.0)
    directionRelativeToWind : float
         Direction relative to wind. Zero angle means collinear wind and current(default 0.0)
    windReferenceLevel : float
         The Level in wind data at which wind speed and direction will be used to define the current(default 0.0)
    windCurrentProfile : Profile
    baseCurrentSpeed : float
         (default 0.0)
    baseCurrentProfile : Profile
    currentLevels : List[CalculationLevel]
    relativeCompassAngle : float
         Relative angle between analysis x-axis and north direction in anti-clockwise direction.\nShould match the angle given in the recieving SIMA task location.(default 0.0)
    inputReferenceSystem : InputReferenceSystem
         Defines the input reference system of the data.\nIf the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated
    scatterData : ScatterData
    directions : List[CalculationDirection]
    windLevels : List[CalculationLevel]
    """

    def __init__(self , description="", currentModel=CurrentModel.FROM_INPUT, kfactor=1.0, directionRelativeToWind=0.0, windReferenceLevel=0.0, baseCurrentSpeed=0.0, relativeCompassAngle=0.0, inputReferenceSystem=InputReferenceSystem.METOCEAN, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.currentModel = currentModel
        self.kfactor = kfactor
        self.directionRelativeToWind = directionRelativeToWind
        self.windReferenceLevel = windReferenceLevel
        self.windCurrentProfile = None
        self.baseCurrentSpeed = baseCurrentSpeed
        self.baseCurrentProfile = None
        self.currentLevels = list()
        self.relativeCompassAngle = relativeCompassAngle
        self.inputReferenceSystem = inputReferenceSystem
        self.scatterData = None
        self.directions = list()
        self.windLevels = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScatterDataCalculationBlueprint()


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
    def currentModel(self) -> CurrentModel:
        """"""
        return self.__currentModel

    @currentModel.setter
    def currentModel(self, value: CurrentModel):
        """Set currentModel"""
        self.__currentModel = value

    @property
    def kfactor(self) -> float:
        """"""
        return self.__kfactor

    @kfactor.setter
    def kfactor(self, value: float):
        """Set kfactor"""
        self.__kfactor = float(value)

    @property
    def directionRelativeToWind(self) -> float:
        """Direction relative to wind. Zero angle means collinear wind and current"""
        return self.__directionRelativeToWind

    @directionRelativeToWind.setter
    def directionRelativeToWind(self, value: float):
        """Set directionRelativeToWind"""
        self.__directionRelativeToWind = float(value)

    @property
    def windReferenceLevel(self) -> float:
        """The Level in wind data at which wind speed and direction will be used to define the current"""
        return self.__windReferenceLevel

    @windReferenceLevel.setter
    def windReferenceLevel(self, value: float):
        """Set windReferenceLevel"""
        self.__windReferenceLevel = float(value)

    @property
    def windCurrentProfile(self) -> Profile:
        """"""
        return self.__windCurrentProfile

    @windCurrentProfile.setter
    def windCurrentProfile(self, value: Profile):
        """Set windCurrentProfile"""
        self.__windCurrentProfile = value

    @property
    def baseCurrentSpeed(self) -> float:
        """"""
        return self.__baseCurrentSpeed

    @baseCurrentSpeed.setter
    def baseCurrentSpeed(self, value: float):
        """Set baseCurrentSpeed"""
        self.__baseCurrentSpeed = float(value)

    @property
    def baseCurrentProfile(self) -> Profile:
        """"""
        return self.__baseCurrentProfile

    @baseCurrentProfile.setter
    def baseCurrentProfile(self, value: Profile):
        """Set baseCurrentProfile"""
        self.__baseCurrentProfile = value

    @property
    def currentLevels(self) -> List[CalculationLevel]:
        """"""
        return self.__currentLevels

    @currentLevels.setter
    def currentLevels(self, value: List[CalculationLevel]):
        """Set currentLevels"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__currentLevels = value

    @property
    def relativeCompassAngle(self) -> float:
        """Relative angle between analysis x-axis and north direction in anti-clockwise direction.
Should match the angle given in the recieving SIMA task location."""
        return self.__relativeCompassAngle

    @relativeCompassAngle.setter
    def relativeCompassAngle(self, value: float):
        """Set relativeCompassAngle"""
        self.__relativeCompassAngle = float(value)

    @property
    def inputReferenceSystem(self) -> InputReferenceSystem:
        """Defines the input reference system of the data.
If the data is defined in the Metocean system the corresponding SIMA coordinate system data is generated"""
        return self.__inputReferenceSystem

    @inputReferenceSystem.setter
    def inputReferenceSystem(self, value: InputReferenceSystem):
        """Set inputReferenceSystem"""
        self.__inputReferenceSystem = value

    @property
    def scatterData(self) -> ScatterData:
        """"""
        return self.__scatterData

    @scatterData.setter
    def scatterData(self, value: ScatterData):
        """Set scatterData"""
        self.__scatterData = value

    @property
    def directions(self) -> List[CalculationDirection]:
        """"""
        return self.__directions

    @directions.setter
    def directions(self, value: List[CalculationDirection]):
        """Set directions"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__directions = value

    @property
    def windLevels(self) -> List[CalculationLevel]:
        """"""
        return self.__windLevels

    @windLevels.setter
    def windLevels(self, value: List[CalculationLevel]):
        """Set windLevels"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__windLevels = value
