import dash
from dash import html, dcc
from commonlayout import common_layout

app = dash.Dash(__name__)
font_family_variable = 'Tahoma'
font_size_titoli = '2vh'
font_size_paragrafi = '2vh'
font_size_paragrafi_corsivo = '1.75vh'

###### Home Layout ######
def layout_home():
    return html.Div([
        common_layout(),
        html.Div([
            html.H1('Smart Scheduler', style={
                'margin': '0', 
                'color': '#00194C',
                'font-family': font_family_variable, 
                'font-size': '2vh', 
                'font-weight': 'bold',
            }),
            html.Div(id='username')
        ], style={
            'display': 'flex',
            'justify-content': 'space-between',
            'align-items': 'center',
            'background-color': '#B5D0FF',
            'padding': '1%',
            'height': '5vh',
            'width': '100%'
        }),
        html.Div([
            html.H2('Benvenuto in Smart Scheduler', style={'color': '#00194C', 'font-weight': 'bold', 'font-size': '3vh'}),
            html.P([
                'Questa funzionalità ti fornisce suggerimenti in merito alla ',
                html.Span('configurazione efficiente delle agende ', style={'font-weight': 'bold'}),
            ], style={'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'textAlign': 'center'}),
        ], style={ 'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'textAlign': 'center','margin-top':'1%'}),
        html.Div([
            # Blue box containing the content
            html.Div([
                # Row containing both the instruction text and the file upload
                html.Div([
                    html.Img(src='/assets/upload.png', style={'height': '8vh'}),  # Ridotto altezza immagine
                    # Instruction text
                    html.Div([
                        html.P([html.Span("1. ",style={'font-weight':'bold'}),'Carica in formato .xlsx le agende da riconfigurare'], style={'margin-bottom': '0.5%', 'color': '#00194C'}),
                    ], style={'margin': '0.5%', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'flex': '1'}),
                    # File Upload
                    html.Div([
                        dcc.Upload(
                            id='upload-data',
                            children=html.Div([
                                html.Img(src='/assets/load_file.png', style={'height': '4vh', 'margin-bottom': '1%'}),  # Ridotto altezza immagine
                                html.Div('Trascina o seleziona il file', id='upload-text', style={'textAlign': 'center', 'font-size': '1.5vh'})
                            ], id='upload-container', style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),
                            style={
                                'width': '100%',
                                'height': '100%',
                                'borderRadius': '50px',  # Border radius modificato
                                'textAlign': 'center',
                                'padding': '1%',
                                'background-color': '#FBDD81',
                                'margin-right': '1%',  # Ridotto margine destro
                            },
                            multiple=False
                        ),
                    ], style={'flex': '1'})
                ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
            ], style={'border': '2px #ECF2FE', 'borderRadius': '50px', 'padding': '1%', 'background-color': '#ECF2FE', 'margin-bottom': '1%', 'margin-right':'3%', 'margin-left':'3%'})  # Ridotto margine e raggio del bordo
        ]),
        
        html.Div([
            # Blue box containing the content
            html.Div([
                # Row containing both the instruction text and the date selection
                html.Div([
                    html.Div([
                        html.P([html.Span("2. ",style={'font-weight':'bold'}),'Scegli il periodo di riconfigurazione (max 6 mesi)'], style={'margin-bottom': '0.5%', 'color': '#00194C'}),
                    ], style={'margin': '0.5%', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'flex': '1'}),  # Ridotto margine
                    
                    # Date selection
                    html.Div([
                        html.Img(src='/assets/DA.png', style={'height': '8vh', 'margin-right': '1%', 'vertical-align': 'middle'}), 
                        html.Div([
                            dcc.Dropdown(
                                id='start-day-dropdown',
                                options=[{'label': str(i), 'value': i} for i in range(1, 32)],
                                value=1,  # giorno_odierno
                                style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','borderRadius': '50px',},
                                clearable=False
                            )
                        ], style={'display': 'inline-block', 'vertical-align': 'middle'}),
                        html.Div([
                            dcc.Dropdown(
                                id='start-month-dropdown',
                                options=[{'label': str(i), 'value': i} for i in range(1, 13)],
                                value=1,  # mese_odierno
                                style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','borderRadius': '50px',},
                                clearable=False
                            )
                        ], style={'display': 'inline-block', 'vertical-align': 'middle'}),
                        html.Div([
                            dcc.Dropdown(
                                id='start-year-dropdown',
                                options=[{'label': str(i), 'value': i} for i in range(2024,2026)],
                                value=2024,  # anno_odierno
                                style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','width':'8vw','borderRadius': '50px',},
                                clearable=False
                            )
                        ], style={'display': 'inline-block','vertical-align': 'middle'}),
                        html.Div([
                            html.Img(src='/assets/A.png', style={'height': '8vh', 'margin-right': '1%', 'vertical-align': 'middle', 'margin-left': '1%'}),  # Ridotto altezza immagine e margini
                        ], style={'display': 'inline-block','vertical-align': 'middle'}),
                        html.Div([
                            dcc.Dropdown(
                                id='end-day-dropdown',
                                options=[{'label': str(i), 'value': i} for i in range(1, 32)],
                                value=27,style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','borderRadius': '50px',},
                                clearable=False
                            )
                        ], style={'display': 'inline-block','vertical-align': 'middle'}),
                        html.Div([
                            dcc.Dropdown(
                                id='end-month-dropdown',
                                options=[{'label': str(i), 'value': i} for i in range(1, 13)],
                                value=10,style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','borderRadius': '50px',},
                                clearable=False
                            )
                        ], style={'display': 'inline-block', 'vertical-align': 'middle'}),
                        html.Div([
                            dcc.Dropdown(
                                id='end-year-dropdown',
                                options=[{'label': str(i), 'value': i} for i in range(2024, 2026)],
                                value=2024,style = {'background-color': '#FBDD81','color': '#002060','font-weight':'bold','border': '2px #FBDD81','width':'8vw','borderRadius': '50px',},
                                clearable=False
                            )
                        ], style={'display': 'inline-block', 'vertical-align': 'middle'})
                    ], style={'display': 'flex', 'align-items': 'center'}),
                ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
            ], style={'border': '2px #ECF2FE', 'borderRadius': '50px', 'padding': '1%', 'background-color': '#ECF2FE', 'margin-bottom': '1%', 'margin-right':'3%', 'margin-left':'3%'})  # Ridotto margine e raggio del bordo
        ]),
        html.Div([
            html.Div([
                # Blue box containing the content
                html.Div([
                    # Row containing both the instruction text and the file upload
                    html.Div([
                        html.Img(src='/assets/areageografica.jpg', style={'height': '8vh', 'margin-right': '1%', 'margin-left': '1%'}),  # Ridotto altezza immagine e margini
                        # Instruction text
                        html.Div([
                            html.P([html.Span("3. ",style={'font-weight':'bold'}),'Seleziona le aree territoriali che vuoi visualizzare'], style={'margin-bottom': '0.5%', 'color': '#00194C'}),
                        ], style={'margin': '0.5%', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'flex': '1'}),  # Ridotto margine
                        # File Upload
                        html.Div([
                            html.Img(src='/assets/position.png', style={'height': '5vh', 'margin-right': '1%', 'horizontal-align': 'middle'}),  # Ridotto altezza immagine e margine destro
                            dcc.Dropdown(
                                id='initial-dropdown',
                                multi=False,
                                placeholder="Seleziona area territoriale",
                                style={'width': '100%', 'background-color': '#FBDD81', 'color': '#002060', 'font-weight': 'bold', 'border': '#FBDD81', 'borderRadius': '30px'}
                            ),
                        ], style={'width': '100%', 'height': '100%', 'borderRadius': '50px', 'padding': '1%', 'background-color': '#FBDD81', 'flex': '1', 'padding': '1%', 'align-items': 'center', 'display': 'flex', 'margin-right': '1%', 'margin-left': '1%'})
                    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
                ], style={'border': '2px #ECF2FE', 'borderRadius': '50px', 'padding': '1%', 'background-color': '#ECF2FE', 'margin-bottom': '1%', 'margin-right':'3%', 'margin-left':'3%'})  # Ridotto margine e raggio del bordo
            ]),
        ]),html.Div(id='output-data-upload'),
        html.Div([
            html.P('Una volta completati tutti i passaggi, avviando lo Smart Scheduler potrai:', style={'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi,'margin':0}),
            html.Ul([
                html.Li([
                    'Visualizzare alcuni ',
                    html.Span('indicatori di qualità', style={'font-weight': 'bold'}),
                    ' delle tue agende;'
                ], style={'listStylePosition': 'inside', 'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi}),
                html.Li([
                    'Accedere ad ulteriori ',
                    html.Span('informazioni', style={'font-weight': 'bold'}),
                    ' sulla loro riconfigurazione'
                ], style={'listStylePosition': 'inside', 'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi}),
            ]),
        ], style={ 'color': '#00194C', 'font-family': font_family_variable, 'font-size': font_size_paragrafi, 'textAlign': 'center','margin':0}),
        html.Div([
            html.Button(
                html.Img(src='/assets/inizia.png', style={'height': '100%', 'width': '100%'}),
                id='button-avanti',
                style={
                    'height': '6vh', 
                    'width': '15vh', 
                    'padding': '0', 
                    'border': 'none', 
                    'background': 'none',
                    'position': 'absolute', 
                    'right': '45%',
                }
            ),
            dcc.Loading(
                id="loading-button",
                type="circle",
                color='blue',
                children=[
                    dcc.Location(id='url-redirect', refresh='callback-nav')
                ]
            )
        ])
    ])








app.layout = layout_home

if __name__ == '__main__':
    app.run_server(debug=True)

