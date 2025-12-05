import math

DIRS = (
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1)
)

def parse_input(file_name):
    parsed = set()
    with open(file_name, "r") as f:
        for m, line in enumerate(f.readlines()):
            for n, c in enumerate(line.strip()):
                if c == "@":
                    parsed.add((m,n))
    return parsed

def count_adjacent(grid, m, n):
    adjacent = 0
    for y, x in DIRS:
        if (m+y, n+x) in grid:
            adjacent += 1
    return adjacent

def part1(file_name):
    ans = 0
    grid = parse_input(file_name)
    for m, n in grid:
        if count_adjacent(grid, m, n) < 4:
            ans += 1
    return ans

def part2(file_name):
    ans = 0
    prevAns = -1
    grid = parse_input(file_name)
    while ans != prevAns:
        prevAns = ans
        toRemove = []
        for m, n in grid:
            if count_adjacent(grid, m, n) < 4:
                ans += 1
                toRemove.append((m, n))
        for t in toRemove:
            grid.remove(t)
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
