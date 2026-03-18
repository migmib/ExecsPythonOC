alimentos: float = 0 
conversao: float = 0 
dias: int = 0 

alimentos = float(input("Digite uma quantidade de alimento em kg:"))

conversao = (alimentos*1000)
dias = (conversao/50)

print("Você tem", conversao, "g de alimento")
print()
print ("Sabendo que uma pessoa come 50g por dia...\nSua comida vai durar", dias, "dias")


