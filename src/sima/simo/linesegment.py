# This an autogenerated file
# 
# Generated with LineSegment
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.linesegment import LineSegmentBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.segmenttype import SegmentType
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.simo.buoytype import BuoyType
    from sima.simo.elongationcharacteristic import ElongationCharacteristic

class LineSegment(MOAO):
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
    length : float
         Length of the segment(default 0.0)
    buoy : BuoyType
    segmentType : SegmentType
         Segment type
    numElements : int
         Number of elements. Used for calculation of fibre rope characteristics and for visualization(default 0)
    bottomFriction : float
         Friction coefficient between line and sea bottom(default 0.0)
    diameter : float
         Segment diameter(default 0.0)
    eMod : float
         Modulus of elasticity(default 0.0)
    emFac : float
         Factor of elasticity - 2 for chains - 1 for other segment types(default 1.0)
    transverseDrag : float
         Transverse drag coefficient(default 0.0)
    longitudinalDrag : float
         Longitudinal drag coefficient(default 0.0)
    uwia : float
         Unit weight in air(default 0.0)
    watfac : float
         The ratio of weight in water to weight in air(default 0.0)
    elongationCharacteristic : ElongationCharacteristic
         Non-linear Elongation characteristic
    """

    def __init__(self , name="", description="", _id="", length=0.0, segmentType=SegmentType.CATENARY, numElements=0, bottomFriction=0.0, diameter=0.0, eMod=0.0, emFac=1.0, transverseDrag=0.0, longitudinalDrag=0.0, uwia=0.0, watfac=0.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.length = length
        self.buoy = None
        self.segmentType = segmentType
        self.numElements = numElements
        self.bottomFriction = bottomFriction
        self.diameter = diameter
        self.eMod = eMod
        self.emFac = emFac
        self.transverseDrag = transverseDrag
        self.longitudinalDrag = longitudinalDrag
        self.uwia = uwia
        self.watfac = watfac
        self.elongationCharacteristic = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return LineSegmentBlueprint()


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
    def length(self) -> float:
        """Length of the segment"""
        return self.__length

    @length.setter
    def length(self, value: float):
        """Set length"""
        self.__length = float(value)

    @property
    def buoy(self) -> BuoyType:
        """"""
        return self.__buoy

    @buoy.setter
    def buoy(self, value: BuoyType):
        """Set buoy"""
        self.__buoy = value

    @property
    def segmentType(self) -> SegmentType:
        """Segment type"""
        return self.__segmentType

    @segmentType.setter
    def segmentType(self, value: SegmentType):
        """Set segmentType"""
        self.__segmentType = value

    @property
    def numElements(self) -> int:
        """Number of elements. Used for calculation of fibre rope characteristics and for visualization"""
        return self.__numElements

    @numElements.setter
    def numElements(self, value: int):
        """Set numElements"""
        self.__numElements = int(value)

    @property
    def bottomFriction(self) -> float:
        """Friction coefficient between line and sea bottom"""
        return self.__bottomFriction

    @bottomFriction.setter
    def bottomFriction(self, value: float):
        """Set bottomFriction"""
        self.__bottomFriction = float(value)

    @property
    def diameter(self) -> float:
        """Segment diameter"""
        return self.__diameter

    @diameter.setter
    def diameter(self, value: float):
        """Set diameter"""
        self.__diameter = float(value)

    @property
    def eMod(self) -> float:
        """Modulus of elasticity"""
        return self.__eMod

    @eMod.setter
    def eMod(self, value: float):
        """Set eMod"""
        self.__eMod = float(value)

    @property
    def emFac(self) -> float:
        """Factor of elasticity - 2 for chains - 1 for other segment types"""
        return self.__emFac

    @emFac.setter
    def emFac(self, value: float):
        """Set emFac"""
        self.__emFac = float(value)

    @property
    def transverseDrag(self) -> float:
        """Transverse drag coefficient"""
        return self.__transverseDrag

    @transverseDrag.setter
    def transverseDrag(self, value: float):
        """Set transverseDrag"""
        self.__transverseDrag = float(value)

    @property
    def longitudinalDrag(self) -> float:
        """Longitudinal drag coefficient"""
        return self.__longitudinalDrag

    @longitudinalDrag.setter
    def longitudinalDrag(self, value: float):
        """Set longitudinalDrag"""
        self.__longitudinalDrag = float(value)

    @property
    def uwia(self) -> float:
        """Unit weight in air"""
        return self.__uwia

    @uwia.setter
    def uwia(self, value: float):
        """Set uwia"""
        self.__uwia = float(value)

    @property
    def watfac(self) -> float:
        """The ratio of weight in water to weight in air"""
        return self.__watfac

    @watfac.setter
    def watfac(self, value: float):
        """Set watfac"""
        self.__watfac = float(value)

    @property
    def elongationCharacteristic(self) -> ElongationCharacteristic:
        """Non-linear Elongation characteristic"""
        return self.__elongationCharacteristic

    @elongationCharacteristic.setter
    def elongationCharacteristic(self, value: ElongationCharacteristic):
        """Set elongationCharacteristic"""
        self.__elongationCharacteristic = value
