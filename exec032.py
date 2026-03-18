n: int = 0 
rf: int = 0

n = int(input("Digite um valor para calcular o Fatorial:"))
rf = 1

for ac in range(1, n+1):
    rf = rf * ac
print (f"Seu resultado de {n}! = {rf}")
