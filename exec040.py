a: int = 0 
b: int = 0

a = int(input("Digite o prmeiro valor:"))
b = int(input("Digite o segundo valor:"))

if a > b:
    maior = a 
    menor = b 
else:
    maior = b
    menor = a 

    for i in range (menor, maior+1):
        cont = 0 
        for i2 in range (1, i+1):
            if i % i2 == 0:
                cont = cont +1
        if cont == 2:
            print (f"{i} é primo")


      
           
