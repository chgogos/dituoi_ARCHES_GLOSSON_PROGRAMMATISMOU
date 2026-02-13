import os

import matplotlib.pyplot as plt
import my_re_functions as mrf


def get_games(pgn_fn):
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


def main(pgn_fn):
    day_names = [
        "ΔΕΥΤΕΡΑ",
        "ΤΡΙΤΗ",
        "ΤΕΤΑΡΤΗ",
        "ΠΕΜΠΤΗ",
        "ΠΑΡΑΣΚΕΥΗ",
        "ΣΑΒΒΑΤΟ",
        "ΚΥΡΙΑΚΗ",
    ]
    games_nr = [0] * 7
    games = get_games(os.path.join(os.path.dirname(__file__), pgn_fn))
    total_games = 0
    for game in games:
        dt = mrf.date_of_game(game)
        if dt is not None:
            games_nr[dt.weekday()] += 1
            total_games += 1
    print(list(zip(day_names, games_nr)))
    print(f"{total_games=}")
    plt.bar(day_names, games_nr, color='mediumseagreen')
    plt.ylabel('Αγώνες')
    plt.show()


if __name__ == "__main__":
    pgn_fn = "RetiKIA.pgn"
    main(pgn_fn)
