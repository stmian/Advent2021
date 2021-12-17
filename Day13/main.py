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

grid = np.zeros((xmax+1,ymax+1))
for idx in range(952):
    x = points[0][idx]
    y = points[1][idx]
    grid[x][y] = 1


def foldX(grid,x):
    