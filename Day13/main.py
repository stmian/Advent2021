# -*- coding: utf-8 -*-
"""
Created on Wed Dec 15 15:49:33 2021

@author: Sami
"""
import numpy as np
with open("input.txt", 'r') as f:
    data = [i.split(',') for i in f.read().splitlines()]
    
folds = data[-12:-1]
points = data[0:len(data)-13]    

points = np.asarray(points, dtype=int).T
xmax = max(points[:][0])
ymax = max(points[:][1])

m = max(ymax,xmax) + 1

grid = np.zeros((m,m))
for idx in range(952):
    xp = points[0][idx]
    yp = points[1][idx]
    grid[yp][xp] = 1


def foldX(grid,line):
    for x in range(line,m,1):
        for y in range(m):            
            if grid[y][x] == 1:
                offset = line - x
                grid[y][line + offset] +=1
                grid[y][x] = 0

def foldY(grid,line):
    for y in range(line,m,1):
        for x in range(m):            
            if grid[y][x] == 1:
                offset = line - y
                grid[line + offset][x] +=1
                grid[y][x] = 0    

print("Start:")                
print(np.count_nonzero(grid))
foldX(grid,655)

for fold in folds:
    tmp = fold[0].split(" ")
    tmp2 = tmp[2].split("=")
    axis = tmp2[0]
    line = int(tmp2[1])
    print(axis,line)
    
    if axis == "x":
        foldX(grid,line)
    elif axis == "y":
        foldY(grid,line)
    
    
print(np.count_nonzero(grid))


                