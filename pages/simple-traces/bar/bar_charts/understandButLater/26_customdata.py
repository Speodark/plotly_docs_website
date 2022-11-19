"""
hovertemplate -> let you format your hover text by adding strings to it or changing the way the data is formatted 
"""
import plotly.graph_objects as go

animals=['giraffes', 'orangutans', 'monkeys']
animals2=['giraffes2', 'orangutans2', 'monkeys2']

fig = go.Figure([
    go.Bar(
        x=animals, # x values
        y=[20, 14, 23], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "first",
        customdata = ["hey", "there"]
    ),
    go.Bar(
        x=animals2, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "second"
    ),
])
fig.show()