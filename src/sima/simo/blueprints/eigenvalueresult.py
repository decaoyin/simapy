# 
# Generated with EigenvalueResultBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.moao import MOAOBlueprint

class EigenvalueResultBlueprint(MOAOBlueprint):
    """"""

    def __init__(self, name="EigenvalueResult", package_path="sima/simo", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("bodyResults","sima/simo/BodyEigenvalueResult","",True,Dimension("*")))