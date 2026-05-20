from pathlib import Path
from ortools.sat.python import cp_model


def read_wt_instance(filename, instance_number):
    """
    Διαβάζει ένα στιγμιότυπο από αρχείο wt40.txt, wt50.txt ή wt100.txt.

    Τα αρχεία της OR-Library έχουν 125 στιγμιότυπα.
    Για κάθε στιγμιότυπο:
        - πρώτα δίνονται οι n χρόνοι επεξεργασίας,
        - μετά τα n βάρη,
        - και τέλος οι n προθεσμίες.
    """

    if instance_number < 1 or instance_number > 125:
        raise ValueError("Ο αριθμός προβλήματος πρέπει να είναι από 1 έως 125.")

    filename = Path(filename)

    if not filename.exists():
        raise FileNotFoundError(f"Δεν βρέθηκε το αρχείο: {filename}")

    # Εντοπισμός πλήθους εργασιών από το όνομα του αρχείου
    if "wt40" in filename.name:
        n = 40
    elif "wt50" in filename.name:
        n = 50
    elif "wt100" in filename.name:
        n = 100
    else:
        raise ValueError("Το όνομα αρχείου πρέπει να περιέχει wt40, wt50 ή wt100.")

    numbers = []
    with open(filename, "r", encoding="utf-8") as f:
        for token in f.read().split():
            numbers.append(int(token))

    integers_per_instance = 3 * n
    expected_total_integers = 125 * integers_per_instance

    if len(numbers) < expected_total_integers:
        raise ValueError(
            f"Το αρχείο περιέχει {len(numbers)} ακεραίους, "
            f"ενώ αναμένονται τουλάχιστον {expected_total_integers}."
        )

    # Μετατροπή από αρίθμηση 1..125 σε δείκτη 0..124
    instance_index = instance_number - 1
    start = instance_index * integers_per_instance

    processing_times = numbers[start : start + n]
    weights = numbers[start + n : start + 2 * n]
    due_dates = numbers[start + 2 * n : start + 3 * n]

    return processing_times, weights, due_dates


def solve_single_machine_weighted_tardiness(
    processing_times, weights, due_dates, time_limit=60
):
    model = cp_model.CpModel()

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
            start, processing_times[j], end, f"interval[{j}]"
        )

        t = model.NewIntVar(0, horizon, f"tardiness[{j}]")

        # T_j = max(C_j - d_j, 0)
        model.Add(t >= end - due_dates[j])
        model.Add(t >= 0)

        starts.append(start)
        ends.append(end)
        intervals.append(interval)
        tardiness.append(t)

    # Μία μηχανή: καμία επικάλυψη μεταξύ εργασιών
    model.AddNoOverlap(intervals)

    # Αντικειμενική συνάρτηση: min sum(w_j * T_j)
    model.Minimize(sum(weights[j] * tardiness[j] for j in range(n)))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    # solver.parameters.num_search_workers = 8

    solver.parameters.log_search_progress = True
    solver.parameters.cp_model_presolve = True
    status = solver.Solve(model)

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        print("Δεν βρέθηκε λύση.")
        print("Κατάσταση:", solver.StatusName(status))
        return None

    schedule = []

    for j in range(n):
        start = solver.Value(starts[j])
        end = solver.Value(ends[j])
        t = solver.Value(tardiness[j])
        wt = weights[j] * t

        schedule.append(
            {
                "job": j,
                "start": start,
                "end": end,
                "processing_time": processing_times[j],
                "weight": weights[j],
                "due_date": due_dates[j],
                "tardiness": t,
                "weighted_tardiness": wt,
            }
        )

    schedule.sort(key=lambda row: row["start"])

    result = {
        "status": solver.StatusName(status),
        "objective_value": int(solver.ObjectiveValue()),
        "best_objective_bound": int(solver.BestObjectiveBound()),
        "wall_time": solver.WallTime(),
        "schedule": schedule,
    }

    return result


def print_solution(result):
    if result is None:
        return

    print("Κατάσταση:", result["status"])
    print("Τιμή αντικειμενικής συνάρτησης:", result["objective_value"])
    print("Καλύτερο κάτω φράγμα:", result["best_objective_bound"])
    print("Χρόνος επίλυσης:", round(result["wall_time"], 3), "sec")
    print()

    print("Σειρά εργασιών:")
    print([row["job"] for row in result["schedule"]])
    print()

    print(
        f"{'Job':>4} | {'Start':>6} | {'End':>6} | "
        f"{'p_j':>5} | {'w_j':>5} | {'d_j':>6} | "
        f"{'T_j':>6} | {'w_j*T_j':>9}"
    )
    print("-" * 72)

    for row in result["schedule"]:
        print(
            f"{row['job']:>4} | "
            f"{row['start']:>6} | "
            f"{row['end']:>6} | "
            f"{row['processing_time']:>5} | "
            f"{row['weight']:>5} | "
            f"{row['due_date']:>6} | "
            f"{row['tardiness']:>6} | "
            f"{row['weighted_tardiness']:>9}"
        )


def solve_from_file(problem_size, instance_number, time_limit=60):
    """
    problem_size: 40, 50 ή 100
    instance_number: 1 έως 125
    """

    if problem_size not in (40, 50, 100):
        raise ValueError("Το μέγεθος πρέπει να είναι 40, 50 ή 100.")

    # Φάκελος όπου βρίσκεται το τρέχον αρχείο .py
    script_dir = Path(__file__).resolve().parent

    filename = script_dir / f"wt{problem_size}.txt"

    processing_times, weights, due_dates = read_wt_instance(filename, instance_number)

    print(f"Αρχείο: {filename}")
    print(f"Στιγμιότυπο: {instance_number}")
    print(f"Πλήθος εργασιών: {len(processing_times)}")
    print()

    result = solve_single_machine_weighted_tardiness(
        processing_times, weights, due_dates, time_limit=time_limit
    )

    print_solution(result)


if __name__ == "__main__":
    solve_from_file(
        problem_size=40, instance_number=1, time_limit=60
    )  # Λύνει το στιγμιότυπο 1 από το wt40.txt
    # solve_from_file(
    #     problem_size=100, instance_number=125, time_limit=60
    # )  # Λύνει το στιγμιότυπο 1 από το wt40.txt
