# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 04:16:45 2021

@author: Sami
"""
import numpy as np

with open("input.txt", 'r') as f:
    dir = [i for i in f.read().split(',')]
    
pos = np.asarray(dir)
pos = pos.astype(int)

maxH = max(pos)
minH = min(pos)
results = {}


for hoz in np.arange(minH,maxH+1):
    results[hoz] = 0
    for val in pos:
        results[hoz] += abs(hoz - val)
        
ans = min(results, key=results.get)
print(results[ans])
     

##Part 2

resultsP2 = {}


for hoz in np.arange(minH,maxH+1):
    results[hoz] = 0
    for val in pos:
        
        dist = abs(hoz-val) +1
        fuel = dist*(dist-1)/2        
        results[hoz] += fuel
        
ans = min(results, key=results.get)
print(results[ans])