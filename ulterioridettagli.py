

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
from commonlayout import common_layout,font_family_variable,font_size_paragrafi,font_size_paragrafi_corsivo,font_size_titoli,calculate_table_height,root_path


config = {
    'modeBarButtonsToRemove': ['toImage'],
    'displaylogo': False
}
#table_ult_dettagli_height = calculate_table_height(data_ult_dettagli)
table_ult_dettagli = dag.AgGrid(
    id='filtered-table-ulteriori',
    className="ag-theme-alpine",
    rowStyle={'background-color': 'rgba(181, 208, 255, 0.2)'},
    dashGridOptions={"rowSelection": "multiple", "suppressRowClickSelection": True, "animateRows": False},
    getRowStyle = { 'backgroundColor':'#ECF2FE'
    },
    #style={'height': '180px'},
    defaultColDef={
        'resizable': True,
        'sortable': True,
        'filter': True,
        'flex': 1
        
    },
    
)

table_sugg_int = dag.AgGrid(
    id='table-suggerimento-intelligente',
    className="ag-theme-alpine",
    rowStyle={'background-color': 'rgba(181, 208, 255, 0.2)'},
    dashGridOptions={"rowSelection": "multiple", "suppressRowClickSelection": True, "animateRows": False},
    getRowStyle = {
    'backgroundColor':'#ECF2FE'
    },
    defaultColDef={
        'resizable': True,
        'sortable': True,
        'filter': True,
        'flex': 1
        
    },
    
)


