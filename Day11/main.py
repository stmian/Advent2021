

import numpy as np


with open("input.txt", 'r') as f:
    data = [list(i) for i in f.read().splitlines()]


running = False
original = np.asarray(data,dtype=int)
g = np.asarray(data,dtype=int)

#print(g)

def incrementAll(grid):


    try:
        grid += 1

    except IndexError:
        print("Ehh")

def incrementNeighbors(grid,x,y):
   
    m = len(grid) -1
    try:       
        
        if(x > 0):
            grid[x-1][y] += 1            
        if(x < m):
            grid[x+1][y] += 1        
        if(y < m):
            grid[x][y+1] += 1        
        if(y > 0):
            grid[x][y-1] += 1            
        if (y < m  and x < m):    
            grid[x+1][y+1] += 1        
        if(y > 0 and x > 0):
            grid[x-1][y-1] += 1
        if(y > 0 and x < m):
            grid[x+1][y-1] += 1
        if(x > 0  and y < m):
            grid[x-1][y+1] += 1
        grid[x][y] = -100
        return grid
    except IndexError:
        print("Ehh")  
        print((x,y))


steps = 100
ilum = 0
i1 = 0

for step in range(steps):
    flashedStep = []
    
    incrementAll(g)
    running = True
    while running:
        itemindex = np.where(g > 9)
        i1 += len(itemindex[0])
        for i in range(len(itemindex[0])):
            
            x = itemindex[0][i]
            y = itemindex[1][i]
#            print(x,y)
 #           print(g[x][y])
            if((x,y) not in flashedStep):
                g = incrementNeighbors(g,x,y)
                flashedStep.append((x,y))
                ilum += 1
            
        if np.count_nonzero(g > 9) > 0:
            running = True
        else:
            running = False
        print(g)
    g = np.where(g<0,0,g)                
    
print(ilum)    
    
    
    
    
    
    