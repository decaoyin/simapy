# This an autogenerated file
# 
# Generated with PostProcessorNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.postprocessornode import PostProcessorNodeBlueprint
from typing import Dict
from .postprocessorinputslot import PostprocessorInputSlot
from .postprocessoroutputslot import PostprocessorOutputSlot
from .variableinputslot import VariableInputSlot
from sima.post import ControlSignalInputSlot
from sima.post import RunNode
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.post import PostProcessorSpecification

class PostProcessorNode(RunNode):
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
    variableInputSlots : List[VariableInputSlot]
    postprocessor : PostProcessorSpecification
    postOutputSlots : List[PostprocessorOutputSlot]
    postInputSlots : List[PostprocessorInputSlot]
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.variableInputSlots = list()
        self.postprocessor = None
        self.postOutputSlots = list()
        self.postInputSlots = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PostProcessorNodeBlueprint()


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
    def variableInputSlots(self) -> List[VariableInputSlot]:
        """"""
        return self.__variableInputSlots

    @variableInputSlots.setter
    def variableInputSlots(self, value: List[VariableInputSlot]):
        """Set variableInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__variableInputSlots = value

    @property
    def postprocessor(self) -> PostProcessorSpecification:
        """"""
        return self.__postprocessor

    @postprocessor.setter
    def postprocessor(self, value: PostProcessorSpecification):
        """Set postprocessor"""
        self.__postprocessor = value

    @property
    def postOutputSlots(self) -> List[PostprocessorOutputSlot]:
        """"""
        return self.__postOutputSlots

    @postOutputSlots.setter
    def postOutputSlots(self, value: List[PostprocessorOutputSlot]):
        """Set postOutputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__postOutputSlots = value

    @property
    def postInputSlots(self) -> List[PostprocessorInputSlot]:
        """"""
        return self.__postInputSlots

    @postInputSlots.setter
    def postInputSlots(self, value: List[PostprocessorInputSlot]):
        """Set postInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__postInputSlots = value