def layout_ulteriori_dettagli():
    return html.Div([
        common_layout(),
        html.Div([
        html.H1('Smart Scheduler - Ulteriori dettagli', style={
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
    }),
        html.Div(
    style={'flex': '2', 'display': 'flex', 'justify-content': 'center'},
    children=[
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Img(src='/assets/calendar.png', style={'height': '50px', 'margin-right': '10px'}),
                        # html.Span("Stai visualizzando: ", style={'font-size': '16px', 'color': '#00194C', 'font-weight': 'bold'}),
                        html.Span(
                            id='agenda_name',
                            style={'font-size': '16px', 'color': '#00194C', 'font-weight': 'bold', 'white-space': 'pre-line', 'margin-left': '10px'}
                        )
                    ],
                    style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
                )
            ],
            style={'display': 'flex', 'flex-direction': 'column'}
        )
    ]
),
            
                    
        html.Div([
        dcc.Tabs(id='tabs-example', value='tab-1', style={'color': '#00338D'},className='custom-tabs', children=[
        dcc.Tab(
    label='Agenda',
    value='tab-1',
    className='custom-tab',
    selected_className='custom-tab--selected',
    children=[
        html.Div(
            style={
                'display': 'flex',
                'flexDirection': 'row',
                'backgroundColor': '#ECF2FE',
                'height': '100%',
                'margin': '10px 20px',  # Margin shorthand
            },
            children=[
                html.Div(
                    style={
                        'border': '2px dashed #0F2471',
                        'padding': '20px',
                        'margin': '20px',
                        'height': '90%',
                        'width': '50%',
                        'marginTop': '20px',
                    },
                    children=[
                        html.Span(
                            'Prestazioni in agenda',
                            style={
                                'position': 'relative',
                                'color': '#0F2471',
                                'fontWeight': 'bold',
                                'top': '-32px',
                                'left': '35%',
                                'transform': 'translateX(50%)',
                                'textAlign': 'center',
                                'backgroundColor': '#ECF2FE',
                                'padding': '10px 20px',
                            }
                        ),
                        html.Div(
                            [
                                html.Div(id='output-container'),
                                table_ult_dettagli
                            ],
                            style={'width': '100%', 'height': '80%'}
                        )
                    ]
                ),
                html.Div(
                    style={
                        'border': '2px dashed #0F2471',
                        'padding': '20px',
                        'margin': '20px',
                        'height': '90%',
                        'width': '50%',
                        'marginTop': '20px',
                        'display': 'flex',
                        'flexDirection': 'column',
                        'alignItems': 'center',
                        'justifyContent': 'center',
                        'position': 'relative',
                        'backgroundColor': '#ECF2FE',
                    },
                    children=[
                        html.Span(
                            "Grado di cooperazione",
                            style={
                                'position': 'absolute',
                                'top': '-22px',
                                'left': '50%',
                                'transform': 'translateX(-50%)',
                                'color': '#0F2471',
                                'fontWeight': 'bold',
                                'textAlign': 'center',
                                'backgroundColor': '#ECF2FE',
                                'padding': '10px 10px',
                                #'height': '20px',
                                'backgroundColor': '#ECF2FE',
                            }
                        ),
                        html.Div(
                            id='chart-text',
                            style={
                                'textAlign': 'center',
                                'color': '#00194C',
                                'fontSize': 16,
                                'marginTop': '25px',  # Aumentato il margine top per separarlo dal titolo
                                'whiteSpace': 'pre-line',
                            },
                            
                        ),
                        html.Div([
                            #html.Img(src="/assets/lampadina.png", style={'margin-right':'50px', 'height': '35px'})
                             html.Img(
        id='image-click-aderenza',
        src='/assets/lampadina.png',
        style={'height': '35px', 'cursor': 'pointer'}
    ),
    dbc.Modal(
            [
                dbc.ModalHeader(
                dbc.Row([
                    dbc.Col(html.Img(src="/assets/lampadina.png", height="30px"), width="auto"),
                    dbc.Col(dbc.ModalTitle("IL GRADO DI COOPERAZIONE "), style={"color": "#FAC424"}),
                    #dbc.Col(html.Img(src="/assets/lente.png", height="30px"), width="auto"),
                ]),
                style={"backgroundColor": "#002060"}  # Blue background
            ),
                dbc.ModalBody([html.P([
                "Il grado di cooperazione rappresenta la percentuale di presenza nelle agende, delle stesse prestazioni «cooperative» ed è composto dai seguenti indicatori:",
                html.Ul([
                    html.Li("La congruenza erogativa"),
                    html.Li("La congruenza al cluster"),
                    html.Li("La congruenza ai raggruppamenti.")
                ],style={'color':"#002060",'font-weight':'bold'}),
                html.P("Tali indicatori sono approfonditi nella sezione «Dettaglio Agenda»")
            ])],style={'backgroundColor':"#ECF2FE",'color':"#002060"}),
                dbc.ModalFooter(
                    dbc.Button(
                        "Chiudi", id="close-aderenza", className="ms-auto", n_clicks=0,style={'backgroundColor':'#FAC424','color':"#002060",'font-weight':'bold'}
                    ), style={"backgroundColor": "#ECF2FE"}
                ),
            ],
            id="modal-aderenza",
            size="lg",
            is_open=False,
        ),
                     ] , style={'margin-left':'auto'})
                        
                    ]
        )])]),

dcc.Tab(
    label='Dettaglio Agenda', 
    value='tab-2', 
    style={'color': '#00338D'}, 
    className='custom-tab', 
    selected_className='custom-tab--selected', 
    children=[
        html.Div(
            style={'backgroundColor': '#ECF2FE', 'padding': '20px', 'marginRight': '20px', 'marginLeft': '20px', 'marginBottom': '20px'}, 
            children=[
                html.Div(
                    style={'backgroundColor': '#ECF2FE', 'padding': '20px', 'marginRight': '20px', 'marginLeft': '20px', 'marginBottom': '20px'}, 
                    children=[
                        html.Div([
                            html.Span(
                                "Gradi di congruenza", 
                                className="table-title", 
                                style={
                                    'position': 'absolute', 
                                    'top': '-15px', 
                                    'left': '50%', 
                                    'transform': 'translateX(-50%)', 
                                    'background-color': '#ECF2FE', 
                                    'font-weight': 'bold', 
                                    'color': '#0F2471', 
                                    'padding-left': '20px', 
                                    'padding-right': '20px'
                                }
                            ),
                            html.Div([
                                html.Div([
                                    dcc.Graph(id='grafo-donut-chart', style={'height': '300px'}),
                                ], style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top', 'textAlign': 'center', 'marginLeft': '35px'}),
                                html.Div([
                                    dcc.Graph(id='cluster-donut-chart', style={'height': '300px'}),
                                ], style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top', 'textAlign': 'center', 'marginLeft': '35px'}),
                                html.Div([
                                    dcc.Graph(id='raggruppamenti-donut-chart', style={'height': '300px'}),
                                ], style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top', 'textAlign': 'center', 'marginLeft': '35px'}),
                            ]), 
    html.Br(),
    html.Div([
    html.Img(
        id='image-click-congruenza',
        src='/assets/lampadina.png',
        style={'height': '70px', 'cursor': 'pointer','margin-left':'1000px'}
    ),
    dbc.Modal(
            [
                dbc.ModalHeader(
                dbc.Row([
                    dbc.Col(html.Img(src="/assets/lampadina.png", height="30px"), width="auto", className="ml-auto"),
                    dbc.Col(dbc.ModalTitle("DETTAGLIO GRADO DI COOPERAZIONE "), style={"color": "#FAC424"}),
                    #dbc.Col(html.Img(src="/assets/lente.png", height="30px"), width="auto"),
                ]),
                style={"backgroundColor": "#002060"}  # Blue background
            ),
                dbc.ModalBody(
    [
        html.P([
            "La ",
                html.Span("congruenza al grafo", style={"font-weight": "bold"}), " è direttamente proporzionale al numero di coppie di prestazioni effettivamente coerenti con la configurazione proposta dal grafo. "
            "Pertanto, valori elevati sono indice di maggiore coerenza dell’agenda in termini di prestazioni inserite in essa. "
            "Viceversa, valori ridotti rappresentano una scarsa coerenza tra le prestazioni presenti nella stessa agenda e suggeriscono l’opzione di riconfigurare l’agenda (secondo le indicazioni del grafo)."
    ]),
        html.P([
            "La ",
                html.Span("congruenza al cluster", style={"font-weight": "bold"})," è la percentuale di congruenza delle coppie di prestazioni presenti in agenda rispetto a cluster di prestazioni. "
            "Valori elevati confermano la congruenza complessiva delle prestazioni presenti; valori ridotti suggeriscono la possibilità di creare diverse agende nelle quali riallocare le prestazioni coerentemente ai cluster individuati."
    ]),
        html.P(
            [
                "La ",
                html.Span("congruenza ai raggruppamenti", style={"font-weight": "bold"}),
                " è rappresentativo del tasso di effettivo efficientamento dell’agenda tramite raggruppamento di prestazioni prescritte e quindi erogate in modalità cooperativa. "
                "Valori ridotti suggeriscono la necessità di raggruppare tramite apposita configurazione in testata agende le prestazioni che si presentano in coppia."
            ]
        )
    ],
style={'backgroundColor': "#ECF2FE",'color':"#002060"}),
                dbc.ModalFooter(
                    dbc.Button(
                        "Chiudi", id="close-congruenza", className="ms-auto", n_clicks=0,style={'backgroundColor':'#FAC424','color':"#002060",'font-weight':'bold'}
                    ), style={"backgroundColor": "#ECF2FE"}
                ),
            ],
            id="modal-congruenza",
            size="lg",
            is_open=False,
        ),
])

                        
                    
        ])]),
                       
                html.Div([
                    html.Img(src='assets/robot.png', style={'display': 'inline-block', 'verticalAlign': 'middle', 'height': '35px'}),
                    html.H1(
                        'Suggerimenti – Scopri quali prestazioni migliorerebbero, se aggiunte, la performance delle tue agende!', 
                        style={
                            'display': 'inline-block',
                            'margin-left': '10px',
                            'color': '#00338D',
                            'font-family': 'Arial, sans-serif',
                            'font-size': '20px',
                            'font-weight': 'bold',
                        }
                    ),
                    html.P(
                        ["Sulla base dell'analisi effettuata su tale agenda, di seguito si indicano le prestazioni da inserire nell'agenda per aumentarne l'efficienza:"],
                        style={
                            'color': '#00338D', 
                            'font-style': 'italic', 
                            'font-family': 'Arial, sans-serif', 
                            'font-size': '16px'
                        }
                    )
                ]),
                html.Div([
                    html.Div([table_sugg_int])
                ], style={'width': '100%', 'display': 'inline-block', 'verticalAlign': 'top'}),
            ]
        )
    ]
)
])
        ])
    ])

        
    