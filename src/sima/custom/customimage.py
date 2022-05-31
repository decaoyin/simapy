# This an autogenerated file
# 
# Generated with CustomImage
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.customimage import CustomImageBlueprint
from typing import Dict
from sima.custom.customcomponent import CustomComponent
from sima.sima.scriptablevalue import ScriptableValue

class CustomImage(CustomComponent):
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
    filename : str
         (default "")
    factor : float
         (default 0.2)
    """

    def __init__(self , name="", description="", _id="", filename="", factor=0.2, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.filename = filename
        self.factor = factor
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomImageBlueprint()


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
    def filename(self) -> str:
        """"""
        return self.__filename

    @filename.setter
    def filename(self, value: str):
        """Set filename"""
        self.__filename = str(value)

    @property
    def factor(self) -> float:
        """"""
        return self.__factor

    @factor.setter
    def factor(self, value: float):
        """Set factor"""
        self.__factor = float(value)
