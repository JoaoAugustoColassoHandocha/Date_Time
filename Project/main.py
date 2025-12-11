'''



'''

import os, time
from datetime import datetime


while True:

    dia_hora = datetime.now()
    dia_formatada = dia_hora.strftime('%d/%m/%Y')
    hora_formatada = dia_hora.strftime('%H:%M:%S')
    print(f'\n{dia_formatada} | {hora_formatada}')
        
    time.sleep(1)
    
    os.system('cls' if os.name== 'nt' else 'clear')