from ortools.sat.python import cp_model


def solve_send_more_money():
    model = cp_model.CpModel()

    letters = {}
    for ch in "SENDMORY":
        letters[ch] = model.NewIntVar(0, 9, ch)

    S = letters["S"]
    E = letters["E"]
    N = letters["N"]
    D = letters["D"]
    M = letters["M"]
    O = letters["O"]
    R = letters["R"]
    Y = letters["Y"]

    # Όλα τα γράμματα πρέπει να έχουν διαφορετικές τιμές
    model.AddAllDifferent(list(letters.values()))

    # Τα πρώτα ψηφία δεν μπορούν να είναι μηδέν
    model.Add(S != 0)
    model.Add(M != 0)

    send = 1000*S + 100*E + 10*N + D
    more = 1000*M + 100*O + 10*R + E
    money = 10000*M + 1000*O + 100*N + 10*E + Y

    # Βασικός περιορισμός του προβλήματος
    model.Add(send + more == money)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        for ch in "SENDMORY":
            print(ch, "=", solver.Value(letters[ch]))

        print(f"{'SEND  ='} {solver.Value(send):>5}")
        print(f"{'MORE  ='} {solver.Value(more):>5}")
        print(f"{'MONEY ='} {solver.Value(money):>5}")
    else:
        print("Δεν βρέθηκε λύση.")


solve_send_more_money()