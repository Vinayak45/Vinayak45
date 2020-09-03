# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 19:49:42 2020

@author: vishw
"""


def tri_recursion(k):
    if(k>0):
      result=k+tri_recursion(k-1)
      print(result)
    else:
       result=0
    return result

print("\n\nrecursion example results")
tri_recursion(6)   