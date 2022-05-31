# This an autogenerated file
# 
# Generated with HindcastDataCalculation
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.hindcastdatacalculation import HindcastDataCalculationBlueprint
from typing import Dict
from sima.metocean.calculationlevel import CalculationLevel
from sima.metocean.currentmodel import CurrentModel
from sima.metocean.inputreferencesystem import InputReferenceSystem
from sima.sima.conditionselectable import ConditionSelectable
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.metocean.profile import Profile
    from sima.metocean.hindcastdata import HindcastData

class HindcastDataCalculation(NamedObject,ConditionSelectable):
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
    hindcastData : HindcastData
    from_ : str
         (default "")
    to : str
         (default "")
    windLevels : List[CalculationLevel]
    """

    def __init__(self , name="", description="", _id="", currentModel=CurrentModel.FROM_INPUT, kfactor=1.0, directionRelativeToWind=0.0, windReferenceLevel=0.0, baseCurrentSpeed=0.0, relativeCompassAngle=0.0, inputReferenceSystem=InputReferenceSystem.METOCEAN, from_="", to="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
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
        self.hindcastData = None
        self.from_ = from_
        self.to = to
        self.windLevels = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HindcastDataCalculationBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def hindcastData(self) -> HindcastData:
        """"""
        return self.__hindcastData

    @hindcastData.setter
    def hindcastData(self, value: HindcastData):
        """Set hindcastData"""
        self.__hindcastData = value

    @property
    def from_(self) -> str:
        """"""
        return self.__from_

    @from_.setter
    def from_(self, value: str):
        """Set from_"""
        self.__from_ = str(value)

    @property
    def to(self) -> str:
        """"""
        return self.__to

    @to.setter
    def to(self, value: str):
        """Set to"""
        self.__to = str(value)

    @property
    def windLevels(self) -> List[CalculationLevel]:
        """"""
        return self.__windLevels

    @windLevels.setter
    def windLevels(self, value: List[CalculationLevel]):
        """Set windLevels"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__windLevels = value
