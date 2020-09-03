# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 19:30:30 2020

@author: vishw
"""


thislist=["apple","banana","cherry"];
print(thislist);

thislist=["apple","banana","cherry"];thislist[1]="blackcurrent";
print(thislist)

thislist=list(("apple","banana","cherry"));

thislist=list(("apple","banana","cherry"));thislist.append("damson");
print(thislist)

thislist=list(("apple","banana","cherry"));thislist.remove("banana");
print(thislist)

thislist=list(("apple","banana","cherry"));
print(len(thislist))

