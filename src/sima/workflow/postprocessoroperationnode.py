# This an autogenerated file
# 
# Generated with PostProcessorOperationNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.postprocessoroperationnode import PostProcessorOperationNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.operationnode import OperationNode
from sima.post.runnode import RunNode
from sima.post.slotconnection import SlotConnection
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.operationinputslot import OperationInputSlot
from sima.workflow.operationoutputslot import OperationOutputSlot
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.post.operationnode import OperationNode

class PostProcessorOperationNode(RunNode):
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
    nodes : List[OperationNode]
    connections : List[SlotConnection]
    operation : OperationNode
    operationOutputSlots : List[OperationOutputSlot]
    operationInputSlots : List[OperationInputSlot]
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
        self.nodes = list()
        self.connections = list()
        self.operation = None
        self.operationOutputSlots = list()
        self.operationInputSlots = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PostProcessorOperationNodeBlueprint()


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
    def nodes(self) -> List[OperationNode]:
        """"""
        return self.__nodes

    @nodes.setter
    def nodes(self, value: List[OperationNode]):
        """Set nodes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__nodes = value

    @property
    def connections(self) -> List[SlotConnection]:
        """"""
        return self.__connections

    @connections.setter
    def connections(self, value: List[SlotConnection]):
        """Set connections"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__connections = value

    @property
    def operation(self) -> OperationNode:
        """"""
        return self.__operation

    @operation.setter
    def operation(self, value: OperationNode):
        """Set operation"""
        self.__operation = value

    @property
    def operationOutputSlots(self) -> List[OperationOutputSlot]:
        """"""
        return self.__operationOutputSlots

    @operationOutputSlots.setter
    def operationOutputSlots(self, value: List[OperationOutputSlot]):
        """Set operationOutputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__operationOutputSlots = value

    @property
    def operationInputSlots(self) -> List[OperationInputSlot]:
        """"""
        return self.__operationInputSlots

    @operationInputSlots.setter
    def operationInputSlots(self, value: List[OperationInputSlot]):
        """Set operationInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__operationInputSlots = value
