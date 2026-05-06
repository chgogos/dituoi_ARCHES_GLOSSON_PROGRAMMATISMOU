import unittest
from itertools import (
    count,
    combinations,
    product,
    accumulate,
    cycle,
    islice,
)


def first_numbers(start, step, n):
    return list(islice(count(start, step), n))


def pair_combinations(items):
    return list(combinations(items, 2))


def cartesian_product(a, b):
    return list(product(a, b))


def cumulative_sums(numbers):
    return list(accumulate(numbers))


def repeat_pattern(pattern, n):
    return list(islice(cycle(pattern), n))


class TestItertools(unittest.TestCase):

    def test_count(self):
        self.assertEqual(
            first_numbers(0, 2, 5),
            [0, 2, 4, 6, 8]
        )

    def test_combinations(self):
        self.assertEqual(
            pair_combinations(["A", "B", "C"]),
            [("A", "B"), ("A", "C"), ("B", "C")]
        )

    def test_product(self):
        self.assertEqual(
            cartesian_product([1, 2], ["x", "y"]),
            [(1, "x"), (1, "y"), (2, "x"), (2, "y")]
        )

    def test_accumulate(self):
        self.assertEqual(
            cumulative_sums([1, 2, 3, 4]),
            [1, 3, 6, 10]
        )

    def test_cycle(self):
        self.assertEqual(
            repeat_pattern(["A", "B"], 5),
            ["A", "B", "A", "B", "A"]
        )


if __name__ == "__main__":
    unittest.main()