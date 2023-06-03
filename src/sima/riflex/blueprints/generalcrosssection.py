# 
# Generated with GeneralCrossSectionBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .crosssection import CrossSectionBlueprint
from .crsaxialfrictionmodel import CRSAxialFrictionModelBlueprint

class GeneralCrossSectionBlueprint(CrossSectionBlueprint,CRSAxialFrictionModelBlueprint):
    """"""

    def __init__(self, name="GeneralCrossSection", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("staticFriction","number","Static friction force corresponding to elongation",default=0.0))
        self.add_attribute(Attribute("staticElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("dynamicFriction","number","Dynamic friction force corresponding to elongation",default=0.0))
        self.add_attribute(Attribute("dynamicElongation","number","Relative elongation",default=0.0))
        self.add_attribute(Attribute("axialFriction","boolean","Local axial friction model",default=False))
        self.add_attribute(Attribute("scfkSpecification","boolean","Scaling of Froude-Krylov term in Morison’s equation in normal direction",default=False))
        self.add_attribute(EnumAttribute("loadFormulation","sima/riflex/LoadFormulation",""))
        self.add_attribute(Attribute("hydrodynamicDiameter","number","Hydrodynamic diameter",default=0.0))
        self.add_attribute(EnumAttribute("hydrodynamicInputCode","sima/riflex/HydrodynamicInputCode","Hydrodynamic input code"))
        self.add_attribute(Attribute("addedMassTanDir","number","Added mass in tangential direction",default=0.0))
        self.add_attribute(Attribute("addedMassNormDir","number","Added mass in normal direction",default=0.0))
        self.add_attribute(Attribute("dampingNormDir","number","Damping coefficients in normal direction",default=0.0))
        self.add_attribute(Attribute("normalDirectionScaling","number","Scaling factor for Froude-Krylov term in Morison’s equation in normal direction",default=1.0))
        self.add_attribute(Attribute("tangentialDirectionScaling","number","Scale for Froude-Krylov term in Morison’s equation in tangential direction",default=1.0))
        self.add_attribute(Attribute("cdx","number","Quadratic drag force coefficient per unit length in tangential direction",default=0.0))
        self.add_attribute(Attribute("cdy","number","Quadratic drag force coefficient per unit length in local y-direction",default=0.0))
        self.add_attribute(Attribute("cdz","number","Quadratic drag force coefficient per unit length local z-direction",default=0.0))
        self.add_attribute(Attribute("amx","number","Added mass per unit length in tangential direction",default=0.0))
        self.add_attribute(Attribute("amy","number","Added mass per unit length in local y-direction",default=0.0))
        self.add_attribute(Attribute("amz","number","Added mass per unit length in local z-direction",default=0.0))
        self.add_attribute(Attribute("addedMass","number","Added mass per unit length for torsional rotation",default=0.0))
        self.add_attribute(Attribute("cdlx","number","Linear drag force coefficient per unit length in tangential direction",default=0.0))
        self.add_attribute(Attribute("cdly","number","Linear drag force coefficient per unit length in local y-direction",default=0.0))
        self.add_attribute(Attribute("cdlz","number","Linear drag force coefficient per unit length in local z-direction",default=0.0))
        self.add_attribute(Attribute("cdt","number","Quadratic drag coefficient in tangential direction.",default=0.0))
        self.add_attribute(Attribute("cdn","number","Quadratic drag coefficient in normal direction.",default=0.0))
        self.add_attribute(Attribute("cdnz","number","Quadratic drag coefficient in normal direction.",default=0.0))
        self.add_attribute(Attribute("massDampingSpecification","boolean","Mass proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("stiffnessDampingSpecification","boolean","Stiffness proportional Rayleigh damping",default=False))
        self.add_attribute(Attribute("axialDampingSpecification","boolean","Local axial damping model",default=False))
        self.add_attribute(BlueprintAttribute("massDamping","sima/riflex/CRSMassDamping","",True))
        self.add_attribute(BlueprintAttribute("stiffnessDamping","sima/riflex/CRSStiffnessDamping","",True))
        self.add_attribute(BlueprintAttribute("axialDamping","sima/riflex/CRSAxialDamping","",True))
        self.add_attribute(Attribute("cdax","number","Quadratic aerodynamic drag force coefficient per unit length in tangential direction",default=0.0))
        self.add_attribute(Attribute("cday","number","Quadratic aerodynamic drag force coefficient per unit length in normal direction",default=0.0))
        self.add_attribute(Attribute("cdaz","number","Quadratic aerodynamic drag force coefficient per unit length in z direction",default=0.0))
        self.add_attribute(EnumAttribute("aerodynamicInputCode","sima/riflex/AerodynamicInputCode","Aerodynamic input code"))
        self.add_attribute(Attribute("aerodynamicDiameter","number","Aerodynamic diameter",default=0.0))
        self.add_attribute(Attribute("temperature","number","Temperature at which the specification applies",default=0.0))
        self.add_attribute(Attribute("pressureDependency","integer","Pressure dependency parameter related to bending moment",default=0))
        self.add_attribute(Attribute("axialStiffness","number","Axial stiffness",default=0.0))
        self.add_attribute(Attribute("tensionCapacity","number","Tension capacity",default=0.0))
        self.add_attribute(Attribute("maxCurvatureY","number","Maximum curvature around local y-axis",default=0.0))
        self.add_attribute(Attribute("maxCurvatureZ","number","Maximum curvature around local z-axis",default=0.0))
        self.add_attribute(BlueprintAttribute("airfoil","sima/windturbine/Airfoil","",False))
        self.add_attribute(Attribute("chordLength","number","",default=0.0))
        self.add_attribute(Attribute("foilOriginY","number","Y-coordinate of foil origin",default=0.0))
        self.add_attribute(Attribute("foilOriginZ","number","Z-coordinate of foil origin",default=0.0))
        self.add_attribute(Attribute("foilInclination","number","Inclination of foil system in the local cross section (strength) system.",default=0.0))
        self.add_attribute(EnumAttribute("aerodynamicForceType","sima/riflex/AerodynamicForceType",""))
        self.add_attribute(Attribute("coupledBendingTorsion","boolean","Geometric stiffness coupling between bending and torsion",default=False))
        self.add_attribute(Attribute("alpha","number","Thermal expansion coefficient",default=0.0))
        self.add_attribute(Attribute("massCenterY","number","Mass center Y-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("massCenterZ","number","Mass center Z-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("buoyancyCenterY","number","Buoyancy center Y-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("buoyancyCenterZ","number","Buoyancy center Z-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("areaCenterY","number","Area center Y-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("areaCenterZ","number","Area center Z-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("principalAxesOrientation","number","Orientation (theta) of principal axes V and W",default=0.0))
        self.add_attribute(Attribute("shearCenterY","number","Shear center Y-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("shearCenterZ","number","Shear center Z-coordinate in beam element system",default=0.0))
        self.add_attribute(Attribute("massCoefficient","number","Mass / unit length",default=0.0))
        self.add_attribute(Attribute("extCrossSectionalArea","number","External cross-sectional area",default=0.0))
        self.add_attribute(Attribute("intCrossSectionalArea","number","Internal cross-sectional area",default=0.0))
        self.add_attribute(Attribute("gyrationRadius","number","Radius of gyration about local x-axis",default=0.0))
        self.add_attribute(Attribute("torsionStiffness","number","Torsion stiffness",default=0.0))
        self.add_attribute(Attribute("bendingStiffnessV","number","Bending stiffness around principal V-axis",default=0.0))
        self.add_attribute(Attribute("bendingStiffnessW","number","Bending stiffness around principal W-axis",default=0.0))
        self.add_attribute(Attribute("shearStiffnessW","number","Shear stiffness in principal W-direction. Infinite shear stiffness if equal to zero",default=0.0))
        self.add_attribute(Attribute("shearStiffnessV","number","Shear stiffness in principal V-direction. Infinite shear stiffness if equal to zero",default=0.0))