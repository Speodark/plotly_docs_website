from dash import html
from .card import card
import uuid

def svg_kpi(kpi_name, value, last_value, svg_path, id = None, class_name = ""):
    # Calculating the percentage
    percent = ((last_value-value)/abs(value))*100
    # formatting the arrow by the percentage
    arrow_format = 'svg-kpi__percent--green filled-arrow__up' if percent >= 0 else 'svg-kpi__percent--red filled-arrow__down'
    # Generating custom id if one is not provided
    id = str(uuid.uuid4()) if not id else id
    # Return the svg_kpi
    return card(
        className='svg-kpi ' + class_name,
        children=[
            # The image
            html.Img(
                className="svg-kpi__svg",
                src=svg_path
            ),
            html.Div(
                className="svg-kpi__content",
                children=[
                    # Kpi name
                    html.Span(
                        className='svg-kpi__name',
                        children=kpi_name
                    ),
                    # Current value
                    html.Span(
                        className='svg-kpi__value',
                        id = {'type':'svg_kpi', 'id':id, 'kpi_name':kpi_name},
                        children="{:,}".format(value)
                    ),
                    html.Div(
                        className="svg-kpi__percent",
                        children=[
                            # Arrow icon
                            html.Span(
                                className='filled-arrow ' + arrow_format
                            ),
                            # Percent
                            html.Span(
                                className='svg-kpi__percent--value', 
                                children=f"{round(percent,2)}%"
                            )
                        ]
                    ), 
                ]
            ),
            
        ] 
    )



def update_kpi_value(value, last_value):

    # formatting the current value
    current_value = "{:,}".format(value)

    # calculating the percentage
    percent = ((last_value-value)/abs(value))*100

    # arrow class_name
    arrow_format = 'svg-kpi__percent--green filled-arrow__up' if percent >= 0 \
                        else 'svg-kpi__percent--red filled-arrow__down'
    arrow_class_name = 'filled-arrow ' + arrow_format

    # formatting the percentage
    percent = f"{round(percent,2)}%"

    return current_value, percent, arrow_class_name