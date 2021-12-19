

#Part 1
D = []

for line in open('input.txt', 'r').readlines():
    p1, p2 = line.rstrip().split('-')
    D.append((p1, p2))

M = {}
path = []


def traverse(cave):
    global current_path
    for x in cave:
        if x.islower() and x in current_path:
            continue
        elif x == 'end':
            current_path.append(x)
            path.append(current_path[:])
            current_path.pop()
        else:
            current_path.append(x)
            traverse(M[x])
    current_path.pop()



for a in D:
    if a[0] not in M:
        M[a[0]] = []
    M[a[0]].append(a[1])
    if a[1] not in M:
        M[a[1]] = []
    M[a[1]].append(a[0])

current_path = ["start"]
traverse(M["start"])

print(len(path))

#Part 2

D = []

for line in open('input.txt', 'r').readlines():
    p1, p2 = line.rstrip().split('-')
    D.append((p1, p2))

M = {}
path = []


def traverse(cave):
    global current_path
    global second_small
    for x in cave:
        if x.islower() and x in current_path:
            if not second_small[0] and x != "start" and x != "end":
                second_small = (True, x)
                current_path.append(x)
                traverse(M[x])
            continue
        elif x == 'end':
            current_path.append(x)
            path.append(current_path[:])
            current_path.pop()
        else:
            current_path.append(x)
            traverse(M[x])
    if current_path.pop() == second_small[1]:
        second_small = (False, "")


for a in D:
    if a[0] not in M:
        M[a[0]] = []
    M[a[0]].append(a[1])
    if a[1] not in M:
        M[a[1]] = []
    M[a[1]].append(a[0])

current_path = ["start"]
second_small = (False, "")
traverse(M["start"])

print(len(path))