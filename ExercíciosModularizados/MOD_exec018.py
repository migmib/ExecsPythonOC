
a: int = 0 
b: int = 0 
diferenca: int = 0

def entrada():
    global a, b
    a = int(input("Digite o primeiro valor:\n"))
    b = int(input("Digite o segundo valor:\n"))




def Calculo():
    global a, b, diferenca   
    if (a > b): 
        diferenca = a - b
    elif (b > a):
        diferenca = b - a
    else:
        diferenca = 0




def exibe():
    global diferenca
    print(f"A sua menor diferença é: {diferenca}")




def main_diferença():
     entrada()
     Calculo()
     exibe()
        
if __name__ == "__main__":
    main_diferença()
