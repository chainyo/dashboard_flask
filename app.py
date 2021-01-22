from flask import Flask
from dash import Dash

import dash_core_components as dcc 
import dash_html_components as html 

server = Flask(__name__)
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

app.layout = html.Div(id='dash_container')

@server.route("/dashboard")
def my_dash_app():
    return app.index()

if __name__ == '__main__':
    app.run_server(debug=True)