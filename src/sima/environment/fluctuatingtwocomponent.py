# This an autogenerated file
# 
# Generated with FluctuatingTwoComponent
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.fluctuatingtwocomponent import FluctuatingTwoComponentBlueprint
from typing import Dict
from sima.environment.wind import Wind
from sima.sima.scriptablevalue import ScriptableValue

class FluctuatingTwoComponent(Wind):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    direction : float
         Wind propagation direction(default 0.0)
    fileName : str
         Path and filename for import of wind velocity time series(default "")
    """

    def __init__(self , _id="", direction=0.0, fileName="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.direction = direction
        self.fileName = fileName
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FluctuatingTwoComponentBlueprint()


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
    def direction(self) -> float:
        """Wind propagation direction"""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def fileName(self) -> str:
        """Path and filename for import of wind velocity time series"""
        return self.__fileName

    @fileName.setter
    def fileName(self, value: str):
        """Set fileName"""
        self.__fileName = str(value)
