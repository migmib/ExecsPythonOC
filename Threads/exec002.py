import threading
import time
import random

def somar_linha(id, valores):
    soma = 0
    for v in valores:
        soma += v
        time.sleep(0.2)
    print(f"Linha {id}: Soma = {soma}")

for i in range(3):
    vetor_valores = [random.randint(1, 100) for _ in range(5)]
    t = threading.Thread(target=somar_linha, args=(i, vetor_valores))
    t.start()