import re
from datetime import datetime

a_pgn_game = """
[Event "WCh 2023"]
[Site "Astana KAZ"]
[Date "2023.04.09"]
[Round "1.1"]
[White "Nepomniachtchi,I"]
[Black "Ding Liren"]
[Result "1/2-1/2"]
[WhiteElo "2795"]
[BlackElo "2788"]
[ECO "C85"]

1.e4 e5 2.Nf3 Nc6 3.Bb5 a6 4.Ba4 Nf6 5.O-O Be7 6.Bxc6 dxc6 7.Re1 Nd7 8.d4 exd4
9.Qxd4 O-O 10.Bf4 Nc5 11.Qe3 Bg4 12.Nd4 Qd7 13.Nc3 Rad8 14.Nf5 Ne6 15.Nxe7+ Qxe7
16.Bg3 Bh5 17.f3 f6 18.h3 h6 19.Kh2 Bf7 20.Rad1 b6 21.a3 a5 22.Ne2 Rxd1 23.Rxd1 Rd8
24.Rd3 c5 25.Qd2 c6 26.Rxd8+ Nxd8 27.Qf4 b5 28.Qb8 Kh7 29.Bd6 Qd7 30.Ng3 Ne6
31.f4 h5 32.c3 c4 33.h4 Qd8 34.Qb7 Be8 35.Nf5 Qd7 36.Qb8 Qd8 37.Qxd8 Nxd8
38.Nd4 Nb7 39.e5 Kg8 40.Kg3 Bd7 41.Bc7 Nc5 42.Bxa5 Kf7 43.Bb4 Nd3 44.e6+ Bxe6
45.Nxc6 Bd7 46.Nd4 Nxb2 47.Kf3 Nd3 48.g3 Nc1 49.Ke3  1/2-1/2
"""


def winner(a_pgn_game):
    result = re.compile(r'\[Result "(.*)"\]').search(a_pgn_game).group(1)
    if result == "1/2-1/2":
        return "ΙΣΟΠΑΛΙΑ"
    if result == "1-0":
        return "ΛΕΥΚΑ"
    if result == "0-1":
        return "ΜΑΥΡΑ"


def date_of_game(a_pgn_game):
    pattern = re.compile(r'\[Date "(.*)"\]')
    match = pattern.search(a_pgn_game)
    a_date = match.group(1)
    if a_date is None:
        return None
    try:
        dt = datetime.strptime(a_date, "%Y.%m.%d")
        return dt.date()
    except ValueError:
        return None


def diff_elo(a_pgn_game):
    w_elo = int(re.compile(r'\[WhiteElo "(\d+)"\]').search(a_pgn_game).group(1))
    b_elo = int(re.compile(r'\[BlackElo "(\d+)"\]').search(a_pgn_game).group(1))
    return abs(w_elo - b_elo)


def moves(a_pgn_game):
    results = re.compile(r"(\d+)\.").findall(a_pgn_game)
    return results[-1]


if __name__ == "__main__":
    print(f"ΔΙΑΦΟΡΑ ΔΥΝΑΜΙΚΟΤΗΤΑΣ: {diff_elo(a_pgn_game)}")
    print(f"ΝΙΚΗΤΗΣ: {winner(a_pgn_game)}")
    dts = datetime.strftime(date_of_game(a_pgn_game), "%d-%m-%Y")
    print(f"ΗΜΕΡΟΜΗΝΙΑ ΑΓΩΝΑ: {dts}")
    print(f"ΠΛΗΘΟΣ ΚΙΝΗΣΕΩΝ: {moves(a_pgn_game)}")