# This an autogenerated file
# Data model for an equally spaced signal.
# Generated with EquallySpacedSignal
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.equallyspacedsignal import EquallySpacedSignalBlueprint
from numpy import ndarray,asarray
from marmo.containers.attribute import Attribute
from marmo.containers.signal import Signal

class EquallySpacedSignal(Signal):
    """
    Data model for an equally spaced signal.
    Keyword arguments
    -----------------
    name : str
         (default "")
    description : str
         (default "")
    attributes : List[Attribute]
    value : ndarray
    xstart : float
         (default 0.0)
    xdelta : float
         (default 0.0)
    unit : str
         (default "")
    xunit : str
         (default "")
    xname : str
         (default "")
    xlabel : str
         (default "")
    xdescription : str
         (default "")
    label : str
         (default "")
    legend : str
         (default "")
    """

    def __init__(self , name:str="", description:str="", xstart:float=0.0, xdelta:float=0.0, unit:str="", xunit:str="", xname:str="", xlabel:str="", xdescription:str="", label:str="", legend:str="", **kwargs):
        super().__init__(**kwargs)
        self.__name = name
        self.__description = description
        self.__attributes = list()
        self.__value = ndarray(1)
        self.__xstart = xstart
        self.__xdelta = xdelta
        self.__unit = unit
        self.__xunit = xunit
        self.__xname = xname
        self.__xlabel = xlabel
        self.__xdescription = xdescription
        self.__label = label
        self.__legend = legend
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return EquallySpacedSignalBlueprint()


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
    def attributes(self) -> List[Attribute]:
        """"""
        return self.__attributes

    @attributes.setter
    def attributes(self, value: List[Attribute]):
        """Set attributes"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__attributes = value

    @property
    def value(self) -> ndarray:
        """"""
        return self.__value

    @value.setter
    def value(self, value: ndarray):
        """Set value"""
        self.__value = asarray(value)

    @property
    def xstart(self) -> float:
        """"""
        return self.__xstart

    @xstart.setter
    def xstart(self, value: float):
        """Set xstart"""
        self.__xstart = float(value)

    @property
    def xdelta(self) -> float:
        """"""
        return self.__xdelta

    @xdelta.setter
    def xdelta(self, value: float):
        """Set xdelta"""
        self.__xdelta = float(value)

    @property
    def unit(self) -> str:
        """"""
        return self.__unit

    @unit.setter
    def unit(self, value: str):
        """Set unit"""
        self.__unit = str(value)

    @property
    def xunit(self) -> str:
        """"""
        return self.__xunit

    @xunit.setter
    def xunit(self, value: str):
        """Set xunit"""
        self.__xunit = str(value)

    @property
    def xname(self) -> str:
        """"""
        return self.__xname

    @xname.setter
    def xname(self, value: str):
        """Set xname"""
        self.__xname = str(value)

    @property
    def xlabel(self) -> str:
        """"""
        return self.__xlabel

    @xlabel.setter
    def xlabel(self, value: str):
        """Set xlabel"""
        self.__xlabel = str(value)

    @property
    def xdescription(self) -> str:
        """"""
        return self.__xdescription

    @xdescription.setter
    def xdescription(self, value: str):
        """Set xdescription"""
        self.__xdescription = str(value)

    @property
    def label(self) -> str:
        """"""
        return self.__label

    @label.setter
    def label(self, value: str):
        """Set label"""
        self.__label = str(value)

    @property
    def legend(self) -> str:
        """"""
        return self.__legend

    @legend.setter
    def legend(self, value: str):
        """Set legend"""
        self.__legend = str(value)
