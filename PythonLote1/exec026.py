n1: int = 0 
n2: int = 0 

n1 = int(input("Digite o primeiro número:\n"))
n2 = int(input("Digite o segundo número :\n"))

if (n1 == 0 or n2 == 0):
    print("Não é possível verificar (divisão por zero)")


elif (n1 > n2):
    if (n1 % n2 == 0 ):
       print ("O primeiro número é multilplo do segundo")
    else:
        print("Não é multiplo")

elif (n2 % n1 == 0 ):
     print ("O segundo número é multilplo do primeiro")
else:
        print("Não é multiplo")
