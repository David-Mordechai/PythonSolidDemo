from abc import ABC, abstractclassmethod


class ISecondTask(ABC):
    @abstractclassmethod
    def execute(self):
        pass


class SecondTask(ISecondTask):
    def execute(self):
        print("Second task executed.")
