# This an autogenerated file
# 
# Generated with ScaleFilter
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.scalefilter import ScaleFilterBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.post.signalaxis import SignalAxis
from sima.sima.scriptablevalue import ScriptableValue

class ScaleFilter(OperationNode):
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
    renameOutput : bool
         (default True)
    scale : float
         scale input series with given factor(default 1.0)
    unit : str
         unit of scale parameter(default '-')
    axis : SignalAxis
         Select the value from the x-axis or the y-axis
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, renameOutput=True, scale=1.0, unit='-', axis=SignalAxis.Y, **kwargs):
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
        self.renameOutput = renameOutput
        self.scale = scale
        self.unit = unit
        self.axis = axis
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ScaleFilterBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
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
    def scale(self) -> float:
        """scale input series with given factor"""
        return self.__scale

    @scale.setter
    def scale(self, value: float):
        """Set scale"""
        self.__scale = float(value)

    @property
    def unit(self) -> str:
        """unit of scale parameter"""
        return self.__unit

    @unit.setter
    def unit(self, value: str):
        """Set unit"""
        self.__unit = value

    @property
    def axis(self) -> SignalAxis:
        """Select the value from the x-axis or the y-axis"""
        return self.__axis

    @axis.setter
    def axis(self, value: SignalAxis):
        """Set axis"""
        self.__axis = value
