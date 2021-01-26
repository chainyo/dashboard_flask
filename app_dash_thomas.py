import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_table
import plotly.express as px
import pandas as pd 
import numpy as np 
import plotly.graph_objs as go 

from dashboard import Plotly
from data import Dates

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
server = app.server
app.config.suppress_callback_exceptions = True

app.layout = html.Div(id='dashboard', children=[
    html.H1(children='COVID-19 DASHBOARD', style={'margin':'25px auto', 'text-align':'center', 'font-size':'80px'}),

    html.Div([
        html.Div([dcc.Dropdown(id='date', options=[{'label': i, 'value': i} for i in Dates.get_dates()],
                value='2021-01-21', style={'margin-left':'10px', 'width':'50%', 'margin-bottom':'25px'})]),

        html.Div([dbc.Row([dbc.Col(html.Div(dcc.Graph(id='map_main')), style={'margin':'0 auto'}),
            dbc.Row(
                [dbc.Col(html.Div(dcc.Graph(id='map_gua')), width=4),
                dbc.Col(html.Div(dcc.Graph(id='map_may')), width=4),
                dbc.Col(html.Div(dcc.Graph(id='map_guy')), width=4,)],
                 style={'margin':'0 auto', 'height':'70%' , 'margin-bottom':'25px'})
        ])]),
        html.Div([
            dbc.Row([
                dbc.Col(html.Div(dcc.Graph(id='bars')), width=8,),
                dbc.Col(
                    html.Div(dbc.Card([dbc.CardBody([
                        html.Div(id='number-rea', style={'font-size':'80px', 'margin-bottom':'40px', 'margin-top':'40px'}),
                        html.P('Personnes en réanimation', style={'font-size':'30px', 'margin-bottom':'30px'}),
                        html.Div(id='date-rea', style={'font-size':'40px', 'margin-bottom':'50px', 'margin-top':'45px'})
                ])]), style={'text-align':'center'}), width=4,
            ),
            ], className="h-50"),
        ])
    ],),

    html.Div(
        dcc.Graph(id='plot', figure=Plotly.graph_line()), style={'margin-top':'25px'}
    )
], style={'width':'90%', 'margin':'0 auto'}) 

@app.callback(Output('map_main', 'figure'), Output('map_gua', 'figure'), Output('map_may', 'figure'), 
                Output('map_guy', 'figure'), Output('bars', 'figure'),
                Input('date', 'value'))
def update_maps(date):

    fig_main = Plotly.graph_map(47, 2.2, 4.5, date)
    fig_gua = Plotly.graph_map(16.2, -61.5, 7.5, date)
    fig_gua.update_layout(coloraxis_showscale=False)
    fig_may = Plotly.graph_map(-12.8, 45.16, 8.9, date)
    fig_may.update_layout(coloraxis_showscale=False)
    fig_guy = Plotly.graph_map(4, -53, 5.2, date)
    fig_guy.update_layout(coloraxis_showscale=False)
    fig_bars = Plotly.graph_bar(date)

    return fig_main, fig_gua, fig_may, fig_guy, fig_bars

@app.callback(Output(component_id='number-rea', component_property='children'),
                Output(component_id='date-rea', component_property='children'),
                Input('date', 'value'))
def update_nb_rea(date):

    fig_rea = Plotly.graph_number(date)
    fig_date = date

    return fig_rea.values[0], fig_date

if __name__ == '__main__':
    app.run_server(debug=True)