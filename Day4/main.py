# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:52:19 2021

@author: Sami
"""
import numpy as np
from numpy.core.numeric import correlate

with open("input.txt", 'r') as f:
    dir = [i for i in f.read().splitlines()]


inputs = dir[0].split(',')

blanks = [idx for idx, line in enumerate(dir) if line == ""]


sheets={}
cards = []

for b in blanks:
    sheets["b%s" %b] = dir[b+1:b+6]
    for row in sheets["b%s" %b]:
        row = row.split()
        row = [int(r.rstrip()) for r in row]
        cards.append(row)

completed = []
results = []
callList = []
left = 10000

def checkBingo(call):
    for sel in range(0,len(cards),5):
        if(sel in completed):
            pass;
        else:
            currCard = cards[sel:sel+5]
            curr = np.vstack((currCard)) 
    #      print(curr)  
            rowTotals = curr.sum(axis=1) 
            colTotals = curr.sum(axis=0)
            diag1 = curr[0][0] + curr[1][1] + curr[2][2] + curr[3][3] + curr[4][4]
            diag2 = curr[4][0] + curr[3][1] + curr[2][2] + curr[3][1] + curr[0][4]
            if -5 in rowTotals or -5 in colTotals or diag1 == -5 or diag2 == -5:
            #    print(sel)
                completed.append(sel)
                left = len(blanks)- len(completed)
                res = 0
                for valueR in currCard:
                    for valueC in valueR:
                        if valueC > -1:
                            res += valueC
                results.append(res)
                if(left == 0):
                    print(res)
                    print(call)
    callList.append(call)

                
    return 0;        

  
for call in inputs:

    for card in cards:
        if int(call) in card:
            loc = card.index(int(call))
            card[loc] = -1
    checkBingo(call)

print(results)
print(callList)
#print(len(results),len(callList))

for it in results:
    if int(it) > 0:
        print(4880 / int(it) , it)
