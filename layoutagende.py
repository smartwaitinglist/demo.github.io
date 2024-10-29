from dash import  html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
from dash import html
from commonlayout import common_layout,font_family_variable,font_size_paragrafi,font_size_paragrafi_corsivo,font_size_titoli,calculate_table_height,root_path
## DF 1 FOGLIO -> COD-DESC-GRADO DI ADERENZA-URGENZA
# Costruisci il percorso completo del file Excel
#data_agende_path = os.path.join(root_path, 'data_agende.xlsx')

# Carica il file Excel utilizzando pandas
#data_agende = pd.read_excel(os.path.join(root_path, 'data_agende.xlsx'))
# Converti i valori delle colonne in stringhe con il simbolo percentuale
#data_agende['Grado di aderenza al grafo*'] *= 100
#data_agende['Grado di urgenza**'] *= 100
#data_agende['Grado di aderenza al grafo*'] = data_agende['Grado di aderenza al grafo*'].apply(lambda x: '-' if pd.isna(x) else f"{x:.0f}%")
#data_agende['Grado di urgenza**'] = data_agende['Grado di urgenza**'].apply(lambda x: '-' if pd.isna(x) else f"{x:.0f}%")
table = dag.AgGrid(
        id = 'table-new',
        className="ag-theme-alpine",
        style={'height': '50vh'},
        #rowStyle=get_row_style,
        selectedRows=[], 
        dashGridOptions={"rowSelection": "multiple", "suppressRowClickSelection": True, "animateRows": False,"rowHeight": 50},
       
        defaultColDef={
            'resizable': True,
            'sortable': True,
            'filter': True,
            'flex': 1
            
        })
