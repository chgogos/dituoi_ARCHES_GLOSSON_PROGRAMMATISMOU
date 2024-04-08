import itertools
import os
import random
import statistics as stats

from utils import area, mean, median, stdev


def generate_points(n, seed=None):
    if seed:
        random.seed(seed)
    points = []
    for _ in range(n):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)
        points.append((x, y))
    return points


def save_points(points, filename):
    with open(os.path.join(os.path.dirname(__file__), filename), "w") as f:
        for x, y in points:
            f.write(f"{x} {y}\n")


# Λύση Α: με χρήση εμφωλευμένων for
# def get_areas(points):
#     areas = []
#     for i in range(len(points)):
#         for j in range(i + 1, len(points)):
#             for k in range(j + 1, len(points)):
#                 p1 = points[i]
#                 p2 = points[j]
#                 p3 = points[k]
#                 try:
#                     areas.append(area(*p1, *p2, *p3))
#                 except ValueError:
#                     pass
#     return areas


# Λύση Β: με χρήση του itertools
def get_areas(points):
    areas = []
    for i, j, k in itertools.combinations(range(len(points)), 3):
        p1 = points[i]
        p2 = points[j]
        p3 = points[k]
        try:
            areas.append(area(*p1, *p2, *p3))
        except ValueError:
            pass
    return areas


if __name__ == "__main__":
    points = generate_points(100, seed=12345)
    # save_points(points, "points.txt")
    areas = get_areas(points)
    print(f"Valid triangles: {len(areas)}")
    print(f"Mean   = {mean(areas):.2f}")
    print(f"Median = {median(areas):.2f}")
    print(f"Stdev  = {stdev(areas):.2f}")

    print("Using statistics module")
    print(f"Mean   = {stats.mean(areas):.2f}")
    print(f"Median = {stats.median(areas):.2f}")
    print(f"Stdev  = {stats.stdev(areas):.2f}")
