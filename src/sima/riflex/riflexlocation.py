# This an autogenerated file
# 
# Generated with RIFLEXLocation
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.riflexlocation import RIFLEXLocationBlueprint
from typing import Dict
from sima.environment.seasurface import SeaSurface
from sima.riflex.regular3dbottom import Regular3DBottom
from sima.sima.flatbottom import FlatBottom
from sima.sima.infrastructurebody import InfrastructureBody
from sima.sima.initialviewpoint import InitialViewpoint
from sima.sima.namedviewpoint import NamedViewpoint
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.commonlocation import CommonLocation
from sima.simo.physicalconstants import PhysicalConstants

class RIFLEXLocation(CommonLocation):
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
    initialViewpoint : InitialViewpoint
    initialRotationpoint : Point3
    viewpoints : List[NamedViewpoint]
    relativeCompassAngle : float
         Relative angle between analysis x-axis and north direction in anti-clockwise direction(default 0.0)
    utmX : float
         Offset of local coordinate system origin (X) relative to UTM (Easting).(default 0.0)
    utmY : float
         Offset of local coordinate system origin (Y) relative to UTM (Northing).(default 0.0)
    gridZone : str
         Zone consists of a number from [01-60] and a letter from [C-Z], or just one of [A,B,Y,Z] if on the antarctic or arctic pole.(default "")
    infrastructureBodies : List[InfrastructureBody]
    waterDepth : float
         Water depth for kinematics(default 1000.0)
    seaSurface : SeaSurface
    flatBottom : FlatBottom
    physicalConstants : PhysicalConstants
    regular3DBottom : Regular3DBottom
    """

    def __init__(self , name="", description="", _id="", relativeCompassAngle=0.0, utmX=0.0, utmY=0.0, gridZone="", waterDepth=1000.0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.initialViewpoint = None
        self.initialRotationpoint = None
        self.viewpoints = list()
        self.relativeCompassAngle = relativeCompassAngle
        self.utmX = utmX
        self.utmY = utmY
        self.gridZone = gridZone
        self.infrastructureBodies = list()
        self.waterDepth = waterDepth
        self.seaSurface = None
        self.flatBottom = None
        self.physicalConstants = None
        self.regular3DBottom = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return RIFLEXLocationBlueprint()


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
    def initialViewpoint(self) -> InitialViewpoint:
        """"""
        return self.__initialViewpoint

    @initialViewpoint.setter
    def initialViewpoint(self, value: InitialViewpoint):
        """Set initialViewpoint"""
        self.__initialViewpoint = value

    @property
    def initialRotationpoint(self) -> Point3:
        """"""
        return self.__initialRotationpoint

    @initialRotationpoint.setter
    def initialRotationpoint(self, value: Point3):
        """Set initialRotationpoint"""
        self.__initialRotationpoint = value

    @property
    def viewpoints(self) -> List[NamedViewpoint]:
        """"""
        return self.__viewpoints

    @viewpoints.setter
    def viewpoints(self, value: List[NamedViewpoint]):
        """Set viewpoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__viewpoints = value

    @property
    def relativeCompassAngle(self) -> float:
        """Relative angle between analysis x-axis and north direction in anti-clockwise direction"""
        return self.__relativeCompassAngle

    @relativeCompassAngle.setter
    def relativeCompassAngle(self, value: float):
        """Set relativeCompassAngle"""
        self.__relativeCompassAngle = float(value)

    @property
    def utmX(self) -> float:
        """Offset of local coordinate system origin (X) relative to UTM (Easting)."""
        return self.__utmX

    @utmX.setter
    def utmX(self, value: float):
        """Set utmX"""
        self.__utmX = float(value)

    @property
    def utmY(self) -> float:
        """Offset of local coordinate system origin (Y) relative to UTM (Northing)."""
        return self.__utmY

    @utmY.setter
    def utmY(self, value: float):
        """Set utmY"""
        self.__utmY = float(value)

    @property
    def gridZone(self) -> str:
        """Zone consists of a number from [01-60] and a letter from [C-Z], or just one of [A,B,Y,Z] if on the antarctic or arctic pole."""
        return self.__gridZone

    @gridZone.setter
    def gridZone(self, value: str):
        """Set gridZone"""
        self.__gridZone = str(value)

    @property
    def infrastructureBodies(self) -> List[InfrastructureBody]:
        """"""
        return self.__infrastructureBodies

    @infrastructureBodies.setter
    def infrastructureBodies(self, value: List[InfrastructureBody]):
        """Set infrastructureBodies"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__infrastructureBodies = value

    @property
    def waterDepth(self) -> float:
        """Water depth for kinematics"""
        return self.__waterDepth

    @waterDepth.setter
    def waterDepth(self, value: float):
        """Set waterDepth"""
        self.__waterDepth = float(value)

    @property
    def seaSurface(self) -> SeaSurface:
        """"""
        return self.__seaSurface

    @seaSurface.setter
    def seaSurface(self, value: SeaSurface):
        """Set seaSurface"""
        self.__seaSurface = value

    @property
    def flatBottom(self) -> FlatBottom:
        """"""
        return self.__flatBottom

    @flatBottom.setter
    def flatBottom(self, value: FlatBottom):
        """Set flatBottom"""
        self.__flatBottom = value

    @property
    def physicalConstants(self) -> PhysicalConstants:
        """"""
        return self.__physicalConstants

    @physicalConstants.setter
    def physicalConstants(self, value: PhysicalConstants):
        """Set physicalConstants"""
        self.__physicalConstants = value

    @property
    def regular3DBottom(self) -> Regular3DBottom:
        """"""
        return self.__regular3DBottom

    @regular3DBottom.setter
    def regular3DBottom(self, value: Regular3DBottom):
        """Set regular3DBottom"""
        self.__regular3DBottom = value
