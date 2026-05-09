n: int = 0 
st: float = 0

n = int(input("Digite um valor para somar:"))

for ac in range (1,n+1):
    st = st + (1/ac)

print (f"a soma das frações de 1 até o denominador {n} é = {st}")    
