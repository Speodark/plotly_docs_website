"""
legendrank -> decides on the order of the legend!
              If you have 2 traces and 1 has a legendrank of 2 and on of 5 
              the legend with the 2 will be first!
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
    ),
    go.Bar(
        x=animals2, # x values
        y=[25, 13, 27], # y values
        # Sets the trace name, lets say we have multiple bar charts and a legend
        # the name will be shown in the legend
        name = "second",
    ),
])
fig.show()