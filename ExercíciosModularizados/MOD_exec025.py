hi: int = 0 
hf: int = 0 
mi: int = 0 
mf: int = 0 
ti: int = 0 
tf: int = 0 
duracao: int = 0 
h: int = 0
m: int = 0

def entrada():
    global hi, mi, hf, mf
    
    hi = int(input("Digite a hora inicial: "))
    mi = int(input("Digite o minuto inicial: "))
    print(f"Você começou a jogar às {hi:02d}:{mi:02d}\n")

    hf = int(input("Digite a hora final: "))
    mf = int(input("Digite o minuto final: "))
    print(f"Você terminou de jogar às {hf:02d}:{mf:02d}\n")




def calcular_tempo():
    global hi, mi, hf, mf, ti, tf, duracao, h, m
    
    ti = (hi * 60) + mi
    tf = (hf * 60) + mf
    
    if tf < ti:
        duracao = (1440 - ti) + tf
    else: 
        duracao = tf - ti 

    h = duracao // 60
    m = duracao % 60




def exibir_resultado():
    global h, m
    print(f"Você jogou um total de {h} horas e {m} minutos.")




def Main_CalculaTempoJogo():
    entrada()
    calcular_tempo()
    exibir_resultado()




if __name__ == "__main__":
    Main_CalculaTempoJogo()