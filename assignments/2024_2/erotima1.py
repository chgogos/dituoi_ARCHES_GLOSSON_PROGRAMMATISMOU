import os
import sys

import my_re_functions as mrf


def main(pgn_fn):
    games = []
    with open(pgn_fn, "r", encoding="latin-1") as f:
        game = ""
        for line in f:
            line = line.strip()
            if line:
                game += line + "\n"
                if (
                    line.endswith("1-0")
                    or line.endswith("0-1")
                    or line.endswith("1/2-1/2")
                ):
                    games.append(game.strip())
                    game = ""
    return games


if __name__ == "__main__":
    # pgn_fn = "WorldChamp2023.pgn"
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <filename.pgn>")
        exit(-1)
    pgn_fn = sys.argv[1]
    games = main(os.path.join(os.path.dirname(__file__), pgn_fn))
    flag = True
    for game in games:
        dt = mrf.date_of_game(game)
        if dt is not None:
            print(f"Ημερομηνία: {dt}")
        print(f"Νικητής: {mrf.winner(game)}")
        print(f"Διαφορά δυναμικότητας: {mrf.diff_elo(game)}")
        print(f"Πλήθος κινήσεων: {mrf.moves(game)}")
        if flag and games != games[-1]:
            c = input("Θέλεις να συνεχίσεις; (ε για επόμενο, ο για όλα, δ για διακοπή)")
            if c == "δ":
                exit(-1)
            if c == "ο":
                flag = False
