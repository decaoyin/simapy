# This an autogenerated file
# 
# Generated with VariableField
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.variablefield import VariableFieldBlueprint
from numpy import ndarray,asarray
from .fieldtype import FieldType
from .filetype import FileType
from .parameterfield import ParameterField
from sima.sima import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima import Variable

class VariableField(ParameterField):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    label : str
         (default None)
    tooltip : str
         (default None)
    fileType : FileType
    directory : bool
         (default False)
    fileExtensions : str
         Describes legal file extensions separated by semicolon, example:  *.txt;*.dat(default None)
    options : ndarray of str
    _type : FieldType
    width : int
         (default 10)
    expandHorizontally : bool
         If set the field will fill all available horzontal space(default False)
    variable : Variable
    unit : str
         (default None)
    constraints : str
         Give a valid range for a number: Use <,> for excluding and [] for including.\nExampless: \n- [0,4] Number from and including 0 to and including 4\n- <0,4> From and to, excluding \n- <,0> All negative numbers excluding 0\n- [0,> All positive numbers, including 0\n(default None)
    """

    def __init__(self , description="", fileType=FileType.INPUT, directory=False, _type=FieldType.TEXT, width=10, expandHorizontally=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.label = None
        self.tooltip = None
        self.fileType = fileType
        self.directory = directory
        self.fileExtensions = None
        self.options = []
        self._type = _type
        self.width = width
        self.expandHorizontally = expandHorizontally
        self.variable = None
        self.unit = None
        self.constraints = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return VariableFieldBlueprint()


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
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = value

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = value

    @property
    def fileType(self) -> FileType:
        """"""
        return self.__fileType

    @fileType.setter
    def fileType(self, value: FileType):
        """Set fileType"""
        self.__fileType = value

    @property
    def directory(self) -> bool:
        """"""
        return self.__directory

    @directory.setter
    def directory(self, value: bool):
        """Set directory"""
        self.__directory = bool(value)

    @property
    def fileExtensions(self) -> str:
        """Describes legal file extensions separated by semicolon, example:  *.txt;*.dat"""
        return self.__fileExtensions

    @fileExtensions.setter
    def fileExtensions(self, value: str):
        """Set fileExtensions"""
        self.__fileExtensions = value

    @property
    def options(self) -> ndarray:
        """"""
        return self.__options

    @options.setter
    def options(self, value: ndarray):
        """Set options"""
        array = asarray(value, dtype=str)
        if len(array) > 0 and array.ndim != 1:
            raise ValueError("Expected array with 1 dimensions")
        self.__options = array

    @property
    def _type(self) -> FieldType:
        """"""
        return self.___type

    @_type.setter
    def _type(self, value: FieldType):
        """Set _type"""
        self.___type = value

    @property
    def width(self) -> int:
        """"""
        return self.__width

    @width.setter
    def width(self, value: int):
        """Set width"""
        self.__width = int(value)

    @property
    def expandHorizontally(self) -> bool:
        """If set the field will fill all available horzontal space"""
        return self.__expandHorizontally

    @expandHorizontally.setter
    def expandHorizontally(self, value: bool):
        """Set expandHorizontally"""
        self.__expandHorizontally = bool(value)

    @property
    def variable(self) -> Variable:
        """"""
        return self.__variable

    @variable.setter
    def variable(self, value: Variable):
        """Set variable"""
        self.__variable = value

    @property
    def unit(self) -> str:
        """"""
        return self.__unit

    @unit.setter
    def unit(self, value: str):
        """Set unit"""
        self.__unit = value

    @property
    def constraints(self) -> str:
        """Give a valid range for a number: Use <,> for excluding and [] for including.
Exampless: 
- [0,4] Number from and including 0 to and including 4
- <0,4> From and to, excluding 
- <,0> All negative numbers excluding 0
- [0,> All positive numbers, including 0
"""
        return self.__constraints

    @constraints.setter
    def constraints(self, value: str):
        """Set constraints"""
        self.__constraints = value
