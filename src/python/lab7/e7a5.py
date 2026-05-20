from ortools.sat.python import cp_model


def solve_wolf_goat_cabbage():
    model = cp_model.CpModel()

    items = ["man", "wolf", "goat", "cabbage"]

    MAN = 0
    WOLF = 1
    GOAT = 2
    CABBAGE = 3

    LEFT = 0
    RIGHT = 1

    max_steps = 7

    # pos[t][i] = όχθη στην οποία βρίσκεται το αντικείμενο i στο χρονικό βήμα t
    # 0 = αριστερή όχθη, 1 = δεξιά όχθη
    pos = []
    for t in range(max_steps + 1):
        row = []
        for i in range(len(items)):
            row.append(model.NewBoolVar(f"pos[{t}][{items[i]}]"))
        pos.append(row)

    # move[t][i] = 1 αν στο βήμα t μετακινείται το αντικείμενο i μαζί με τον άνθρωπο
    # Το t αναφέρεται στη μετακίνηση από την κατάσταση t στη κατάσταση t+1
    move = []
    for t in range(max_steps):
        row = []
        for i in range(len(items)):
            row.append(model.NewBoolVar(f"move[{t}][{items[i]}]"))
        move.append(row)

    # Αρχική κατάσταση: όλοι στην αριστερή όχθη
    for i in range(len(items)):
        model.Add(pos[0][i] == LEFT)

    # Τελική κατάσταση: όλοι στη δεξιά όχθη
    for i in range(len(items)):
        model.Add(pos[max_steps][i] == RIGHT)

    for t in range(max_steps):
        # Ο άνθρωπος μετακινείται σε κάθε βήμα
        model.Add(move[t][MAN] == 1)

        # Ο άνθρωπος αλλάζει πάντα όχθη
        model.Add(pos[t + 1][MAN] + pos[t][MAN] == 1)

        # Το πολύ ένα από τα wolf, goat, cabbage μετακινείται μαζί με τον άνθρωπο
        model.Add(
            move[t][WOLF] + move[t][GOAT] + move[t][CABBAGE] <= 1
        )

        for i in [WOLF, GOAT, CABBAGE]:
            # Αν το αντικείμενο μετακινηθεί, τότε αλλάζει όχθη
            model.Add(pos[t + 1][i] + pos[t][i] == 1).OnlyEnforceIf(move[t][i])

            # Αν το αντικείμενο δεν μετακινηθεί, τότε μένει στην ίδια όχθη
            model.Add(pos[t + 1][i] == pos[t][i]).OnlyEnforceIf(move[t][i].Not())

            # Ένα αντικείμενο μπορεί να μετακινηθεί μόνο αν βρίσκεται
            # στην ίδια όχθη με τον άνθρωπο πριν από τη μετακίνηση
            model.Add(pos[t][i] == pos[t][MAN]).OnlyEnforceIf(move[t][i])

        # Περιορισμοί ασφάλειας μετά από κάθε μετακίνηση
        add_safety_constraints(model, pos[t + 1], MAN, WOLF, GOAT, CABBAGE)

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        print("Δεν βρέθηκε λύση.")
        return

    print("Βρέθηκε λύση:")
    print()

    print_state(0, pos, solver, items)

    for t in range(max_steps):
        moved_item = None

        for i in [WOLF, GOAT, CABBAGE]:
            if solver.Value(move[t][i]) == 1:
                moved_item = items[i]

        direction = "δεξιά" if solver.Value(pos[t + 1][MAN]) == RIGHT else "αριστερά"

        if moved_item is None:
            print(f"Βήμα {t + 1}: ο άνθρωπος μετακινείται μόνος προς τα {direction}")
        else:
            print(
                f"Βήμα {t + 1}: ο άνθρωπος μεταφέρει το/την "
                f"{translate_item(moved_item)} προς τα {direction}"
            )

        print_state(t + 1, pos, solver, items)


def add_safety_constraints(model, state, MAN, WOLF, GOAT, CABBAGE):
    """
    Προσθέτει τους περιορισμούς ασφάλειας για μία κατάσταση.

    Δεν επιτρέπεται:
    1. λύκος και κατσίκα στην ίδια όχθη χωρίς τον άνθρωπο,
    2. κατσίκα και λάχανο στην ίδια όχθη χωρίς τον άνθρωπο.
    """

    # Αν wolf == goat, τότε man == wolf
    # Δηλαδή, αν λύκος και κατσίκα είναι μαζί, πρέπει να είναι μαζί τους και ο άνθρωπος.
    wolf_goat_same = model.NewBoolVar("wolf_goat_same")
    model.Add(state[WOLF] == state[GOAT]).OnlyEnforceIf(wolf_goat_same)
    model.Add(state[WOLF] != state[GOAT]).OnlyEnforceIf(wolf_goat_same.Not())
    model.Add(state[MAN] == state[WOLF]).OnlyEnforceIf(wolf_goat_same)

    # Αν goat == cabbage, τότε man == goat
    # Δηλαδή, αν κατσίκα και λάχανο είναι μαζί, πρέπει να είναι μαζί τους και ο άνθρωπος.
    goat_cabbage_same = model.NewBoolVar("goat_cabbage_same")
    model.Add(state[GOAT] == state[CABBAGE]).OnlyEnforceIf(goat_cabbage_same)
    model.Add(state[GOAT] != state[CABBAGE]).OnlyEnforceIf(goat_cabbage_same.Not())
    model.Add(state[MAN] == state[GOAT]).OnlyEnforceIf(goat_cabbage_same)


def print_state(t, pos, solver, items):
    left_bank = []
    right_bank = []

    for i, item in enumerate(items):
        if solver.Value(pos[t][i]) == 0:
            left_bank.append(translate_item(item))
        else:
            right_bank.append(translate_item(item))

    print(f"Κατάσταση {t}:")
    print("  Αριστερή όχθη:", left_bank)
    print("  Δεξιά όχθη:   ", right_bank)
    print()


def translate_item(item):
    translations = {
        "man": "άνθρωπος",
        "wolf": "λύκος",
        "goat": "κατσίκα",
        "cabbage": "λάχανο"
    }

    return translations[item]


solve_wolf_goat_cabbage()