from ortools.sat.python import cp_model


def solve_single_machine_weighted_tardiness():
    model = cp_model.CpModel()

    # Δεδομένα
    processing_times = [12, 8, 15, 6, 20, 7, 10, 14, 9, 11]
    weights = [4, 2, 5, 3, 6, 1, 4, 7, 2, 5]
    due_dates = [25, 20, 35, 18, 45, 30, 28, 40, 32, 38]

    n = len(processing_times)
    horizon = sum(processing_times)

    starts = []
    ends = []
    intervals = []
    tardiness = []

    for j in range(n):
        start = model.NewIntVar(0, horizon, f"start[{j}]")
        end = model.NewIntVar(0, horizon, f"end[{j}]")

        interval = model.NewIntervalVar(
            start,
            processing_times[j],
            end,
            f"interval[{j}]"
        )

        t = model.NewIntVar(0, horizon, f"tardiness[{j}]")

        # T_j = max(C_j - d_j, 0)
        model.Add(t >= end - due_dates[j])
        model.Add(t >= 0)

        starts.append(start)
        ends.append(end)
        intervals.append(interval)
        tardiness.append(t)

    # Η μηχανή εκτελεί μόνο μία εργασία κάθε χρονική στιγμή
    model.AddNoOverlap(intervals)

    # Ελαχιστοποίηση συνολικής σταθμισμένης καθυστέρησης
    model.Minimize(
        sum(weights[j] * tardiness[j] for j in range(n))
    )

    solver = cp_model.CpSolver()

    # Προαιρετικά: χρονικό όριο
    solver.parameters.max_time_in_seconds = 30

    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        print("Κατάσταση λύσης:", solver.StatusName(status))
        print("Τιμή αντικειμενικής συνάρτησης:", int(solver.ObjectiveValue()))
        print()

        schedule = []

        for j in range(n):
            start = solver.Value(starts[j])
            end = solver.Value(ends[j])
            t = solver.Value(tardiness[j])
            weighted_tardiness = weights[j] * t

            schedule.append((
                start,
                end,
                j,
                processing_times[j],
                due_dates[j],
                weights[j],
                t,
                weighted_tardiness
            ))

        schedule.sort()

        print("Πρόγραμμα εκτέλεσης:")
        print(
            f"{'Job':>3} | {'Start':>5} | {'End':>5} | "
            f"{'p_j':>4} | {'d_j':>4} | {'w_j':>4} | "
            f"{'T_j':>4} | {'w_j*T_j':>7}"
        )
        print("-" * 58)

        for start, end, j, p, d, w, t, wt in schedule:
            print(
                f"{j:>3} | {start:>5} | {end:>5} | "
                f"{p:>4} | {d:>4} | {w:>4} | "
                f"{t:>4} | {wt:>7}"
            )

        print()
        print("Σειρά εργασιών:", [j for _, _, j, _, _, _, _, _ in schedule])

    else:
        print("Δεν βρέθηκε λύση.")


solve_single_machine_weighted_tardiness()