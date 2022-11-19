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
        name = "%{meta[i]}",
        meta = 4
    ),
    go.Bar(
        x=animals, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "y",
    ),
])
fig.show()