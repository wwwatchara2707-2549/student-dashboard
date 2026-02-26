import dash
from dash import html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Student Performance Dashboard"),
    html.P("Day 1 Setup Successful")
])

if __name__ == '__main__':
    app.run(debug=True)
app.layout = html.Div([
    html.H1("Student Performance Dashboard"),
    html.P("Day 1 Setup Successful")
], style={"textAlign": "center", "marginTop": "50px"})
# Import required libraries
import dash
from dash import html

# Initialize Dash application
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    html.H1("Student Performance Dashboard"),
    html.P("Day 1 Setup Successful")
], style={"textAlign": "center", "marginTop": "50px"})

# Run the server
if __name__ == '__main__':
    app.run(debug=True)