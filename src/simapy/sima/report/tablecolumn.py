# This an autogenerated file
# 
# Generated with TableColumn
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.tablecolumn import TableColumnBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .tablecell import TableCell
from .tablecellstyle import TableCellStyle

class TableColumn(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    header : str
         (default None)
    headerStyle : TableCellStyle
    cells : List[TableCell]
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.header = None
        self.headerStyle = None
        self.cells = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TableColumnBlueprint()


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
    def header(self) -> str:
        """"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = value

    @property
    def headerStyle(self) -> TableCellStyle:
        """"""
        return self.__headerStyle

    @headerStyle.setter
    def headerStyle(self, value: TableCellStyle):
        """Set headerStyle"""
        self.__headerStyle = value

    @property
    def cells(self) -> List[TableCell]:
        """"""
        return self.__cells

    @cells.setter
    def cells(self, value: List[TableCell]):
        """Set cells"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__cells = value