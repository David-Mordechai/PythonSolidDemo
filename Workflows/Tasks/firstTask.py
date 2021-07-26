from abc import ABC, abstractclassmethod

class IFirstTask(ABC):
    @abstractclassmethod
    def execute(self):
        pass

class FirstTask(IFirstTask):
    def execute(self):
        print("First task executed.")