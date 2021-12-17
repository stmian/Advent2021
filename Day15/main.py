# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 01:12:28 2021

@author: Sami
"""

import numpy as np
data = open("input.txt").read().strip().split("\n")
data2 = [list(i) for i in data]
grid = np.asarray(data2)


