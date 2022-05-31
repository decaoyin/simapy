# This an autogenerated file
# 
# Generated with TaskFolder
from __future__ import annotations
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.taskfolder import TaskFolderBlueprint
from typing import Dict
from sima.sima.moao import MOAO
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.task import Task

class TaskFolder(MOAO):
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
    childFolders : List[TaskFolder]
    childTasks : List[Task]
    visible : bool
         (default True)
    """

    def __init__(self , name="", description="", _id="", visible=True, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.childFolders = list()
        self.childTasks = list()
        self.visible = visible
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return TaskFolderBlueprint()


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
    def childFolders(self) -> List[TaskFolder]:
        """"""
        return self.__childFolders

    @childFolders.setter
    def childFolders(self, value: List[TaskFolder]):
        """Set childFolders"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__childFolders = value

    @property
    def childTasks(self) -> List[Task]:
        """"""
        return self.__childTasks

    @childTasks.setter
    def childTasks(self, value: List[Task]):
        """Set childTasks"""
        if not isinstance(value, Sequence):
            raise Exception("Expected sequense, but was " , type(value))
        self.__childTasks = value

    @property
    def visible(self) -> bool:
        """"""
        return self.__visible

    @visible.setter
    def visible(self, value: bool):
        """Set visible"""
        self.__visible = bool(value)
