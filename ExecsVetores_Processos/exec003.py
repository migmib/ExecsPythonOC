med: float = 0 
quant: int = 0 
soma: float = 0 
vet = [0]*10  
acumulador: str = ""


for i in range (0, 30):

    vet[i] = float(input(f"Pessoa {i } digite a sua nota: "))
    soma = soma + vet[i]

med = soma/30

print(f"\nA média do grupo é = {med}\n")

for i in range (0, 30):
    if vet[i] > med:
        quant = quant +1

    elif vet[i] < med:
         
        #(opção2)
        # acumulador += str(i) + ","
        
         print(f"A pessoa {i} esta abaixo da média ")
    
# (opção 2)
# print(F"As pessoas {acumulador[:-1]} tiveram a nota abaixo da média") 
print (f"\n{quant} Pessoas tiveram nota acima da média")


# pessoa no caso seria a posição do indice
