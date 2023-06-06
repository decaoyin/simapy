# 
# Generated with DiffractedWaveVelocityBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from ...sima.blueprints.moao import MOAOBlueprint

class DiffractedWaveVelocityBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="DiffractedWaveVelocity", package_path="sima/hydro", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("directions","number","",Dimension("*"),default=0.0))
        self.add_attribute(Attribute("frequencies","number","",Dimension("*"),default=0.0))
        self.add_attribute(BlueprintAttribute("u","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("v","sima/hydro/DirectionDependentComplexValues","",True))
        self.add_attribute(BlueprintAttribute("w","sima/hydro/DirectionDependentComplexValues","",True))