"""
hovertemplate -> let you format your hover text by adding strings to it or changing the way the data is formatted 
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

    fig = go.Figure([
        go.Bar(
            x=animals, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "x",
            text=["second text 1","second text 2","second text 3"],
            hoverinfo="x",
            hovertemplate="value: %{x}"
        ),
        go.Bar(
            x=animals, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "y",
            text=["second text 1","second text 2","second text 3"],
            hoverinfo="y",
            hovertemplate = "value: %{y}"
        ),
        go.Bar(
            x=animals, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "x+y",
            text=["second text 1","second text 2","second text 3"],
            hoverinfo="x+y",
            hovertemplate="value: %{y:$.2f}"
        ),
        go.Bar(
            x=animals, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "all",
            text=["second text 1","second text 2","second text 3"],
            hoverinfo="all",
            hovertemplate="y: %{y}"
        ),
    ])
    return html.Div(
        dcc.Graph(
            figure = fig
        )
    )

def layout():
    return layout_template(code)