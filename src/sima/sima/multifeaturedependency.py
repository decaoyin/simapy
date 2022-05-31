# This an autogenerated file
# 
# Generated with MultiFeatureDependency
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.multifeaturedependency import MultiFeatureDependencyBlueprint
from typing import Dict
from sima.sima.dependency import Dependency
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.sima.moao import MOAO

class MultiFeatureDependency(Dependency):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    object : MOAO
    feature : str
         (default "")
    root : MOAO
    """

    def __init__(self , name="", description="", _id="", feature="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.object = None
        self.feature = feature
        self.root = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return MultiFeatureDependencyBlueprint()


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
    def object(self) -> MOAO:
        """"""
        return self.__object

    @object.setter
    def object(self, value: MOAO):
        """Set object"""
        self.__object = value

    @property
    def feature(self) -> str:
        """"""
        return self.__feature

    @feature.setter
    def feature(self, value: str):
        """Set feature"""
        self.__feature = str(value)

    @property
    def root(self) -> MOAO:
        """"""
        return self.__root

    @root.setter
    def root(self, value: MOAO):
        """Set root"""
        self.__root = value
