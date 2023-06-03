# This an autogenerated file
# 
# Generated with SuperNode
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.supernode import SuperNodeBlueprint
from typing import Dict
from .boundarycondition import BoundaryCondition
from .boundaryconditionframe import BoundaryConditionFrame
from .nodeconstraint import NodeConstraint
from sima.sima import NamedObject
from sima.sima import ScriptableValue
from sima.simo import SuperNodeReference
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .referenceframe import ReferenceFrame
    from .supportvessel import SupportVessel
    from sima.simo import SuperNodeReference
    from .arline import ARLine

class SuperNode(NamedObject,SuperNodeReference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default None)
    constraint : NodeConstraint
         Supernode type.
    referenceFrame : ReferenceFrame
         Reference frame for local coordinates.
    supportVessel : SupportVessel
         Support body reference.
    automaticInitialPosition : bool
         Initial position calculated using stress free reference line length, stress free coordinate of the other super node and static coordinates of both super nodes.(default False)
    masterNode : SuperNodeReference
         Master node for Slaved / Fixed Relative Orientation nodes.
    xConstraint : BoundaryCondition
         Boundary condition for translation in X-direction.
    yConstraint : BoundaryCondition
         Boundary condition for translation in Y-direction.
    zConstraint : BoundaryCondition
         Boundary condition for translation in Z-direction.
    rxConstraint : BoundaryCondition
         Boundary condition for rotation about X-axis
    ryConstraint : BoundaryCondition
         Boundary condition for rotation about Y-axis
    rzConstraint : BoundaryCondition
         Boundary condition for rotation about Z-axis
    xInitial : float
         Initial (stress-free) local coordinate X(default 0.0)
    yInitial : float
         Initial (stress-free) local coordinate Y(default 0.0)
    zInitial : float
         Initial (stress-free) local coordinate Z(default 0.0)
    xStatic : float
         Static local coordinate X(default 0.0)
    yStatic : float
         Static local coordinate Y(default 0.0)
    zStatic : float
         Static local coordinate Z(default 0.0)
    rotation : float
         Specified rotation of supernode from stress free position \nto static equilibrium position.(default 0.0)
    direction : float
         Direction of axis for specified rotation.(default 0.0)
    referenceLine : ARLine
         Used for automatic calculation of initial super node position
    beta : float
         Direction to horisontal if set. Rotation is about 'local y-axis' i.e. positive downwards.(default 0.0)
    radial : bool
         Used to define the supernode position relative to \nthe x axis spanned by the reference supernodes(default False)
    radialReference1 : SuperNode
         Master node for Slaved / Fixed Relative Orientation nodes.
    radialReference2 : SuperNode
         Master node for Slaved / Fixed Relative Orientation nodes.
    radialAngle : float
         (default 0.0)
    verticalOffset : float
         (default 0.0)
    radialDistance : float
         (default 0.0)
    boundaryConditionFrame : BoundaryConditionFrame
         Boundary condition reference co-ordinate system
    xx : float
         Skew x-axis x-component in reference system(default 0.0)
    xy : float
         Skew x-axis y-component in reference system(default 0.0)
    xz : float
         Skew x-axis z-component in reference system(default 0.0)
    xp : float
         XY-plane reference vector x-component  in reference system(default 0.0)
    yp : float
         XY-plane reference vector y-component  in reference system(default 0.0)
    zp : float
         XY-plane reference vector z-component  in reference system(default 0.0)
    """

    def __init__(self , description="", constraint=NodeConstraint.FIXED_PRESCRIBED, automaticInitialPosition=False, xConstraint=BoundaryCondition.FREE, yConstraint=BoundaryCondition.FREE, zConstraint=BoundaryCondition.FREE, rxConstraint=BoundaryCondition.FREE, ryConstraint=BoundaryCondition.FREE, rzConstraint=BoundaryCondition.FREE, xInitial=0.0, yInitial=0.0, zInitial=0.0, xStatic=0.0, yStatic=0.0, zStatic=0.0, rotation=0.0, direction=0.0, beta=0.0, radial=False, radialAngle=0.0, verticalOffset=0.0, radialDistance=0.0, boundaryConditionFrame=BoundaryConditionFrame.GLOBAL, xx=0.0, xy=0.0, xz=0.0, xp=0.0, yp=0.0, zp=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.name = None
        self.constraint = constraint
        self.referenceFrame = None
        self.supportVessel = None
        self.automaticInitialPosition = automaticInitialPosition
        self.masterNode = None
        self.xConstraint = xConstraint
        self.yConstraint = yConstraint
        self.zConstraint = zConstraint
        self.rxConstraint = rxConstraint
        self.ryConstraint = ryConstraint
        self.rzConstraint = rzConstraint
        self.xInitial = xInitial
        self.yInitial = yInitial
        self.zInitial = zInitial
        self.xStatic = xStatic
        self.yStatic = yStatic
        self.zStatic = zStatic
        self.rotation = rotation
        self.direction = direction
        self.referenceLine = None
        self.beta = beta
        self.radial = radial
        self.radialReference1 = None
        self.radialReference2 = None
        self.radialAngle = radialAngle
        self.verticalOffset = verticalOffset
        self.radialDistance = radialDistance
        self.boundaryConditionFrame = boundaryConditionFrame
        self.xx = xx
        self.xy = xy
        self.xz = xz
        self.xp = xp
        self.yp = yp
        self.zp = zp
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SuperNodeBlueprint()


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
    def constraint(self) -> NodeConstraint:
        """Supernode type."""
        return self.__constraint

    @constraint.setter
    def constraint(self, value: NodeConstraint):
        """Set constraint"""
        self.__constraint = value

    @property
    def referenceFrame(self) -> ReferenceFrame:
        """Reference frame for local coordinates."""
        return self.__referenceFrame

    @referenceFrame.setter
    def referenceFrame(self, value: ReferenceFrame):
        """Set referenceFrame"""
        self.__referenceFrame = value

    @property
    def supportVessel(self) -> SupportVessel:
        """Support body reference."""
        return self.__supportVessel

    @supportVessel.setter
    def supportVessel(self, value: SupportVessel):
        """Set supportVessel"""
        self.__supportVessel = value

    @property
    def automaticInitialPosition(self) -> bool:
        """Initial position calculated using stress free reference line length, stress free coordinate of the other super node and static coordinates of both super nodes."""
        return self.__automaticInitialPosition

    @automaticInitialPosition.setter
    def automaticInitialPosition(self, value: bool):
        """Set automaticInitialPosition"""
        self.__automaticInitialPosition = bool(value)

    @property
    def masterNode(self) -> SuperNodeReference:
        """Master node for Slaved / Fixed Relative Orientation nodes."""
        return self.__masterNode

    @masterNode.setter
    def masterNode(self, value: SuperNodeReference):
        """Set masterNode"""
        self.__masterNode = value

    @property
    def xConstraint(self) -> BoundaryCondition:
        """Boundary condition for translation in X-direction."""
        return self.__xConstraint

    @xConstraint.setter
    def xConstraint(self, value: BoundaryCondition):
        """Set xConstraint"""
        self.__xConstraint = value

    @property
    def yConstraint(self) -> BoundaryCondition:
        """Boundary condition for translation in Y-direction."""
        return self.__yConstraint

    @yConstraint.setter
    def yConstraint(self, value: BoundaryCondition):
        """Set yConstraint"""
        self.__yConstraint = value

    @property
    def zConstraint(self) -> BoundaryCondition:
        """Boundary condition for translation in Z-direction."""
        return self.__zConstraint

    @zConstraint.setter
    def zConstraint(self, value: BoundaryCondition):
        """Set zConstraint"""
        self.__zConstraint = value

    @property
    def rxConstraint(self) -> BoundaryCondition:
        """Boundary condition for rotation about X-axis"""
        return self.__rxConstraint

    @rxConstraint.setter
    def rxConstraint(self, value: BoundaryCondition):
        """Set rxConstraint"""
        self.__rxConstraint = value

    @property
    def ryConstraint(self) -> BoundaryCondition:
        """Boundary condition for rotation about Y-axis"""
        return self.__ryConstraint

    @ryConstraint.setter
    def ryConstraint(self, value: BoundaryCondition):
        """Set ryConstraint"""
        self.__ryConstraint = value

    @property
    def rzConstraint(self) -> BoundaryCondition:
        """Boundary condition for rotation about Z-axis"""
        return self.__rzConstraint

    @rzConstraint.setter
    def rzConstraint(self, value: BoundaryCondition):
        """Set rzConstraint"""
        self.__rzConstraint = value

    @property
    def xInitial(self) -> float:
        """Initial (stress-free) local coordinate X"""
        return self.__xInitial

    @xInitial.setter
    def xInitial(self, value: float):
        """Set xInitial"""
        self.__xInitial = float(value)

    @property
    def yInitial(self) -> float:
        """Initial (stress-free) local coordinate Y"""
        return self.__yInitial

    @yInitial.setter
    def yInitial(self, value: float):
        """Set yInitial"""
        self.__yInitial = float(value)

    @property
    def zInitial(self) -> float:
        """Initial (stress-free) local coordinate Z"""
        return self.__zInitial

    @zInitial.setter
    def zInitial(self, value: float):
        """Set zInitial"""
        self.__zInitial = float(value)

    @property
    def xStatic(self) -> float:
        """Static local coordinate X"""
        return self.__xStatic

    @xStatic.setter
    def xStatic(self, value: float):
        """Set xStatic"""
        self.__xStatic = float(value)

    @property
    def yStatic(self) -> float:
        """Static local coordinate Y"""
        return self.__yStatic

    @yStatic.setter
    def yStatic(self, value: float):
        """Set yStatic"""
        self.__yStatic = float(value)

    @property
    def zStatic(self) -> float:
        """Static local coordinate Z"""
        return self.__zStatic

    @zStatic.setter
    def zStatic(self, value: float):
        """Set zStatic"""
        self.__zStatic = float(value)

    @property
    def rotation(self) -> float:
        """Specified rotation of supernode from stress free position 
