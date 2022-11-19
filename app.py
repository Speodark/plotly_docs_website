from whitenoise import WhiteNoise
import dash
from dash import html, dcc, Input, Output
from pprint import pprint

TITLE = 'Plotly By Example'
# initilaize the app
external_stylesheets = [
    '//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/default.min.css',
]
external_scripts = [
    '//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js',
]
app = dash.Dash(
    __name__, 
    suppress_callback_exceptions=True,
    use_pages=True,
    external_scripts=external_scripts,
    external_stylesheets=external_stylesheets
)


# Generate the app layout
def layout():
    ordered_page_registry = dict(sorted(dash.page_registry.items(), key= lambda kv: int(kv[0].split('.')[-1].split("_")[0])))
    attribute_options = [{
        "label": dcc.Link(children=path_info['name'],href=path_info['path']),
        "value": path_info['path'] 
    } for path_info in ordered_page_registry.values()]
    return html.Div(
        className="container",
        children=[
            html.Div(
                className='layout',
                children=[
                    html.Div(
                        children="Plotly Visual Documentation",
                        className="layout__header"
                    ),


                    html.Div(
                        children=[
                            html.Span(
                                children="Graphing Library:",
                                className="layout__dropdown-title"
                            ),
                            dcc.Dropdown(
                                options=[
                                    "Simple Traces",
                                    "Distribution Traces",
                                    "Finance Traces",
                                    "3D Traces",
                                    "Map Traces",
                                    "Specialized Traces",
                                    "Layout",
                                    "Axes and Subplots",
                                    "Layers"
                                ],
                                value='Simple Traces',
                                id='library-value',
                                clearable=False
                            )
                        ],
                        className="layout__library layout__dropdown-container"
                    ),
                    html.Div(
                        children=[
                            html.Span(
                                children="Simple Traces:",
                                className="layout__dropdown-title",
                                id = "library-value-text"
                            ),
                            dcc.Dropdown(
                                options=[
                                    "Scatter",
                                    "Scatter GL"
                                ],
                                value='Scatter',
                                id="library-value-drilldown",
                                clearable=False
                            )
                        ],
                        className="layout__library-value layout__dropdown-container"
                    ),
                    html.Div(
                        children=[
                            html.Span(
                                children="Attribute:",
                                className="layout__dropdown-title"
                            ),
                            dcc.Dropdown(
                                options=attribute_options,
                                value=attribute_options[0]['value'],
                                id="attribute",
                                clearable=False
                            )
                        ],
                        className="layout__attribute layout__dropdown-container"
                    ),
                    html.Div(
                        className="layout__page-container",
                        children=dash.page_container
                    )
                ]
            ),
        ]
    )



# For the heroku deployment
server = app.server
# set the static folder
server.wsgi_app = WhiteNoise(server.wsgi_app, root='assets/')
# set the layout
app.layout = layout
# start the app
if __name__ == "__main__":
    app.run_server(debug=True, port=5050, host="0.0.0.0")