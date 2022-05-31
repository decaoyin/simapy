# This an autogenerated file
# 
# Generated with RollerContact
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.rollercontact import RollerContactBlueprint
from typing import Dict
from sima.riflex.roller import Roller
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue

class RollerContact(NamedObject):
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
    rollers : List[Roller]
    """

    def __init__(self , name="", description="", _id="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.rollers = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RollerContactBlueprint()


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
    def rollers(self) -> List[Roller]:
        """"""
        return self.__rollers

    @rollers.setter
    def rollers(self, value: List[Roller]):
        """Set rollers"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__rollers = value
