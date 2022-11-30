# 
# Generated with PipeStressFilterBlueprint
from dmt.blueprint import Blueprint
from dmt.dimension import Dimension
from dmt.attribute import Attribute
from dmt.enum_attribute import EnumAttribute
from dmt.blueprint_attribute import BlueprintAttribute
from .operationnode import OperationNodeBlueprint

class PipeStressFilterBlueprint(OperationNodeBlueprint):
    """"""

    def __init__(self, name="PipeStressFilter", package_path="sima/post", description=""):
        super().__init__(name,package_path,description)
        self.add_attribute(Attribute("description","string","",default=""))
        self.add_attribute(BlueprintAttribute("scriptableValues","sima/sima/ScriptableValue","",True,Dimension("*")))
        self.add_attribute(Attribute("name","string",""))
        self.add_attribute(Attribute("x","integer","",default=0))
        self.add_attribute(Attribute("y","integer","",default=0))
        self.add_attribute(Attribute("h","integer","",default=0))
        self.add_attribute(Attribute("w","integer","",default=0))
        self.add_attribute(BlueprintAttribute("controlSignalInputSlots","sima/post/ControlSignalInputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterInputSlots","sima/post/InputSlot","",True,Dimension("*")))
        self.add_attribute(BlueprintAttribute("filterOutputSlots","sima/post/OutputSlot","",True,Dimension("*")))
        self.add_attribute(Attribute("outerDiameter","number","",default=0.0))
        self.add_attribute(Attribute("pipeThickness","number","",default=0.0))
        self.add_attribute(Attribute("internalPressure","number","",default=0.0))
        self.add_attribute(Attribute("externalPressure","number","",default=0.0))
        self.add_attribute(Attribute("numberOfPoints","integer","",default=8))
        self.add_attribute(EnumAttribute("positionForStressCalculation","sima/post/WallPoint",""))