import re
from sre_constants import ANY_ALL
from typing import List, Dict


def parse_input(input: str) -> List[Dict[str, str]]:
    regexp = re.compile(r'(\S+):(\S+)')
    ret: List[Dict] = []

    passport = {}
    for line in input.splitlines():
        line = line.strip()
        if line != "":
            for (key, value) in regexp.findall(line):
                passport[key] = value
        else:
            ret.append(passport)
            passport = {}

    if len(passport) != 0:
        ret.append(passport)
    return ret


def is_valid_passport(passport: Dict[str, str]) -> bool:
    birth_year = int(passport['byr'])
    if not (birth_year >= 1920 and birth_year <= 2002):
        print(f"## birth_year: {birth_year}")
        return False

    issue_year = int(passport['iyr'])
    if not (issue_year >= 2010 and issue_year <= 2020):
        print(f"## issue_year: {issue_year}")
        return False

    expiration_year = int(passport['eyr'])
    if not (expiration_year >= 2020 and expiration_year <= 2030):
        print(f"## expiration_year: {expiration_year}")
        return False

    match = re.search(r'^(\d+)(cm|in)$', passport['hgt'])
    if match:
        height = int(match.group(1))
        unit = match.group(2)
        if not ((unit == "cm" and height >= 150 and height <= 193) or (unit == "in" and height >= 59 and height <= 76)):
            print(f"## height: {passport['hgt']}")
            return False
    else:
        print(f"## height: {passport['hgt']}")
        return False

    hair_color = passport['hcl']
    if not re.search(r'^#[0-9a-f]{6}$', hair_color):
        print(f"## hair_color: {hair_color}")
        return False

    eye_color = passport['ecl']
    if not eye_color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        print(f"## eye_color: {eye_color}")
        return False

    passport_id = passport['pid']
    if not re.search(r'^[0-9]{9}$', passport_id):
        print(f"## passport_id: {passport_id}")
        return False

    return True


def part1(data: List[Dict[str, str]]) -> int:
    ret = 0
    required_key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in data:
        ok = True
        for key in required_key:
            if key not in passport:
                ok = False
                break

        if ok:
            ret += 1

    return ret


def part2(data: List[Dict[str, str]]) -> int:
    ret = 0
    required_key = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for passport in data:
        ok = True
        for key in required_key:
            if key not in passport:
                ok = False
                break

        if ok:
            if is_valid_passport(passport):
                ret += 1

    print(ret)
    return ret


def test():
    input = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in
"""
    data = parse_input(input)
    assert part1(data) == 2

    input = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719
"""
    data = parse_input(input)
    assert part2(data) == 4


def main() -> None:
    test()

    with open('input.txt', 'r') as f:
        input = f.read()

    data = parse_input(input)
    answer1 = part1(data)
    answer2 = part2(data)
    print(f"Part1: {answer1}")
    print(f"Part2: {answer2}")
    assert answer1 == 213
    assert answer2 == 147


main()
