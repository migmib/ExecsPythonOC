
def calcular_velocidade(nvol, ext, t): 
    dist = nvol * ext    
    dist = dist / 1000   
    t_horas = t / 60     
    vm = dist / t_horas
    
    print(f"A sua velocidade média foi de {vm:.2f} KM/H")


def Main_VM():
   
    numeroVoltas = float(input("Digite o número de voltas:\n"))
    extensao = float(input("Digite a extensão do circuito (em metros):\n"))
    tempo = float(input("Digite o tempo de duração (em minutos):\n"))
    calcular_velocidade(numeroVoltas, extensao, tempo)


if __name__ == "__main__":
    Main_VM()