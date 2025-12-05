import math

def parse_input(file_name):
    parsed = [[], []]
    with open(file_name, "r") as f:
        s = f.read().split("\n\n")
        for r in s[0].split("\n"):
            start, end = r.split("-")
            parsed[0].append([int(start), int(end)])
        for r in s[1].split("\n"):
            parsed[1].append(int(r))
    return parsed

def merge_ranges(ranges):
    merged_ranges = []
    for start, end in sorted(ranges):
        if merged_ranges and merged_ranges[-1][1] >= start:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)
        else:
            merged_ranges.append([start, end])
    return merged_ranges

def part1(file_name):
    ans = 0
    ranges, ingredients = parse_input(file_name)
    ranges = merge_ranges(ranges)
    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                ans += 1
                break
    return ans

def part2(file_name):
    ans = 0
    ranges, _ingredients = parse_input(file_name)
    ranges = merge_ranges(ranges)
    for start, end in ranges:
        ans += (end-start)+1
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
