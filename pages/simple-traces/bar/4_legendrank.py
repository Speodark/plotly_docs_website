"""
legendrank -> decides on the order of the legend!
              If you have 2 traces and 1 has a legendrank of 2 and on of 5 
              the legend with the 2 will be first!
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
            name = "first in code but second in legend",
            legendrank=2
        ),
        go.Bar(
            x=animals2, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "second in code but first in legend",
            legendrank=1
        ),
    ])
    return html.Div(
        dcc.Graph(
            figure=fig
        )
    )

def layout():
    return layout_template(code)