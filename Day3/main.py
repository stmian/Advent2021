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




import numpy as np
import pandas as pd

data = np.genfromtxt('input.txt',dtype=str)
data_df = pd.DataFrame(data=[list(i) for i in data])


# Part One

bin_num = data_df.mode().sum().sum()
b1 = data_df.mode()
b2 = data_df.mode().sum()
gamma = int(bin_num,2)
inverted_bin = ''.join([str(1 - int(i)) for i in bin_num])
epsilon = int(inverted_bin,2)

print(gamma * epsilon)


#### Part 2

binO = data_df
bin1 = data_df[0].value_counts()
bin2 = data_df[0]



ox_gen_df = data_df.copy()
for digit in ox_gen_df.columns:
    mode = ox_gen_df[digit].mode()
    if len(mode) > 1:
        ox_gen_df = ox_gen_df[ox_gen_df[digit].values == '1']
    else:
        ox_gen_df = ox_gen_df[ox_gen_df[digit].values == mode.iloc[0]]
    if len(ox_gen_df) == 1:
        ox = int(ox_gen_df.iloc[0].sum(),2)
        break

CO2_scrub_df = data_df.copy()
for digit in CO2_scrub_df.columns:
    mode = CO2_scrub_df[digit].mode()
    if len(mode) > 1:
        CO2_scrub_df = CO2_scrub_df[CO2_scrub_df[digit].values == '0']
    else:
        CO2_scrub_df = CO2_scrub_df[CO2_scrub_df[digit].values == str(1-int(mode.iloc[0]))]
    if len(CO2_scrub_df) == 1:
        CO2 = int(CO2_scrub_df.iloc[0].sum(),2)
        break
        
print(ox * CO2)


