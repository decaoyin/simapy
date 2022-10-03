# This an autogenerated file
# 
# Generated with HLAROV
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.hlarov import HLAROVBlueprint
from typing import Dict
from sima.hla.hlabody import HLABody
from sima.hla.hlabodyviewpoint import HLABodyViewpoint
from sima.sima.appearance import Appearance
from sima.sima.position import Position
from sima.sima.scriptablevalue import ScriptableValue

class HLAROV(HLABody):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    length : float
         Length(default 10.0)
    width : float
         Width(default 5.0)
    height : float
         Height(default 5.0)
    appearance : Appearance
    position : Position
    viewpoints : List[HLABodyViewpoint]
    """

    def __init__(self , _id="", name="", length=10.0, width=5.0, height=5.0, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.length = length
        self.width = width
        self.height = height
        self.appearance = None
        self.position = None
        self.viewpoints = list()
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return HLAROVBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def length(self) -> float:
        """Length"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def width(self) -> float:
        """Width"""
        return self.__width

    @width.setter
    def width(self, value: float):
        """Set width"""
        self.__width = float(value)

    @property
    def height(self) -> float:
        """Height"""
        return self.__height

    @height.setter
    def height(self, value: float):
        """Set height"""
        self.__height = float(value)

    @property
    def appearance(self) -> Appearance:
        """"""
        return self.__appearance

    @appearance.setter
    def appearance(self, value: Appearance):
        """Set appearance"""
        self.__appearance = value

    @property
    def position(self) -> Position:
        """"""
        return self.__position

    @position.setter
    def position(self, value: Position):
        """Set position"""
        self.__position = value

    @property
    def viewpoints(self) -> List[HLABodyViewpoint]:
        """"""
        return self.__viewpoints

    @viewpoints.setter
    def viewpoints(self, value: List[HLABodyViewpoint]):
        """Set viewpoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__viewpoints = value
