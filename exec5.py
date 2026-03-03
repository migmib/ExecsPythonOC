import math

a : int = 0 
b : int = 0 
c : int = 0 
delta : float = 0 
r1 : int = 0 
r2 : int  = 0 


a = int(input("Digite o seu coeficiente a:"))
b = int(input("Digite o seu coeficiente b:"))
c = int(input("Digite o seu coeficiente c:"))

delta = (b^b + (-4*a*c))
r1 = (-b + math.sqrt(delta)) / (2*a)
r2 = (-b - math.sqrt(delta))/ (2*a)

print ("A sua raiz 1 é:", r1)
print ("A sua raiz 2 é:", r2)