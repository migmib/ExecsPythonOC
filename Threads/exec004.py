import threading
import subprocess
import platform
import re

def realizar_ping(nome, servidor):
    so = platform.system().lower()
    comando = ["ping", "-n", "10", servidor] if so == "windows" else ["ping", "-c", "10", servidor]
    
    processo = subprocess.Popen(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    tempos = []
    for linha in processo.stdout:
        match = re.search(r"time[:=]\s*([\d.]+)", linha)
        if match:
            tempo = float(match.group(1))
            tempos.append(tempo)
            print(f"{nome}: {tempo}ms")
            
    if tempos:
        media = sum(tempos) / len(tempos)
        print(f"Final {nome} - Média: {media:.2(f)}ms")

servidores = [("UOL", "www.uol.com.br"), ("Terra", "www.terra.com.br"), ("Google", "www.google.com.br")]

for nome, url in servidores:
    threading.Thread(target=realizar_ping, args=(nome, url)).start()