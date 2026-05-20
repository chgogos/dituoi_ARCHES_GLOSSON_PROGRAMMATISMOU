from ortools.sat.python import cp_model
import plotly.express as px
import pandas as pd


def solve_usa_map_coloring():
    model = cp_model.CpModel()

    states = [
        "AL", "AZ", "AR", "CA", "CO", "CT", "DE", "FL",
        "GA", "ID", "IL", "IN", "IA", "KS", "KY", "LA",
        "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT",
        "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND",
        "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN",
        "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]

    colors = ["Red", "Green", "Blue", "Yellow"]

    color_names_gr = {
        "Red": "Κόκκινο",
        "Green": "Πράσινο",
        "Blue": "Μπλε",
        "Yellow": "Κίτρινο"
    }

    x = {}
    for state in states:
        x[state] = model.NewIntVar(0, len(colors) - 1, state)

    edges = [
        ("AL", "FL"), ("AL", "GA"), ("AL", "MS"), ("AL", "TN"),
        ("AZ", "CA"), ("AZ", "CO"), ("AZ", "NV"), ("AZ", "NM"), ("AZ", "UT"),
        ("AR", "LA"), ("AR", "MS"), ("AR", "MO"), ("AR", "OK"), ("AR", "TN"), ("AR", "TX"),
        ("CA", "NV"), ("CA", "OR"),
        ("CO", "KS"), ("CO", "NE"), ("CO", "NM"), ("CO", "OK"), ("CO", "UT"), ("CO", "WY"),
        ("CT", "MA"), ("CT", "NY"), ("CT", "RI"),
        ("DE", "MD"), ("DE", "NJ"), ("DE", "PA"),
        ("FL", "GA"),
        ("GA", "NC"), ("GA", "SC"), ("GA", "TN"),
        ("ID", "MT"), ("ID", "NV"), ("ID", "OR"), ("ID", "UT"), ("ID", "WA"), ("ID", "WY"),
        ("IL", "IN"), ("IL", "IA"), ("IL", "KY"), ("IL", "MO"), ("IL", "WI"),
        ("IN", "KY"), ("IN", "MI"), ("IN", "OH"),
        ("IA", "MN"), ("IA", "MO"), ("IA", "NE"), ("IA", "SD"), ("IA", "WI"),
        ("KS", "MO"), ("KS", "NE"), ("KS", "OK"),
        ("KY", "MO"), ("KY", "OH"), ("KY", "TN"), ("KY", "VA"), ("KY", "WV"),
        ("LA", "MS"), ("LA", "TX"),
        ("ME", "NH"),
        ("MD", "PA"), ("MD", "VA"), ("MD", "WV"),
        ("MA", "NH"), ("MA", "NY"), ("MA", "RI"), ("MA", "VT"),
        ("MI", "OH"), ("MI", "WI"),
        ("MN", "ND"), ("MN", "SD"), ("MN", "WI"),
        ("MS", "TN"),
        ("MO", "NE"), ("MO", "OK"), ("MO", "TN"),
        ("MT", "ND"), ("MT", "SD"), ("MT", "WY"),
        ("NE", "SD"), ("NE", "WY"),
        ("NV", "OR"), ("NV", "UT"),
        ("NH", "VT"),
        ("NJ", "NY"), ("NJ", "PA"),
        ("NM", "OK"), ("NM", "TX"), ("NM", "UT"),
        ("NY", "PA"), ("NY", "VT"),
        ("NC", "SC"), ("NC", "TN"), ("NC", "VA"),
        ("ND", "SD"),
        ("OH", "PA"), ("OH", "WV"),
        ("OK", "TX"),
        ("OR", "WA"),
        ("PA", "WV"),
        ("SD", "WY"),
        ("TN", "VA"),
        ("TX", "NM"),
        ("UT", "WY"),
        ("VA", "WV")
    ]

    for s1, s2 in edges:
        model.Add(x[s1] != x[s2])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        print("Δεν βρέθηκε λύση.")
        return

    solution = {}

    print("Βρέθηκε χρωματισμός:")
    for state in states:
        color_index = solver.Value(x[state])
        color = colors[color_index]
        solution[state] = color

        print(state, "->", color_names_gr[color])

    plot_solution_on_map(solution)


def plot_solution_on_map(solution):
    data = []

    for state, color in solution.items():
        data.append({
            "state": state,
            "color": color
        })

    df = pd.DataFrame(data)

    fig = px.choropleth(
        df,
        locations="state",
        locationmode="USA-states",
        color="color",
        scope="usa",
        color_discrete_map={
            "Red": "red",
            "Green": "green",
            "Blue": "blue",
            "Yellow": "yellow"
        },
        hover_name="state",
        title="Χρωματισμός χάρτη των ΗΠΑ χωρίς Alaska και Hawaii"
    )

    fig.update_layout(
        geo=dict(
            lakecolor="white"
        )
    )

    fig.show()


solve_usa_map_coloring()