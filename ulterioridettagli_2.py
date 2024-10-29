from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

from commonlayout import common_layout, font_family_variable, font_size_paragrafi, font_size_titoli, calculate_table_height, root_path


config = {
    'modeBarButtonsToRemove': ['toImage'],
    'displaylogo': False
}

table_ult_dettagli = dag.AgGrid(
    id='filtered-table-ulteriori',
    className="ag-theme-alpine",
    rowStyle={'background-color': 'rgba(181, 208, 255, 0.2)'},
    dashGridOptions={"rowSelection": "multiple", "suppressRowClickSelection": True, "animateRows": False},
    getRowStyle={'backgroundColor': '#ECF2FE'},
    defaultColDef={
        'resizable': True,
        'sortable': True,
        'filter': True,
        'flex': 1,
        'headerClass': 'custom-header-span' 
    },
)

table_sugg_int = dag.AgGrid(
    id='table-suggerimento-intelligente',
    className="ag-theme-alpine",
    rowStyle={'background-color': 'rgba(181, 208, 255, 0.2)','height':'1%'},
    dashGridOptions={"rowSelection": "multiple", "suppressRowClickSelection": True, "animateRows": False},
    getRowStyle={'backgroundColor': '#ECF2FE'},
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
            html.H1('Smart wAIting List', style={
                'margin': '0', 
                'color': '#00194C',
                'font-family': font_family_variable, 
                'font-size': '14px', 
                'font-weight': 'bold',
            }),
            html.Div('Smart Tips – Suggerimenti per la tua Agenda efficace ')
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
        html.Div(
            style={'flex': '2', 'display': 'flex', 'justify-content': 'center'},
            children=[
                html.Div(
                    children=[
                        dcc.Link(
                            html.Img(src='/assets/backward.png', style={'height': '7vh', 'vertical-align': 'middle','display':'flex','align-items':'central'}),
                            href='/tempi_attesa',
                            style={'left': '1vh'}
                        ),
                        html.Div(
                            children=[
                                html.Img(src='/assets/calendar.png', style={'height': '7vh', 'margin-right': '1vh'}),
                                html.Span(
                                    id='agenda_name',
                                    style={'font-size': '2vh', 'color': '#00194C', 'font-weight': 'bold', 'white-space': 'pre-line', 'margin-left': '1vh'}
                                )
                            ],
                            style={'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}
                        )
                    ],
                    style={'display': 'flex', 'flex-direction': 'row', 'margin': '1vh'}
                )
            ]
        ),
        html.Div([
            dcc.Tabs(id='tabs-example', value='tab-1', style={'color': '#00338D'}, className='custom-tabs', children=[
                dcc.Tab(
                    label='Agenda',
                    value='tab-1',
                    selected_className='custom-tab--selected',
                    children=[
                        html.Div(
                            style={
                                'display': 'flex',
                                'flexDirection': 'row',
                                'backgroundColor': '#ECF2FE',
                                'height': '65vh',
                                'margin': '2vh 2%',
                            },
                            children=[
                                html.Div(
                                    className='dashed-border',
                                    children=[
                                        html.Span('Prestazioni in agenda',className='title-span'),
                                        html.Div(id='output-container', style={'fontSize': '2vh'}),
                                        html.Div(
                                            className='responsive-table-container content',
                                            children=[
                                                table_ult_dettagli
                                            ]
                                        )
                                    ]
                                
                                ),
                                html.Div(
                                    className='dashed-border',
                                    children=[
                                        html.Span('Grado di cooperazione',className='title-span'),
                                        html.Div(
                                            id='chart-text',
                                            style={
                                                'textAlign': 'center',
                                                'color': '#00194C',
                                                'fontSize': '1.5vh',
                                                'marginTop': '2vh',
                                                'whiteSpace': 'pre-line',
                                                'width': '100%',
                                                'height': '100%'
                                            },
                                        ),
                                        html.Div([
                                            html.Img(
                                                id='image-click-aderenza',
                                                src='/assets/lampadina.png',
                                                style={'height': '5vh', 'cursor': 'pointer'}
                                            ),
                                            dbc.Modal(
                                            
                                                [
                                                    dbc.ModalHeader(
                                                        dbc.Row([
                                                            dbc.Col(html.Img(src="/assets/lampadina.png", height="30px"), width="auto"),
                                                            dbc.Col(dbc.ModalTitle("IL GRADO DI COOPERAZIONE "), style={"color": "#FAC424"}),
                                                        ]),
                                                        style={"backgroundColor": "#002060"},
                                                        close_button = False
                                                    ),
                                                    dbc.ModalBody([html.P([
                                                        "Il grado di cooperazione rappresenta la percentuale di presenza nelle agende, delle stesse prestazioni «cooperative» ed è composto dai seguenti indicatori:",
                                                        html.Ul([
                                                            html.Li("La congruenza erogativa"),
                                                            html.Li("La congruenza al cluster"),
                                                            html.Li("La congruenza ai raggruppamenti.")
                                                        ], style={'color': "#002060", 'font-weight': 'bold'}),
                                                        html.P("Tali indicatori sono approfonditi nella sezione «Dettaglio Agenda»")
                                                    ])], style={'backgroundColor': "#ECF2FE", 'color': "#002060"}),
                                                    dbc.ModalFooter(
                                                        dbc.Button(
                                                            "Chiudi", id="close-aderenza", className="ms-auto", n_clicks=0,
                                                            style={'backgroundColor': '#FAC424', 'color': "#002060", 'font-weight': 'bold'}
                                                        ), style={"backgroundColor": "#ECF2FE"}
                                                    ),
                                                    
                                                ],
                                                id="modal-aderenza",
                                                size="lg",
                                                is_open=False,
                                                scrollable=True
                                            ),
                                        ], style={'margin-left': 'auto'})
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dcc.Tab(
                    label='Dettaglio Agenda',
                    value='tab-2',
                    selected_className='custom-tab--selected',
                    children=[
                        html.Div(
                            style={
                                'backgroundColor': '#ECF2FE',
                                'padding': '2vh',
                                'marginRight': '2.5%',
                                'marginLeft': '2.5%',
                                'marginBottom': '2vh'
                            },
                            children=[
                                html.Div(
                                    style={
                                        'backgroundColor': '#ECF2FE',
                                        'padding': '2vh',
                                        'marginRight': '2.5%',
                                        'marginLeft': '2.5%',
                                        'marginBottom': '2vh'
                                    },
                                    children=[
                                        html.Div([
                                            html.Div([
                                                html.Div([
                                                    dcc.Graph(id='grafo-donut-chart', style={'height': '20vh'}),
                                                ], style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top', 'textAlign': 'center', 'marginLeft': '2vh'}),
                                                html.Div([
                                                    dcc.Graph(id='cluster-donut-chart', style={'height': '20vh'}),
                                                ], style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top', 'textAlign': 'center', 'marginLeft': '2vh'}),
                                                html.Div([
                                                    dcc.Graph(id='raggruppamenti-donut-chart', style={'height': '20vh'}),
                                                ], style={'display': 'inline-block', 'width': '30%', 'verticalAlign': 'top', 'textAlign': 'center', 'marginLeft': '2vh'}),
                                            ]),
                                            html.Div([
                                                html.Img(
                                                    id='image-click-congruenza',
                                                    src='/assets/lampadina.png',
                                                    style={'height': '5vh', 'cursor': 'pointer', 'margin-left': 'auto'}
                                                ),
                                                dbc.Modal(
                                                    [
                                                        dbc.ModalHeader(
                                                            dbc.Row([
                                                                dbc.Col(html.Img(src="/assets/lampadina.png", height="30px"), width="auto"),
                                                                dbc.Col(dbc.ModalTitle("DETTAGLIO GRADO DI COOPERAZIONE "), style={"color": "#FAC424"}),
                                                            ]),
                                                            style={"backgroundColor": "#002060"},
                                                            close_button = False
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
                                                                html.P([
                                                                    "La ",
                                                                    html.Span("congruenza ai raggruppamenti", style={"font-weight": "bold"}),
                                                                    " è rappresentativo del tasso di effettivo efficientamento dell’agenda tramite raggruppamento di prestazioni prescritte e quindi erogate in modalità cooperativa. "
                                                                    "Valori ridotti suggeriscono la necessità di raggruppare tramite apposita configurazione in testata agende le prestazioni che si presentano in coppia."
                                                                ])
                                                            ],
                                                            style={'backgroundColor': "#ECF2FE", 'color': "#002060"}),
                                                        dbc.ModalFooter(
                                                            dbc.Button(
                                                                "Chiudi", id="close-congruenza", className="ms-auto", n_clicks=0, style={'backgroundColor': '#FAC424', 'color': "#002060", 'font-weight': 'bold'}
                                                            ), style={"backgroundColor": "#ECF2FE"}
                                                        ),
                                                    ],
                                                    id="modal-congruenza",
                                                    size="lg",
                                                    is_open=False,
                                                    scrollable=True
                                                ),
                                            ],style={'display':'flex'})
                                        ]),
                                        html.Div([
                                            html.Img(src='assets/robot.png', style={'display': 'inline-block', 'verticalAlign': 'middle', 'height': '4vh'}),
                                            html.H1(
                                                'Suggerimenti – Scopri quali prestazioni migliorerebbero, se aggiunte, la performance delle tue agende!',
                                                style={
                                                    'display': 'inline-block',
                                                    'margin-left': '1vh',
                                                    'color': '#00338D',
                                                    'font-family': 'Arial, sans-serif',
                                                    'font-size': '2vh',
                                                    'font-weight': 'bold',
                                                }
                                            ),
                                            html.P(
                                                ["Sulla base dell'analisi effettuata su tale agenda, di seguito si indicano le prestazioni da inserire nell'agenda per aumentarne l'efficienza:"],
                                                style={
                                                    'color': '#00338D',
                                                    'font-style': 'italic',
                                                    'font-family': 'Arial, sans-serif',
                                                    'font-size': '1.8vh'
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
                    ]
                ),
            ]),
        ])
    ])


        












