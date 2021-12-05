from typing import List


class Solver:
    rows: int
    colums: int
    map_data: List[str]

    def __init__(self, input: str):
        self.map_data = []
        for line in input.split("\n"):
            s = line.strip()
            if s == "":
                continue

            self.map_data.append(s)

        self.rows = len(self.map_data)
        self.cols = len(self.map_data[0])

    def part1(self) -> int:
        row = 0
        col = 0
        ret = 0

        while row < self.rows:
            if self.map_data[row][col] == '#':
                ret += 1

            row += 1
            col = (col + 3) % self.cols

        return ret


def test() -> None:
    data = """
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
"""

    s = Solver(data)
    assert s.part1() == 7


def main() -> None:
    test()

    with open('input.txt', 'r') as f:
        data = f.read()

    s = Solver(data)
    part1 = s.part1()
    assert part1 == 299
    print(f"part1: {part1}")


if __name__ == '__main__':
    main()
