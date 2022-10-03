# This an autogenerated file
# 
# Generated with RetardationElementData
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.retardationelementdata import RetardationElementDataBlueprint
from numpy import ndarray,asarray
from sima.hydro.dof import DOF
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class RetardationElementData(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    dof1 : DOF
    dof2 : DOF
    values : ndarray
    """

    def __init__(self , _id="", dof1=DOF.X, dof2=DOF.X, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.dof1 = dof1
        self.dof2 = dof2
        self.values = ndarray(1)
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RetardationElementDataBlueprint()


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
    def dof1(self) -> DOF:
        """"""
        return self.__dof1

    @dof1.setter
    def dof1(self, value: DOF):
        """Set dof1"""
        self.__dof1 = value

    @property
    def dof2(self) -> DOF:
        """"""
        return self.__dof2

    @dof2.setter
    def dof2(self, value: DOF):
        """Set dof2"""
        self.__dof2 = value

    @property
    def values(self) -> ndarray:
        """"""
        return self.__values

    @values.setter
    def values(self, value: ndarray):
        """Set values"""
        self.__values = asarray(value)
