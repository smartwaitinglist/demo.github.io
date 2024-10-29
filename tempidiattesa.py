import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from datetime import date
from dash.exceptions import PreventUpdate
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import dash_ag_grid as dag
import base64
import os
from datetime import date
from dateutil.relativedelta import relativedelta
from io import BytesIO
#from PIL import Image, ImageDraw, ImageFont
from flask import send_from_directory
from roots import base_path
from commonlayout import common_layout, font_family_variable, font_size_paragrafi, font_size_paragrafi_corsivo, font_size_titoli, calculate_table_height, root_path

# Percorso dell'immagine
path = os.path.join(base_path, 'assets', 'nuvoletta.png')
encoded_image = base64.b64encode(open(path, 'rb').read()).decode('utf-8')



path = os.path.join(base_path, 'assets', 'nuvoletta.png')
#buffer = write_on_image(path, 'Testo da scrivere')
#encoded_image = base64.b64encode(buffer.read()).decode()

def layout_tempi_attesa():
    return html.Div([
        common_layout(),
        html.Div([
            html.H1('Smart Scheduler - Dashboard', style={
                'margin': '0', 
                'color': '#00194C',
                'font-family': font_family_variable, 
                'font-size': '14px', 
                'font-weight': 'bold',
            }),
            html.Div('Suggerimenti degli slot da allocare e prioritizzare')
        ], style={
            'display': 'flex',
            'justify-content': 'space-between',
            'align-items': 'center',
            'background-color': '#B5D0FF',
            'padding': '10px',
            'height': '0.5cm',
            'font-weight':'bold',
            'width': '100%'
        }),
        html.Div([
    # Row containing both the instruction text and the file upload
    html.Div([
        html.Img(src='/assets/book.png', style={'height': '5vw', 'margin-right': '2vw', 'margin-left': '2vw'}),
        # Instruction text
        html.Div([
            html.P('Stai visualizzando', style={'color': '#00194C', 'margin': '0'}),
        ], style={'font-family': 'Tahoma', 'font-size': '3vh', 'flex': 'none', 'margin-right': '2vw'}),
        # File Upload
        html.Div([
            dcc.Dropdown(
                id='dropdown-tempi-attesa',
                multi=False,
                style={'width': '100%', 'background-color': '#FBDD81', 'color': '#002060', 'font-weight': 'bold', 'border': 'none', 'borderRadius': '30px'}
            ),
        ], style={'width': '100%', 'height': '100%', 'borderRadius': '50px', 'padding': '1%', 'background-color': '#FBDD81', 'display': 'flex', 'align-items': 'center', 'margin-right': '1%', 'margin-left': '7%'})
    ], style={'display': 'flex', 'align-items': 'center', 'justify-content': 'space-between'})
], style={'border': '2px solid #ECF2FE', 'borderRadius': '50px', 'padding': '1%', 'background-color': '#ECF2FE', 'margin-bottom': '1%', 'margin-right': '3%', 'margin-left': '3%','margin-top': '1%'}),

        html.Div([
            dbc.Row([
                dbc.Col([
                    html.Div([
                        html.Span("Recap classi di priorità", className="table-title", style={
                            'position': 'absolute', 'top': '-1vw', 'left': '50%', 'transform': 'translateX(-50%)', 'background-color': 'white', 'font-weight': 'bold', 'color': '#0F2471', 'padding': '0 1vw'}),
                        html.Div([
                            html.Table([
                                html.Thead(html.Tr([
                                    html.Th("Priorità", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                    html.Th("Classe", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                    html.Th("Stato attuale", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                    html.Th("Stato post riconfigurazione", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                ])),
                                html.Tbody(id='table-actual-slot', style={'text-align': 'center', 'padding': '0.5vw'})
                            ], className="table custom-table"),
                        ], className="dashed-container"),
                    ], className="table", style={'margin-top': '0px', 'border': '2px dashed #00194C', 'padding': '1em', 'position': 'relative', 'width': '100%', 'border-color': '#00338D', 'borderRadius': '50px', 'margin-left': '2em'}),  # Ridotto margine sinistro
                ], width=6),
                dbc.Col([
                    html.Div([
                        html.Span("Attesa stimata", className="table-title", style={'position': 'absolute', 'top': '-1vw', 'left': '50%', 'transform': 'translateX(-50%)', 'background-color': 'white', 'font-weight': 'bold',  'color': '#0F2471','padding': '0 1vw'}),
                        html.Div([
                            html.Table([
                                html.Thead(html.Tr([
                                    html.Th("Priorità", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                    html.Th("Classe", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                    html.Th("Stato attuale", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                    html.Th("Stato post riconfigurazione", className="table-header", style={'font-size': '0.8vw', 'font-family': font_family_variable, 'font-style': 'italic', 'color': '#0F2471', 'text-align': 'center', 'padding': '0.5vw'}),
                                ])),
                                html.Tbody(id='table-actual-days', style={'text-align': 'center', 'padding': '0.5vw'})
                            ], className="table custom-table"),
                        ], className="dashed-container"),
                    ], className="table", style={'margin-top': '0px', 'border': '2px dashed #00194C', 'padding': '1em', 'position': 'relative', 'width': '100%', 'border-color': '#00338D', 'borderRadius': '50px','margin-left':'2em'}),  # Ridotto borderRadius
                ], width=6),
            ]),
            html.Div([
                html.Div([
                    html.Img(src=f'data:image/png;base64,{encoded_image}', style={
                        'width': '20vw',
                        'height': '20vw',
                        'margin-bottom': '2vh'
                    }),
                    html.Div([
                        html.Img(src='/assets/calendar.png', style={'height': '10vw', 'margin-bottom': '1vw'}),
                        html.Span(id='stima-tempi-attesa', style={
                            'color': '#00338D',
                            'font-size': '1vw',
                            'text-align': 'center',
                            'white-space': 'normal'
                        })
                    ], style={
    'position': 'absolute',
    'top': '1%',
    'left': '10%',
    'transform': 'matrix(1, 0, 0, 1, 0, 0)',
    'display': 'flex',
    'flex-direction': 'column',
    'align-items': 'center',
    'justify-content': 'space-evenly',
    'width': '80%',
    'padding': '1vw',
    'flex-wrap': 'nowrap',
    'align-content': 'stretch'
}
)
                ], style={'position': 'relative', 'display': 'inline-block'})
            ], style={'text-align': 'center', 'margin-top': '5vh'})  
        ], style={'padding': '1vw', 'display': 'flex'}),
        html.Div([
    dcc.Link(
        html.Img(src='/assets/backward.png', style={'height': '8vh', 'margin-top': '-5vh', 'margin-left':'2vw'}),
        href='/agende',
        style={'position': 'static', 'font-size': '2vw'},
    ),
    html.Div([
        dcc.Link(
            html.Img(src='/assets/ulterioridettagli.png', style={'height': '7vh', 'margin-top': '-5vh','margin-left': '-30vw'}),
            href='/ulteriori_dettagli',
        ),
        html.Img(
            id = 'download-image',
            src='/assets/conisglio_di_dimensionamento.png',
            style={'height': '7vh', 'margin-top': '-5vh', 'margin-left': '1vw'}
        ),
        dbc.Tooltip(
            id='tooltip-download-image',
            target='download-image',
            children=html.Div('Ottieni il dettaglio della riconfigurazione da apportare nella sezione «Sbarramenti» del CUP Regionale!',
            style={'font-weight': 'bold', "backgroundColor": "#ECF2FE", "color": "#00194C", 'padding': '0.5vw', 'border-radius': '0.3vw'})
        ),
        dcc.Loading(
            id="loading-button",
            style= {'margin-left':'30vh','margin-bottom':'7vh'},
            type="circle",
            color='blue',
            children=[
                dcc.Download(id="download-file")
            ]
        )
    ], style={
        'display': 'flex',
        'justify-content': 'center',  # Modificato per centrare le ultime due immagini
        'align-items': 'baseline',
        'position': 'relative',
        'width': '100%',
    }),
], style={
    'display': 'flex',
    'justify-content': 'space-between',  # Spazio tra gli elementi per mettere le ultime due immagini al centro
    'align-items': 'baseline',
    'position': 'relative',
    'width': '100%',
})

        ]),







        











