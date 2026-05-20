def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def area(x1, y1, x2, y2, x3, y3):
    a = distance(x1, y1, x2, y2)
    b = distance(x2, y2, x3, y3)
    c = distance(x3, y3, x1, y1)
    s = (a + b + c) / 2
    if s * (s - a) * (s - b) * (s - c) <= 0:
        raise ValueError(
            f"Invalid triangle with sides {a}, {b}, {c} and semiperimeter {s}, points {x1, y1}, {x2, y2}, {x3, y3}"
        )
    return (s * (s - a) * (s - b) * (s - c)) ** 0.5


def mean(values):
    return sum(values) / len(values)


def median(values):
    values.sort()
    n = len(values)
    if n % 2 == 0:
        return (values[n // 2 - 1] + values[n // 2]) / 2
    else:
        return values[n // 2]


def stdev(values):
    m = mean(values)
    return (sum((x - m) ** 2 for x in values) / len(values)) ** 0.5
