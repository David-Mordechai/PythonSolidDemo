from abc import ABC, abstractclassmethod
from .Tasks.firstTask import IFirstTask
from .Tasks.secondTask import ISecondTask

class IMyWorkflow(ABC):
    @abstractclassmethod
    def execute(self):
        pass


class MyWorkflow(IMyWorkflow):
    
    def __init__(self, task1: IFirstTask, task2: ISecondTask):
        self.firstTask = task1
        self.secondTask = task2
        pass
    
    def execute(self):
        self.firstTask.execute()
        self.secondTask.execute()