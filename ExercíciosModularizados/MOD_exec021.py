n1: float = 0 
n2: float = 0 
n3: float = 0 
n4: float = 0 
med: float = 0 

def VerificaEntrada():
    global n1, n2, n3, n4

    n1 =  float(input("DIGITE A SUA NOTA 1:\n"))
    while n1 > 10:
        n1 =  float(input("NOTA MAIOR QUE 10! Digite uma nota válida:"))
        

    n2 =  float(input("DIGITE A SUA NOTA 2:\n"))
    while n2 > 10:
        n2 =  float(input("NOTA MAIOR QUE 10! Digite uma nota válida:"))


    n3 =  float(input("DIGITE A SUA NOTA 3:\n"))
    while n3 > 10:
        n3 =  float(input("NOTA MAIOR QUE 10! Digite uma nota válida:"))


    n4 =  float(input("DIGITE A SUA NOTA 4:\n"))
    while n4 > 10:
        n4 =  float(input("NOTA MAIOR QUE 10! Digite uma nota válida:"))




def calcMedia():
    global n1, n2, n3, n4, med

    med = (n1+n2+n3+n4)/4

    print()




def VerificaMed():
    global n1, n2, n3, n4, med

    if (med >= 6):
        print(f"Média = {n2} + {n2} + {n3} + {n4} ÷ 4 = {med}")
        print(f"Sua média foi de {med}! Parabéns, você foi aprovado.")

    elif(med >= 3 and med < 6):
        print(f"Média = {n2} + {n2} + {n3} + {n4} ÷ 4 = {med}")
        print(f"Sua média foi de {med}, você vai precisar fazer o exame.")

    else:
        print(f"Média = {n2} + {n2} + {n3} + {n4} ÷ 4 = {med}")
        print(f"Sua média foi de {med}, você foi reprovado!")




def Main_CalculoMedia():
    VerificaEntrada()
    calcMedia()
    VerificaMed()

if __name__ == "__main__":
    Main_CalculoMedia()