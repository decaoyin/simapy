# This an autogenerated file
# 
# Generated with ColumnConfiguration
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.columnconfiguration import ColumnConfigurationBlueprint
from typing import Dict
from .pathspecification import PathSpecification
from sima.sima import ScriptableValue

class ColumnConfiguration(PathSpecification):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    path : str
         (default None)
    header : str
         Column header. The default value is the header,legend or name attribute of the signal(default None)
    label : str
         Column label. The default value is the unit of the y axis, or the label attribute, or ylabel + unit if specified(default None)
    format : str
         Column number format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description(default '0.####E0')
    fontSize : int
         Column font size. Will be used when renderin the table in a report,etc.(default 0)
    """

    def __init__(self , description="", format='0.####E0', fontSize=0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.path = None
        self.header = None
        self.label = None
        self.format = format
        self.fontSize = fontSize
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ColumnConfigurationBlueprint()


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
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = value

    @property
    def header(self) -> str:
        """Column header. The default value is the header,legend or name attribute of the signal"""
        return self.__header

    @header.setter
    def header(self, value: str):
        """Set header"""
        self.__header = value

    @property
    def label(self) -> str:
        """Column label. The default value is the unit of the y axis, or the label attribute, or ylabel + unit if specified"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = value

    @property
    def format(self) -> str:
        """Column number format. Please refer to https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html for a description"""
        return self.__format

    @format.setter
    def format(self, value: str):
        """Set format"""
        self.__format = value

    @property
    def fontSize(self) -> int:
        """Column font size. Will be used when renderin the table in a report,etc."""
        return self.__fontSize

    @fontSize.setter
    def fontSize(self, value: int):
        """Set fontSize"""
        self.__fontSize = int(value)
