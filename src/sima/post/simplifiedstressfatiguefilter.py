# This an autogenerated file
# 
# Generated with SimplifiedStressFatigueFilter
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simplifiedstressfatiguefilter import SimplifiedStressFatigueFilterBlueprint
from typing import Dict
from .controlsignalinputslot import ControlSignalInputSlot
from .inputslot import InputSlot
from .operationnode import OperationNode
from .outputslot import OutputSlot
from sima.sima import ScriptableValue

class SimplifiedStressFatigueFilter(OperationNode):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    x : int
         (default 0)
    y : int
         (default 0)
    h : int
         (default 0)
    w : int
         (default 0)
    controlSignalInputSlots : List[ControlSignalInputSlot]
    filterInputSlots : List[InputSlot]
    filterOutputSlots : List[OutputSlot]
    numberOfPoints : int
         Number of points in the calculation(default 8)
    radius : float
         Distance from pipe center to a point in the pipe wall(default 0.0)
    innerRadius : float
         Inner radius of the pipe(default 0.0)
    outerRadius : float
         Outer radius of the pipe(default 0.0)
    numberOfCycles : int
         Number of cycles(default 0)
    shape : float
         Shape parameter of stress distribution(default 0.0)
    intercept : float
         Intercept parameter of the SN curve(default 0.0)
    slope : float
         Slope parameter of the SN curve(default 0.0)
    """

    def __init__(self , description="", x=0, y=0, h=0, w=0, numberOfPoints=8, radius=0.0, innerRadius=0.0, outerRadius=0.0, numberOfCycles=0, shape=0.0, intercept=0.0, slope=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.x = x
        self.y = y
        self.h = h
        self.w = w
        self.controlSignalInputSlots = list()
        self.filterInputSlots = list()
        self.filterOutputSlots = list()
        self.numberOfPoints = numberOfPoints
        self.radius = radius
        self.innerRadius = innerRadius
        self.outerRadius = outerRadius
        self.numberOfCycles = numberOfCycles
        self.shape = shape
        self.intercept = intercept
        self.slope = slope
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SimplifiedStressFatigueFilterBlueprint()


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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = value

    @property
    def x(self) -> int:
        """"""
        return self.__x

    @x.setter
    def x(self, value: int):
        """Set x"""
        self.__x = int(value)

    @property
    def y(self) -> int:
        """"""
        return self.__y

    @y.setter
    def y(self, value: int):
        """Set y"""
        self.__y = int(value)

    @property
    def h(self) -> int:
        """"""
        return self.__h

    @h.setter
    def h(self, value: int):
        """Set h"""
        self.__h = int(value)

    @property
    def w(self) -> int:
        """"""
        return self.__w

    @w.setter
    def w(self, value: int):
        """Set w"""
        self.__w = int(value)

    @property
    def controlSignalInputSlots(self) -> List[ControlSignalInputSlot]:
        """"""
        return self.__controlSignalInputSlots

    @controlSignalInputSlots.setter
    def controlSignalInputSlots(self, value: List[ControlSignalInputSlot]):
        """Set controlSignalInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__controlSignalInputSlots = value

    @property
    def filterInputSlots(self) -> List[InputSlot]:
        """"""
        return self.__filterInputSlots

    @filterInputSlots.setter
    def filterInputSlots(self, value: List[InputSlot]):
        """Set filterInputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__filterInputSlots = value

    @property
    def filterOutputSlots(self) -> List[OutputSlot]:
        """"""
        return self.__filterOutputSlots

    @filterOutputSlots.setter
    def filterOutputSlots(self, value: List[OutputSlot]):
        """Set filterOutputSlots"""
        if not isinstance(value, Sequence):
            raise ValueError("Expected sequense, but was " , type(value))
        self.__filterOutputSlots = value

    @property
    def numberOfPoints(self) -> int:
        """Number of points in the calculation"""
        return self.__numberOfPoints

    @numberOfPoints.setter
    def numberOfPoints(self, value: int):
        """Set numberOfPoints"""
        self.__numberOfPoints = int(value)

    @property
    def radius(self) -> float:
        """Distance from pipe center to a point in the pipe wall"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def innerRadius(self) -> float:
        """Inner radius of the pipe"""
        return self.__innerRadius

    @innerRadius.setter
    def innerRadius(self, value: float):
        """Set innerRadius"""
        self.__innerRadius = float(value)

    @property
    def outerRadius(self) -> float:
        """Outer radius of the pipe"""
        return self.__outerRadius

    @outerRadius.setter
    def outerRadius(self, value: float):
        """Set outerRadius"""
        self.__outerRadius = float(value)

    @property
    def numberOfCycles(self) -> int:
        """Number of cycles"""
        return self.__numberOfCycles

    @numberOfCycles.setter
    def numberOfCycles(self, value: int):
        """Set numberOfCycles"""
        self.__numberOfCycles = int(value)

    @property
    def shape(self) -> float:
        """Shape parameter of stress distribution"""
        return self.__shape

    @shape.setter
    def shape(self, value: float):
        """Set shape"""
        self.__shape = float(value)

    @property
    def intercept(self) -> float:
        """Intercept parameter of the SN curve"""
        return self.__intercept

    @intercept.setter
    def intercept(self, value: float):
        """Set intercept"""
        self.__intercept = float(value)

    @property
    def slope(self) -> float:
        """Slope parameter of the SN curve"""
        return self.__slope

    @slope.setter
    def slope(self, value: float):
        """Set slope"""
        self.__slope = float(value)
