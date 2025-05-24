class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return f"({self.start},{self.end})"

    def __add__(self, other):
        return Interval(self.start + other.start, self.end + other.end)

    def __sub__(self, other):
        return Interval(self.start - other.end, self.end - other.start)

    def __mul__(self, other):
        minimum = min(
            [
                self.start * other.start,
                self.start * other.end,
                self.end * other.start,
                self.end * other.end,
            ]
        )
        maximum = max(
            [
                self.start * other.start,
                self.start * other.end,
                self.end * other.start,
                self.end * other.end,
            ]
        )
        return Interval(minimum, maximum)


i1 = Interval(1, 5)
i2 = Interval(4, 6)
print(i1 + i2)
print(i1 - i2)
print(i2 - i1)
print(i1 * i2)
