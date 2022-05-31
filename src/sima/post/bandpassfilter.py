# This an autogenerated file
# 
# Generated with BandPassFilter
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.bandpassfilter import BandPassFilterBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.sima.scriptablevalue import ScriptableValue

class BandPassFilter(OperationNode):
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
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    filterInputSlots : List[InputSlot]
    filterOutputSlots : List[OutputSlot]
    renameOutput : bool
         (default True)
    taperingFactor : float
         Exponent in tapering of coefficient(default 0.5)
    coefficientCount : int
         Number of coefficients. If not set it will be set to round(k/(2*dt*fCut))(default 0)
    normalizedWindowDuration : int
         normalized window duration: k. Used to calculate default coefficientCount(default 4)
    lowerCutoffFrequency : float
         Lower cut off frequency(default 0.0)
    upperCutoffFrequency : float
         Upper cut off frequency(default 0.0)
    """

    def __init__(self , name="", description="", _id="", x=0, y=0, h=0, w=0, renameOutput=True, taperingFactor=0.5, coefficientCount=0, normalizedWindowDuration=4, lowerCutoffFrequency=0.0, upperCutoffFrequency=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.filterInputSlots = list()
        self.filterOutputSlots = list()
        self.renameOutput = renameOutput
        self.taperingFactor = taperingFactor
        self.coefficientCount = coefficientCount
        self.normalizedWindowDuration = normalizedWindowDuration
        self.lowerCutoffFrequency = lowerCutoffFrequency
        self.upperCutoffFrequency = upperCutoffFrequency
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return BandPassFilterBlueprint()


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
    def x(self) -> int:
        """"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """Set x"""
        self.__x = int(value)

    @property
    def y(self) -> int:
        """"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """Set y"""
        self.__y = int(value)

    @property
    def h(self) -> int:
        """"""
        return self.__h

    @h.setter
    def h(self, value: int):
        """Set h"""
        self.__h = int(value)

    @property
    def w(self) -> int:
        """"""
        return self.__w

    @w.setter
    def w(self, value: int):
        """Set w"""
        self.__w = int(value)

    @property
    def controlSignalInputSlots(self) -> List[ControlSignalInputSlot]:
        """"""
        return self.__controlSignalInputSlots

    @controlSignalInputSlots.setter
    def controlSignalInputSlots(self, value: List[ControlSignalInputSlot]):
        """Set controlSignalInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def filterInputSlots(self) -> List[InputSlot]:
        """"""
        return self.__filterInputSlots

    @filterInputSlots.setter
    def filterInputSlots(self, value: List[InputSlot]):
        """Set filterInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__filterInputSlots = value

    @property
    def filterOutputSlots(self) -> List[OutputSlot]:
        """"""
        return self.__filterOutputSlots

    @filterOutputSlots.setter
    def filterOutputSlots(self, value: List[OutputSlot]):
        """Set filterOutputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__filterOutputSlots = value

    @property
    def renameOutput(self) -> bool:
        """"""
        return self.__renameOutput

    @renameOutput.setter
    def renameOutput(self, value: bool):
        """Set renameOutput"""
        self.__renameOutput = bool(value)

    @property
    def taperingFactor(self) -> float:
        """Exponent in tapering of coefficient"""
        return self.__taperingFactor

    @taperingFactor.setter
    def taperingFactor(self, value: float):
        """Set taperingFactor"""
        self.__taperingFactor = float(value)

    @property
    def coefficientCount(self) -> int:
        """Number of coefficients. If not set it will be set to round(k/(2*dt*fCut))"""
        return self.__coefficientCount

    @coefficientCount.setter
    def coefficientCount(self, value: int):
        """Set coefficientCount"""
        self.__coefficientCount = int(value)

    @property
    def normalizedWindowDuration(self) -> int:
        """normalized window duration: k. Used to calculate default coefficientCount"""
        return self.__normalizedWindowDuration

    @normalizedWindowDuration.setter
    def normalizedWindowDuration(self, value: int):
        """Set normalizedWindowDuration"""
        self.__normalizedWindowDuration = int(value)

    @property
    def lowerCutoffFrequency(self) -> float:
        """Lower cut off frequency"""
        return self.__lowerCutoffFrequency

    @lowerCutoffFrequency.setter
    def lowerCutoffFrequency(self, value: float):
        """Set lowerCutoffFrequency"""
        self.__lowerCutoffFrequency = float(value)

    @property
    def upperCutoffFrequency(self) -> float:
        """Upper cut off frequency"""
        return self.__upperCutoffFrequency

    @upperCutoffFrequency.setter
    def upperCutoffFrequency(self, value: float):
        """Set upperCutoffFrequency"""
        self.__upperCutoffFrequency = float(value)
