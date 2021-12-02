
from numpy import loadtxt
lines = loadtxt("input.txt", comments="#", delimiter=",", unpack=False)
counter = 0;
prev = 0;
for value in lines:
    
    if value > prev:
        counter += 1
    prev = value;    
print(counter-1)


with open("input.txt", 'r') as f:
    nums = [int(i) for i in f.read().splitlines()]

def day1_pt2(nums):
    return sum(b+c+d > a+b+c for a, b,c,d in zip(nums, nums[1:],nums[2:],nums[3:]))


print(day1_pt2(nums))

