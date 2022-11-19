import dash_mantine_components as dmc
import inspect
from dash import html

def layout_template(func):
    return dmc.Tabs(
        children=[
            dmc.Tab(
                label="Example",
                children=func()
            ),
            dmc.Tab(
                label="Code",
                children=html.Pre(
                    children=html.Code(
                        className="hljs language-python code",
                        children=inspect.getsource(func)
                    )
                )
            )
        ],
        class_name="layout__tabs"
    )