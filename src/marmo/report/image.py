# This an autogenerated file
# 
# Generated with Image
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.image import ImageBlueprint
from typing import Dict
from marmo.report.reportitem import ReportItem

class Image(ReportItem):
    """
    Keyword arguments
    -----------------
    path : str
         (default "")
    caption : str
         (default "")
    height : int
         (default 0)
    width : int
         (default 0)
    """

    def __init__(self , path="", caption="", height=0, width=0, **kwargs):
        super().__init__(**kwargs)
        self.path = path
        self.caption = caption
        self.height = height
        self.width = width
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return ImageBlueprint()


    @property
    def path(self) -> str:
        """"""
        return self.__path

    @path.setter
    def path(self, value: str):
        """Set path"""
        self.__path = str(value)

    @property
    def caption(self) -> str:
        """"""
        return self.__caption

    @caption.setter
    def caption(self, value: str):
        """Set caption"""
        self.__caption = str(value)

    @property
    def height(self) -> int:
        """"""
        return self.__height

    @height.setter
    def height(self, value: int):
        """Set height"""
        self.__height = int(value)

    @property
    def width(self) -> int:
        """"""
        return self.__width

    @width.setter
    def width(self, value: int):
        """Set width"""
        self.__width = int(value)
