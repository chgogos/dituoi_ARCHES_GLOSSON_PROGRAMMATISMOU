import random


class Dice:
    def __init__(self, probs):
        self.probs = probs

    @classmethod
    def from_sides(cls, n=6):
        return Dice({i: 1 / n for i in range(1, n + 1)})

    def roll(self, n=1):
        sides = list(self.probs.keys())
        probabilities = list(self.probs.values())
        return random.choices(sides, weights=probabilities, k=n)

    @property
    def expected_value(self):
        return sum(i * p for i, p in self.probs.items())

    def __len__(self):
        return len(self.probs)

    def __add__(self, other):
        if not isinstance(other, Dice):
            raise ValueError("Only dice + dice is allowed!")
        new_probs = {}
        for s1, p1 in self.probs.items():
            for s2, p2 in other.probs.items():
                new_key = s1 + s2
                if new_key not in new_probs:
                    new_probs[new_key] = 0
                new_probs[new_key] += p1 * p2
        return Dice(new_probs)

    def __repr__(self):
        return f"Dice({self.probs})"

    def __str__(self):
        sides = ", ".join(map(str, self.probs.keys()))
        return f"Dice with sides: {sides}"


if __name__ == "__main__":
    d6 = Dice({1: 1 / 6, 2: 1 / 6, 3: 1 / 6, 4: 1 / 6, 5: 1 / 6, 6: 1 / 6})
    print(repr(d6))
    print(str(d6))
    print(f"Rolls: {d6.roll(5)}")
    print(f"Expected value of d6 = {d6.expected_value}, sides = {len(d6)}")

    d4 = Dice.from_sides(4)
    print(repr(d4))
    print(str(d4))
    print(f"Rolls: {d4.roll(5)}")
    print(f"Expected value of d4 = {d4.expected_value}, sides = {len(d4)}")

    d6_d4 = d6 + d4
    print(repr(d6_d4))
    print(str(d6_d4))
    print(f"Rolls: {d6_d4.roll(5)}")
    print(f"Expected value of d6_d4 = {d6_d4.expected_value}, sides = {len(d6_d4)}")
