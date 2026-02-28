# Import required libraries
import dash
from dash import html, dcc
import pandas as pd
import plotly.express as px

# Load dataset
df = pd.read_csv("data.csv")

# Initialize Dash application
app = dash.Dash(__name__)

# Create Graph 1: Bar Chart (Math Scores)
fig1 = px.bar(
    df,
    x="Name",
    y="Math",
    title="Math Scores by Student",
    color="Major"
)

# Create Graph 2: Line Chart (GPA by Age)
fig2 = px.line(
    df,
    x="Age",
    y="GPA",
    title="GPA by Age",
    markers=True
)

# Create Graph 3: Pie Chart (Major Distribution)
fig3 = px.pie(
    df,
    names="Major",
    title="Major Distribution"
)

# Define layout
app.layout = html.Div([

    html.H1("Student Performance Dashboard",
            style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(figure=fig1),
        dcc.Graph(figure=fig2),
    ], style={"display": "flex", "gap": "20px"}),

    dcc.Graph(figure=fig3)

], style={"margin": "40px"})


# Run the server
if __name__ == '__main__':
    app.run(debug=True)