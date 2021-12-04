#!/usr/bin/env python
import re
from dataclasses import dataclass
from typing import List


@dataclass
class PasswordData:
    first: int
    second: int
    char: str
    value: str

    def valid_part1(self) -> bool:
        count = 0
        for c in self.value:
            if c == self.char:
                count += 1

        return self.first <= count <= self.second

    def valid_part2(self) -> bool:
        if self.value[self.first - 1] == self.char and self.value[self.second - 1] == self.char:
            return False
        if self.value[self.first - 1] == self.char or self.value[self.second - 1] == self.char:
            return True
        return False


def parse_input(input_str: str) -> List[PasswordData]:
    ret: List[PasswordData] = []
    for line in input_str.split("\n"):
        line = line.strip()
        if line == "":
            continue

        match = re.match(r"^(\d+)-(\d+)\s+([^:]+):\s+(.+)$", line)
        if match:
            first = int(match.group(1))
            second = int(match.group(2))
            char = match.group(3)
            value = match.group(4)
            ret.append(PasswordData(first, second, char, value))

    return ret


def part1(passwords: List[PasswordData]) -> int:
    ret = 0
    for data in passwords:
        if data.valid_part1():
            ret += 1

    return ret


def part2(passwords: List[PasswordData]) -> int:
    ret = 0
    for data in passwords:
        if data.valid_part2():
            ret += 1

    return ret


def test():
    test_data = r"""
    1-3 a: abcde
    1-3 b: cdefg
    2-9 c: ccccccccc
    """

    password_data = parse_input(test_data)
    assert part1(password_data) == 2
    assert part2(password_data) == 1


def main() -> None:
    test()

    with open('input.txt', 'r') as f:
        data = f.read()
        passwords = parse_input(data)

    answer1 = part1(passwords)
    answer2 = part2(passwords)
    assert answer1 == 580
    assert answer2 == 611
    print(f"Part1: {answer1}")
    print(f"Part2: {answer2}")


if __name__ == '__main__':
    main()
