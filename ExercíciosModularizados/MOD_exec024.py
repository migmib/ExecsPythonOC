n1: int = 0 

def entrada():
    global n1 
    n1 = int(input("Digite um número:\n"))




def verifica():
    global n1 
    if (n1 % 2 == 0) and (n1 % 3 == 0):
        print (f"Entre 2 e 3 o número {n1} é divisivel tanto por 2 quento por 3")
        
    elif (n1 % 2 == 0):
        print (f"Entre 2 e 3 o número {n1} é divisivel apenas por 2")

    elif (n1 % 3 == 0):
        print (f"Entre 2 e 3 o número {n1} é divisivel apenas por 3")

    else:
        print (f"{n1} não é divisivel por 2 nem por 3")




def Main_VerificaDiv():
    entrada()
    verifica()

if __name__ == "__main__":
    Main_VerificaDiv()
