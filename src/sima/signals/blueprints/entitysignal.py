# 
# Generated with EntitySignalBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .signal import SignalBlueprint

class EntitySignalBlueprint(SignalBlueprint):
    """"""

    def __init__(self, name="EntitySignal", package_path="sima/signals", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(Attribute("name","string","",optional=False))
        self.add_attribute(BlueprintAttribute("attributes","sima/signals/Attribute","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("value","system/SIMOS/Entity","",True))