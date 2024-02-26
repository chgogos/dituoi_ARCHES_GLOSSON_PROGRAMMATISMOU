import unittest


def is_pangram(s):
    greekletters = "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"
    a_set = set()
    for c in greekletters:
        a_set.add(c)

    for c in s.upper():
        if c in a_set:
            a_set.remove(c)

    return len(a_set) == 0


# συντομότερη λύση
# def is_pangram(s):
#     return len({c for c in "ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"} - {c for c in s}) == 0


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestPantogram(unittest.TestCase):
    def test(self):
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"), True)
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ"[::-1]), True)
        self.assertEqual(is_pangram("ΞΕΣΚΕΠΑΖΩ ΤΗΝ ΨΥΧΟΦΘΟΡΟ ΒΔΕΛΥΓΜΙΑ"), True)
        self.assertEqual(
            is_pangram(
                "Ο ΚΑΛΥΜΝΙΟΣ ΣΦΟΥΓΓΑΡΑΣ ΨΙΘΥΡΙΣΕ ΠΩΣ ΘΑ ΒΟΥΤΗΞΕΙ ΧΩΡΙΣ ΝΑ ΔΙΣΤΑΖΕΙ"
            ),
            True,
        )
        self.assertEqual(is_pangram(""), False)
        self.assertEqual(is_pangram("A" * 24), False)
        self.assertEqual(is_pangram("ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨA"), False)


if __name__ == "__main__":
    unittest.main()
