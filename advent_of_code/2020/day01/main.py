#!/usr/bin/env python
from typing import List, Set


def add_two_2020(nums: List[int]) -> int:
    s: Set[int] = set(nums)
    for num in nums:
        diff = 2020 - num
        if diff in s:
            return num * diff

    raise Exception("never reach here")


def add_three_2020(nums: List[int]) -> int:
    s: Set[int] = set(nums)

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            diff = 2020 - nums[i] - nums[j]
            if diff in s:
                return diff * nums[i] * nums[j]

    raise Exception("never reach here")


test_data: List[int] = [1721, 979, 366, 299, 675, 1456]
assert add_two_2020(test_data) == 514579
assert add_three_2020(test_data) == 241861950

data: List[int] = []
with open('input.txt', 'r') as f:
    for line in f.readlines():
        data.append(int(line))

part1 = add_two_2020(data)
part2 = add_three_2020(data)

assert part1 == 157059
assert part2 == 165080960

print(f"part1 = {part1}")
print(f"part2 = {part2}")
