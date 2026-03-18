l: float = 0 
distancia: float = 0 
tempo: float = 0 
v: float = 0 

tempo = float(input("Qual o tempo da sua viagem:\n"))
v = float(input("Digite a velocidade que vc vai:\n"))

distancia =  tempo * v 
l = distancia /12

print ("Nessa viagem vc vai gastar", l, "litros")