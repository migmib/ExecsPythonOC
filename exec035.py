# resultado da soma = rs
a: int = 0 
b: int = 0
rs: float = 0 


a = int(input("Digite o prmeiro valor:"))
b = int(input("Digite o segundo valor:"))

if a > b:
    maior = a
    menor = b 
else:
    maior = b
    menor = a

for ac in range (menor, maior+1):
    if ac % 2 != 0:
        rs = rs + ac
print(f"o resultado da soma dos números ímpares entre {menor} e {maior} é: {rs}")




