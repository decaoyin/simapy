# This an autogenerated file
# 
# Generated with CrossSectionReference
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.crosssectionreference import CrossSectionReferenceBlueprint
from typing import Dict
from sima.riflex.elementreference import ElementReference
from sima.riflex.end import End
from sima.sima.scriptablevalue import ScriptableValue
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from sima.riflex.arline import ARLine

class CrossSectionReference(ElementReference):
    """
    Keyword arguments
    -----------------
    description : str
         (default "")
    scriptableValues : List[ScriptableValue]
    line : ARLine
         Line
    segment : int
         Segment on given line(default 1)
    allSegments : bool
         All segments(default False)
    elementNumber : int
         Local element number on actual segment(default 1)
    allElements : bool
         All elements(default False)
    allEnds : bool
         All ends(default False)
    elementEnd : End
         End number 1 or 2
    scfa : float
         Stress concentration factor for axial force contribution(default 0.0)
    scfy : float
         Stress concentration factor for bending about y axis(default 0.0)
    scfz : float
         Value	Stress concentration factor for bending about z axis(default 0.0)
    """

    def __init__(self , description="", segment=1, allSegments=False, elementNumber=1, allElements=False, allEnds=False, elementEnd=End.ONE, scfa=0.0, scfy=0.0, scfz=0.0, **kwargs):
        super().__init__(**kwargs)
        self.description = description
        self.scriptableValues = list()
        self.line = None
        self.segment = segment
        self.allSegments = allSegments
        self.elementNumber = elementNumber
        self.allElements = allElements
        self.allEnds = allEnds
        self.elementEnd = elementEnd
        self.scfa = scfa
        self.scfy = scfy
        self.scfz = scfz
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return CrossSectionReferenceBlueprint()


    @property
    def description(self) -> str:
        """"""
        return self.__description

    @description.setter
    def description(self, value: str):
        """Set description"""
        self.__description = value

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
    def line(self) -> ARLine:
        """Line"""
        return self.__line

    @line.setter
    def line(self, value: ARLine):
        """Set line"""
        self.__line = value

    @property
    def segment(self) -> int:
        """Segment on given line"""
        return self.__segment

    @segment.setter
    def segment(self, value: int):
        """Set segment"""
        self.__segment = int(value)

    @property
    def allSegments(self) -> bool:
        """All segments"""
        return self.__allSegments

    @allSegments.setter
    def allSegments(self, value: bool):
        """Set allSegments"""
        self.__allSegments = bool(value)

    @property
    def elementNumber(self) -> int:
        """Local element number on actual segment"""
        return self.__elementNumber

    @elementNumber.setter
    def elementNumber(self, value: int):
        """Set elementNumber"""
        self.__elementNumber = int(value)

    @property
    def allElements(self) -> bool:
        """All elements"""
        return self.__allElements

    @allElements.setter
    def allElements(self, value: bool):
        """Set allElements"""
        self.__allElements = bool(value)

    @property
    def allEnds(self) -> bool:
        """All ends"""
        return self.__allEnds

    @allEnds.setter
    def allEnds(self, value: bool):
        """Set allEnds"""
        self.__allEnds = bool(value)

    @property
    def elementEnd(self) -> End:
        """End number 1 or 2"""
        return self.__elementEnd

    @elementEnd.setter
    def elementEnd(self, value: End):
        """Set elementEnd"""
        self.__elementEnd = value

    @property
    def scfa(self) -> float:
        """Stress concentration factor for axial force contribution"""
        return self.__scfa

    @scfa.setter
    def scfa(self, value: float):
        """Set scfa"""
        self.__scfa = float(value)

    @property
    def scfy(self) -> float:
        """Stress concentration factor for bending about y axis"""
        return self.__scfy

    @scfy.setter
    def scfy(self, value: float):
        """Set scfy"""
        self.__scfy = float(value)

    @property
    def scfz(self) -> float:
        """Value	Stress concentration factor for bending about z axis"""
        return self.__scfz

    @scfz.setter
    def scfz(self, value: float):
        """Set scfz"""
        self.__scfz = float(value)
