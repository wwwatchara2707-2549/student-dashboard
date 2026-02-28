"""
Student Performance Dashboard
------------------------------
This dashboard is built using Dash and Plotly.

Features:
- Dropdown to filter by Major
- RangeSlider to filter by GPA
- 4 Interactive Graphs (Bar, Line, Pie, Scatter)
- KPI summary cards
- Interactive DataTable

Author: Your Name
"""

# Import required libraries
import dash
from dash import html, dcc, dash_table
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
        marks={round(g, 1): str(round(g, 1)) for g in sorted(df["GPA"].unique())}
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
    dcc.Graph(id="pie-chart"),
    dcc.Graph(id="scatter-chart"),

    # Data Table
    dash_table.DataTable(
        id="student-table",
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=10,
        style_table={"overflowX": "auto"},
        style_header={
            "backgroundColor": "#1f2c56",
            "color": "white",
            "fontWeight": "bold"
        },
        style_cell={
            "textAlign": "center"
        }
    )

], style={"margin": "40px"})


# Callback
@app.callback(
    Output("bar-chart", "figure"),
    Output("line-chart", "figure"),
    Output("pie-chart", "figure"),
    Output("scatter-chart", "figure"),
    Output("total-students", "children"),
    Output("avg-gpa", "children"),
    Output("max-gpa", "children"),
    Output("student-table", "data"),
    Input("major-dropdown", "value"),
    Input("gpa-slider", "value")
)
def update_graphs(selected_major, gpa_range):

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

    # Pie chart
    pie_df = df[
        (df["GPA"] >= gpa_range[0]) &
        (df["GPA"] <= gpa_range[1])
    ]

    fig3 = px.pie(
        pie_df,
        names="Major",
        title="Major Distribution"
    )

    # Scatter plot
    fig4 = px.scatter(
        filtered_df,
        x="Math",
        y="GPA",
        size="Age",
        title="Math vs GPA (size = Age)",
        hover_data=["Name"]
    )

    # KPI values
    total_students = f"👨‍🎓 Total Students: {len(filtered_df)}"
    avg_gpa = f"📊 Average GPA: {round(filtered_df['GPA'].mean(), 2) if not filtered_df.empty else 0}"
    max_gpa = f"🏆 Highest GPA: {filtered_df['GPA'].max() if not filtered_df.empty else 0}"

    # Table data
    table_data = filtered_df.to_dict("records")

    return fig1, fig2, fig3, fig4, total_students, avg_gpa, max_gpa, table_data


if __name__ == '__main__':
    app.run(debug=True)