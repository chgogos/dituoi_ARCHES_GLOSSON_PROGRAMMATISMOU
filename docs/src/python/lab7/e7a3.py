from ortools.sat.python import cp_model


def solve_n_queens(n):
    model = cp_model.CpModel()

    # q[i] = η στήλη στην οποία τοποθετείται η βασίλισσα της γραμμής i
    q = []
    for i in range(n):
        q.append(model.NewIntVar(0, n - 1, f"q[{i}]"))

    # Καμία δύο βασίλισσες στην ίδια στήλη
    model.AddAllDifferent(q)

    # Περιορισμοί για τις διαγωνίους
    for i in range(n):
        for j in range(i + 1, n):
            # Δεν πρέπει να βρίσκονται στην ίδια κύρια διαγώνιο
            model.Add(q[i] - i != q[j] - j)

            # Δεν πρέπει να βρίσκονται στην ίδια δευτερεύουσα διαγώνιο
            model.Add(q[i] + i != q[j] + j)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        print()

        # Εμφάνιση θέσεων βασιλισσών
        for i in range(n):
            print(f"Γραμμή {i}: στήλη {solver.Value(q[i])}")

        print()
        print("Σκακιέρα:")
        print_board(q, solver, n)

    else:
        print(f"Δεν βρέθηκε λύση!!!")


def print_board(q, solver, n):
    for i in range(n):
        row = []
        queen_col = solver.Value(q[i])

        for j in range(n):
            if j == queen_col:
                row.append("Q")
            else:
                row.append(".")

        print(" ".join(row))


solve_n_queens(8)