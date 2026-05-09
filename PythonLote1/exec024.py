n1: int = 0 

n1 = int(input("Digite um número:\n"))

if (n1 % 2 == 0) and (n1 % 3 == 0):
    print (f"Entre 2 e 3 o número {n1} é divisivel tanto por 2 quento por 3")
    
elif (n1 % 2 == 0):
     print (f"Entre 2 e 3 o número {n1} é divisivel apenas por 2")

elif (n1 % 3 == 0):
     print (f"Entre 2 e 3 o número {n1} é divisivel apenas por 3")

else:
       print (f"{n1} não é divisivel por 2 nem por 3")


