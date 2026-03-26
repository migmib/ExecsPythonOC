import math 

a : int = 0 
b : int = 0 
c : int = 0 
delta : float = 0 
r1 : float = 0 
r2 : float  = 0 

def entrada():
    global a, b, c

    a = int(input("Digite o seu coeficiente a:\n"))
    b = int(input("Digite o seu coeficiente b:\n"))
    c = int(input("Digite o seu coeficiente c:\n"))




def calculaDelta():
    global a, b, c, delta 
    delta = (b**2 + (-4*a*c))




def VerificaDelta():
        global a, b, delta, r1, r2  
        if (delta > 0):
            r1 = (-b + math.sqrt(delta))/(2*a)
            r2 = (-b - math.sqrt(delta))/(2*a)
            print (f"A sua primeira raiz é {r1}")
            print (f"A sua segunda raiz é {r2}")

        elif (delta ==  0 ):
            r1 = (-b + math.sqrt(delta))/(2*a)
            r2 = (-b - math.sqrt(delta))/(2*a)
            print(f"A sua equação tem apenas uma raiz, e ela é {r1}") 

        else: 
            print ("Sua equação não tem raiz real")




def Main_VerificaRaiz():
    entrada()
    calculaDelta()
    VerificaDelta()

if __name__ == "__main__":
    Main_VerificaRaiz()