# This an autogenerated file
# 
# Generated with SIMAScript
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.simascript import SIMAScriptBlueprint
from typing import Dict
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simascriptcontext import SIMAScriptContext
from sima.sima.simascripttrigger import SIMAScriptTrigger

class SIMAScript(NamedObject):
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
    script : str
         (default "")
    contextItems : List[SIMAScriptContext]
    triggers : List[SIMAScriptTrigger]
    """

    def __init__(self , name="", description="", _id="", script="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.script = script
        self.contextItems = list()
        self.triggers = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMAScriptBlueprint()


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
    def script(self) -> str:
        """"""
        return self.__script

    @script.setter
    def script(self, value: str):
        """Set script"""
        self.__script = str(value)

    @property
    def contextItems(self) -> List[SIMAScriptContext]:
        """"""
        return self.__contextItems

    @contextItems.setter
    def contextItems(self, value: List[SIMAScriptContext]):
        """Set contextItems"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__contextItems = value

    @property
    def triggers(self) -> List[SIMAScriptTrigger]:
        """"""
        return self.__triggers

    @triggers.setter
    def triggers(self, value: List[SIMAScriptTrigger]):
        """Set triggers"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__triggers = value
