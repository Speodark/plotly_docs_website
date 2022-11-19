"""
legendgrouptitle -> let's you name a legendgroup, easier to understand and filter.
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
            name = "group 1 item 1",
            legendgroup="group1",
            legendgrouptitle={
                'font': {
                    'color':'red',
                    'family':'Balto',
                    'size': 20
                },
                'text':'Group 1 Title!'
            }
        ),
        go.Bar(
            x=animals2, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "group 1 item 2",
            legendgroup="group1",
        ),
        go.Bar(
            x=animals, # x values
            y=[20, 14, 23], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "group 2 item 1",
            legendgroup="group2",
            legendgrouptitle={
                'font': {
                    'color':'blue',
                    'family':'Balto',
                    'size': 20
                },
                'text':'Group 2 Title!'
            }
        ),
        go.Bar(
            x=animals2, # x values
            y=[25, 13, 27], # y values
            # Sets the trace name, lets say we have multiple bar charts and a legend
            # the name will be shown in the legend
            name = "group 2 item 2",
            legendgroup="group2"
        ),
    ])
    return html.Div(
        dcc.Graph(
            figure=fig
        )
    )

def layout():
    return layout_template(code)