"""
hovertemplate -> let you format your hover text by adding strings to it or changing the way the data is formatted 
"""
import plotly.graph_objects as go

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
        xhoverformat="%{x} hello"
    ),
    go.Bar(
        x=animals, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "y",
        text=["second text 1","second text 2","second text 3"],
        hoverinfo="y",
    ),
    go.Bar(
        x=animals, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "x+y",
        text=["second text 1","second text 2","second text 3"],
        hoverinfo="x+y",
    ),
    go.Bar(
        x=animals, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "all",
        text=["second text 1","second text 2","second text 3"],
        hoverinfo="all",
    ),
])
fig.show()