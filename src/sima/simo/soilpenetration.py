# This an autogenerated file
# 
# Generated with SoilPenetration
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.soilpenetration import SoilPenetrationBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.simo.hla import HLA
from sima.simo.soilcapacityelement import SoilCapacityElement
from sima.simo.soilfriction import SoilFriction
from sima.simo.soilfrictionelement import SoilFrictionElement

class SoilPenetration(MOAO):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    frictionModel : SoilFriction
         Soil force control parameter
    zcont : float
         Vertical coordinate of the lifted structure giving first\ncontact with the soil (landing)(default 0.0)
    penetrationDepth : float
         Depth at full penetration from first contact (positive upwards)(default 0.0)
    barArea : float
         Soil buoyancy cross section area(default 0.0)
    sodens : float
         Soil mass density(default 0.0)
    cArea : float
         Section area of cavity(default 0.0)
    seabedImport : HLA
         Import of seabead depth values from HLA Depth value replaces ZCONT
    frictionElements : List[SoilFrictionElement]
    capacityElements : List[SoilCapacityElement]
    wstiff : float
         Stiffness due to compressibility of water inside the cavity(default 0.0)
    tsuct : float
         Time for starting suction pumps(default 0.0)
    cflow : float
         Flow coefficient in/out of closed compartment(default 0.0)
    """

    def __init__(self , description="", frictionModel=SoilFriction.OPEN_COMPARTMENT, zcont=0.0, penetrationDepth=0.0, barArea=0.0, sodens=0.0, cArea=0.0, seabedImport=HLA.NO_IMPORT, wstiff=0.0, tsuct=0.0, cflow=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.frictionModel = frictionModel
        self.zcont = zcont
        self.penetrationDepth = penetrationDepth
        self.barArea = barArea
        self.sodens = sodens
        self.cArea = cArea
        self.seabedImport = seabedImport
        self.frictionElements = list()
        self.capacityElements = list()
        self.wstiff = wstiff
        self.tsuct = tsuct
        self.cflow = cflow
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SoilPenetrationBlueprint()


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
            raise Exception("Expected sequense, but was " , type(value))
        self.__scriptableValues = value

    @property
    def frictionModel(self) -> SoilFriction:
        """Soil force control parameter"""
        return self.__frictionModel

    @frictionModel.setter
    def frictionModel(self, value: SoilFriction):
        """Set frictionModel"""
        self.__frictionModel = value

    @property
    def zcont(self) -> float:
        """Vertical coordinate of the lifted structure giving first
contact with the soil (landing)"""
        return self.__zcont

    @zcont.setter
    def zcont(self, value: float):
        """Set zcont"""
        self.__zcont = float(value)

    @property
    def penetrationDepth(self) -> float:
        """Depth at full penetration from first contact (positive upwards)"""
        return self.__penetrationDepth

    @penetrationDepth.setter
    def penetrationDepth(self, value: float):
        """Set penetrationDepth"""
        self.__penetrationDepth = float(value)

    @property
    def barArea(self) -> float:
        """Soil buoyancy cross section area"""
        return self.__barArea

    @barArea.setter
    def barArea(self, value: float):
        """Set barArea"""
        self.__barArea = float(value)

    @property
    def sodens(self) -> float:
        """Soil mass density"""
        return self.__sodens

    @sodens.setter
    def sodens(self, value: float):
        """Set sodens"""
        self.__sodens = float(value)

    @property
    def cArea(self) -> float:
        """Section area of cavity"""
        return self.__cArea

    @cArea.setter
    def cArea(self, value: float):
        """Set cArea"""
        self.__cArea = float(value)

    @property
    def seabedImport(self) -> HLA:
        """Import of seabead depth values from HLA Depth value replaces ZCONT"""
        return self.__seabedImport

    @seabedImport.setter
    def seabedImport(self, value: HLA):
        """Set seabedImport"""
        self.__seabedImport = value

    @property
    def frictionElements(self) -> List[SoilFrictionElement]:
        """"""
        return self.__frictionElements

    @frictionElements.setter
    def frictionElements(self, value: List[SoilFrictionElement]):
        """Set frictionElements"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__frictionElements = value

    @property
    def capacityElements(self) -> List[SoilCapacityElement]:
        """"""
        return self.__capacityElements

    @capacityElements.setter
    def capacityElements(self, value: List[SoilCapacityElement]):
        """Set capacityElements"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__capacityElements = value

    @property
    def wstiff(self) -> float:
        """Stiffness due to compressibility of water inside the cavity"""
        return self.__wstiff

    @wstiff.setter
    def wstiff(self, value: float):
        """Set wstiff"""
        self.__wstiff = float(value)

    @property
    def tsuct(self) -> float:
        """Time for starting suction pumps"""
        return self.__tsuct

    @tsuct.setter
    def tsuct(self, value: float):
        """Set tsuct"""
        self.__tsuct = float(value)

    @property
    def cflow(self) -> float:
        """Flow coefficient in/out of closed compartment"""
        return self.__cflow

    @cflow.setter
    def cflow(self, value: float):
        """Set cflow"""
        self.__cflow = float(value)
