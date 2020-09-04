# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 18:28:36 2020

@author: vishw
"""


class family_members:
    def __init__(self,fathername,mothername,brothername):
        self.fathername =fathername
        self.mothername =mothername
        self.brothername =brothername
        
n=family_members("manjunath","rajeshwari","vishwas")

print("my father name is",n.fathername)
print("my mother name is",n.mothername)
print("my brother name is",n.brothername)
