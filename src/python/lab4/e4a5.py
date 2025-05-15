import math


class Cylinder:
    def __init__(self, radius, height):
        self._radius = radius
        self._height = height

    def __str__(self):
        return (
            f"(ακτίνα={self._radius}, ύψος={self._height}, όγκος={self.volume():.2f})"
        )

    def volume(self):
        return math.pi * self._radius**2 * self._height


if __name__ == "__main__":
    list_of_cylinders = []
    for i in range(5):
        while True:
            try:
                r, h = input(f"Δώσε ακτίνα και ύψος για κύλιδρο {i+1}: ").split()
                r = float(r)
                h = float(h)
                if r > 0 and h > 0:
                    break
                else:
                    print("Λάθος τιμή, εισάγετε θετικές τιμές")
            except ValueError:
                print("Λάθος τιμή, εισάγετε αριθμητικές τιμές με υποδιαστολή την .")
        list_of_cylinders.append(Cylinder(r, h))

    list_of_cylinders.sort(reverse=True, key=lambda c: c.volume())

    for cyl in list_of_cylinders:
        print(cyl)
