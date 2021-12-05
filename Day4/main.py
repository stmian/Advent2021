# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:52:19 2021

@author: Sami
"""

with open("input.txt", 'r') as f:
    dir = [i for i in f.read().splitlines()]


inputs = dir[0].split(',')

blanks = [idx for idx, line in enumerate(dir) if line == ""]


sheets={}

for b in blanks:
    sheets["b%s" %b] = dir[b+1:b+6]
    for row in sheets["b%s" %b]:
        row = row.split()

    
  
for call in inputs[1]:
    print(call)
    for s in sheets:
            if call in sheets[s]:
                loc = sheets[s].index(call)
                sheets[s][loc] = "F"

            


