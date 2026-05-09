n : int = 0 
conta : int = 0 

n = int(input("Digite um número para ver a tabuada dele:"))

for ac in range (0, 11):
    conta = n * ac
    print (f"{n} X {ac} = {conta}")
        
