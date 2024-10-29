from dash import html

from roots import root_path


font_family_variable = 'Tahoma'
font_size_titoli = '2vh'
font_size_paragrafi = '1.8vh'
font_size_paragrafi_corsivo = '1.75vh'

## Layout comune a tutte le pagine
def common_layout():
    return html.Div([
        # Dark Blue Banner
        html.Div(style={'background-color': '#00194C', 'height': '1cm'}),#mod
        html.Div([
            html.Div([
                html.Img(src='/assets/img_regione_campania.png', style={'height': '50px'})
            ], style={'flex': '1', 'display': 'flex', 'justify-content': 'flex-start', 'align-items': 'center'}),

            html.Div([
                html.Img(src='/assets/img_medici.png', style={'height': '50px'})
            ], style={'flex': '1', 'display': 'flex', 'justify-content': 'center', 'align-items': 'center'}),

            html.Div([
                html.Img(src='/assets/img_sinfonia.png', style={'height': '50px'})
            ], style={'flex': '1', 'display': 'flex', 'justify-content': 'flex-end', 'align-items': 'center'})
        ], style={'display': 'flex', 'padding': '10px', 'background-color': 'white'})
    ])


# Funzione per calcolare l'altezza della tabella in base al numero di righe
def calculate_table_height(data):
    num_rows = len(data)
    
    # Set row height and header height
    row_height = 30  # Estimated row height
    
    
    # Set max table height for 8 rows plus header
    max_table_height = row_height * 4
    
    # Determine the table height
    return min(num_rows * row_height, max_table_height)