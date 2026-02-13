import os

from core import quicksort
from math import sqrt
from timeit import default_timer as timer


def main(input_file_name):
    points = []
    with open(input_file_name, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            a_point = tuple(float(x) for x in line.split())
            distance = sqrt(a_point[0] ** 2 + a_point[1] ** 2 + a_point[2] ** 2)
            points.append((distance,) + a_point)

    start = timer()
    # points = quicksort(points)
    points.sort()
    time_passed = timer() - start
    print(f"Elapsed time for sorting alone: {time_passed:.6f}")

    output_file_name = f"{input_file_name[:-4]}-sorted-python-plain.txt"
    output_file_name = os.path.join(os.path.dirname(__file__), output_file_name)
    with open(output_file_name, "w") as fp:
        for a_point in points:
            fp.write(f"{a_point[1]} {a_point[2]} {a_point[3]}\n")


if __name__ == "__main__":
    inputs = ["input1000.txt", "input100000.txt", "input1000000.txt"]
    for input in inputs:
        input = os.path.join(os.path.dirname(__file__), input)
        start = timer()
        main(input)
        time_passed = timer() - start
        print(f"{input} - elapsed time {time_passed:.6f}")
