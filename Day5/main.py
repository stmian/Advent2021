# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 02:52:19 2021

@author: Sami
"""
import re 

with open("input.txt", 'r') as f:
    dir = [i for i in f.read().splitlines()]
    dir2 = [i.split(' -> ') for i in dir]
    dir3 = [i[:].split(',') for i in dir2]

