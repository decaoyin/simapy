# 
# Generated with ConstraintItemBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class ConstraintItemBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="ConstraintItem", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(Attribute("path","string","",default=""))
        self.attributes.append(EnumAttribute("_type","sima/post/ConstraintType",""))
        self.attributes.append(Attribute("value","number","",default=0.0))