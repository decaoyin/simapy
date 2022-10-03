# This an autogenerated file
# 
# Generated with SIMOTask
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.simotask import SIMOTaskBlueprint
from typing import Dict
from sima.condition.conditiontask import ConditionTask
from sima.condition.conditiontaskcondition import ConditionTaskCondition
from sima.condition.initialcondition import InitialCondition
from sima.condition.modelvariation import ModelVariation
from sima.sima.doublevariable import DoubleVariable
from sima.sima.integervariable import IntegerVariable
from sima.sima.modelreferencevariable import ModelReferenceVariable
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.simascript import SIMAScript
from sima.sima.stringvariable import StringVariable
from sima.simo.massunit import MassUnit
from sima.simo.simomodel import SIMOModel

class SIMOTask(ConditionTask):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    name : str
         (default "")
    doubleVariables : List[DoubleVariable]
    integerVariables : List[IntegerVariable]
    stringVariables : List[StringVariable]
    runNumber : int
         (default 0)
    scripts : List[SIMAScript]
    variations : List[ModelVariation]
    referenceVariables : List[ModelReferenceVariable]
    initialCondition : InitialCondition
    conditions : List[ConditionTaskCondition]
    model : SIMOModel
    simoMemory : int
         Enables override of the default memory settings for SIMO. Given in MB(default 128)
    removeIntermediateFiles : bool
         (default True)
    exportMassUnit : MassUnit
         Used as export unit for mass ( and indirectly force)
    exportAsFMU : bool
         Generate FMU (Functional Mockup Unit) from model(default False)
    """

    def __init__(self , _id="", name="", runNumber=0, simoMemory=128, removeIntermediateFiles=True, exportMassUnit=MassUnit.MG, exportAsFMU=False, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.name = name
        self.doubleVariables = list()
        self.integerVariables = list()
        self.stringVariables = list()
        self.runNumber = runNumber
        self.scripts = list()
        self.variations = list()
        self.referenceVariables = list()
        self.initialCondition = None
        self.conditions = list()
        self.model = None
        self.simoMemory = simoMemory
        self.removeIntermediateFiles = removeIntermediateFiles
        self.exportMassUnit = exportMassUnit
        self.exportAsFMU = exportAsFMU
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return SIMOTaskBlueprint()


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
    def doubleVariables(self) -> List[DoubleVariable]:
        """"""
        return self.__doubleVariables

    @doubleVariables.setter
    def doubleVariables(self, value: List[DoubleVariable]):
        """Set doubleVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__doubleVariables = value

    @property
    def integerVariables(self) -> List[IntegerVariable]:
        """"""
        return self.__integerVariables

    @integerVariables.setter
    def integerVariables(self, value: List[IntegerVariable]):
        """Set integerVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__integerVariables = value

    @property
    def stringVariables(self) -> List[StringVariable]:
        """"""
        return self.__stringVariables

    @stringVariables.setter
    def stringVariables(self, value: List[StringVariable]):
        """Set stringVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__stringVariables = value

    @property
    def runNumber(self) -> int:
        """"""
        return self.__runNumber

    @runNumber.setter
    def runNumber(self, value: int):
        """Set runNumber"""
        self.__runNumber = int(value)

    @property
    def scripts(self) -> List[SIMAScript]:
        """"""
        return self.__scripts

    @scripts.setter
    def scripts(self, value: List[SIMAScript]):
        """Set scripts"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__scripts = value

    @property
    def variations(self) -> List[ModelVariation]:
        """"""
        return self.__variations

    @variations.setter
    def variations(self, value: List[ModelVariation]):
        """Set variations"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__variations = value

    @property
    def referenceVariables(self) -> List[ModelReferenceVariable]:
        """"""
        return self.__referenceVariables

    @referenceVariables.setter
    def referenceVariables(self, value: List[ModelReferenceVariable]):
        """Set referenceVariables"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__referenceVariables = value

    @property
    def initialCondition(self) -> InitialCondition:
        """"""
        return self.__initialCondition

    @initialCondition.setter
    def initialCondition(self, value: InitialCondition):
        """Set initialCondition"""
        self.__initialCondition = value

    @property
    def conditions(self) -> List[ConditionTaskCondition]:
        """"""
        return self.__conditions

    @conditions.setter
    def conditions(self, value: List[ConditionTaskCondition]):
        """Set conditions"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__conditions = value

    @property
    def model(self) -> SIMOModel:
        """"""
        return self.__model

    @model.setter
    def model(self, value: SIMOModel):
        """Set model"""
        self.__model = value

    @property
    def simoMemory(self) -> int:
        """Enables override of the default memory settings for SIMO. Given in MB"""
        return self.__simoMemory

    @simoMemory.setter
    def simoMemory(self, value: int):
        """Set simoMemory"""
        self.__simoMemory = int(value)

    @property
    def removeIntermediateFiles(self) -> bool:
        """"""
        return self.__removeIntermediateFiles

    @removeIntermediateFiles.setter
    def removeIntermediateFiles(self, value: bool):
        """Set removeIntermediateFiles"""
        self.__removeIntermediateFiles = bool(value)

    @property
    def exportMassUnit(self) -> MassUnit:
        """Used as export unit for mass ( and indirectly force)"""
        return self.__exportMassUnit

    @exportMassUnit.setter
    def exportMassUnit(self, value: MassUnit):
        """Set exportMassUnit"""
        self.__exportMassUnit = value

    @property
    def exportAsFMU(self) -> bool:
        """Generate FMU (Functional Mockup Unit) from model"""
        return self.__exportAsFMU

    @exportAsFMU.setter
    def exportAsFMU(self, value: bool):
        """Set exportAsFMU"""
        self.__exportAsFMU = bool(value)
