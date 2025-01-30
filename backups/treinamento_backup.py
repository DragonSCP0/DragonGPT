import shutil
import os
import time

def backup_treinamento():
    origem = "GPT/treinamento.json"
    destino = f"backups/treinamento_backup_{time.strftime('%Y%m%d%H%M%S')}.json"
    
    # Copiar o arquivo de treinamento para backup
    shutil.copy(origem, destino)
    
    print(f"Backup de treinamento salvo em: {destino}")
