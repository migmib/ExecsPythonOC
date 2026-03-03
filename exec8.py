deposito: int = 0 
rendi : float = 0 
total: float = 0 

deposito = float(input("Quanto vc vai depositar?\nR$"))
rendi = deposito * 0.013
total = deposito + rendi

print ("o seu saldo atual com a aplicação é de R$", total)