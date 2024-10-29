import dash
from dash import Dash, html, dcc, Input, Output
from dash.dependencies import Input, Output, State

import dash_bootstrap_components as dbc

from dash import html

from commonlayout import common_layout


font_family_variable = 'Tahoma'
font_size_titoli = '20px'
font_size_paragrafi = '16px'
font_size_paragrafi_corsivo = '14px'
def layout_login():
    
    return html.Div([
        common_layout(),
        html.Div([
            html.H1('Smart Scheduler', style={
                'margin': '0', 
                'color': '#00194C',
                'font-family': font_family_variable, 
                'font-size': '14px', 
                'font-weight': 'bold',
            })
        ], style={
            'display': 'flex',
            'justify-content': 'space-between',
            'align-items': 'center',
            'background-color': '#B5D0FF',
            'padding': '10px',
            'height': '0.5cm',
            'width': '100%'
        }),
        html.Div([
            html.Div([
                html.Strong("Sei un operatore CUP?",style={'font-size': '30px','margin-botton':'30px','color': '#0F2471'}),
                html.Br(),
                html.Br(),
                html.Span("Username",style={'margin-top': '30px','color': '#00338D','font-family': font_family_variable}),
                dbc.Input(
                    #type="password",
                    id="username1",
                    placeholder="Digita qui...",
                ),
                html.Br(),
                html.Br(),
                html.Span("Password",style={'margin-top': '30px', 'color': '#00338D','font-family': font_family_variable}),
                dbc.Input(
                    type="password",
                    id="password1",
                    placeholder="Digita qui...",
                ),
                html.Br(),
                dcc.Link(html.Button('Accedi', id='button-1', n_clicks=0,style={'margin-top': '30px','margin-left':'160px', 'background-color': '#00338D', 'color': 'white', 'border-radius': '10px','width': '100px', 'height': '50px','font-weight': 'bold'}), href='/calendario')
            ], style={
                'width': '450px',
                'height': '380px',
                'background-color': 'white',
                'margin': 'auto',  # Center the squares horizontally
                'border-radius': '20px',  # Rounded corners
                'border': '2px solid #0F2471',  # Blue border
                'padding': '20px',
                'box-sizing': 'border-box',
            }),
            html.Div([
                html.Strong("Sei un direttore?",style={'font-size': '30px','margin-bottom':'50px','color': '#0F2471'}),
                html.Br(),
                html.Br(),
                html.Span("Username",style={'margin-top': '30px','color': '#00338D','font-family': font_family_variable }),
                dbc.Input(
                    #type="password",
                    id="username2",
                    placeholder="Digita qui...",
                ),
                html.Br(),
                html.Br(),
                html.Span("Password",style={'margin-top': '30px','color': '#00338D','font-family': font_family_variable}),
                dbc.Input(
                    type="password",
                    id="password2",
                    placeholder="Digita qui...",
                ),
                html.Br(),
                html.Div([
                    dcc.Link(html.Button('Accedi', id='button-2', n_clicks=0, style={'background-color': '#00338D', 'color': 'white', 'border-radius': '10px','width': '100px', 'height': '50px','font-weight': 'bold'}), href='/calendario'),
                    #EventListener(html.Div(id='dummy-output'), id='button-listener', events={'event': 'click'})
                ], style={'margin-top': '30px','margin-left':'180px'})
            ], style={
                'width': '450px',
                'height': '380px',
                'background-color': 'white',
                'margin': 'auto',  # Center the squares horizontally
                'border-radius': '20px',  # Rounded corners
                'border': '2px solid #0F2471',  # Blue border
                'padding': '20px',
                'box-sizing': 'border-box',
                'family-font': font_family_variable
            })
        ], style={
            'display': 'flex',
            'justify-content': 'center',  # Center the squares horizontally
            'margin-top': '20px'
        })
    ])