# This an autogenerated file
# 
# Generated with CustomWizardPage
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.customwizardpage import CustomWizardPageBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class CustomWizardPage(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    children : List[CustomComponent]
    title : str
         (default "")
    """

    def __init__(self , _id="", title="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.children = list()
        self.title = title
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomWizardPageBlueprint()


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
    def children(self) -> List[CustomComponent]:
        """"""
        return self.__children

    @children.setter
    def children(self, value: List[CustomComponent]):
        """Set children"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__children = value

    @property
    def title(self) -> str:
        """"""
        return self.__title

    @title.setter
    def title(self, value: str):
        """Set title"""
        self.__title = str(value)
