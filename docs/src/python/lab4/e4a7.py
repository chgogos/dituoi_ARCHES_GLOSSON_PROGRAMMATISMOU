class Length:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value}{self.unit}"

    def __repr__(self):
        return f"value={self.value} unit={self.unit}"

    def __add__(self, another_length):
        if self.unit == another_length.unit:
            return Length(self.unit, self.value + another_length.value)
        total_length = 0
        if self.unit == "in":
            total_length += self.value * 2.54
        else:
            total_length += self.value
        if another_length.unit == "in":
            total_length += another_length.value * 2.54
        else:
            total_length += another_length.value
        return Length(total_length, "cm")


def main():
    a = Length(5.5, "cm")
    b = Length(3.0, "in")

    print("Εκτύπωση αντικειμένου με τη μέθοδο __str__")
    print(a)
    print(str(a))
    print(a.__str__())

    print("Εκτύπωση αντικειμένου με τη μέθοδο __repr__")
    print(repr(b))
    print(b.__repr__())

    print("Υπερφόρτωση τελεστή +")
    c = a + b
    print(f"{a} + {b} = {c}")


if __name__ == "__main__":
    main()
