pa: float = 0 
mm: float = 0 
pn: float = 0 

pa = float(input("Digite o preço atual do seu produto:\n"))
mm = float(input("Digite a média mensal de vendas do seu produto\n"))

if (mm < 500) and (pa < 30):
    pn = pa + (pa  * 0.10)
    print (f"O produto tera um novo preço de R${pn}")

elif (mm >= 500 and mm < 1000) and (pa >= 30 and pa < 80):
    pn = pa + (pa * 0.15)
    print (f"O produto tera um novo preço de R${pn}")
       
elif (mm >= 1000) and (pa >= 80):
    pn = pa-(pa * 0.05)
    print (f"O produto tera um novo preço de R${pn}")
else:
         print (f"Seu preço continua sendo R${pa}")
            
