# This an autogenerated file
# 
# Generated with ARWinch
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.arwinch import ARWinchBlueprint
from typing import Dict
from sima.riflex.centerofwinch import CenterOfWinch
from sima.riflex.end import End
from sima.riflex.segmentreference import SegmentReference
from sima.sima.namedobject import NamedObject
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine
    from sima.sima.body import Body

class ARWinch(SegmentReference,NamedObject):
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
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    segmentEnd : End
         End of segment (and line) attached to winch (1 or 2)
    relativeSegmentLength : float
         Relative segment length where segment is attached to winch point(default 0.0)
    x1 : float
         X-coordinate for static equilibrium position(default 0.0)
    y1 : float
         Y-coordinate for static equilibrium position(default 0.0)
    z1 : float
         Z-coordinate for static equilibrium position(default 0.0)
    rotation : float
         Specified rotation of supernode from stress free position to static equilibrium position.(default 0.0)
    rotationDirection : float
         Direction of axis for specified rotation(default 0.0)
    attachedBody : Body
    maxVelocity : float
         Maximum winch velocity(default 0.0)
    timeToMaxVelocity : float
         Time to reach maximum velocity (from zero)(default 0.0)
    lineRelease : bool
         Line release when no more line on winch (Dynamic analysis)(default False)
    radius : float
         Radius of winch(default 0.0)
    winchCenter : CenterOfWinch
         Center of winch in positive or negative local Z-axis
    lengthJustification : bool
         Control parameter for adjusting the length of elements attached to winch(default False)
    """

    def __init__(self , name="", description="", _id="", segment=1, allSegments=False, segmentEnd=End.ONE, relativeSegmentLength=0.0, x1=0.0, y1=0.0, z1=0.0, rotation=0.0, rotationDirection=0.0, maxVelocity=0.0, timeToMaxVelocity=0.0, lineRelease=False, radius=0.0, winchCenter=CenterOfWinch.NEGATIVE_Z_AXIS, lengthJustification=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.segmentEnd = segmentEnd
        self.relativeSegmentLength = relativeSegmentLength
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.rotation = rotation
        self.rotationDirection = rotationDirection
        self.attachedBody = None
        self.maxVelocity = maxVelocity
        self.timeToMaxVelocity = timeToMaxVelocity
        self.lineRelease = lineRelease
        self.radius = radius
        self.winchCenter = winchCenter
        self.lengthJustification = lengthJustification
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ARWinchBlueprint()


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
    def line(self) -> ARLine:
        """Line"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def segment(self) -> int:
        """Segment on given line"""
        return self.__segment

    @segment.setter
    def segment(self, value: int):
        """Set segment"""
        self.__segment = int(value)

    @property
    def allSegments(self) -> bool:
        """All segments"""
        return self.__allSegments

    @allSegments.setter
    def allSegments(self, value: bool):
        """Set allSegments"""
        self.__allSegments = bool(value)

    @property
    def segmentEnd(self) -> End:
        """End of segment (and line) attached to winch (1 or 2)"""
        return self.__segmentEnd

    @segmentEnd.setter
    def segmentEnd(self, value: End):
        """Set segmentEnd"""
        self.__segmentEnd = value

    @property
    def relativeSegmentLength(self) -> float:
        """Relative segment length where segment is attached to winch point"""
        return self.__relativeSegmentLength

    @relativeSegmentLength.setter
    def relativeSegmentLength(self, value: float):
        """Set relativeSegmentLength"""
        self.__relativeSegmentLength = float(value)

    @property
    def x1(self) -> float:
        """X-coordinate for static equilibrium position"""
        return self.__x1

    @x1.setter
    def x1(self, value: float):
        """Set x1"""
        self.__x1 = float(value)

    @property
    def y1(self) -> float:
        """Y-coordinate for static equilibrium position"""
        return self.__y1

    @y1.setter
    def y1(self, value: float):
        """Set y1"""
        self.__y1 = float(value)

    @property
    def z1(self) -> float:
        """Z-coordinate for static equilibrium position"""
        return self.__z1

    @z1.setter
    def z1(self, value: float):
        """Set z1"""
        self.__z1 = float(value)

    @property
    def rotation(self) -> float:
        """Specified rotation of supernode from stress free position to static equilibrium position."""
        return self.__rotation

    @rotation.setter
    def rotation(self, value: float):
        """Set rotation"""
        self.__rotation = float(value)

    @property
    def rotationDirection(self) -> float:
        """Direction of axis for specified rotation"""
        return self.__rotationDirection

    @rotationDirection.setter
    def rotationDirection(self, value: float):
        """Set rotationDirection"""
        self.__rotationDirection = float(value)

    @property
    def attachedBody(self) -> Body:
        """"""
        return self.__attachedBody

    @attachedBody.setter
    def attachedBody(self, value: Body):
        """Set attachedBody"""
        self.__attachedBody = value

    @property
    def maxVelocity(self) -> float:
        """Maximum winch velocity"""
        return self.__maxVelocity

    @maxVelocity.setter
    def maxVelocity(self, value: float):
        """Set maxVelocity"""
        self.__maxVelocity = float(value)

    @property
    def timeToMaxVelocity(self) -> float:
        """Time to reach maximum velocity (from zero)"""
        return self.__timeToMaxVelocity

    @timeToMaxVelocity.setter
    def timeToMaxVelocity(self, value: float):
        """Set timeToMaxVelocity"""
        self.__timeToMaxVelocity = float(value)

    @property
    def lineRelease(self) -> bool:
        """Line release when no more line on winch (Dynamic analysis)"""
        return self.__lineRelease

    @lineRelease.setter
    def lineRelease(self, value: bool):
        """Set lineRelease"""
        self.__lineRelease = bool(value)

    @property
    def radius(self) -> float:
        """Radius of winch"""
        return self.__radius

    @radius.setter
    def radius(self, value: float):
        """Set radius"""
        self.__radius = float(value)

    @property
    def winchCenter(self) -> CenterOfWinch:
        """Center of winch in positive or negative local Z-axis"""
        return self.__winchCenter

    @winchCenter.setter
    def winchCenter(self, value: CenterOfWinch):
        """Set winchCenter"""
        self.__winchCenter = value

    @property
    def lengthJustification(self) -> bool:
        """Control parameter for adjusting the length of elements attached to winch"""
        return self.__lengthJustification

    @lengthJustification.setter
    def lengthJustification(self, value: bool):
        """Set lengthJustification"""
        self.__lengthJustification = bool(value)
