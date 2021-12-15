octopodes = [[int(c) for c in line.strip()] for line in open("input.txt", "r").readlines()]
R = len(octopodes)
C = len(octopodes[0])


def neighbours(r, c):
    for dr, dc in [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]:
        if 0 <= r + dr < R and 0 <= c + dc < C:
            yield r + dr, c + dc


def count_flashes(has_been_flashed):
    return sum(1 for line in has_been_flashed for has_been in line if has_been)


def simulate_octopodes(octs):
    has_been_flashed = [[False for _ in range(R)] for __ in range(C)]

    for r in range(R):
        for c in range(C):
            octs[r][c] += 1
    flashes = -1
    while flashes != count_flashes(has_been_flashed):
        flashes = count_flashes(has_been_flashed)
        for r in range(R):
            for c in range(C):
                if octs[r][c] == 10 and not has_been_flashed[r][c]:
                    for rr, cc in neighbours(r, c):
                        octs[rr][cc] = min(octs[rr][cc] + 1, 10)
                    has_been_flashed[r][c] = True
    for r in range(R):
        for c in range(C):
            octs[r][c] %= 10

    return octs, flashes


def count_flashes_over_time_steps(octs, number_of_time_steps):
    total = 0
    for _ in range(number_of_time_steps):
        octs, count = simulate_octopodes(octs)
        total += count
    return total


def find_first_synchronization_time(octs):
    all_equal = all(octs[0][0] == octopus for line in octs for octopus in line)
    time = 0
    while not all_equal:
        octs, _ = simulate_octopodes(octs)
        all_equal = all(octs[0][0] == octopus for line in octs for octopus in line)
        time += 1
    return time


print("Part 1:", count_flashes_over_time_steps([[o for o in os] for os in octopodes], 5))
print("Part 2:", find_first_synchronization_time([[o for o in os] for os in octopodes]))