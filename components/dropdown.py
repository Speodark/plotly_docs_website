from dash import dcc
import uuid

# def dropdown(options, value, column_name, id = None, sub_type='default', filter=False, class_name = ""):
#     # Generating custom id if one is not provided
#     id = str(uuid.uuid4()) if not id else id
#     return dcc.Dropdown(
#         id = {'type':'dropdown', 'id':id, 'column_name':column_name, 'sub_type':sub_type, 'filter':filter},
#         className='dropdown' if not class_name else 'dropdown ' + class_name,
#         options=options,
#         value=value,
#         searchable=False,
#         clearable=False
#     )

def dropdown(options, value, column_name, id = None, sub_type='default', filter=False, class_name = ""):
    # Generating custom id if one is not provided
    id = str(uuid.uuid4()) if not id else id
    return dcc.Dropdown(
        id = {'type':'dropdown', 'id':id, 'column_name':column_name},
        className='dropdown' if not class_name else 'dropdown ' + class_name,
        options=options,
        value=value,
        searchable=False,
        clearable=False
    )
