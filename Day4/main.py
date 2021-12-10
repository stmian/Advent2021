# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:52:19 2021

@author: Sami
"""
import numpy as np

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




    
  
for call in inputs[1]:

    for card in cards:
        if int(call) in card:
            loc = card.index(int(call))
            card[loc] = -1




def checkBingo():
    for card in cards:
        
