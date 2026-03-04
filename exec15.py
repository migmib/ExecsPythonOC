import math

c1: float = 0 
c2: float = 0 
h: float = 0 

c1 = float(input("Digite o valor do seu cateto 1 :"))
c2 = float(input("Digite o valor do seu cateto 1 :"))

c1 = (c1*c1)
c2 = (c2*c2)
h = math.sqrt(c1 + c2)

print ("A hipotenusa do seu triângulo é igual a", h)