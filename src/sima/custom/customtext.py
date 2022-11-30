# This an autogenerated file
# 
# Generated with CustomText
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.customtext import CustomTextBlueprint
from numpy import ndarray,asarray
from sima.custom.fieldtype import FieldType
from sima.custom.filetype import FileType
from sima.custom.parameterfield import ParameterField
from sima.sima.named import Named
from sima.sima.scriptablevalue import ScriptableValue

class CustomText(ParameterField,Named):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    label : str
         (default None)
    tooltip : str
         (default None)
    fileType : FileType
    directory : bool
         (default False)
    fileExtensions : str
         Describes legal file extensions separated by semicolon, example:  *.txt;*.dat(default None)
    options : ndarray
    _type : FieldType
    width : int
         (default 10)
    expandHorizontally : bool
         If set the field will fill all available horzontal space(default False)
    value : str
         (default None)
    """

    def __init__(self , description="", fileType=FileType.INPUT, directory=False, _type=FieldType.TEXT, width=10, expandHorizontally=False, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.label = None
        self.tooltip = None
        self.fileType = fileType
        self.directory = directory
        self.fileExtensions = None
        self.options = ndarray(1)
        self._type = _type
        self.width = width
        self.expandHorizontally = expandHorizontally
        self.value = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomTextBlueprint()


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
        self.__options = asarray(value)

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
    def value(self) -> str:
        """"""
        return self.__value

    @value.setter
    def value(self, value: str):
        """Set value"""
        self.__value = value
