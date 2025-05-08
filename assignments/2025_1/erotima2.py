from erotima1 import compute
import unittest


class TestErotima1(unittest.TestCase):
    def test1(self):
        test_cases = [
            ("ΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩΩ", 0),
            ("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(10,10)", 100),
            ("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(10,10)ΠΟΛΛΑΠΛΑΣΙΑΣΕ(1,2)", 102),
            ("ΠΟΛΛΑΠΛΑΣΙΑΣΕ(10ΠΟΛΛΑΠΛΑΣΙΑΣΕ(1,2)ΧΧΧΧ", 2),
            (
                "μΖσ5ηΜκΑΩΠΟΛΛΑΠΛΑΣΙΑΣΕ(37,46)19Ν1ΝΒΠΟΛΛΑΠΛΑΣΙΑΣΕ(71,18)(20,35)0Σε4νΜ4ψΦκελ33ζβφΕ0ωνδσ9ξΒ0Χ6π5ΠΨΟλκοΥ",
                2980,
            ),
        ]
        for txt, result in test_cases:
            self.assertEqual(compute(txt), result)

    def test2(self):
        with open("test_multiplications1.txt", "r") as f:
            txt = f.read()
            self.assertEqual(compute(txt), 1035105)


if __name__ == "__main__":
    unittest.main()
