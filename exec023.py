n1: int = 0 
n2: int = 0 
n3: int = 0 
n4: int = 0 

n1 = int(input("Digite o primeiro número:\n"))

n2 = int(input("Digite o segundo número :\n"))
while (n2 <= n1):
    print("O segundo número precisa ser diferente e maior que o primeiro")
    n2 = int(input("Por favor digite o segundo número novamente:"))

n3 = int(input("Digite o terceiro número :\n"))
while (n3 <= n2):
    print("O terceiro número precisa ser diferente e maior que o segundo")
    n3 = int(input("Por favor digite o terceiro número novamente:"))

n4 = int(input("Digite o quarto número:\n"))

if (n4 >= n1 and n4 <= n2):
    print(f"Os números em ordem crescentes são: {n1}, {n4}, {n2}, {n3}")

elif (n4 >= n2 and n4 <= n3):
    print(f"Os números em ordem crescentes são: {n1}, {n2}, {n4}, {n3}")

elif (n4 <= n1 ):
    print(f"Os números em ordem crescentes são: {n4}, {n1}, {n2}, {n3}")

else:
    print(f"Os números em ordem crescentes são: {n1}, {n2}, {n3}, {n4}")
    
