import os
import time
from datetime import datetime

PASTA_MONITORADA = "~/storage/shared/Importante" # Pasta com permissão
LIMITE_ARQUIVOS = 5 # Se mudar 5+ arquivos em 10s = alerta
TEMPO_JANELA = 10 # segundos

def contar_arquivos(pasta):
	total = 0
	pasta = os.path.expanduser(pasta) # Expande o ~ pra /data/data/...
	for root, dirs, files in os.walk(pasta):
		total += len(files)
	return total

def log(msg):
	hora = datetime.now().strftime("%H:%M:%S")
	print(f"[{hora}] {msg}")

print("=== RANSOM GUARD v1.1 ===")
print(f"Monitorando: {PASTA_MONITORADA}")
print("Ctrl + C pra sair\n")

pasta_final = os.path.expanduser(PASTA_MONITORADA)
os.makedirs(pasta_final, exist_ok=True)

arquivos_anterior = contar_arquivos(pasta_final)

try:
	while True:
		time.sleep(TEMPO_JANELA)
		arquivos_atual = contar_arquivos(pasta_final)
		diferenca = abs(arquivos_atual - arquivos_anterior)

		if diferenca >= LIMITE_ARQUIVOS:
			log(f"🚨 ALERTA! {diferenca} arquivos mudaram em {TEMPO_JANELA}s")
			log("Possível atividade de ransomware detectada!")
		else:
			log(f"Tudo ok. {arquivos_atual} arquivos na pasta")

		arquivos_anterior = arquivos_atual

except KeyboardInterrupt:
	log("Monitoramento encerrado")

