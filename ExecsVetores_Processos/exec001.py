med: float = 0 
soma: int = 0 
somaimpar: int = 0 
quant: int = 0
vet = [0]*50 

for i in range (0,50):
    vet[i] = int(input("Digite um valor:\n"))
    if vet[i] >= 10 and vet[i] <= 200:
        soma = soma + vet[i]
        quant = quant + 1

    if vet[i]%2 == 1:
        somaimpar = somaimpar = vet[i]

med = soma /quant

print(f"A média dos seus valores entre 10 e 200 é = {med}\nA soma dos seus números ímpares é = {somaimpar} ")
    