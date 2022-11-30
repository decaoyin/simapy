# This an autogenerated file
# 
# Generated with ReportText
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.reporttext import ReportTextBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.workflow.reportfragmentitem import ReportFragmentItem

class ReportText(ReportFragmentItem):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    text : str
         (default None)
    """

    def __init__(self , description="", **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.text = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ReportTextBlueprint()


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
    def text(self) -> str:
        """"""
        return self.__text

    @text.setter
    def text(self, value: str):
        """Set text"""
        self.__text = value
