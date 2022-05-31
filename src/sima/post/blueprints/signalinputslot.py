# 
# Generated with SignalInputSlotBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .inputslot import InputSlotBlueprint
from .signalgeneratorcontainer import SignalGeneratorContainerBlueprint

class SignalInputSlotBlueprint(InputSlotBlueprint,SignalGeneratorContainerBlueprint):
    """"""

    def __init__(self, name="SignalInputSlot", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.attributes.append(Attribute("name","string","",default=""))
        self.attributes.append(Attribute("description","string","",default=""))
        self.attributes.append(Attribute("_id","string","",default=""))
        self.attributes.append(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("properties","sima/post/SignalProperties","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("signals","sima/post/GeneratorSignal","",True,Dimension("*")))
        self.attributes.append(BlueprintAttribute("children","sima/post/SignalGeneratorContainer","",True,Dimension("*")))
        self.attributes.append(Attribute("includeRootFolder","boolean","Will add a root folder to the output",default=False))