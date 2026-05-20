from ortools.sat.python import cp_model
import geopandas as gpd
import pandas as pd
import plotly.express as px
import requests
from pathlib import Path


GEOJSON_URL = (
    "https://raw.githubusercontent.com/codeforgermany/"
    "click_that_hood/refs/heads/main/public/data/greece-prefectures.geojson"
)

LOCAL_GEOJSON = Path("greece-prefectures.geojson")


def download_geojson():
    """
    Κατεβάζει το GeoJSON αρχείο με τους νομούς της Ελλάδας,
    αν δεν υπάρχει ήδη τοπικά.
    """
    if LOCAL_GEOJSON.exists():
        return LOCAL_GEOJSON

    response = requests.get(GEOJSON_URL, timeout=30)
    response.raise_for_status()

    LOCAL_GEOJSON.write_text(response.text, encoding="utf-8")
    return LOCAL_GEOJSON


def find_name_column(gdf):
    """
    Προσπαθεί να εντοπίσει αυτόματα τη στήλη που περιέχει
    το όνομα κάθε νομού.
    """
    possible_columns = ["name", "NAME", "Name", "nomos", "prefecture"]

    for col in possible_columns:
        if col in gdf.columns:
            return col

    print("Διαθέσιμες στήλες στο GeoJSON:")
    print(list(gdf.columns))

    raise ValueError(
        "Δεν βρέθηκε αυτόματα στήλη ονόματος. "
        "Ελέγξτε τις στήλες του GeoDataFrame."
    )


def build_adjacency_edges(gdf, name_col):
    """
    Υπολογίζει αυτόματα τις ακμές γειτνίασης.

    Δύο νομοί θεωρούνται γειτονικοί όταν τα γεωμετρικά τους
    όρια εφάπτονται.
    """
    edges = []

    # Spatial index για αποδοτικότερο έλεγχο γειτνιάσεων
    spatial_index = gdf.sindex

    for i, row_i in gdf.iterrows():
        geom_i = row_i.geometry
        name_i = row_i[name_col]

        # Υποψήφια γειτονικά γεωμετρικά αντικείμενα
        candidate_indices = list(spatial_index.intersection(geom_i.bounds))

        for j in candidate_indices:
            if j <= i:
                continue

            row_j = gdf.iloc[j]
            geom_j = row_j.geometry
            name_j = row_j[name_col]

            # touches: έχουν κοινό σύνορο ή κοινό σημείο
            if geom_i.touches(geom_j):
                edges.append((name_i, name_j))

    return edges


def solve_greece_prefecture_coloring():
    geojson_path = download_geojson()

    gdf = gpd.read_file(geojson_path)

    # Κρατάμε μόνο έγκυρες γεωμετρίες
    gdf = gdf[gdf.geometry.notnull()].copy()
    gdf = gdf[gdf.is_valid].copy()

    name_col = find_name_column(gdf)

    prefectures = list(gdf[name_col])

    edges = build_adjacency_edges(gdf, name_col)

    print("Πλήθος νομών:", len(prefectures))
    print("Πλήθος ακμών γειτνίασης:", len(edges))

    model = cp_model.CpModel()

    colors = ["Κόκκινο", "Πράσινο", "Μπλε", "Κίτρινο"]

    color_map_plotly = {
        "Κόκκινο": "red",
        "Πράσινο": "green",
        "Μπλε": "blue",
        "Κίτρινο": "yellow",
    }

    # Μεταβλητές απόφασης:
    # κάθε νομός παίρνει ένα από τα διαθέσιμα χρώματα
    x = {}
    for prefecture in prefectures:
        x[prefecture] = model.NewIntVar(
            0,
            len(colors) - 1,
            f"x[{prefecture}]"
        )

    # Περιορισμοί γειτνίασης:
    # δύο γειτονικοί νομοί δεν μπορούν να έχουν το ίδιο χρώμα
    for p1, p2 in edges:
        model.Add(x[p1] != x[p2])

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status not in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        print("Δεν βρέθηκε λύση.")
        return

    solution = {}

    print()
    print("Βρέθηκε χρωματισμός:")
    for prefecture in prefectures:
        color_index = solver.Value(x[prefecture])
        color = colors[color_index]
        solution[prefecture] = color
        print(prefecture, "->", color)

    plot_solution_on_map(gdf, name_col, solution, color_map_plotly)


def plot_solution_on_map(gdf, name_col, solution, color_map_plotly):
    """
    Απεικονίζει τη λύση σε διαδραστικό χάρτη.
    """
    gdf = gdf.copy()

    gdf["color"] = gdf[name_col].map(solution)

    # Plotly θέλει GeoJSON σε μορφή λεξικού
    geojson = gdf.__geo_interface__

    fig = px.choropleth_mapbox(
        gdf,
        geojson=geojson,
        locations=gdf.index,
        color="color",
        color_discrete_map=color_map_plotly,
        hover_name=name_col,
        mapbox_style="carto-positron",
        center={"lat": 39.0, "lon": 22.0},
        zoom=5.2,
        opacity=0.75,
        title="Χρωματισμός νομών της Ελλάδας με CP-SAT"
    )

    fig.update_layout(
        margin={"r": 0, "t": 50, "l": 0, "b": 0}
    )

    fig.show()


solve_greece_prefecture_coloring()