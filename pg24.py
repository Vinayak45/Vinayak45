# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 11:00:52 2020

@author: vishw
"""


x=300

def myfunc():
    global x
    x=200
    
myfunc()

print(x)    