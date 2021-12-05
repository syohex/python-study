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

    def _count_tree(self, row_step: int, col_step: int) -> int:
        row = 0
        col = 0
        ret = 0

        while row < self.rows:
            if self.map_data[row][col] == '#':
                ret += 1

            row += row_step
            col = (col + col_step) % self.cols

        return ret

    def part1(self) -> int:
        return self._count_tree(1, 3)

    def part2(self) -> int:
        ret = 1
        steps = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
        for (row_step, col_step) in steps:
            ret *= self._count_tree(row_step, col_step)

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
    assert s.part2() == 336


def main() -> None:
    test()

    with open('input.txt', 'r') as f:
        data = f.read()

    s = Solver(data)
    part1 = s.part1()
    part2 = s.part2()
    assert part1 == 299
    assert part2 == 3621285278

    print(f"part1: {part1}")
    print(f"part2: {part2}")


if __name__ == '__main__':
    main()
