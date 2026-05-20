class Interval:
    _cnt = 0

    @staticmethod
    def number_of_intervals():
        return Interval._cnt

    def __init__(self, f, t):
        if f >= t:
            raise ValueError('To "από" πρέπει να είναι μικρότερο του "μέχρι"')
        self._from = f
        self._to = t
        Interval._cnt += 1

    @property
    def length(self):
        return self._to - self._from

    @length.setter
    def length(self, new_length):
        self._to = self._from + new_length

    def __str__(self):
        return f"[{self._from},{self._to})"

    def __repr__(self):
        return f"{self._from=} {self._to=}"


def main():
    for _ in range(5):
        try:
            f, t = input('Δώσε "από", "μέχρι" όρια διαστήματος: ').split()
            f = int(f)
            t = int(t)
            an_interval = Interval(f, t)
            print(an_interval)
            an_interval.length = 10
            print(repr(an_interval))
        except ValueError as ve:
            print(ve)
    print(
        f"Το πλήθος έγκυρων διαστημάτων που εισήχθησαν είναι {Interval.number_of_intervals()}"
    )


if __name__ == "__main__":
    main()
