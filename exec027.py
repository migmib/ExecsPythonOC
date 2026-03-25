
nvol: float = 0 
ext: float = 0 
vm: float = 0 
t: float = 0 

nvol = float(input("Digite o número de voltas:\n"))
ext = float(input("Digite a extenção do circuito:(em metros)\n"))
t = float(input("Digite o tempo de duração:(em minutos)\n"))

dist = nvol * ext    
dist = dist / 1000
t = t /60
vm = dist/t

print (f"A sua velocidade média foi de {vm} KM/H") 