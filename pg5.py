# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 10:55:44 2020

@author: vishw
"""


x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)

print(x)