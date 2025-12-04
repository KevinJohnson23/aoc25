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
    parsed = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            parsed.append([1 if c == "@" else 0 for c in line.strip()])
    return parsed

def count_adjacent(grid, m, n):
    adjacent = 0
    for y, x in DIRS:
        if 0 <= m-y < len(grid) and 0 <= n-x < len(grid[0]):
            adjacent += grid[m-y][n-x]
    return adjacent

def part1(file_name):
    ans = 0
    grid = parse_input(file_name)
    for m in range(len(grid)):
        for n in range(len(grid[0])):
            if grid[m][n] == 0:
                continue
            if count_adjacent(grid, m, n) < 4:
                ans += 1
    return ans

def part2(file_name):
    ans = 0
    prevAns = -1
    grid = parse_input(file_name)
    while ans != prevAns:
        prevAns = ans
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    continue
                if count_adjacent(grid, m, n) < 4:
                    grid[m][n] = 0
                    ans += 1
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
