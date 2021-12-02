

with open("input.txt", 'r') as f:
    dir = [i for i in f.read().splitlines()]



hPos = 0
depth = 0
aim = 0

directions = {'forward' : 0, 'up' : 0, 'down' :0}

def parse(entry):
    val = entry.split()
    return (val[0],int(val[1]))

for val in dir:
    move, i = parse(val)
    directions[move] += i

    #Part 2 code below
    if(move == "forward"):
        hPos += i
        depth += i*aim
    elif(move == "up"):
        aim -= i

    elif(move == "down"):
        aim +=i

    print(depth,aim)

print("Part 1 Answer:")

print(directions["forward"] , directions['down'] , directions['up'],directions["forward"] * (directions['down'] - directions['up']))

print("Part 2 Answer:")
print(hPos , depth, hPos * depth) 

