import sys
from core import quicksort
from math import sqrt


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

    points = quicksort(points)

    output_file_name = f"{input_file_name[:-4]}-sorted-python-plain.txt"
    with open(output_file_name, "w") as fp:
        for a_point in points:
            fp.write(f"{a_point[1]} {a_point[2]} {a_point[3]}\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(
            f"Wrong number of command line arguments. \nUse: python {sys.argv[0]} input1000.txt"
        )
        exit()
    main(sys.argv[1])
