"""
legendgroup -> let's you group together traces names inside the legend and filter them both together!
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
        name = "item 1",
        legendwidth=0
    ),
    go.Bar(
        x=animals2, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "item 2",
        legendwidth=2
    ),
])
fig.show()