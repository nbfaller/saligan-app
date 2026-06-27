# Import necessary libraries
from dash import dash, dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import webbrowser
from urllib.parse import urlparse, parse_qs

# App modules
from app import app

# Layout definition
CONTENT_STYLE = {
    "margin-top" : "1em",
    "margin-left" : "1em",
    "margin-right" : "1em",
    "padding" : "1em 1em",
}

app.layout = html.Div(
    [
        html.Meta(
            name = "theme-color",
            content = '#12355B'
        ),
        dcc.Location(id = 'url', refresh = False),

        # Login and Logout session storage
        dcc.Store(id = 'session_logout', data = True, storage_type = 'session'),

        # User session storage
        dcc.Store(id = 'current_user_id', data = -1, storage_type = 'session'),

        # User role session storage
        dcc.Store(id = 'current_user_role', data = -1, storage_type = 'session'),

        #cm.navbar
        html.Div(id = 'page_content', style = CONTENT_STYLE)
        #cm.footer
    ]
)

@app.callback(
    [
        Output('page_content', 'children'),
        Output('session_logout', 'data'),
        #Output('current_user_id', 'data'),
        #Output('current_user_role', 'data')
    ],
    [
        Input('url', 'pathname'),
        #Input('url', 'search'),
        #Input('session_logout', 'data')
    ],
    [
        State('session_logout', 'data'),
        State('current_user_id', 'data'),
        State('current_user_role', 'data'),
        State('url', 'search')
    ]
)

def display_page(pathname, session_logout, user_id, user_role, search):
    ctx = dash.callback_context
    if ctx.triggered:
        event_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if event_id == 'url':
            if pathname == '/' or pathname == '/home':
                returnlayout = "It works!"
            else:
                returnlayout = "404 Page Not Found"
        else:
            raise PreventUpdate
        return [returnlayout, session_logout]
    else:
        raise PreventUpdate

if __name__ == '__main__':
    # Open the app in a web browser
    webbrowser.open_new('http://127.0.0.1:8050/', new = 0, autoraise = True)
    app.run_server(debug = False)