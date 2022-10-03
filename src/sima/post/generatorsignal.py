# This an autogenerated file
# 
# Generated with GeneratorSignal
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.generatorsignal import GeneratorSignalBlueprint
from typing import Dict
from sima.post.signalproperties import SignalProperties
from sima.post.signalpropertiescontainer import SignalPropertiesContainer
from sima.sima.named import Named
from sima.sima.scriptablevalue import ScriptableValue

class GeneratorSignal(SignalPropertiesContainer,Named):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    properties : List[SignalProperties]
    name : str
         (default "")
    """

    def __init__(self , _id="", name="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.properties = list()
        self.name = name
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GeneratorSignalBlueprint()


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
    def properties(self) -> List[SignalProperties]:
        """"""
        return self.__properties

    @properties.setter
    def properties(self, value: List[SignalProperties]):
        """Set properties"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__properties = value

    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)
