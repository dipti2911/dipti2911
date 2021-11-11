from datetime import *
class project:
    def __init__(self,name,startdate,enddate):
        self.name=name
        self.startdate=startdate
        self.enddate=enddate
        self.tasks=[]
    def addtask(self,task):
        self.tasks.append(task)
class Task:
    def __init__(self,name,duration):
        self.name = name
        self.duration=duration
        self.resourses=[]
    def addresource(self,resource):
        self.resourses.append(resource)
class Resources:
    def __init__(self,name,skill):
        self.name = name
        self.skill=skill
p=project("Machine Learning",date(2020,12,22),date(2021,12,22))
t=Task("bot",98)
r=Resources("dipti","python")
p.addtask
t.addresource

for eachtask in project.tasks:
    print(eachtask.name)
    for eachresource in eachtask.resources:
        print(eachtask.name)
        print(eachresource.skill)