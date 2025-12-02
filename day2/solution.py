from functools import cache
import math

def parse_input(file_name):
    parsed = []
    with open(file_name, "r") as f:
        for r in f.read().split(","):
            split = r.split("-")
            parsed.append((int(split[0]), int(split[1])))
    return parsed

@cache
def is_repeating_length(string, repeat_length):
    if len(string) % repeat_length != 0:
        return False
    return string == string[:repeat_length]*(len(string)//repeat_length)

def is_repeating(string):
    for repeat_length in range(1, len(string)//2+1):
        if is_repeating_length(string, repeat_length):
            return True
    return False

def part1(file_name):
    ans = 0
    for s, e in parse_input(file_name):
        for i in range(s, e+1):
            string = str(i)
            if len(string) % 2 != 0:
                continue
            if is_repeating_length(string, len(string)//2):
                ans += i
    return ans

def part2(file_name):
    ans = 0
    for s, e in parse_input(file_name):
        for i in range(s, e+1):
            string = str(i)
            if is_repeating(string):
                ans += i
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
