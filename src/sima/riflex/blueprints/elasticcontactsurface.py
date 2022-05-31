# 
# Generated with ElasticContactSurfaceBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from sima.sima.blueprints.namedobject import NamedObjectBlueprint

class ElasticContactSurfaceBlueprint(NamedObjectBlueprint):
    """"""

    def __init__(self, name="ElasticContactSurface", package_path="sima/riflex", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("points","sima/riflex/ContactSurfacePoint","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("lines","sima/riflex/ContactSurfaceLine","",True,Dimension("*")))