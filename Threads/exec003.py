import threading
import random
import time

distancia_maxima = 20

def sapo_correndo(id):
    percorrido = 0
    while percorrido < distancia_maxima:
        salto = random.randint(1, 5)
        percorrido += salto
        print(f"Sapo {id} saltou {salto}cm. Total: {percorrido}cm")
        if percorrido >= distancia_maxima:
            print(f"--- Sapo {id} CHEGOU! ---")
            break
        time.sleep(0.1)

threads = []
for i in range(1, 6):
    t = threading.Thread(target=sapo_correndo, args=(i,))
    threads.append(t)
    t.start()