nasc : int = 0 
anoAtual : int = 0 
futuro : int = 0 
idd : int = 0 

nasc = int(input("Digite seu ano de nascimento:\n"))
anoAtual = int(input("Digite o ano atual:\n"))

idd = (anoAtual - nasc)
futuro = (idd + 17)

print("Com base nos dados vc têm", idd, "anos de idade")
print ("Daqui 15 anos vc terá", futuro, "anos")