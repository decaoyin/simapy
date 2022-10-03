# This an autogenerated file
# 
# Generated with DifferenceFrequencyWaveForce
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.differencefrequencywaveforce import DifferenceFrequencyWaveForceBlueprint
from numpy import ndarray,asarray
from sima.hydro.qtfdofitem import QTFDofItem
from sima.hydro.quadratictransferfunction import QuadraticTransferFunction
from sima.sima.scriptablevalue import ScriptableValue

class DifferenceFrequencyWaveForce(QuadraticTransferFunction):
    """
    Keyword arguments
    -----------------
    _id : str
         (default "")
    scriptableValues : List[ScriptableValue]
    nFreq : int
         (default 0)
    nDir : int
         (default 0)
    bichromatic : bool
         (default False)
    bidirectional : bool
         (default False)
    frequencies : ndarray
    directions : ndarray
    onFile : bool
         (default False)
    file : str
         (default "")
    surge : QTFDofItem
    sway : QTFDofItem
    heave : QTFDofItem
    roll : QTFDofItem
    pitch : QTFDofItem
    yaw : QTFDofItem
    """

    def __init__(self , _id="", nFreq=0, nDir=0, bichromatic=False, bidirectional=False, onFile=False, file="", **kwargs):
        super().__init__(**kwargs)
        self._id = _id
        self.scriptableValues = list()
        self.nFreq = nFreq
        self.nDir = nDir
        self.bichromatic = bichromatic
        self.bidirectional = bidirectional
        self.frequencies = ndarray(1)
        self.directions = ndarray(1)
        self.onFile = onFile
        self.file = file
        self.surge = None
        self.sway = None
        self.heave = None
        self.roll = None
        self.pitch = None
        self.yaw = None
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return DifferenceFrequencyWaveForceBlueprint()


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
    def nFreq(self) -> int:
        """"""
        return self.__nFreq

    @nFreq.setter
    def nFreq(self, value: int):
        """Set nFreq"""
        self.__nFreq = int(value)

    @property
    def nDir(self) -> int:
        """"""
        return self.__nDir

    @nDir.setter
    def nDir(self, value: int):
        """Set nDir"""
        self.__nDir = int(value)

    @property
    def bichromatic(self) -> bool:
        """"""
        return self.__bichromatic

    @bichromatic.setter
    def bichromatic(self, value: bool):
        """Set bichromatic"""
        self.__bichromatic = bool(value)

    @property
    def bidirectional(self) -> bool:
        """"""
        return self.__bidirectional

    @bidirectional.setter
    def bidirectional(self, value: bool):
        """Set bidirectional"""
        self.__bidirectional = bool(value)

    @property
    def frequencies(self) -> ndarray:
        """"""
        return self.__frequencies

    @frequencies.setter
    def frequencies(self, value: ndarray):
        """Set frequencies"""
        self.__frequencies = asarray(value)

    @property
    def directions(self) -> ndarray:
        """"""
        return self.__directions

    @directions.setter
    def directions(self, value: ndarray):
        """Set directions"""
        self.__directions = asarray(value)

    @property
    def onFile(self) -> bool:
        """"""
        return self.__onFile

    @onFile.setter
    def onFile(self, value: bool):
        """Set onFile"""
        self.__onFile = bool(value)

    @property
    def file(self) -> str:
        """"""
        return self.__file

    @file.setter
    def file(self, value: str):
        """Set file"""
        self.__file = str(value)

    @property
    def surge(self) -> QTFDofItem:
        """"""
        return self.__surge

    @surge.setter
    def surge(self, value: QTFDofItem):
        """Set surge"""
        self.__surge = value

    @property
    def sway(self) -> QTFDofItem:
        """"""
        return self.__sway

    @sway.setter
    def sway(self, value: QTFDofItem):
        """Set sway"""
        self.__sway = value

    @property
    def heave(self) -> QTFDofItem:
        """"""
        return self.__heave

    @heave.setter
    def heave(self, value: QTFDofItem):
        """Set heave"""
        self.__heave = value

    @property
    def roll(self) -> QTFDofItem:
        """"""
        return self.__roll

    @roll.setter
    def roll(self, value: QTFDofItem):
        """Set roll"""
        self.__roll = value

    @property
    def pitch(self) -> QTFDofItem:
        """"""
        return self.__pitch

    @pitch.setter
    def pitch(self, value: QTFDofItem):
        """Set pitch"""
        self.__pitch = value

    @property
    def yaw(self) -> QTFDofItem:
        """"""
        return self.__yaw

    @yaw.setter
    def yaw(self, value: QTFDofItem):
        """Set yaw"""
        self.__yaw = value
