maior: int = 0 
menor: int = 0 
vet = [0] * 10
med = float = 0


for i in range(0, 10):
    vet[i] = int(input(f"Digite um valor no índice {i} do vetor: "))

    if i == 0:
        menor = vet[i]
        maior = vet[i]
    else:

        if vet[i] > maior:
            maior = vet[i]
       

        if vet[i] < menor:
            menor = vet[i]
    
    

med = (maior + menor) / 2

print(f"Maior = {maior} e Menor = {menor}")
print(f"A média do maior com o menor é = {med}")



