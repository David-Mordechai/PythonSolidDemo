from Workflows.Tasks.firstTask import FirstTask
from Workflows.Tasks.secondTask import SecondTask
from Workflows.myWorkflow import MyWorkflow


def doMyWorkflow():
    myWorkflow = MyWorkflow(FirstTask(), SecondTask())
    myWorkflow.execute()

doMyWorkflow()