to static equilibrium position."""
        return self.__rotation

    @rotation.setter
    def rotation(self, value: float):
        """Set rotation"""
        self.__rotation = float(value)

    @property
    def direction(self) -> float:
        """Direction of axis for specified rotation."""
        return self.__direction

    @direction.setter
    def direction(self, value: float):
        """Set direction"""
        self.__direction = float(value)

    @property
    def referenceLine(self) -> ARLine:
        """Used for automatic calculation of initial super node position"""
        return self.__referenceLine

    @referenceLine.setter
    def referenceLine(self, value: ARLine):
        """Set referenceLine"""
        self.__referenceLine = value

    @property
    def beta(self) -> float:
        """Direction to horisontal if set. Rotation is about 'local y-axis' i.e. positive downwards."""
        return self.__beta

    @beta.setter
    def beta(self, value: float):
        """Set beta"""
        self.__beta = float(value)

    @property
    def radial(self) -> bool:
        """Used to define the supernode position relative to 
the x axis spanned by the reference supernodes"""
        return self.__radial

    @radial.setter
    def radial(self, value: bool):
        """Set radial"""
        self.__radial = bool(value)

    @property
    def radialReference1(self) -> SuperNode:
        """Master node for Slaved / Fixed Relative Orientation nodes."""
        return self.__radialReference1

    @radialReference1.setter
    def radialReference1(self, value: SuperNode):
        """Set radialReference1"""
        self.__radialReference1 = value

    @property
    def radialReference2(self) -> SuperNode:
        """Master node for Slaved / Fixed Relative Orientation nodes."""
        return self.__radialReference2

    @radialReference2.setter
    def radialReference2(self, value: SuperNode):
        """Set radialReference2"""
        self.__radialReference2 = value

    @property
    def radialAngle(self) -> float:
        """"""
        return self.__radialAngle

    @radialAngle.setter
    def radialAngle(self, value: float):
        """Set radialAngle"""
        self.__radialAngle = float(value)

    @property
    def verticalOffset(self) -> float:
        """"""
        return self.__verticalOffset

    @verticalOffset.setter
    def verticalOffset(self, value: float):
        """Set verticalOffset"""
        self.__verticalOffset = float(value)

    @property
    def radialDistance(self) -> float:
        """"""
        return self.__radialDistance

    @radialDistance.setter
    def radialDistance(self, value: float):
        """Set radialDistance"""
        self.__radialDistance = float(value)

    @property
    def boundaryConditionFrame(self) -> BoundaryConditionFrame:
        """Boundary condition reference co-ordinate system"""
        return self.__boundaryConditionFrame

    @boundaryConditionFrame.setter
    def boundaryConditionFrame(self, value: BoundaryConditionFrame):
        """Set boundaryConditionFrame"""
        self.__boundaryConditionFrame = value

    @property
    def xx(self) -> float:
        """Skew x-axis x-component in reference system"""
        return self.__xx

    @xx.setter
    def xx(self, value: float):
        """Set xx"""
        self.__xx = float(value)

    @property
    def xy(self) -> float:
        """Skew x-axis y-component in reference system"""
        return self.__xy

    @xy.setter
    def xy(self, value: float):
        """Set xy"""
        self.__xy = float(value)

    @property
    def xz(self) -> float:
        """Skew x-axis z-component in reference system"""
        return self.__xz

    @xz.setter
    def xz(self, value: float):
        """Set xz"""
        self.__xz = float(value)

    @property
    def xp(self) -> float:
        """XY-plane reference vector x-component  in reference system"""
        return self.__xp

    @xp.setter
    def xp(self, value: float):
        """Set xp"""
        self.__xp = float(value)

    @property
    def yp(self) -> float:
        """XY-plane reference vector y-component  in reference system"""
        return self.__yp

    @yp.setter
    def yp(self, value: float):
        """Set yp"""
        self.__yp = float(value)

    @property
    def zp(self) -> float:
        """XY-plane reference vector z-component  in reference system"""
        return self.__zp

    @zp.setter
    def zp(self, value: float):
        """Set zp"""
        self.__zp = float(value)
