import datetime
import unittest

from my_re_functions import a_pgn_game, date_of_game, diff_elo, moves, winner


class TestReFunctions(unittest.TestCase):
    def test_diff_elo(self):
        self.assertEqual(diff_elo(a_pgn_game), 7)

    def test_date_of_game(self):
        self.assertEqual(date_of_game(a_pgn_game), datetime.date(2023, 4, 9))

    def test_winner(self):
        self.assertEqual(winner(a_pgn_game), "ΙΣΟΠΑΛΙΑ")

    def test_moves(self):
        self.assertEqual(moves(a_pgn_game), "49")


if __name__ == "__main__":
    unittest.main()
