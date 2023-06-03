# This an autogenerated file
# 
# Generated with AutoSpectrumFilter
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.autospectrumfilter import AutoSpectrumFilterBlueprint
from typing import Dict
from .controlsignalinputslot import ControlSignalInputSlot
from .inputslot import InputSlot
from .operationnode import OperationNode
from .outputslot import OutputSlot
from sima.sima import ScriptableValue

class AutoSpectrumFilter(OperationNode):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
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
    subtractMean : bool
         Subtract mean value from input(default False)
    smoothingParameter : int
         Smoothing parameter(default 3)
    fadedOverlap : bool
         Faded overlap coefficient(default False)
    numPointsFFT : int
         Number of points to be used in fft (default is all input points)(default 0)
    taperWindowLength : float
         Relative length of cosine taper window(default 0.1)
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, subtractMean=False, smoothingParameter=3, fadedOverlap=False, numPointsFFT=0, taperWindowLength=0.1, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.filterInputSlots = list()
        self.filterOutputSlots = list()
        self.subtractMean = subtractMean
        self.smoothingParameter = smoothingParameter
        self.fadedOverlap = fadedOverlap
        self.numPointsFFT = numPointsFFT
        self.taperWindowLength = taperWindowLength
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return AutoSpectrumFilterBlueprint()


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
            raise ValueError("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def filterInputSlots(self) -> List[InputSlot]:
        """"""
        return self.__filterInputSlots

    @filterInputSlots.setter
    def filterInputSlots(self, value: List[InputSlot]):
        """Set filterInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__filterInputSlots = value

    @property
    def filterOutputSlots(self) -> List[OutputSlot]:
        """"""
        return self.__filterOutputSlots

    @filterOutputSlots.setter
    def filterOutputSlots(self, value: List[OutputSlot]):
        """Set filterOutputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__filterOutputSlots = value

    @property
    def subtractMean(self) -> bool:
        """Subtract mean value from input"""
        return self.__subtractMean

    @subtractMean.setter
    def subtractMean(self, value: bool):
        """Set subtractMean"""
        self.__subtractMean = bool(value)

    @property
    def smoothingParameter(self) -> int:
        """Smoothing parameter"""
        return self.__smoothingParameter

    @smoothingParameter.setter
    def smoothingParameter(self, value: int):
        """Set smoothingParameter"""
        self.__smoothingParameter = int(value)

    @property
    def fadedOverlap(self) -> bool:
        """Faded overlap coefficient"""
        return self.__fadedOverlap

    @fadedOverlap.setter
    def fadedOverlap(self, value: bool):
        """Set fadedOverlap"""
        self.__fadedOverlap = bool(value)

    @property
    def numPointsFFT(self) -> int:
        """Number of points to be used in fft (default is all input points)"""
        return self.__numPointsFFT

    @numPointsFFT.setter
    def numPointsFFT(self, value: int):
        """Set numPointsFFT"""
        self.__numPointsFFT = int(value)

    @property
    def taperWindowLength(self) -> float:
        """Relative length of cosine taper window"""
        return self.__taperWindowLength

    @taperWindowLength.setter
    def taperWindowLength(self, value: float):
        """Set taperWindowLength"""
        self.__taperWindowLength = float(value)
