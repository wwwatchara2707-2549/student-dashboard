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

    # Dropdown for Major selection
    dcc.Dropdown(
        id="major-dropdown",
        options=[{"label": m, "value": m} for m in df["Major"].unique()],
        value=df["Major"].unique()[0],
        clearable=False
    ),

    # GPA Range Slider
    dcc.RangeSlider(
        id="gpa-slider",
        min=df["GPA"].min(),
        max=df["GPA"].max(),
        step=0.1,
        value=[df["GPA"].min(), df["GPA"].max()],
        marks={round(g,1): str(round(g,1)) for g in df["GPA"].unique()}
    ),

    html.Div([
        dcc.Graph(id="bar-chart"),
        dcc.Graph(id="line-chart"),
    ], style={"display": "flex", "gap": "20px"}),

    dcc.Graph(id="pie-chart")

], style={"margin": "40px"})


# Callback for interactivity
@app.callback(
    Output("bar-chart", "figure"),
    Output("line-chart", "figure"),
    Output("pie-chart", "figure"),
    Input("major-dropdown", "value"),
    Input("gpa-slider", "value")
)
def update_graphs(selected_major, gpa_range):
    
    filtered_df = df[
        (df["Major"] == selected_major) &
        (df["GPA"] >= gpa_range[0]) &
        (df["GPA"] <= gpa_range[1])
    ]

    fig1 = px.bar(
        filtered_df,
        x="Name",
        y="Math",
        title="Math Scores"
    )

    fig2 = px.line(
        filtered_df,
        x="Age",
        y="GPA",
        title="GPA by Age",
        markers=True
    )

    # FIXED PART
    pie_df = df[
        (df["GPA"] >= gpa_range[0]) &
        (df["GPA"] <= gpa_range[1])
    ]

    fig3 = px.pie(
        pie_df,
        names="Major",
        title="Major Distribution"
    )

    return fig1, fig2, fig3

if __name__ == '__main__':
    app.run(debug=True)