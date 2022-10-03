# 
# Generated with ThrusterForbiddenZoneBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ThrusterForbiddenZoneBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ThrusterForbiddenZone", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("zoneStart","number","Start of forbidden zone of thrust force",default=0.0))
        self.attributes.append(Attribute("zoneEnd","number","End of forbidden zone of thrust force",default=0.0))