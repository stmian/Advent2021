# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 00:56:06 2021

@author: Sami
"""

with open("input.txt") as file:
    data = file.read().split()

x = data[2].split("..")
y = data[3].split("..")
xmin = int(x[0][2:5])
xmax = int(x[1][0:3])
ymax = int(y[0][2:5])
ymin = int(y[1][0:3])


def step(origin,x,y):
    o1,o2 = origin
    o1 += x
    o2 += y
    if(o1 > 0):
        o1 -= 1
    elif (o1 < 0):
        o1 += 1
    o2 -= 1
    
    return(o1,o2)


def checkTarget(x,y):
    if(x >= xmin and x <= xmax and y >= ymax and y <= ymin):
        print("on target")
        return True
    else:
        return False
    
def checkPass(x,y):
    if(x > xmax and y < ymax):
        return True
    elif(x > xmax):
        return True
    elif(y < ymax):
        return True
    else:
        return False
       

start = (0,0)
currX = 0
currY = 0
win = []
peaks = []

print(start)

#start = (step(start,5,4))
#print(step(start,5,4))
#print(checkPass(start[0],start[1]))

for xV in range(1,100):
    for yV in range(-30,100):
        print(xV,yV)
        peak = 0
        
        currX,currY = step(start,xV,yV)

        if xV == 1 and yV == 1:
            break;
        
        while not checkTarget(currX,currY):
            currX,currY = step((currX,currY),xV,yV)
            if currY > peak:
                peak = currY
            
            if checkPass(currX,currY):
                print("failed")
                break;
                
        if checkTarget(currX,currY):
            print("OMG")
            win.append((currX,currY))
            peaks.append(peak)
        
     
print(win)        
print(max(peaks))        
        
        
        
        
        
        
        

