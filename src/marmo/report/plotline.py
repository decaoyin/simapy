# This an autogenerated file
# 
# Generated with PlotLine
from typing import Dict,Sequence,List
from dmt.blueprint import Blueprint
from .blueprints.plotline import PlotLineBlueprint
from numpy import ndarray,asarray
from dmt.entity import Entity
from marmo.report.linestyle import LineStyle
from marmo.report.pointstyle import PointStyle

class PlotLine(Entity):
    """
    Keyword arguments
    -----------------
    xlabel : str
         (default "")
    ylabel : str
         (default "")
    showlegend : bool
         (default True)
    x : ndarray
    y : ndarray
    linewidth : int
         (default 1)
    pointsize : int
         (default 1)
    linestyle : LineStyle
    pointstyle : PointStyle
    color : str
         (default "")
    """

    def __init__(self , xlabel="", ylabel="", showlegend=True, linewidth=1, pointsize=1, linestyle=LineStyle.SOLID, pointstyle=PointStyle.NONE, color="", **kwargs):
        super().__init__(**kwargs)
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.showlegend = showlegend
        self.x = ndarray(1)
        self.y = ndarray(1)
        self.linewidth = linewidth
        self.pointsize = pointsize
        self.linestyle = linestyle
        self.pointstyle = pointstyle
        self.color = color
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return PlotLineBlueprint()


    @property
    def xlabel(self) -> str:
        """"""
        return self.__xlabel

    @xlabel.setter
    def xlabel(self, value: str):
        """Set xlabel"""
        self.__xlabel = str(value)

    @property
    def ylabel(self) -> str:
        """"""
        return self.__ylabel

    @ylabel.setter
    def ylabel(self, value: str):
        """Set ylabel"""
        self.__ylabel = str(value)

    @property
    def showlegend(self) -> bool:
        """"""
        return self.__showlegend

    @showlegend.setter
    def showlegend(self, value: bool):
        """Set showlegend"""
        self.__showlegend = bool(value)

    @property
    def x(self) -> ndarray:
        """"""
        return self.__x

    @x.setter
    def x(self, value: ndarray):
        """Set x"""
        self.__x = asarray(value)

    @property
    def y(self) -> ndarray:
        """"""
        return self.__y

    @y.setter
    def y(self, value: ndarray):
        """Set y"""
        self.__y = asarray(value)

    @property
    def linewidth(self) -> int:
        """"""
        return self.__linewidth

    @linewidth.setter
    def linewidth(self, value: int):
        """Set linewidth"""
        self.__linewidth = int(value)

    @property
    def pointsize(self) -> int:
        """"""
        return self.__pointsize

    @pointsize.setter
    def pointsize(self, value: int):
        """Set pointsize"""
        self.__pointsize = int(value)

    @property
    def linestyle(self) -> LineStyle:
        """"""
        return self.__linestyle

    @linestyle.setter
    def linestyle(self, value: LineStyle):
        """Set linestyle"""
        self.__linestyle = value

    @property
    def pointstyle(self) -> PointStyle:
        """"""
        return self.__pointstyle

    @pointstyle.setter
    def pointstyle(self, value: PointStyle):
        """Set pointstyle"""
        self.__pointstyle = value

    @property
    def color(self) -> str:
        """"""
        return self.__color

    @color.setter
    def color(self, value: str):
        """Set color"""
        self.__color = str(value)
