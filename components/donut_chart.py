import plotly.graph_objects as go
from dash import dcc
import uuid


def donut_chart_figure(title=None, selected_points=None):
    labels = ['diageo americas', 'jim beam brands', 'pernod ricard usa/austin nichols', 'luxco-st louis', 'brown-forman corporation', 'etc']
    values = [247579983, 88441429, 78240639, 74993978, 69342053, 4405015]
    fig = go.Figure(
        go.Pie(
            labels=labels, 
            values=values, 
            textinfo='percent',
            hole=.6
        )
    )
    fig.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        margin={"t": 0, "b": 0, "r": 0, "l": 0, "pad": 0},
        title_text = title
    )
    return fig


def donut_chart(id=None, agg='count', title=None):
    id = str(uuid.uuid4()) if not id else id
    return dcc.Graph(
        figure=donut_chart_figure(),
        responsive=True, 
        className="fill-parent-div sm-padding",
        id = {'type':'donut_chart', 'id':id}
    )
