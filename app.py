"""
Student Performance Dashboard
------------------------------
Built with Dash & Plotly
Features:
- Major & GPA Filter
- 4 Interactive Graphs
- KPI Cards
- DataTable
- Reset + Download
- Dark Theme UI
"""

# ===============================
# Import Libraries
# ===============================
import dash
from dash import html, dcc, dash_table
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

# ===============================
# Load Dataset
# ===============================
df = pd.read_csv("data.csv")

# ===============================
# Helper Function
# ===============================
def filter_data(selected_major, gpa_range):
    return df[
        (df["Major"] == selected_major) &
        (df["GPA"] >= gpa_range[0]) &
        (df["GPA"] <= gpa_range[1])
    ]

# ===============================
# Initialize App
# ===============================
app = dash.Dash(__name__)

# ===============================
# Layout
# ===============================
app.layout = html.Div([

    # -------- Header --------
    html.Div([
        html.H1("🎓 Student Performance Dashboard",
                style={
                    "margin": "0",
                    "color": "white",
                    "fontSize": "32px",
                    "fontWeight": "bold"
                })
    ], style={
        "textAlign": "center",
        "padding": "25px",
        "background": "linear-gradient(90deg, #1e3c72, #2a5298)",
        "borderRadius": "12px",
        "marginBottom": "20px"
    }),

    # -------- Filter Card --------
    html.Div([

        html.H3("🔎 Filter Students"),

        html.Label("Select Major"),
        dcc.Dropdown(
            id="major-dropdown",
            options=[{"label": m, "value": m} for m in df["Major"].unique()],
            value=df["Major"].unique()[0],
            clearable=False,
            style={"marginBottom": "20px"}
        ),

        html.Label("Select GPA Range"),
        dcc.RangeSlider(
            id="gpa-slider",
            min=df["GPA"].min(),
            max=df["GPA"].max(),
            step=0.1,
            value=[df["GPA"].min(), df["GPA"].max()],
            marks={round(g,1): str(round(g,1)) for g in sorted(df["GPA"].unique())}
        ),

    ], style={
        "backgroundColor": "#1e293b",
        "padding": "25px",
        "borderRadius": "12px",
    }),

    # -------- Buttons --------
    html.Div([
        html.Button("Reset Filters",
                    id="reset-button",
                    n_clicks=0,
                    style={
                        "padding": "10px 20px",
                        "backgroundColor": "#ff4d4f",
                        "color": "white",
                        "border": "none",
                        "cursor": "pointer"
                    }),

        html.Button("Download Filtered Data",
                    id="download-button",
                    n_clicks=0,
                    style={
                        "padding": "10px 20px",
                        "backgroundColor": "#1890ff",
                        "color": "white",
                        "border": "none",
                        "cursor": "pointer",
                        "marginLeft": "10px"
                    }),

        dcc.Download(id="download-data"),

    ], style={"marginTop": "15px"}),

    # -------- KPI Cards --------
    html.Div([
        html.Div(id="total-students", style={
            "backgroundColor": "#1e293b",
            "padding": "20px",
            "borderRadius": "12px",
            "flex": "1",
            "textAlign": "center",
            "fontWeight": "bold"
        }),
        html.Div(id="avg-gpa", style={
            "backgroundColor": "#1e293b",
            "padding": "20px",
            "borderRadius": "12px",
            "flex": "1",
            "textAlign": "center",
            "fontWeight": "bold"
        }),
        html.Div(id="max-gpa", style={
            "backgroundColor": "#1e293b",
            "padding": "20px",
            "borderRadius": "12px",
            "flex": "1",
            "textAlign": "center",
            "fontWeight": "bold"
        }),
    ], style={
        "display": "flex",
        "gap": "20px",
        "marginTop": "30px"
    }),

    # -------- Graph Grid --------
    html.Div([
        html.Div(dcc.Graph(id="bar-chart"), style={"flex": "1"}),
        html.Div(dcc.Graph(id="line-chart"), style={"flex": "1"}),
    ], style={"display": "flex", "gap": "20px", "marginTop": "30px"}),

    html.Div([
        html.Div(dcc.Graph(id="pie-chart"), style={"flex": "1"}),
        html.Div(dcc.Graph(id="scatter-chart"), style={"flex": "1"}),
    ], style={"display": "flex", "gap": "20px", "marginTop": "20px"}),

    # -------- Data Table --------
    dash_table.DataTable(
        id="student-table",
        columns=[{"name": col, "id": col} for col in df.columns],
        page_size=10,
        style_table={"overflowX": "auto", "marginTop": "30px"},
        style_header={
            "backgroundColor": "#1e293b",
            "color": "white",
            "fontWeight": "bold"
        },
        style_cell={
            "backgroundColor": "#1f2937",
            "color": "white",
            "textAlign": "center"
        }
    )

], style={
    "margin": "40px",
    "backgroundColor": "#0f172a",
    "color": "white",
    "minHeight": "100vh",
    "fontFamily": "Arial"
})

# ===============================
# Main Callback
# ===============================
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

    filtered_df = filter_data(selected_major, gpa_range)

    fig1 = px.bar(filtered_df, x="Name", y="Math", title="Math Scores")
    fig2 = px.line(filtered_df, x="Age", y="GPA", markers=True)
    fig3 = px.pie(df[(df["GPA"] >= gpa_range[0]) &
                     (df["GPA"] <= gpa_range[1])],
                  names="Major")
    fig4 = px.scatter(filtered_df, x="Math", y="GPA",
                      size="Age", hover_data=["Name"])

    for fig in [fig1, fig2, fig3, fig4]:
        fig.update_layout(template="plotly_dark")

    return (
        fig1,
        fig2,
        fig3,
        fig4,
        f"👨‍🎓 Total Students: {len(filtered_df)}",
        f"📊 Average GPA: {round(filtered_df['GPA'].mean(),2) if not filtered_df.empty else 0}",
        f"🏆 Highest GPA: {filtered_df['GPA'].max() if not filtered_df.empty else 0}",
        filtered_df.to_dict("records")
    )

# ===============================
# Reset Callback
# ===============================
@app.callback(
    Output("major-dropdown", "value"),
    Output("gpa-slider", "value"),
    Input("reset-button", "n_clicks"),
    prevent_initial_call=True
)
def reset_filters(n):
    if df.empty:
        return dash.no_update, dash.no_update

    return (
        df["Major"].unique()[0],
        [df["GPA"].min(), df["GPA"].max()]
    )

# ===============================
# Download Callback
# ===============================
@app.callback(
    Output("download-data", "data"),
    Input("download-button", "n_clicks"),
    Input("major-dropdown", "value"),
    Input("gpa-slider", "value"),
    prevent_initial_call=True
)
def download_filtered_data(n, major, gpa_range):
    
    if not n:
        return dash.no_update

    filtered_df = filter_data(major, gpa_range)

    if filtered_df.empty:
        return dash.no_update

    return dcc.send_data_frame(
        filtered_df.to_csv,
        "filtered_students.csv",
        index=False
    )

# ===============================
# Run App
# ===============================
if __name__ == '__main__':
    app.run(debug=True)