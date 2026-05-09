base: int = 0
expo: int = 0
resul: int = 1

base = int(input("Digite a sua base:\n"))
expo = int(input("Digite o seu expoente:\n"))

for i in range(1, expo+1 ):
    resul = resul * base 

print(f"O resultada do sua potência de base {base} elevado a {expo} é = {resul}")