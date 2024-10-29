import dash
from dash import Dash, html, dcc, Input, Output
from dash.dependencies import Input, Output, State
from datetime import date
from dash.exceptions import PreventUpdate
from dash import dash_table
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import dash_ag_grid as dag
import os
from datetime import date
from dateutil.relativedelta import relativedelta
from dash import html
from flask import send_from_directory
import dash_mantine_components as dmc
from commonlayout import common_layout
from roots import giorno_odierno,mese_odierno,anno_odierno

app = dash.Dash(__name__)
font_family_variable = 'Tahoma'
font_size_titoli = '20px'
font_size_paragrafi = '16px'
font_size_paragrafi_corsivo = '14px'

###### Home Layout ######
def layout_home():
    return html.Div([
        common_layout(),
        html.Div([
            html.H1('Smart Scheduler', style={
                'margin': '0', 
                'color': '#00194C',
                'font-family': font_family_variable, 
                'font-size': '14px', 
                'font-weight': 'bold',
            }),
            html.Div(id='username')
        ], style={
            'display': 'flex',
            'justify-content': 'space-between',
            'align-items': 'center',
            'background-color': '#B5D0FF',
            'padding': '10px',
            'height': '0.5cm',
            'width': '100%'
        }),html.Div([
            html.Br(),
            html.H2('Benvenuto in Smart Scheduler', style={'color': '#00194C', 'font-weight': 'bold', 'font-size': font_size_titoli}),
            html.Br(),
            html.P([
                'Questa funzionalità ti fornisce suggerimenti in merito alla  ',
                html.Span('configurazione efficiente delle agende ', style={'font-weight': 'bold'}),
            ]),
        ], style={ 'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi,'textAlign': 'center' }),
        html.Br(),
        html.Div([
    # Blue box containing the content
    html.Div([
        # Row containing both the instruction text and the file upload
        html.Div([
            html.Img(src='/assets/upload.png', style={'height': '80px'}),
            # Instruction text
            html.Div([
                
                html.P([html.Span("1.",style={'font-weight':'bold'}),'Carica in formato .xlsx le agende da riconfigurare.',], style={'margin-bottom': '10px', 'color': '#00194C'}),
            ], style={'margin': '20px', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'flex': '1'}),
            
            # File Upload
            html.Div([
                dcc.Upload(
                    id='upload-data',
                    children=html.Div([
                        html.Img(src='/assets/load_file.png', style={'height': '50px', 'margin-bottom': '5px'}),
                        html.Div('Trascina o seleziona il file', id='upload-text', style={'textAlign': 'center', 'font-size': '14px'})
                    ], id='upload-container', style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),
                    style={
                        'width': '100%',
                        'height': '100%',
                        'borderRadius': '50px',
                        'textAlign': 'center',
                        'padding': '5px',
                        'background-color': '#FBDD81',
                        'margin-right': '20px', # Yellow background for file upload area
                    },
                    multiple=False
                ),
            ], style={'flex': '1', 'padding': '10px'})
        ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
    ], style={'border': '2px #ECF2FE', 'borderRadius': '50px', 'padding': '10px', 'background-color': '#ECF2FE','margin-right':'20px','margin-left':'20px'})
]),
html.Br(),
html.Div([
    # Row containing both the instruction text and the file upload
    html.Div([
        # Instruction text
        html.Div([
            html.P([html.Span("2.",style={'font-weight':'bold'}),'Scegli il periodo di riconfigurazione (max 6 mesi):'], style={'margin-bottom': '10px', 'color': '#00194C'}),
        ], style={'margin': '20px', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'flex': '1'}),
        
        # Date selection
        html.Div([
            # Etichetta "Da"
            html.Img(src='/assets/DA.png', style={'height': '50px','margin-right': '10px','vertical-align': 'middle'}),
            
            # Dropdown per il giorno di inizio
            html.Div([
                dcc.Dropdown(
                    id='start-day-dropdown',
                    options=[{'label': str(i), 'value': i} for i in range(1, 32)],
                    value=1 , # giorno_odierno
                    style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81'},
                    clearable=False
                )
            ], style={'display': 'inline-block', 'vertical-align': 'middle'}),
            html.Div([ html.P('/', style={'color': '#002060','font-weight':'bold'})], style={'display': 'inline-block'}),
            # Dropdown per il mese di inizio
            html.Div([
                dcc.Dropdown(
                    id='start-month-dropdown',
                    options=[{'label': str(i), 'value': i} for i in range(1, 13)],
                    value=1,  # mese_odierno
                    style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81'},
                    clearable=False
                )
            ], style={'display': 'inline-block', 'vertical-align': 'middle'}),
            html.Div([ html.P('/', style={'color': '#002060','font-weight':'bold'})], style={'display': 'inline-block'}),
            # Dropdown per l'anno di inizio
            html.Div([
                dcc.Dropdown(
                    id='start-year-dropdown',
                    options=[{'label': str(2024), 'value': 2024}],
                    value=2024,  # anno_odierno
                    style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','width':'80px'},
                    clearable=False
                )
            ], style={'display': 'inline-block','vertical-align': 'middle'}),
            
            # Etichetta "A"
             html.Img(src='/assets/A.png', style={'height': '50px','margin-right': '40px','vertical-align': 'middle','margin-left':'20px'}),
            
            # Dropdown per il giorno di fine
            html.Div([
                dcc.Dropdown(
                    id='end-day-dropdown',
                    options=[{'label': str(i), 'value': i} for i in range(1, 32)],
                    value=27,style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81'},
                    clearable=False
                )
            ], style={'display': 'inline-block','vertical-align': 'middle'}),
            html.Div([ html.P('/', style={'color': '#002060','font-weight':'bold'})], style={'display': 'inline-block'}),
            # Dropdown per il mese di fine
            html.Div([
                dcc.Dropdown(
                    id='end-month-dropdown',
                    options=[{'label': str(i), 'value': i} for i in range(1, 11)],
                    value=10,style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81'},
                    clearable=False
                )
            ], style={'display': 'inline-block', 'vertical-align': 'middle'}),
            html.Div([ html.P('/', style={'color': '#002060','font-weight':'bold'})], style={'display': 'inline-block'}),
            # Dropdown per l'anno di fine
            html.Div([
                dcc.Dropdown(
                    id='end-year-dropdown',
                    options=[{'label': str(i), 'value': i} for i in range(2024, 2025)],
                    value=2024,style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','width':'80px'},
                    clearable=False
                )
            ], style={'display': 'inline-block','vertical-align': 'middle'})
        ], style={'flex': '2',
                        'borderRadius': '5px',
                        #'textAlign': 'center',
                        'padding': '5px',
                        'background-color': '#FBDD81','margin-left':'60px','borderRadius': '50px','width':'100px','margin-right': '20px'})
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
], style={'border': '2px #ECF2FE', 'borderRadius': '50px', 'padding': '10px', 'background-color': '#ECF2FE', 'margin-right': '20px'}),
html.Br(),
        html.Div([
    # Blue box containing the content
    html.Div([
        # Row containing both the instruction text and the file upload
        html.Div([
            html.Img(src='/assets/areageografica.jpg', style={'height': '70px','margin-right':'20px','margin-left':'20px'}),
            # Instruction text
            html.Div([
                html.P([html.Span("3.",style={'font-weight':'bold'}),'Seleziona le aree territoriali che vuoi visualizzare.'], style={'margin-bottom': '10px', 'color': '#00194C'}),
            ], style={'margin': '20px', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'flex': '1'}),
            
            # File Upload
            html.Div([
                 html.Img(src='/assets/position.png', style={'height': '40px','margin-right': '20px','horizontal-align': 'middle'}),
                dcc.Dropdown(
            id='initial-dropdown',
            options=[
                {'label': 'Provincia di Caserta', 'value': 'ASL Caserta A04'},  
                {'label': 'Provincia di Caserta 1', 'value': 'ASL Caserta 1'},
                {'label': 'Provincia di Caserta 2', 'value': 'ASL Caserta 2'},
                {'label': 'Provincia di Caserta 3', 'value': 'ASL Caserta 3'},
            ],
            multi=False,
            placeholder="Seleziona area territoriale",
            style={'width': '100%','background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '#FBDD81','borderRadius': '50px',}
                    
                   
                ),
            ], style={'width': '100%',
                        'height': '100%',
                        'borderRadius': '5px',
                        'padding': '5px',
                        'background-color': '#FBDD81','flex': '1', 'padding': '10px','align-items': 'center','display': 'flex','margin-right':'20px','margin-left':'20px','borderRadius': '50px'})
        ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
    ], style={'border': '2px #ECF2FE', 'borderRadius': '50px', 'padding': '10px', 'background-color': '#ECF2FE','margin-right':'20px','margin-left':'20px'})
]),html.Div(id='output-data-upload'),
        html.Br(),
        html.Div([ html.P('Una volta completati tutti i passaggi, avviando lo Smart Scheduler potrai:', style={'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi}),
        html.Ul([
        html.Li([
            'Visualizzare alcuni ',
            html.Span('indicatori di qualità', style={'font-weight': 'bold'}),
            ' delle tue agende;'
        ], style={'listStylePosition': 'inside','color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi}),
        html.Li([
            'Accedere ad ulteriori ',
            html.Span('informazioni', style={'font-weight': 'bold'}),
            ' sulla loro riconfigurazione'
        ], style={'listStylePosition': 'inside','color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi}),
    ]),
], style={ 'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'textAlign': 'center' }),
    html.Br(),
    html.Div([
            html.Button(
                    html.Img(src='/assets/inizia.png', style={'height': '100%', 'width': '100%'}),
                    id='button-avanti',
                    style={
                'height': '50px', 
                'width': '150px', 
                'padding': '0', 
                'border': 'none', 
                'background': 'none',
                'position': 'absolute', 
                #'vertical-align':'middle'
                'right': '45%',
                
            }
                ),
            dcc.Loading(
            id="loading-button",
            type="circle",
            color='blue',
            children=[
                #html.Button('Avanti', id='button-avanti', style={'height': '50px', 'width': '200px', 'font-size': '16px'}),
                dcc.Location(id='url-redirect',refresh='callback-nav')
            ]
        )
    ])])

    
