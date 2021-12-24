

import numpy as np

D = []
for line in open('input.txt', 'r').readlines():
    p1 = line.rstrip().split(' ')
    D.append(p1)

print(D)


x = 0 ; y = 0; z = 0; w = 0
A = 0
B = 0

def inp(w,a):
    a = w;
    return a

def add(a,b):
    a = a+b
    return a

def mul(a,b):
    a = a*b
    return a

def div(a,b):
    a = a//b
    return a

def mod(a,b):
    a = a % b
    return a

def eql(a,b):
    if a == b:
        return 1
    else:
        return 0    #A

