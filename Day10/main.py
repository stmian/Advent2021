# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 03:29:35 2021

@author: Sami
"""

import numpy as np
err = []
with open("input.txt", 'r') as f:
    data = [i for i in f.read().splitlines()]
    

incomplete = 0
good = 0
todo = []
    
start = ["(","[", "{","<"]
end = [")","]","}",">"]
opposites = {"(":")","[":"]", "{":"}","<":">"}
revpoints = {")":1,"]":2,"}":3,">":4,"(":1,"[":2, "{":3,"<":4}

for line in data:
    items = list(line)
    stack = []
    for item in items:
        if item in start:
            stack.append(item)
        elif item in end:
  #          print("ending item")
            curr = stack.pop()
            if item == curr:
  #              print("Good")
                good += 1
            elif item != opposites[curr]:
                err.append(item)
   #             print("BROKEN")
                break;

    if len(stack) > 0:
        incomplete += 1
        todo.append(stack)

print(incomplete)




def score(vals):
    points = 0
    for item in vals:
        if item == ")":
            points +=3
        elif item == "]":
            points += 57
        elif item == "}":
            points += 1197
        elif item == ">":
            points += 25137
        else:
            print("BOO")
    return points

print(score(err))
#print(err)

def get_key(val):
    for key, value in opposites.items():
        if val == value:
            return key
 
    return "key doesn't exist"

### Part 2
output = []

for line in todo:
    sums = 0
    for beg in (line[::-1]):
        sums *= 5
        sums += revpoints[beg]
    output.append(sums)
        
        
import statistics

output.sort()

        
        
        
        
        
        

