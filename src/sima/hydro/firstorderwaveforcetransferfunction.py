# This an autogenerated file
# 
# Generated with FirstOrderWaveForceTransferFunction
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.firstorderwaveforcetransferfunction import FirstOrderWaveForceTransferFunctionBlueprint
from numpy import ndarray,asarray
from sima.hydro.directiondependentcomplexvalues import DirectionDependentComplexValues
from sima.hydro.directionsymmetry import DirectionSymmetry
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue

class FirstOrderWaveForceTransferFunction(MOAO):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    directions : ndarray
    frequencies : ndarray
    symmetry : DirectionSymmetry
    fx : DirectionDependentComplexValues
    fy : DirectionDependentComplexValues
    fz : DirectionDependentComplexValues
    mx : DirectionDependentComplexValues
    my : DirectionDependentComplexValues
    mz : DirectionDependentComplexValues
    """

    def __init__(self , _id="", symmetry=DirectionSymmetry.NO_SYMMETRY, **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.directions = ndarray(1)
        self.frequencies = ndarray(1)
        self.symmetry = symmetry
        self.fx = None
        self.fy = None
        self.fz = None
        self.mx = None
        self.my = None
        self.mz = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return FirstOrderWaveForceTransferFunctionBlueprint()


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
    def directions(self) -> ndarray:
        """"""
        return self.__directions

    @directions.setter
    def directions(self, value: ndarray):
        """Set directions"""
        self.__directions = asarray(value)

    @property
    def frequencies(self) -> ndarray:
        """"""
        return self.__frequencies

    @frequencies.setter
    def frequencies(self, value: ndarray):
        """Set frequencies"""
        self.__frequencies = asarray(value)

    @property
    def symmetry(self) -> DirectionSymmetry:
        """"""
        return self.__symmetry

    @symmetry.setter
    def symmetry(self, value: DirectionSymmetry):
        """Set symmetry"""
        self.__symmetry = value

    @property
    def fx(self) -> DirectionDependentComplexValues:
        """"""
        return self.__fx

    @fx.setter
    def fx(self, value: DirectionDependentComplexValues):
        """Set fx"""
        self.__fx = value

    @property
    def fy(self) -> DirectionDependentComplexValues:
        """"""
        return self.__fy

    @fy.setter
    def fy(self, value: DirectionDependentComplexValues):
        """Set fy"""
        self.__fy = value

    @property
    def fz(self) -> DirectionDependentComplexValues:
        """"""
        return self.__fz

    @fz.setter
    def fz(self, value: DirectionDependentComplexValues):
        """Set fz"""
        self.__fz = value

    @property
    def mx(self) -> DirectionDependentComplexValues:
        """"""
        return self.__mx

    @mx.setter
    def mx(self, value: DirectionDependentComplexValues):
        """Set mx"""
        self.__mx = value

    @property
    def my(self) -> DirectionDependentComplexValues:
        """"""
        return self.__my

    @my.setter
    def my(self, value: DirectionDependentComplexValues):
        """Set my"""
        self.__my = value

    @property
    def mz(self) -> DirectionDependentComplexValues:
        """"""
        return self.__mz

    @mz.setter
    def mz(self, value: DirectionDependentComplexValues):
        """Set mz"""
        self.__mz = value
