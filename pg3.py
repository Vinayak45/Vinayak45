# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:48:55 2020

@author: vishw
"""


fruits=['apple','banana','cherry','orange']
fruits.clear()

points=[1,4,2,9,7,9,3,1]
x=points.count(4)
print(x)

fruits=['apple','banana','cherry']
cars=['ford','bmw','volvo']
fruits.extend(cars)
print(fruits)

fruits=['apple','banana','cherry']
points=(1,4,5,9)
fruits.extend(points)
print(fruits)

fruits=['apple','banana','cherry']
x=fruits.copy()
print(x)

fruits=['apple','banana','cherry']
x=fruits.index("cherry")
print(x)

fruits=['apple','banana','cherry']
x=fruits.insert(1,"orange")
print(fruits)

fruits=['apple','banana','cherry']
fruits.pop(1)
print(fruits)

fruits=['apple','banana','cherry']
fruits.remove("banana")
print(fruits)

fruits=['apple','banana','cherry']
fruits.reverse()
print(fruits)

cars=['ford','bmw','volvo']
cars.sort()
print(cars)