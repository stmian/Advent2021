

import numpy as np


with open("input.txt", 'r') as f:
    data = [list(i) for i in f.read().splitlines()]

print(data)

running = False

grid = np.asarray(data)

print(grid)