# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:28:36 2020

@author: vishw
"""


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = Person("John",36)

print(p1.name)
print(p1.age)        