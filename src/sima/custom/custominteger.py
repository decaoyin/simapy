# This an autogenerated file
# 
# Generated with CustomInteger
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.custominteger import CustomIntegerBlueprint
from typing import Dict
from sima.custom.parameterfield import ParameterField
from sima.sima.named import Named
from sima.sima.scriptablevalue import ScriptableValue

class CustomInteger(ParameterField,Named):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    label : str
         (default "")
    tooltip : str
         (default "")
    value : int
         (default 0)
    constraints : str
         Give a valid range for a number: Use <,> for excluding and [] for including.\nExampless: \n- [0,4] Number from and including 0 to and including 4\n- <0,4> From and to, excluding \n- <,0> All negative numbers excluding 0\n- [0,> All positive numbers, including 0\n(default "")
    """

    def __init__(self , _id="", name="", label="", tooltip="", value=0, constraints="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.label = label
        self.tooltip = tooltip
        self.value = value
        self.constraints = constraints
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CustomIntegerBlueprint()


    @property
    def _id(self) -> str:
        """"""
        return self.___id

    @_id.setter
    def _id(self, value: str):
        """Set _id"""
        self.___id = str(value)

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
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def tooltip(self) -> str:
        """"""
        return self.__tooltip

    @tooltip.setter
    def tooltip(self, value: str):
        """Set tooltip"""
        self.__tooltip = str(value)

    @property
    def value(self) -> int:
        """"""
        return self.__value

    @value.setter
    def value(self, value: int):
        """Set value"""
        self.__value = int(value)

    @property
    def constraints(self) -> str:
        """Give a valid range for a number: Use <,> for excluding and [] for including.
Exampless: 
- [0,4] Number from and including 0 to and including 4
- <0,4> From and to, excluding 
- <,0> All negative numbers excluding 0
- [0,> All positive numbers, including 0
"""
        return self.__constraints

    @constraints.setter
    def constraints(self, value: str):
        """Set constraints"""
        self.__constraints = str(value)