def layout_agende():
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
        }),
        html.Div([
            html.H2('Benvenuto in Smart Scheduler', style={
                'color': '#00194C', 
                'font-weight': 'bold', 
                'font-size': font_size_titoli, 
                'font-family': font_family_variable, 
                'margin-left': '20px', 
                'margin-right': '20px',
                'margin-top':'20px'
            }),
            html.Div([
                html.P([
                    'Navigando tra i file caricati, ',
                    html.Span('prioritizzare gli slot delle agende', style={
                        'font-weight': 'bold', 
                        'font-size': font_size_paragrafi, 
                        'font-family': font_family_variable
                    }),
                    ', seleziona ',
                    html.Span('corretta allocazione delle priorità', style={
                        'font-weight': 'bold', 
                        'font-size': font_size_paragrafi, 
                        'font-family': font_family_variable
                    }),
                    ' una o più agende da attenzionare attraverso le apposite spunte.'
                ], style={
                    'margin-bottom': '0', 
                    'color': '#00194C', 
                    'font-family': font_family_variable, 
                    'font-size': font_size_paragrafi, 
                    'margin-left': '20px', 
                    'margin-right': '20px'
                }),
                html.Div([
                            #html.Img(src="/assets/lampadina.png", style={'margin-right':'50px', 'height': '35px'})
                             html.Img(
        id='image-click-agende',
        src='/assets/lampadina.png',
        style={'height': '35px', 'cursor': 'pointer'}
    ),
    dbc.Modal(
            [
                dbc.ModalHeader(
                dbc.Row([
                    dbc.Col(html.Img(src="/assets/lampadina.png", height="30px"), width="auto"),
                    dbc.Col(dbc.ModalTitle("QUALI AGENDE RICHIEDONO LA TUA ATTENZIONE "), style={"color": "#FAC424"}),
                    #dbc.Col(html.Img(src="/assets/lente.png", height="30px"), width="auto"),
                ]),
                close_button = False,
                style={"backgroundColor": "#002060"}  # Blue background
            ),
dbc.ModalBody(
    dbc.Container([
        dbc.Row([
            dbc.Col(html.Img(src="/assets/attenzione.png", height="40px", width="auto"), width="auto"),
            dbc.Col(html.P(html.U("I valori degli indicatori esposti rappresentano delle indicazioni a supporto dell’utente nella scelta delle agende da attenzionare.")), width=True),
        ], align="center"),  # Align items vertically centered
        html.H4(html.B("1. Prestazioni «cooperative»")),
        html.P("Il grado di cooperazione rappresenta la percentuale di presenza nelle agende delle stesse prestazioni «cooperative». Esso è determinato da una serie di indicatori:"),
        html.Ul([
            html.Li([html.B("Congruenza erogativa:"), " è direttamente proporzionale al numero di prestazioni erogate contemporaneamente. Pertanto, maggiore è il valore di tale indicatore e maggiore sarà il grado di cooperazione."]),
            html.Li([html.B("Congruenza al cluster:"), " rappresenta la percentuale di congruenza delle coppie di prestazioni presenti in agenda rispetto a cluster di prestazioni. Anche tale indicatore è direttamente proporzionale al grado di cooperazione."]),
            html.Li([html.B("Congruenza ai raggruppamenti:"), " rappresenta il tasso di effettivo efficientamento dell’agenda tramite raggruppamento di prestazioni cooperative ovvero prescritte e quindi erogate in modalità cooperativa."])
        ]),
        html.H4(html.B("2. Grado di Urgenza")),
        html.P("Il grado di urgenza rappresenta il tasso di urgenza con il quale l’agenda deve essere modificata. Maggiore risulta essere il valore di tale indicatore, maggiore risulta essere l’urgenza con la quale modificare l’agenda. È determinato da una serie di fattori:"),
        html.Ul([
            html.Li([html.B("Saturazione dell’agenda:"), " è inversamente proporzionale al livello di saturazione dell’agenda. Maggiori saranno gli slot occupati, minore sarà il grado di urgenza"]),
            html.Li([html.B("Prioritizzazione:"), " è inversamente proporzionale al livello di prioritizzazione dell’agenda. Maggiori saranno gli slot ai quali è stata attribuita una classe di priorità, minore sarà il grado di urgenza;"]),
            html.Li([html.B("Grado di attesa:"), " è inversamente proporzionale alla data di prima disponibilità dell’agenda, più lontana sarà la prima data di disponibilità dell’agenda e minore sarà il grado di urgenza."])
        ])
    ]),
    style={'backgroundColor': "#ECF2FE", 'color': "#002060"}
),
                dbc.ModalFooter(
                    dbc.Button(
                        "Chiudi", id="close-agende", className="ms-auto", n_clicks=0,style={'backgroundColor':'#FAC424','color':"#002060",'font-weight':'bold'}
                    ), style={"backgroundColor": "#ECF2FE"}
                ),
            ],
            id="modal-agende",
            size="lg",
            scrollable=True,
            is_open=False,
        ),
                     ] , style={'margin-left':'auto'})
            ], style={
                'display': 'flex', 
                'align-items': 'center'
            })
        ]),
        html.Br(),
        html.Div([
            html.Div([
                #html.Div(dag.AgGrid(id='table-new'))
                table
            ]),
            html.Div([
                dcc.Link(
                        html.Img(src='/assets/backward.png', style={'height': '50px', 'vertical-align': 'middle'}),
                        href='/calendario',
                        style={'position': 'static', 'display': 'inline-block', 'margin-right': '10px'}
                    ),
                html.Div([
                   
                    dcc.Link(
                        html.Img(src='/assets/arrow_avanti.png', style={'height': '50px', 'vertical-align': 'middle'}),
                        href='/tempi_attesa',
                        style={'position': 'static', 'display': 'inline-block', 'margin-left': '10px'}
                    #,refresh = 'callback-nav')
                    )
                ], style={'display': 'flex', 'align-items': 'center', 'margin-left': 'auto'})  
            ], style={'display': 'flex', 'align-items': 'center'})  
        ], style={
            'margin-left': '20px',  
            'margin-right': '20px'  
        })
    ])

