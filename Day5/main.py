# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:52:19 2021

@author: Sami
"""
import numpy as np
from collections import Counter

p1_ans = 0
p2_ans = 0

data = open("input.txt").read().strip().split("\n")
pts1 = []
pts2 = []
for line in data:
    x1, y1 = tuple(int(x) for x in line.split(" -> ")[0].split(","))
    x2, y2 = tuple(int(x) for x in line.split(" -> ")[1].split(","))
    
## Part 1

    if x1 == x2 or y1 == y2:
        for x in range(min(x1,x2),max(x1,x2) +1):
            for y in range(min(y1,y2), max(y1,y2) +1):
                pts1.append((x,y))
                pts2.append((x,y))
                
    else:
        xslope = 1 if x1 < x2 else -1
        yslope = 1 if y1 < y2 else -1
        y = y1
        for x in range(x1,x2+xslope, xslope):
            pts2.append((x,y))
            y += yslope
                
for pt in Counter(pts1).values():
    if pt > 1:
        p1_ans +=1
        
for pt in Counter(pts2).values():
    if pt > 1:
        p2_ans +=1
        
print(p1_ans, p2_ans)