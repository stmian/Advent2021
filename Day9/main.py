# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 21:52:02 2021

@author: Sami
"""

import numpy as np
new = []
with open("input.txt", 'r') as f:
    dir = [i for i in f.read().splitlines()]

data = np.empty((100,100))

for i, entry in enumerate(dir):
 #   print(entry)
    for j,item in enumerate(entry):
        data[i][j] = int(item)



#data = np.loadtxt("input.txt",dtype=str)

sr = sl = sd = su = 0

def searchUp(x,y,val):
    if(y>0):
        if val < data[x][y-1]:
            return "1"
        else:
            return "0"
    else:
        return "10"

def searchDown(x,y,val):
    if(y<99):
        if val < data[x][y+1]:
            return "1"
        else:
            return "0"
    else:
        return "10"

def searchLeft(x,y,val):
    if(x > 0):
        if val < data[x-1][y]:
            return "1"
        else:
            return "0"
    else:
        return "10"

def searchRight(x,y,val):
    if(x<99):
        if val < data[x+1][y]:
            return "1"
        else:
            return "0"
    else:
        return "10"
    
lows = []
entries = []
basins = []

for row in range(len(data)):
    for col in range(len(data[row])):

        tmp = data[row][col]
  #      print(row,col)
       
        sr = searchRight(row, col, tmp)
        sl = searchLeft(row, col, tmp)
        sd = searchDown(row, col, tmp)
        su = searchUp(row, col, tmp)      

        res = int(sr) + int(sl) + int(su) + int(sd)
        entries.append(res)
        
        if res > 3 and res < 5:
            lows.append(tmp)
            basins.append((row,col))
        if res == 13:
            lows.append(tmp)
            basins.append((row,col))
        
        
print(sum(lows) + len(lows))        
        
        
#Part 2

sizes = []

for basin in basins:
    size = 0
    


        
        
        