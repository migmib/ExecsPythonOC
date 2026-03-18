import random
n: int = 0 
maior: int = 0  
menor: int = 0

for i in range (1,101):
    n= int(input(f"Digite o número {i}:\n"))
    # n = random.randint(1, 1000)
    # print(f"Número {i} =  {n}")
    while n < 0:
        print("O número digitado é negativo, por favor digitar um valor válido")
        n= int(input("digite um num:"))

    if  (i == 1):
        maior = n 
        menor = n

    elif (n < menor):
            menor = n 

    elif (n > maior):
            maior = n 

print(f"Menor número = {menor} e o maior  número =  {maior}")

