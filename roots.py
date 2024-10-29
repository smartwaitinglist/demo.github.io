import os
from datetime import datetime

# Ottieni il percorso assoluto della directory del file corrente
current_dir = os.path.dirname(os.path.abspath(__file__))

# Definisci il percorso base per evitare duplicazioni
base_path = os.path.join(current_dir)

# Costruisci i percorsi relativi
root_path = os.path.join(base_path, 'Df_demo')
root_path_download = os.path.join(base_path, 'assets', 'Smart Scheduler_Slot Giornalieri Consigliati_AAAAMMGG.xlsx')
root_scheduler_input = os.path.join(base_path, 'INPUT')
root_scheduler_output = os.path.join(base_path, 'OUTPUT')

# Ottieni la data odierna
oggi = datetime.today()

# Estrai giorno, mese e anno
giorno_odierno = oggi.day
mese_odierno = oggi.month
anno_odierno = oggi.year



