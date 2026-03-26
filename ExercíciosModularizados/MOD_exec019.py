a: int = 0 
b: int= 0 
 
def entrada():
    global  a, b

    a = int(input("Digite um valor:"))
    b = int(input("Digite outro valor:"))




def verifica():    
    global  a, b

    if a > b:
            print(a, "esse é o seu maior valor")
    else:
            print(b, "esse é o seu maior valor")




def Main_VerificaMaior():
    entrada()
    verifica()

if __name__ == "__main__":
    Main_VerificaMaior()
