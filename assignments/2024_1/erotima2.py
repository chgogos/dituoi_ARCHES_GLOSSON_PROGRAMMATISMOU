import os
import unittest

from erotima1 import get_areas
from utils import mean, median, stdev


def load_points(filename):
    points = []
    with open(os.path.join(os.path.dirname(__file__), filename), "r") as f:
        for line in f:
            x, y = line.strip().split()
            points.append((int(x), int(y)))
    return points


class TestPoints(unittest.TestCase):
    def test_100_points_from_file(self):
        points = load_points("points.txt")
        areas = get_areas(points)
        self.assertEqual(len(areas), 161673)
        self.assertAlmostEqual(mean(areas), 3206.82, places=2)
        self.assertAlmostEqual(median(areas), 2392.50, places=2)
        self.assertAlmostEqual(stdev(areas), 2843.24, places=2)


if __name__ == "__main__":
    unittest.main()
