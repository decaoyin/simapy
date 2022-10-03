# This an autogenerated file
# 
# Generated with ReportGeneratorNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.reportgeneratornode import ReportGeneratorNodeBlueprint
from typing import Dict
from sima.post.controlsignalinputslot import ControlSignalInputSlot
from sima.post.outputslot import OutputSlot
from sima.post.runnode import RunNode
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.modelreferenceinputslot import ModelReferenceInputSlot
from sima.workflow.reportformat import ReportFormat
from sima.workflow.reportfragmentreferenceinputslot import ReportFragmentReferenceInputSlot
from sima.workflow.variableinputslot import VariableInputSlot
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.report.report import Report

class ReportGeneratorNode(RunNode):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
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
    modelReferenceInputSlot : ModelReferenceInputSlot
    report : Report
    fragmentInputSlots : List[ReportFragmentReferenceInputSlot]
    outputSlot : OutputSlot
    inputReport : bool
         Set the report input from the outside. Use a model reference as source.(default False)
    format : ReportFormat
    """

    def __init__(self , _id="", name="", x=0, y=0, h=0, w=0, inputReport=False, format=ReportFormat.WORD, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.variableInputSlots = list()
        self.modelReferenceInputSlot = None
        self.report = None
        self.fragmentInputSlots = list()
        self.outputSlot = None
        self.inputReport = inputReport
        self.format = format
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportGeneratorNodeBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

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
    def variableInputSlots(self) -> List[VariableInputSlot]:
        """"""
        return self.__variableInputSlots

    @variableInputSlots.setter
    def variableInputSlots(self, value: List[VariableInputSlot]):
        """Set variableInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variableInputSlots = value

    @property
    def modelReferenceInputSlot(self) -> ModelReferenceInputSlot:
        """"""
        return self.__modelReferenceInputSlot

    @modelReferenceInputSlot.setter
    def modelReferenceInputSlot(self, value: ModelReferenceInputSlot):
        """Set modelReferenceInputSlot"""
        self.__modelReferenceInputSlot = value

    @property
    def report(self) -> Report:
        """"""
        return self.__report

    @report.setter
    def report(self, value: Report):
        """Set report"""
        self.__report = value

    @property
    def fragmentInputSlots(self) -> List[ReportFragmentReferenceInputSlot]:
        """"""
        return self.__fragmentInputSlots

    @fragmentInputSlots.setter
    def fragmentInputSlots(self, value: List[ReportFragmentReferenceInputSlot]):
        """Set fragmentInputSlots"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__fragmentInputSlots = value

    @property
    def outputSlot(self) -> OutputSlot:
        """"""
        return self.__outputSlot

    @outputSlot.setter
    def outputSlot(self, value: OutputSlot):
        """Set outputSlot"""
        self.__outputSlot = value

    @property
    def inputReport(self) -> bool:
        """Set the report input from the outside. Use a model reference as source."""
        return self.__inputReport

    @inputReport.setter
    def inputReport(self, value: bool):
        """Set inputReport"""
        self.__inputReport = bool(value)

    @property
    def format(self) -> ReportFormat:
        """"""
        return self.__format

    @format.setter
    def format(self, value: ReportFormat):
        """Set format"""
        self.__format = value
