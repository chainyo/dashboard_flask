from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

import flask
import dash_html_components as html

server = flask.Flask(__name__)
dash_app1 = Dash(__name__, server = server, url_base_pathname='/dashboard1/')
dash_app1.layout = html.Div([html.H1('Hi there, I am Dash1')])

@server.route('/')
@server.route('/index')
def hello():
    return 'Bienvenue sur nos dashboards'

@server.route('/dashboard1/')
def render_dashboard():
    return flask.redirect('/dash1')


@server.route('/dashboard2/')
def render_reports():
    return flask.redirect('/dash2')

app = DispatcherMiddleware(server, {
    '/dash1': dash_app1.server,
})

run_simple('0.0.0.0', 8080, app, use_reloader=True, use_debugger=True)
