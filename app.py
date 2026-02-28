"""
Student Performance Dashboard
------------------------------
This dashboard is built using Dash and Plotly.

Features:
- Dropdown to filter by Major
- RangeSlider to filter by GPA
- 3 Interactive Graphs (Bar, Line, Pie)
- KPI summary cards (Total Students, Avg GPA, Max GPA)

Author: Your Name
"""
# Import required libraries
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("data.csv")

# Initialize Dash app
app = dash.Dash(__name__)

# Layout
app.layout = html.Div([

    html.H1("Student Performance Dashboard",
            style={"textAlign": "center"}),

    # Dropdown
    dcc.Dropdown(
        id="major-dropdown",
        options=[{"label": m, "value": m} for m in df["Major"].unique()],
        value=df["Major"].unique()[0],
        clearable=False
    ),

    # GPA Slider
    dcc.RangeSlider(
        id="gpa-slider",
        min=df["GPA"].min(),
        max=df["GPA"].max(),
        step=0.1,
        value=[df["GPA"].min(), df["GPA"].max()],
        marks={round(g,1): str(round(g,1)) for g in sorted(df["GPA"].unique())}
    ),

    # KPI Cards
    html.Div([
        html.Div(id="total-students", className="card"),
        html.Div(id="avg-gpa", className="card"),
        html.Div(id="max-gpa", className="card"),
    ], style={"display": "flex", "gap": "20px", "marginTop": "20px"}),

    # Graphs
    dcc.Graph(id="bar-chart"),
    dcc.Graph(id="line-chart"),
    dcc.Graph(id="pie-chart")

], style={"margin": "40px"})


# Layout
app.layout = html.Div([

    html.H1("Student Performance Dashboard",
            style={"textAlign": "center"}),

    # Dropdown
    dcc.Dropdown(
        id="major-dropdown",
        options=[{"label": m, "value": m} for m in df["Major"].unique()],
        value=df["Major"].unique()[0],
        clearable=False
    ),

    # GPA Slider
    dcc.RangeSlider(
        id="gpa-slider",
        min=df["GPA"].min(),
        max=df["GPA"].max(),
        step=0.1,
        value=[df["GPA"].min(), df["GPA"].max()],
        marks={round(g,1): str(round(g,1)) for g in sorted(df["GPA"].unique())}
    ),

    # KPI Cards
    html.Div([
        html.Div(id="total-students", className="card"),
        html.Div(id="avg-gpa", className="card"),
        html.Div(id="max-gpa", className="card"),
    ], style={"display": "flex", "gap": "20px", "marginTop": "20px"}),

    # Graphs
    dcc.Graph(id="bar-chart", style={"marginTop": "30px"}),
    dcc.Graph(id="line-chart"),
    dcc.Graph(id="pie-chart")

], style={"margin": "40px"})


# Callback
@app.callback(
    Output("bar-chart", "figure"),
    Output("line-chart", "figure"),
    Output("pie-chart", "figure"),
    Output("total-students", "children"),
    Output("avg-gpa", "children"),
    Output("max-gpa", "children"),
    Input("major-dropdown", "value"),
    Input("gpa-slider", "value")
)
def update_graphs(selected_major, gpa_range):

    # Filter dataset by selected major and GPA range
    filtered_df = df[
        (df["Major"] == selected_major) &
        (df["GPA"] >= gpa_range[0]) &
        (df["GPA"] <= gpa_range[1])
    ]

    # Bar chart
    fig1 = px.bar(
        filtered_df,
        x="Name",
        y="Math",
        title="Math Scores"
    )

    # Line chart
    fig2 = px.line(
        filtered_df,
        x="Age",
        y="GPA",
        title="GPA by Age",
        markers=True
    )

    # Pie chart (all majors within selected GPA range)
    pie_df = df[
        (df["GPA"] >= gpa_range[0]) &
        (df["GPA"] <= gpa_range[1])
    ]

    fig3 = px.pie(
        pie_df,
        names="Major",
        title="Major Distribution"
    )

    # KPI values
    total_students = f"👨‍🎓 Total Students: {len(filtered_df)}"
    avg_gpa = f"📊 Average GPA: {round(filtered_df['GPA'].mean(),2) if not filtered_df.empty else 0}"
    max_gpa = f"🏆 Highest GPA: {filtered_df['GPA'].max() if not filtered_df.empty else 0}"

    return fig1, fig2, fig3, total_students, avg_gpa, max_gpa


if __name__ == '__main__':
    app.run(debug=True)