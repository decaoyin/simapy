# This an autogenerated file
# 
# Generated with WamitCalculationParameters
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.wamitcalculationparameters import WamitCalculationParametersBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.point3 import Point3
from sima.sima.scriptablevalue import ScriptableValue
from sima.wamit.calculateexcitingforcesoption import CalculateExcitingForcesOption
from sima.wamit.calculatemeanforceandmomentintegrationoption import CalculateMeanForceAndMomentIntegrationOption
from sima.wamit.calculateresponseamplitudeoperatoroption import CalculateResponseAmplitudeOperatorOption
from sima.wamit.diffractionpotentailoption import DiffractionPotentailOption
from sima.wamit.geometryorderoption import GeometryOrderOption
from sima.wamit.linearsystemsolvingmethod import LinearSystemSolvingMethod
from sima.wamit.pointfield import PointField
from sima.wamit.potenproblemoption import PotenProblemOption
from sima.wamit.yesnooption import YesNoOption

class WamitCalculationParameters(MOAO):
    """
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    solveRadiationProblem : YesNoOption
         IRAD
    solveDiffractionProblem : PotenProblemOption
         IDIFF
    calculateAddedMassAndDampingCoefficients : YesNoOption
         Corresponds to IOPTN(1)
    calculateExcitingForcesFromHaskindRelations : CalculateExcitingForcesOption
         Corresponds to IOPTN(2)
    calculateExcitingForcesFromDiffractionPotential : CalculateExcitingForcesOption
         Corresponds to IOPTN(3)
    calculateResponseAmplitudeOperator : CalculateResponseAmplitudeOperatorOption
         Corresponds to IOPTN(4)
    useMomentumIntegration : CalculateMeanForceAndMomentIntegrationOption
         Corresponds to IOPTN(8)
    usePressureIntegration : CalculateMeanForceAndMomentIntegrationOption
         Corresponds to IOPTN(9)
    pointField : List[PointField]
    useControlSurfaceIntegration : CalculateMeanForceAndMomentIntegrationOption
         Corresponds to IOPTN(7)
    methodForSolvingLinearSystems : LinearSystemSolvingMethod
         ISOLVE
    numberOfBlocksInBlockIterativeSolver : int
         (default 2)
    geometryMethod : GeometryOrderOption
         ILOWHI
    integrateLogarithmicSingularitySeparately : YesNoOption
         ILOG
    panelSize : float
         (default 10.0)
    evaluateSourceStrength : YesNoOption
         ISOR
    calculationOfDiffractionPotential : DiffractionPotentailOption
         ISCATT
    fieldPoints : List[Point3]
    useInfiniteWaterDepth : bool
         HBOT(default True)
    maximumNumberOfIterations : int
         The maximum number of iterations when using an iterative solver(default 35)
    maxNumOfIterationsAdaptiveIntegrationMomentum : int
         (default 8)
    generateReport : bool
         (default False)
    briefOverviewOfTheory : bool
         (default False)
    taskDescription : bool
         (default False)
    wavePeriodsAndHeadings : bool
         (default False)
    calculationParameters : bool
         (default False)
    hydrostaticResults : bool
         (default False)
    structuralMass : bool
         (default False)
    externalStiffnessMatrix : bool
         (default False)
    linearDampingMatrix : bool
         (default False)
    firstOrderMotionTransferFunction : bool
         (default False)
    firstOrderWaveForceTransferFunctionDiffraction : bool
         (default False)
    firstOrderWaveForceTransferFunctionHaskind : bool
         (default False)
    addedMassZeroFrequency : bool
         (default False)
    addedMassInfiniteFrequency : bool
         (default False)
    frequencyDependentAddedMass : bool
         (default False)
    frequencyDependentDamping : bool
         (default False)
    diffractedWaveField : bool
         (default False)
    waveDriftForcePressure : bool
         (default False)
    waveDriftForceMomentum : bool
         (default False)
    waveDriftForceControlSurfaceIntegration : bool
         (default False)
    runPotenOnceInConditionSetsAndSpaces : bool
         This will make WAMIT run POTEN for one condition only, and copy that result and only run FORCE on the the rest of the conditions.(default False)
    ignoreExitCode : bool
         Ignore process exit code. Be careful to check the result when checked(default False)
    """

    def __init__(self , name="", description="", _id="", solveRadiationProblem=YesNoOption.YES, solveDiffractionProblem=PotenProblemOption.YESFORALL, calculateAddedMassAndDampingCoefficients=YesNoOption.YES, calculateExcitingForcesFromHaskindRelations=CalculateExcitingForcesOption.NO, calculateExcitingForcesFromDiffractionPotential=CalculateExcitingForcesOption.YES, calculateResponseAmplitudeOperator=CalculateResponseAmplitudeOperatorOption.YESDIFFRACTION, useMomentumIntegration=CalculateMeanForceAndMomentIntegrationOption.YESUNIDIRECTIONAL, usePressureIntegration=CalculateMeanForceAndMomentIntegrationOption.NO, useControlSurfaceIntegration=CalculateMeanForceAndMomentIntegrationOption.NO, methodForSolvingLinearSystems=LinearSystemSolvingMethod.ITERATIVE, numberOfBlocksInBlockIterativeSolver=2, geometryMethod=GeometryOrderOption.LOW, integrateLogarithmicSingularitySeparately=YesNoOption.NO, panelSize=10.0, evaluateSourceStrength=YesNoOption.NO, calculationOfDiffractionPotential=DiffractionPotentailOption.DIFFRACTION, useInfiniteWaterDepth=True, maximumNumberOfIterations=35, maxNumOfIterationsAdaptiveIntegrationMomentum=8, generateReport=False, briefOverviewOfTheory=False, taskDescription=False, wavePeriodsAndHeadings=False, calculationParameters=False, hydrostaticResults=False, structuralMass=False, externalStiffnessMatrix=False, linearDampingMatrix=False, firstOrderMotionTransferFunction=False, firstOrderWaveForceTransferFunctionDiffraction=False, firstOrderWaveForceTransferFunctionHaskind=False, addedMassZeroFrequency=False, addedMassInfiniteFrequency=False, frequencyDependentAddedMass=False, frequencyDependentDamping=False, diffractedWaveField=False, waveDriftForcePressure=False, waveDriftForceMomentum=False, waveDriftForceControlSurfaceIntegration=False, runPotenOnceInConditionSetsAndSpaces=False, ignoreExitCode=False, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.solveRadiationProblem = solveRadiationProblem
        self.solveDiffractionProblem = solveDiffractionProblem
        self.calculateAddedMassAndDampingCoefficients = calculateAddedMassAndDampingCoefficients
        self.calculateExcitingForcesFromHaskindRelations = calculateExcitingForcesFromHaskindRelations
        self.calculateExcitingForcesFromDiffractionPotential = calculateExcitingForcesFromDiffractionPotential
        self.calculateResponseAmplitudeOperator = calculateResponseAmplitudeOperator
        self.useMomentumIntegration = useMomentumIntegration
        self.usePressureIntegration = usePressureIntegration
        self.pointField = list()
        self.useControlSurfaceIntegration = useControlSurfaceIntegration
        self.methodForSolvingLinearSystems = methodForSolvingLinearSystems
        self.numberOfBlocksInBlockIterativeSolver = numberOfBlocksInBlockIterativeSolver
        self.geometryMethod = geometryMethod
        self.integrateLogarithmicSingularitySeparately = integrateLogarithmicSingularitySeparately
        self.panelSize = panelSize
        self.evaluateSourceStrength = evaluateSourceStrength
        self.calculationOfDiffractionPotential = calculationOfDiffractionPotential
        self.fieldPoints = list()
        self.useInfiniteWaterDepth = useInfiniteWaterDepth
        self.maximumNumberOfIterations = maximumNumberOfIterations
        self.maxNumOfIterationsAdaptiveIntegrationMomentum = maxNumOfIterationsAdaptiveIntegrationMomentum
        self.generateReport = generateReport
        self.briefOverviewOfTheory = briefOverviewOfTheory
        self.taskDescription = taskDescription
        self.wavePeriodsAndHeadings = wavePeriodsAndHeadings
        self.calculationParameters = calculationParameters
        self.hydrostaticResults = hydrostaticResults
        self.structuralMass = structuralMass
        self.externalStiffnessMatrix = externalStiffnessMatrix
        self.linearDampingMatrix = linearDampingMatrix
        self.firstOrderMotionTransferFunction = firstOrderMotionTransferFunction
        self.firstOrderWaveForceTransferFunctionDiffraction = firstOrderWaveForceTransferFunctionDiffraction
        self.firstOrderWaveForceTransferFunctionHaskind = firstOrderWaveForceTransferFunctionHaskind
        self.addedMassZeroFrequency = addedMassZeroFrequency
        self.addedMassInfiniteFrequency = addedMassInfiniteFrequency
        self.frequencyDependentAddedMass = frequencyDependentAddedMass
        self.frequencyDependentDamping = frequencyDependentDamping
        self.diffractedWaveField = diffractedWaveField
        self.waveDriftForcePressure = waveDriftForcePressure
        self.waveDriftForceMomentum = waveDriftForceMomentum
        self.waveDriftForceControlSurfaceIntegration = waveDriftForceControlSurfaceIntegration
        self.runPotenOnceInConditionSetsAndSpaces = runPotenOnceInConditionSetsAndSpaces
        self.ignoreExitCode = ignoreExitCode
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return WamitCalculationParametersBlueprint()


    @property
    def name(self) -> str:
        """"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Set name"""
        self.__name = str(value)

    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = str(value)

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
    def solveRadiationProblem(self) -> YesNoOption:
        """IRAD"""
        return self.__solveRadiationProblem

    @solveRadiationProblem.setter
    def solveRadiationProblem(self, value: YesNoOption):
        """Set solveRadiationProblem"""
        self.__solveRadiationProblem = value

    @property
    def solveDiffractionProblem(self) -> PotenProblemOption:
        """IDIFF"""
        return self.__solveDiffractionProblem

    @solveDiffractionProblem.setter
    def solveDiffractionProblem(self, value: PotenProblemOption):
        """Set solveDiffractionProblem"""
        self.__solveDiffractionProblem = value

    @property
    def calculateAddedMassAndDampingCoefficients(self) -> YesNoOption:
        """Corresponds to IOPTN(1)"""
        return self.__calculateAddedMassAndDampingCoefficients

    @calculateAddedMassAndDampingCoefficients.setter
    def calculateAddedMassAndDampingCoefficients(self, value: YesNoOption):
        """Set calculateAddedMassAndDampingCoefficients"""
        self.__calculateAddedMassAndDampingCoefficients = value

    @property
    def calculateExcitingForcesFromHaskindRelations(self) -> CalculateExcitingForcesOption:
        """Corresponds to IOPTN(2)"""
        return self.__calculateExcitingForcesFromHaskindRelations

    @calculateExcitingForcesFromHaskindRelations.setter
    def calculateExcitingForcesFromHaskindRelations(self, value: CalculateExcitingForcesOption):
        """Set calculateExcitingForcesFromHaskindRelations"""
        self.__calculateExcitingForcesFromHaskindRelations = value

    @property
    def calculateExcitingForcesFromDiffractionPotential(self) -> CalculateExcitingForcesOption:
        """Corresponds to IOPTN(3)"""
        return self.__calculateExcitingForcesFromDiffractionPotential

    @calculateExcitingForcesFromDiffractionPotential.setter
    def calculateExcitingForcesFromDiffractionPotential(self, value: CalculateExcitingForcesOption):
        """Set calculateExcitingForcesFromDiffractionPotential"""
        self.__calculateExcitingForcesFromDiffractionPotential = value

    @property
    def calculateResponseAmplitudeOperator(self) -> CalculateResponseAmplitudeOperatorOption:
        """Corresponds to IOPTN(4)"""
        return self.__calculateResponseAmplitudeOperator

    @calculateResponseAmplitudeOperator.setter
    def calculateResponseAmplitudeOperator(self, value: CalculateResponseAmplitudeOperatorOption):
        """Set calculateResponseAmplitudeOperator"""
        self.__calculateResponseAmplitudeOperator = value

    @property
    def useMomentumIntegration(self) -> CalculateMeanForceAndMomentIntegrationOption:
        """Corresponds to IOPTN(8)"""
        return self.__useMomentumIntegration

    @useMomentumIntegration.setter
    def useMomentumIntegration(self, value: CalculateMeanForceAndMomentIntegrationOption):
        """Set useMomentumIntegration"""
        self.__useMomentumIntegration = value

    @property
    def usePressureIntegration(self) -> CalculateMeanForceAndMomentIntegrationOption:
        """Corresponds to IOPTN(9)"""
        return self.__usePressureIntegration

    @usePressureIntegration.setter
    def usePressureIntegration(self, value: CalculateMeanForceAndMomentIntegrationOption):
        """Set usePressureIntegration"""
        self.__usePressureIntegration = value

    @property
    def pointField(self) -> List[PointField]:
        """"""
        return self.__pointField

    @pointField.setter
    def pointField(self, value: List[PointField]):
        """Set pointField"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__pointField = value

    @property
    def useControlSurfaceIntegration(self) -> CalculateMeanForceAndMomentIntegrationOption:
        """Corresponds to IOPTN(7)"""
        return self.__useControlSurfaceIntegration

    @useControlSurfaceIntegration.setter
    def useControlSurfaceIntegration(self, value: CalculateMeanForceAndMomentIntegrationOption):
        """Set useControlSurfaceIntegration"""
        self.__useControlSurfaceIntegration = value

    @property
    def methodForSolvingLinearSystems(self) -> LinearSystemSolvingMethod:
        """ISOLVE"""
        return self.__methodForSolvingLinearSystems

    @methodForSolvingLinearSystems.setter
    def methodForSolvingLinearSystems(self, value: LinearSystemSolvingMethod):
        """Set methodForSolvingLinearSystems"""
        self.__methodForSolvingLinearSystems = value

    @property
    def numberOfBlocksInBlockIterativeSolver(self) -> int:
        """"""
        return self.__numberOfBlocksInBlockIterativeSolver

    @numberOfBlocksInBlockIterativeSolver.setter
    def numberOfBlocksInBlockIterativeSolver(self, value: int):
        """Set numberOfBlocksInBlockIterativeSolver"""
        self.__numberOfBlocksInBlockIterativeSolver = int(value)

    @property
    def geometryMethod(self) -> GeometryOrderOption:
        """ILOWHI"""
        return self.__geometryMethod

    @geometryMethod.setter
    def geometryMethod(self, value: GeometryOrderOption):
        """Set geometryMethod"""
        self.__geometryMethod = value

    @property
    def integrateLogarithmicSingularitySeparately(self) -> YesNoOption:
        """ILOG"""
        return self.__integrateLogarithmicSingularitySeparately

    @integrateLogarithmicSingularitySeparately.setter
    def integrateLogarithmicSingularitySeparately(self, value: YesNoOption):
        """Set integrateLogarithmicSingularitySeparately"""
        self.__integrateLogarithmicSingularitySeparately = value

    @property
    def panelSize(self) -> float:
        """"""
        return self.__panelSize

    @panelSize.setter
    def panelSize(self, value: float):
        """Set panelSize"""
        self.__panelSize = float(value)

    @property
    def evaluateSourceStrength(self) -> YesNoOption:
        """ISOR"""
        return self.__evaluateSourceStrength

    @evaluateSourceStrength.setter
    def evaluateSourceStrength(self, value: YesNoOption):
        """Set evaluateSourceStrength"""
        self.__evaluateSourceStrength = value

    @property
    def calculationOfDiffractionPotential(self) -> DiffractionPotentailOption:
        """ISCATT"""
        return self.__calculationOfDiffractionPotential

    @calculationOfDiffractionPotential.setter
    def calculationOfDiffractionPotential(self, value: DiffractionPotentailOption):
        """Set calculationOfDiffractionPotential"""
        self.__calculationOfDiffractionPotential = value

    @property
    def fieldPoints(self) -> List[Point3]:
        """"""
        return self.__fieldPoints

    @fieldPoints.setter
    def fieldPoints(self, value: List[Point3]):
        """Set fieldPoints"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__fieldPoints = value

    @property
    def useInfiniteWaterDepth(self) -> bool:
        """HBOT"""
        return self.__useInfiniteWaterDepth

    @useInfiniteWaterDepth.setter
    def useInfiniteWaterDepth(self, value: bool):
        """Set useInfiniteWaterDepth"""
        self.__useInfiniteWaterDepth = bool(value)

    @property
    def maximumNumberOfIterations(self) -> int:
        """The maximum number of iterations when using an iterative solver"""
        return self.__maximumNumberOfIterations

    @maximumNumberOfIterations.setter
    def maximumNumberOfIterations(self, value: int):
        """Set maximumNumberOfIterations"""
        self.__maximumNumberOfIterations = int(value)

    @property
    def maxNumOfIterationsAdaptiveIntegrationMomentum(self) -> int:
        """"""
        return self.__maxNumOfIterationsAdaptiveIntegrationMomentum

    @maxNumOfIterationsAdaptiveIntegrationMomentum.setter
    def maxNumOfIterationsAdaptiveIntegrationMomentum(self, value: int):
        """Set maxNumOfIterationsAdaptiveIntegrationMomentum"""
        self.__maxNumOfIterationsAdaptiveIntegrationMomentum = int(value)

    @property
    def generateReport(self) -> bool:
        """"""
        return self.__generateReport

    @generateReport.setter
    def generateReport(self, value: bool):
        """Set generateReport"""
        self.__generateReport = bool(value)

    @property
    def briefOverviewOfTheory(self) -> bool:
        """"""
        return self.__briefOverviewOfTheory

    @briefOverviewOfTheory.setter
    def briefOverviewOfTheory(self, value: bool):
        """Set briefOverviewOfTheory"""
        self.__briefOverviewOfTheory = bool(value)

    @property
    def taskDescription(self) -> bool:
        """"""
        return self.__taskDescription

    @taskDescription.setter
    def taskDescription(self, value: bool):
        """Set taskDescription"""
        self.__taskDescription = bool(value)

    @property
    def wavePeriodsAndHeadings(self) -> bool:
        """"""
        return self.__wavePeriodsAndHeadings

    @wavePeriodsAndHeadings.setter
    def wavePeriodsAndHeadings(self, value: bool):
        """Set wavePeriodsAndHeadings"""
        self.__wavePeriodsAndHeadings = bool(value)

    @property
    def calculationParameters(self) -> bool:
        """"""
        return self.__calculationParameters

    @calculationParameters.setter
    def calculationParameters(self, value: bool):
        """Set calculationParameters"""
        self.__calculationParameters = bool(value)

    @property
    def hydrostaticResults(self) -> bool:
        """"""
        return self.__hydrostaticResults

    @hydrostaticResults.setter
    def hydrostaticResults(self, value: bool):
        """Set hydrostaticResults"""
        self.__hydrostaticResults = bool(value)

    @property
    def structuralMass(self) -> bool:
        """"""
        return self.__structuralMass

    @structuralMass.setter
    def structuralMass(self, value: bool):
        """Set structuralMass"""
        self.__structuralMass = bool(value)

    @property
    def externalStiffnessMatrix(self) -> bool:
        """"""
        return self.__externalStiffnessMatrix

    @externalStiffnessMatrix.setter
    def externalStiffnessMatrix(self, value: bool):
        """Set externalStiffnessMatrix"""
        self.__externalStiffnessMatrix = bool(value)

    @property
    def linearDampingMatrix(self) -> bool:
        """"""
        return self.__linearDampingMatrix

    @linearDampingMatrix.setter
    def linearDampingMatrix(self, value: bool):
        """Set linearDampingMatrix"""
        self.__linearDampingMatrix = bool(value)

    @property
    def firstOrderMotionTransferFunction(self) -> bool:
        """"""
        return self.__firstOrderMotionTransferFunction

    @firstOrderMotionTransferFunction.setter
    def firstOrderMotionTransferFunction(self, value: bool):
        """Set firstOrderMotionTransferFunction"""
        self.__firstOrderMotionTransferFunction = bool(value)

    @property
    def firstOrderWaveForceTransferFunctionDiffraction(self) -> bool:
        """"""
        return self.__firstOrderWaveForceTransferFunctionDiffraction

    @firstOrderWaveForceTransferFunctionDiffraction.setter
    def firstOrderWaveForceTransferFunctionDiffraction(self, value: bool):
        """Set firstOrderWaveForceTransferFunctionDiffraction"""
        self.__firstOrderWaveForceTransferFunctionDiffraction = bool(value)

    @property
    def firstOrderWaveForceTransferFunctionHaskind(self) -> bool:
        """"""
        return self.__firstOrderWaveForceTransferFunctionHaskind

    @firstOrderWaveForceTransferFunctionHaskind.setter
    def firstOrderWaveForceTransferFunctionHaskind(self, value: bool):
        """Set firstOrderWaveForceTransferFunctionHaskind"""
        self.__firstOrderWaveForceTransferFunctionHaskind = bool(value)

    @property
    def addedMassZeroFrequency(self) -> bool:
        """"""
        return self.__addedMassZeroFrequency

    @addedMassZeroFrequency.setter
    def addedMassZeroFrequency(self, value: bool):
        """Set addedMassZeroFrequency"""
        self.__addedMassZeroFrequency = bool(value)

    @property
    def addedMassInfiniteFrequency(self) -> bool:
        """"""
        return self.__addedMassInfiniteFrequency

    @addedMassInfiniteFrequency.setter
    def addedMassInfiniteFrequency(self, value: bool):
        """Set addedMassInfiniteFrequency"""
        self.__addedMassInfiniteFrequency = bool(value)

    @property
    def frequencyDependentAddedMass(self) -> bool:
        """"""
        return self.__frequencyDependentAddedMass

    @frequencyDependentAddedMass.setter
    def frequencyDependentAddedMass(self, value: bool):
        """Set frequencyDependentAddedMass"""
        self.__frequencyDependentAddedMass = bool(value)

    @property
    def frequencyDependentDamping(self) -> bool:
        """"""
        return self.__frequencyDependentDamping

    @frequencyDependentDamping.setter
    def frequencyDependentDamping(self, value: bool):
        """Set frequencyDependentDamping"""
        self.__frequencyDependentDamping = bool(value)

    @property
    def diffractedWaveField(self) -> bool:
        """"""
        return self.__diffractedWaveField

    @diffractedWaveField.setter
    def diffractedWaveField(self, value: bool):
        """Set diffractedWaveField"""
        self.__diffractedWaveField = bool(value)

    @property
    def waveDriftForcePressure(self) -> bool:
        """"""
        return self.__waveDriftForcePressure

    @waveDriftForcePressure.setter
    def waveDriftForcePressure(self, value: bool):
        """Set waveDriftForcePressure"""
        self.__waveDriftForcePressure = bool(value)

    @property
    def waveDriftForceMomentum(self) -> bool:
        """"""
        return self.__waveDriftForceMomentum

    @waveDriftForceMomentum.setter
    def waveDriftForceMomentum(self, value: bool):
        """Set waveDriftForceMomentum"""
        self.__waveDriftForceMomentum = bool(value)

    @property
    def waveDriftForceControlSurfaceIntegration(self) -> bool:
        """"""
        return self.__waveDriftForceControlSurfaceIntegration

    @waveDriftForceControlSurfaceIntegration.setter
    def waveDriftForceControlSurfaceIntegration(self, value: bool):
        """Set waveDriftForceControlSurfaceIntegration"""
        self.__waveDriftForceControlSurfaceIntegration = bool(value)

    @property
    def runPotenOnceInConditionSetsAndSpaces(self) -> bool:
        """This will make WAMIT run POTEN for one condition only, and copy that result and only run FORCE on the the rest of the conditions."""
        return self.__runPotenOnceInConditionSetsAndSpaces

    @runPotenOnceInConditionSetsAndSpaces.setter
    def runPotenOnceInConditionSetsAndSpaces(self, value: bool):
        """Set runPotenOnceInConditionSetsAndSpaces"""
        self.__runPotenOnceInConditionSetsAndSpaces = bool(value)

    @property
    def ignoreExitCode(self) -> bool:
        """Ignore process exit code. Be careful to check the result when checked"""
        return self.__ignoreExitCode

    @ignoreExitCode.setter
    def ignoreExitCode(self, value: bool):
        """Set ignoreExitCode"""
        self.__ignoreExitCode = bool(value)
