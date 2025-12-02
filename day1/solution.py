import math

def parse_input(file_name):
    parsed = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            num = int(line[1:])
            if line[0] == "L":
                num *= -1
            parsed.append(num)
    return parsed

def part1(file_name):
    ans = 0
    dial = 50
    for num in parse_input(file_name):
        dial += num
        dial %= 100
        if dial == 0:
            ans += 1
    return ans

def part2(file_name):
    ans = 0
    dial = 50
    for num in parse_input(file_name):
        if num > 0:
            ans += (dial+num) // 100 - dial // 100
        else:
            ans += (dial-1) // 100 - (dial-1+num) // 100
        dial += num
        dial %= 100

    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
