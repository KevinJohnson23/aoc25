import math

def parse_input(file_name):
    parsed = []
    with open(file_name, "r") as f:
        for line in f.readlines():
            parsed.append([int(x) for x in line.strip()])
    return parsed

def get_largest(nums, k):
    largest = 0

    prev = -1
    for i in range(k):
        curLargest = prev+1
        for j in range(prev+1, len(nums)-(k-i)+1):
            if nums[j] > nums[curLargest]:
                curLargest = j
        largest *= 10
        largest += nums[curLargest]
        prev = curLargest

    return largest

def solve(file_name, k):
    ans = 0
    for nums in parse_input(file_name):
        ans += get_largest(nums, k)
    return ans

def part1(file_name):
    return solve(file_name, 2)

def part2(file_name):
    return solve(file_name, 12)

if __name__ == "__main__":
    print(part1("input.txt"))
    print(part2("input.txt"))
