# This an autogenerated file
# 
# Generated with ISO19901_7Filter
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.iso19901_7filter import ISO19901_7FilterBlueprint
from typing import Dict
from sima.post.consequenceclass import ConsequenceClass
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.inputslot import InputSlot
from sima.post.iso19901_7_analysis import ISO19901_7_analysis
from sima.post.mooringtype import MooringType
from sima.post.operationnode import OperationNode
from sima.post.outputslot import OutputSlot
from sima.sima.scriptablevalue import ScriptableValue

class ISO19901_7Filter(OperationNode):
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
    breakingStrength : float
         Breaking strength(default 0.0)
    customSafetyFactor : float
         Safety factor(default 0.0)
    analysis : ISO19901_7_analysis
    mooringType : MooringType
    consequenceClass : ConsequenceClass
    useCustomSafetyFactor : bool
         (default False)
    """

    def __init__(self , name="", description="", _id="", x=0, y=0, h=0, w=0, breakingStrength=0.0, customSafetyFactor=0.0, analysis=ISO19901_7_analysis.INTACT_CONDITION, mooringType=MooringType.PERMANENT_MOORING, consequenceClass=ConsequenceClass.CLASS_ONE, useCustomSafetyFactor=False, **kwargs):
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
        self.breakingStrength = breakingStrength
        self.customSafetyFactor = customSafetyFactor
        self.analysis = analysis
        self.mooringType = mooringType
        self.consequenceClass = consequenceClass
        self.useCustomSafetyFactor = useCustomSafetyFactor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ISO19901_7FilterBlueprint()


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
    def breakingStrength(self) -> float:
        """Breaking strength"""
        return self.__breakingStrength

    @breakingStrength.setter
    def breakingStrength(self, value: float):
        """Set breakingStrength"""
        self.__breakingStrength = float(value)

    @property
    def customSafetyFactor(self) -> float:
        """Safety factor"""
        return self.__customSafetyFactor

    @customSafetyFactor.setter
    def customSafetyFactor(self, value: float):
        """Set customSafetyFactor"""
        self.__customSafetyFactor = float(value)

    @property
    def analysis(self) -> ISO19901_7_analysis:
        """"""
        return self.__analysis

    @analysis.setter
    def analysis(self, value: ISO19901_7_analysis):
        """Set analysis"""
        self.__analysis = value

    @property
    def mooringType(self) -> MooringType:
        """"""
        return self.__mooringType

    @mooringType.setter
    def mooringType(self, value: MooringType):
        """Set mooringType"""
        self.__mooringType = value

    @property
    def consequenceClass(self) -> ConsequenceClass:
        """"""
        return self.__consequenceClass

    @consequenceClass.setter
    def consequenceClass(self, value: ConsequenceClass):
        """Set consequenceClass"""
        self.__consequenceClass = value

    @property
    def useCustomSafetyFactor(self) -> bool:
        """"""
        return self.__useCustomSafetyFactor

    @useCustomSafetyFactor.setter
    def useCustomSafetyFactor(self, value: bool):
        """Set useCustomSafetyFactor"""
        self.__useCustomSafetyFactor = bool(value)
