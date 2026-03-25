hi: int = 0 
hf: int = 0 
mi: int = 0 
mf: int = 0 
ti: float = 0 
tf: float = 0 
duracao: float = 0 

hi = int(input("Digite a hora inicial:"))
mi = int(input("Digite o minuto inicial:"))
print(f"Você começou a jogar às {hi:02d}:{mi:02d}")

hf = int(input("Digite a hora final:"))
mf = int(input("Digite o minuto final:"))
print(f"Você terminou a jogar às {hf:02d}:{mf:02d}")


ti = hi *60 + mi
tf = hf *60 + mf
    

if (tf < ti) :
    duracao = (1440 - ti) + tf
else: 
    duracao = (tf - ti) 

h = duracao // 60
m = duracao % 60

print (f"Voçê jogou um total de {h} horas e {m} minutos")