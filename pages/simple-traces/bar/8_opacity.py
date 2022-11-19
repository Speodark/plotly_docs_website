"""
opacity -> set's the opacity of the graph, how much can u see through.
"""
from dash import html, dcc
import plotly.graph_objects as go
import dash
import os
from app import TITLE
from layout_template import layout_template

file_name = os.path.basename(__file__).split('.')[0].split("_")[1]
path = '/' + '/'.join(__name__.split('.')[1:-1]) + '/' + file_name
dash.register_page(
    __name__,
    title = TITLE,
    name = file_name,
    path = path
)

def code():
    animals=['giraffes', 'orangutans', 'monkeys']
    animals2=['giraffes2', 'orangutans2', 'monkeys2']
    fig = go.Figure([
        go.Bar(
            x=animals, # x values
            y=[20, 14, 23], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "opacity 0",
            opacity=0
        ),
        go.Bar(
            x=animals2, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "opacity 0.5",
            opacity=0.5
        ),
        go.Bar(
            x=animals2, # x values
            y=[20, 10, 44], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "opacity 1",
            opacity=1
        ),
    ])
    return html.Div(
        dcc.Graph(
            figure=fig
        )
    )

def layout():
    return layout_template(code)