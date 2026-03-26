i2: int = 1
soma: float = 0 
resul: float = 0 

for i in range(1 ,51):
    resul = (i/i2)
    print(f"{i}/{i2} = {resul:.5f}")
    soma = soma + resul
    i2 = i2 +2
   
print (f"A soma de todos esses números é = {soma:.5f}")