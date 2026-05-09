# resultado fatorial = rf
# resultado soma = rs

n: int = 0 
rf: int = 1
rs: float = 1

n = int(input("Digite um valor:"))



for ac in range(1, n+1):
    rf = rf * ac
    rs = rs + (1/rf)
print (f"O resultado da soma de 1 divido até {n}! é: {rs}")
