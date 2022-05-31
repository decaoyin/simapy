# This an autogenerated file
# 
# Generated with ISO13628_7Filter
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.iso13628_7filter import ISO13628_7FilterBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.sima.scriptablevalue import ScriptableValue

class ISO13628_7Filter(OperationNode):
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
    ultimateTensionCapacity : float
         Single load ultimate tension capacity(default 0.0)
    ultimateBendingCapacity : float
         Single load ultimate bending capacity(default 0.0)
    ultimatePressureCapacity : float
         Single load ultimate pressure capacity due to end cap effect(default 0.0)
    internalPressure : float
         Internal pressure(default 0.0)
    externalPressure : float
         External pressure(default 0.0)
    designFactor : float
         Design factor(default 0.8)
    """

    def __init__(self , name="", description="", _id="", x=0, y=0, h=0, w=0, ultimateTensionCapacity=0.0, ultimateBendingCapacity=0.0, ultimatePressureCapacity=0.0, internalPressure=0.0, externalPressure=0.0, designFactor=0.8, **kwargs):
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
        self.ultimateTensionCapacity = ultimateTensionCapacity
        self.ultimateBendingCapacity = ultimateBendingCapacity
        self.ultimatePressureCapacity = ultimatePressureCapacity
        self.internalPressure = internalPressure
        self.externalPressure = externalPressure
        self.designFactor = designFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ISO13628_7FilterBlueprint()


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
    def ultimateTensionCapacity(self) -> float:
        """Single load ultimate tension capacity"""
        return self.__ultimateTensionCapacity

    @ultimateTensionCapacity.setter
    def ultimateTensionCapacity(self, value: float):
        """Set ultimateTensionCapacity"""
        self.__ultimateTensionCapacity = float(value)

    @property
    def ultimateBendingCapacity(self) -> float:
        """Single load ultimate bending capacity"""
        return self.__ultimateBendingCapacity

    @ultimateBendingCapacity.setter
    def ultimateBendingCapacity(self, value: float):
        """Set ultimateBendingCapacity"""
        self.__ultimateBendingCapacity = float(value)

    @property
    def ultimatePressureCapacity(self) -> float:
        """Single load ultimate pressure capacity due to end cap effect"""
        return self.__ultimatePressureCapacity

    @ultimatePressureCapacity.setter
    def ultimatePressureCapacity(self, value: float):
        """Set ultimatePressureCapacity"""
        self.__ultimatePressureCapacity = float(value)

    @property
    def internalPressure(self) -> float:
        """Internal pressure"""
        return self.__internalPressure

    @internalPressure.setter
    def internalPressure(self, value: float):
        """Set internalPressure"""
        self.__internalPressure = float(value)

    @property
    def externalPressure(self) -> float:
        """External pressure"""
        return self.__externalPressure

    @externalPressure.setter
    def externalPressure(self, value: float):
        """Set externalPressure"""
        self.__externalPressure = float(value)

    @property
    def designFactor(self) -> float:
        """Design factor"""
        return self.__designFactor

    @designFactor.setter
    def designFactor(self, value: float):
        """Set designFactor"""
        self.__designFactor = float(value)
