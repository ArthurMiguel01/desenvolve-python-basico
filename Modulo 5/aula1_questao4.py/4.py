# aula1_questao4.py

import datetime

agora = datetime.datetime.now()

data = f"{agora.day:02}/{agora.month:02}/{agora.year}"
hora = f"{agora.hour:02}:{agora.minute:02}"

print(f"Data: {data}")
print(f"Hora: {hora}")
