# -*- coding: utf-8 -*-
"""
Created on Sat Dec 18 03:58:48 2021

@author: Sami
"""

import numpy as np
with open("input.txt", 'r') as f:
    data = [i.split(',') for i in f.read().splitlines()]
    
    
polymer =    list(data[0])
polymer = polymer[0] 
rules = data[2:]
book = {}
for item in rules:
    tmp = item[0].split(" -> ")
    book[tmp[0]] = tmp[1]

def part1(line):
    
    fdist=dict(zip(*np.unique(list(line), return_counts=True)))
    print("The elements with their counts are -", fdist)
       

    
def step(inp):
    template = list(inp)
    res = []
    for idx in range(len(template)-1):
        step = template[idx] + template[idx +1]
        mid = book[step]
        ans = template[idx] + mid
        res.append(ans)
    res.append(template[-1])

    return "".join(res)    

steps = 10
for i in range(steps):

    results = step(polymer)
    polymer = results
    print(i)
part1(results)