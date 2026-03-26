n1: int = 0 
n2: int = 0 

def entrada():
    global n1, n2
    n1 = int(input("Digite o primeiro número:\n"))
    n2 = int(input("Digite o segundo número:\n"))




def verificar_multiplo():
    global n1, n2
    if n1 == 0 or n2 == 0:
        print("Não é possível verificar (divisão por zero)")
    elif n1 > n2:
        if n1 % n2 == 0:
           print("O primeiro número é múltiplo do segundo")
        else:
            print("Não é múltiplo")
    elif n2 % n1 == 0:
         print("O segundo número é múltiplo do primeiro")
    else:
        print("Não é múltiplo")




def Main_multiplo():
    entrada()
    verificar_multiplo()

if __name__ == "__main__":
    Main_multiplo()