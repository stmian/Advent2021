with open("input.txt", 'r') as f:
    dir = [i for i in f.read().splitlines()]

arr = [] 

for n, line in enumerate(dir):
#    print(line)
    arr.append(line.split())

ones = [0,0,0,0,0,0,0,0,0,0,0,0]
zeros = [0,0,0,0,0,0,0,0,0,0,0,0]

for row in arr:
    for idx, entry in enumerate(row[0]):
        if entry == "1":
            ones[idx] += 1
        elif entry == "0":
            zeros[idx] += 1

gamma = ""
epsilon = ""

for i, e in enumerate(ones):
    if(ones[i] > zeros[i]):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"        

print(int(gamma, 2) *int(epsilon, 2))


#### Part 2

import numpy as np
import pandas as pd

data = np.genfromtxt('input.csv',dtype=str)
data_df = pd.DataFrame(data=[list(i) for i in data])
