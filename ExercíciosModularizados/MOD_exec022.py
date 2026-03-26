n1: float = 0 
n2: float = 0 

def entrada():
    global n1, n2

    n1 = int(input("Digite o número 1:\n"))
    n2 = int(input("Digite o número 1:\n"))




def Verificacao():
    global n1,n2

    if n1 > n2:
        print(f"A ordem crescente é:\n {n2},{n1}")
    elif n2 > n1:
        print(f"A ordem crescente é:\n {n1},{n2}")
    else:
        print("Os números são iguais")




def Main_Crescente():
    entrada()
    Verificacao()

if __name__ == "__main__":
    Main_Crescente()
