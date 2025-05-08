import unittest


def hamming_distance(s, t):
    if len(s) != len(t):
        return -1
    c = 0
    for i in range(len(s)):
        if s[i] != t[i]:
            c += 1
    return c


# Mην αλλάξετε κάτι από εδώ και κάτω
class TestHammingDistance(unittest.TestCase):
    def test_HD(self):
        self.assertEqual(hamming_distance("G", ""), -1)
        self.assertEqual(hamming_distance("", "G"), -1)
        self.assertEqual(hamming_distance("G", "A"), 1)
        self.assertEqual(hamming_distance("G", "G"), 0)
        self.assertEqual(hamming_distance("GA", "GA"), 0)
        self.assertEqual(hamming_distance("GA", "AG"), 2)
        self.assertEqual(hamming_distance("AGCT", "AGCT"), 0)
        self.assertEqual(hamming_distance("AGCT", "TCGA"), 4)
        self.assertEqual(hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)


if __name__ == "__main__":
    unittest.main()
