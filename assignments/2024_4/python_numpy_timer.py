import os
from timeit import default_timer as timer

import numpy as np
from core import quicksort_with_indices


def main(input_file_name):
    points = []
    distances = []
    with open(input_file_name, "r") as fp:
        while True:
            line = fp.readline()
            if not line:
                break
            a_point = tuple(float(x) for x in line.split())
            points.append(a_point)
            distance = np.sqrt(a_point[0] ** 2 + a_point[1] ** 2 + a_point[2] ** 2)
            distances.append(distance)

    sorted_indices_distances = np.argsort(distances)

    # υλοποίηση του argsort (λιγότερο γρήγορο σε σχέση με το np.argsort)
    # sorted_indices_distances = np.arange(len(distances))
    # quicksort_with_indices(distances, sorted_indices_distances)

    output_file_name = f"{input_file_name[:-4]}-sorted-python-numpy.txt"
    with open(output_file_name, "w") as fp:
        for si in sorted_indices_distances:
            a_point = points[si]
            fp.write(f"{a_point[0]} {a_point[1]} {a_point[2]}\n")


if __name__ == "__main__":
    inputs = ["input1000.txt", "input100000.txt", "input1000000.txt"]
    for input in inputs:
        input = os.path.join(os.path.dirname(__file__), input)
        start = timer()
        main(input)
        time_passed = timer() - start
        print(f"{input} - elapsed time {time_passed:.6f}")
