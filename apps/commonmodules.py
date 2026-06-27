# Dash-related dependencies
from dash import dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
from datetime import datetime
import pytz
import hashlib

navbar = dbc.Navbar(
    [
        dbc.Col(
            dbc.Button(
                html.I(className = 'bi bi-list'),
                id = 'btn_sidebar',
                color = 'primary',
                outline = True,
                style = {
                    'height' : '2em',
                    'width' : '2em',
                    'padding' : '0px',
                    #'background-color' : '#12355B',
                    #'border-color' : '#12355B'
                }
            ),
            id = 'navbar_col1',
            width = 'auto',
            class_name = 'd-none ms-4'
        ),
        dbc.Col(
            align = 'center',
            class_name = 'ms-md-4 me-md-2 ms-0 me-0',
        ),
        dbc.Col(
            width = 'auto',
            class_name = 'ms-md-2 me-4'
        )
    ],
    id = 'navbar',
    style = {
        'position' : 'fixed',
        'top' : 0,
        'width' : '100vw',
        'z-index' : 1000,
        'padding-top' : '1em',
        'padding-bottom' : '1em',
        'color' : '#12355B'
    },
)