# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 04:36:24 2021

@author: Sami
"""
import numpy as np

with open("input.txt", 'r') as f:
    dir = [i for i in f.read().split(',')]
    
initAge = np.asarray(dir)
initAge = initAge.astype(int) 

currAge = initAge.copy()


def simDay(input):
    add = 0
    for idx, age in enumerate(input):
        if age > 0:
            input[idx] -= 1
        elif age == 0:
            input[idx] = 6
            add += 1
            
    new = np.concatenate((input, np.ones((add)) * 8))
    return new


##Part 1
days = 1

for i in range(0,days):
    currAge = simDay(currAge)

#print(len(currAge))


##Part 2

def solve(data, days):
    tracker = [data.count(i) for i in range(9)]
    print(tracker)
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)


data = [int(x) for x in open("input.txt").read().strip().split(",")]
print(f"Part 1: {solve(data, 80)}")
print(f"Part 2: {solve(data, 256)}")
