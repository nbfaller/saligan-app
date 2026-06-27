import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import logging

# Create the app object (stored in app variable) along with the external stylesheets
app = dash.Dash(
    __name__,
    assets_folder = 'static',
    assets_url_path = 'static',
    include_assets_files = True,
    external_stylesheets = [
        "static/bootstrap-5.3.8-dist/css/bootstrap.css",
        #"static/dcc.css",
        dbc.themes.BOOTSTRAP,
        dbc.icons.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ],
)

# Make sure that all callbacks are not activated when input elements enter the layout
app.config.suppress_callback_exceptions = True

# Get CSS from a local folder
app.css.config.serve_locally = True

# Set app title that appears in the browser tab
app.title = "SALIGAN • Statutory Atlas of Legal Instruments and Governance"

# Reduce logs on termina for better debugging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)