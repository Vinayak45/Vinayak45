# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 18:57:29 2020

@author: vishw
"""


class Student:
    def __init__(self,name,school):
        self.name=name
        self.school=school
        self.marks=[]
        
    def average(self):
         return sum(self.marks)/len(self.marks)
     
class Workingstudent(Student):
    def __init__(self,name,school,salary):
        super().__init__(name,school)
        self.salary=salary

rolf=Workingstudent('rolf','MIT',15.50)
print(rolf.salary)
rolf.marks.append(57)
print(rolf.average())        