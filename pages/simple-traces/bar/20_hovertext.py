"""
hovertext -> add text to the hover
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
            name = "text_position_outside",
            text=["second text 1","second text 2","second text 3"],
            textposition="outside",
            texttemplate="value: %{y:$.2f}",
            hovertext="Hello I am the text hover!"
        ),
        go.Bar(
            x=animals, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "text_position_list",
            text=["second text 1","second text 2","second text 3"],
            textposition=["inside", "outside", "inside"],
            texttemplate=["value: %{y:$.2f}", "value: %{x}", "value: %{x} Great"],
            hovertext=["text 1", "text 2", "text 3"]
        ),
    ])
    return html.Div(
        dcc.Graph(
            figure=fig
        )
    )

def layout():
    return layout_template(code)