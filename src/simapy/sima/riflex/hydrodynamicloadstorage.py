# This an autogenerated file
# 
# Generated with HydrodynamicLoadStorage
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hydrodynamicloadstorage import HydrodynamicLoadStorageBlueprint
from typing import Dict
from ..sima import MOAO
from ..sima import ScriptableValue
from .hydrodynamicloadelementstorage import HydrodynamicLoadElementStorage

class HydrodynamicLoadStorage(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    store : bool
         Store hydrodynamic loads(default False)
    storageStep : int
         Storage for every <storage step> given.(default 1)
    elements : List[HydrodynamicLoadElementStorage]
         Specification of nodes for displacement storage
    """

    def __init__(self , description="", store=False, storageStep=1, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.store = store
        self.storageStep = storageStep
        self.elements = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HydrodynamicLoadStorageBlueprint()


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
    def store(self) -> bool:
        """Store hydrodynamic loads"""
        return self.__store

    @store.setter
    def store(self, value: bool):
        """Set store"""
        self.__store = bool(value)

    @property
    def storageStep(self) -> int:
        """Storage for every <storage step> given."""
        return self.__storageStep

    @storageStep.setter
    def storageStep(self, value: int):
        """Set storageStep"""
        self.__storageStep = int(value)

    @property
    def elements(self) -> List[HydrodynamicLoadElementStorage]:
        """Specification of nodes for displacement storage"""
        return self.__elements

    @elements.setter
    def elements(self, value: List[HydrodynamicLoadElementStorage]):
        """Set elements"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__elements = value
