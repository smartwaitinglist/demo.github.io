from dash import html, dcc
from commonlayout import common_layout, font_family_variable, font_size_paragrafi, font_size_paragrafi_corsivo, font_size_titoli, calculate_table_height, root_path
import dash_bootstrap_components as dbc
def consigli_di_dimensionamento():
    return html.Div([
        common_layout(),

        html.Div([
            html.H1('Smart Scheduler - Dettagli Area territoriale', style={
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
        html.Div("Dettagli Area territoriale ", style={
            'margin': '20px', 'display': 'inline-block', 'margin-left': '80px', 'color': '#00194C',
            'font-family': font_family_variable, 'font-size': '20px', 'font-weight': 'bold'
        }),
        html.Div([
            html.Div("In questa sezione, sulla base della prioritizzazione ottimale degli slot in agenda è possibile visualizzare:", style={
                'margin-left': '80px',
                'color': '#00194C',
                'font-family': font_family_variable,
                'font-size': font_size_paragrafi
            }),
            html.Ul([
                html.Li([
                    "i ",
                    html.Span("tempi medi stimati di attesa", style={'font-weight': 'bold'}),
                    ", allo stato attuale e applicando la riconfigurazione proposta dallo Smart Scheduler, per tipologia di ambulatorio/attrezzature e classe di priorità;"
                ]),
                html.Li([
                    "le ",
                    html.Span("ore di ambulatorio da aggiungere", style={'font-weight': 'bold'}),
                    ", per ogni tipo di ambulatorio/attrezzatura, ",
                    html.Span("con l’obiettivo di recuperare le code, riducendo i ritardi.", style={'font-weight': 'bold'})
                ])
            ], style={
                'margin': '20px',
                'display': 'inline-block',
                'margin-left': '80px',
                'color': '#00194C',
                'font-family': font_family_variable,
                'font-size': '16px'
            })
        ]),
        html.Br(),
        # Menu a tendina
        html.Div("Stai visualizzando l'area territoriale: ", style={
            'margin-left': '80px', 'display': 'inline-block', 'vertical-align': 'middle',
            'font-family': font_family_variable, 'color': '#00194C', 'font-size': '16px'
        }),
        dbc.Input(
            id = 'dropdown-menu',
            style={
            'width': '200px', 'display': 'inline-block', 'vertical-align': 'middle',
            'font-family': font_family_variable,'font-size': '16px'
        }
        ),
        html.Div([
    html.Div([
        html.Div([
            html.Img(src='/assets/hourglass.png', style={'height': '20px', 'margin-right': '10px'}),  # Replace with your icon path
            html.B("Tempi medi stimati di attesa (giorni)", style={
                'font-weight': 'bold', 'font-style': 'italic'
            }),
        ], style={
            'display': 'flex', 'align-items': 'center', 'justify-content': 'center',
            'padding': '8px', 'background-color': '#F0F6FF', 'color': '#00194C', 'font-family': font_family_variable,
            'font-size': '16px'
        }),
        html.Div(id='table-container-1'),
        html.Div("* Gli effetti della riconfigurazione sui tempi medi stimati d’attesa saranno visibili a partire dal periodo temporale indicato; i tempi medi stimati di attesa post-riconfigurazione saranno osservabili una volta a regime.", style={
            'margin-top': '10px', 'font-family': font_family_variable, 'color': '#00194C', 'font-size': font_size_paragrafi_corsivo, 'font-style': 'italic' 
        })
    ], style={
        'width': '48%', 'text-align': 'left', 'margin-top': '40px',
    }),
    html.Div([
        html.Div([
            html.Img(src='/assets/CalendarClock.png', style={'height': '20px', 'margin-right': '10px'}),  # Replace with your icon path
            html.B("Ore ambulatorio da aggiungere (h)", style={
                'font-weight': 'bold', 'font-style': 'italic'
            }),
        ], style={
            'display': 'flex', 'align-items': 'center', 'justify-content': 'center',
            'padding': '8px', 'background-color': '#F0F6FF', 'color': '#00194C', 'font-family': font_family_variable,
            'font-size': '16px'
        }),
        html.Div(id='table-container-2')
            ], style={
                'width': '48%', 'text-align': 'center', 'margin-top': '40px',
            })
        ], style={
            'display': 'flex', 'flex-direction': 'row', 'justify-content': 'space-around',
            'width': '90%', 'margin': 'auto'
        }),
        html.Div([
            dcc.Link(
                html.Img(src='/assets/backward.png', style={
                    'height': '50px', 'margin-top': '0px', 'margin-left': '30px'
                }),
                href='/agende',
                style={'position': 'static', 'left': '5%', 'font-size': '20px'}
            )
        ])

    ])
