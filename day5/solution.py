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

def part1(file_name):
    ans = 0
    ranges, ingredients = parse_input(file_name)
    for ingredient in ingredients:
        for start, end in ranges:
            if start <= ingredient <= end:
                ans += 1
                break
    return ans

def part2(file_name):
    ans = 0
    ranges, _ingredients = parse_input(file_name)
    mergedRanges = []
    for start, end in sorted(ranges):
        if mergedRanges and mergedRanges[-1][1] >= start:
            mergedRanges[-1][1] = max(mergedRanges[-1][1], end)
        else:
            mergedRanges.append([start, end])
    for start, end in mergedRanges:
        ans += (end-start)+1
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
