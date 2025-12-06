import math

def parse_input(file_name):
    parsed = [[], []]
    with open(file_name, "r") as f:
        lines = f.readlines()
        operators_line = lines[-1]
        
        start = 0
        end = 0
        while end < len(operators_line):
            if end < len(operators_line)-1 and operators_line[end+1] == " ":
                end += 1
            else:
                parsed[1].append(operators_line[start:start+1])
                parsed[0].append([])
                if end == len(operators_line)-1:
                    end += 1
                for numbers_line in lines[:-1]:
                    parsed[0][-1].append(numbers_line[start:end])
                
                start = end+1
                end = start
            
    return parsed

def part1(file_name):
    ans = 0
    numbers, operators = parse_input(file_name)
    for i in range(len(operators)):
        op = operators[i]
        nums = numbers[i]
        cur = 1 if op == "*" else 0
        for num in nums:
            if op == "*":
                cur *= int(num)
            else:
                cur += int(num)
        ans += cur
    return ans

def part2(file_name):
    ans = 0
    numbers, operators = parse_input(file_name)
    for i in range(len(operators)):
        op = operators[i]
        nums = numbers[i]
        cur = 1 if op == "*" else 0
        colNums = {}
        for num in nums:
            for j in range(len(num)):
                if num[j].isnumeric():
                    if j not in colNums:
                        colNums[j] = ""
                    colNums[j] += num[j]
        for num in colNums.values():
            if op == "*":
                cur *= int(num)
            else:
                cur += int(num)
        ans += cur
    return ans

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
