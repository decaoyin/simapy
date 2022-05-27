# This an autogenerated file
# 
# Generated with GitTaskFolder
from typing import Dict,Sequence,List
from dmt.entity import Entity
from dmt.blueprint import Blueprint
from .blueprints.gittaskfolder import GitTaskFolderBlueprint
from typing import Dict
from sima.sima.scriptablevalue import ScriptableValue
from sima.sima.task import Task
from sima.sima.taskfolder import TaskFolder

class GitTaskFolder(TaskFolder):
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
    remoteURI : str
         (default "")
    branch : str
         (default "")
    lastCommitMessage : str
         (default "")
    repositoryFolder : str
         (default "")
    """

    def __init__(self , name="", description="", _id="", visible=True, remoteURI="", branch="", lastCommitMessage="", repositoryFolder="", **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description
        self._id = _id
        self.scriptableValues = list()
        self.childFolders = list()
        self.childTasks = list()
        self.visible = visible
        self.remoteURI = remoteURI
        self.branch = branch
        self.lastCommitMessage = lastCommitMessage
        self.repositoryFolder = repositoryFolder
        for key, value in kwargs.items():
            if not isinstance(value, Dict):
                setattr(self, key, value)


    @property
    def blueprint(self) -> Blueprint:
        """Return blueprint that this entity represents"""
        return GitTaskFolderBlueprint()


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

    @property
    def remoteURI(self) -> str:
        """"""
        return self.__remoteURI

    @remoteURI.setter
    def remoteURI(self, value: str):
        """Set remoteURI"""
        self.__remoteURI = str(value)

    @property
    def branch(self) -> str:
        """"""
        return self.__branch

    @branch.setter
    def branch(self, value: str):
        """Set branch"""
        self.__branch = str(value)

    @property
    def lastCommitMessage(self) -> str:
        """"""
        return self.__lastCommitMessage

    @lastCommitMessage.setter
    def lastCommitMessage(self, value: str):
        """Set lastCommitMessage"""
        self.__lastCommitMessage = str(value)

    @property
    def repositoryFolder(self) -> str:
        """"""
        return self.__repositoryFolder

    @repositoryFolder.setter
    def repositoryFolder(self, value: str):
        """Set repositoryFolder"""
        self.__repositoryFolder = str(value)
