tipo: int = 0 
vi: float = 0 
vf: float = 0 
diferença: float = 0 


print ("TIPO DE INVESTIMNETO\n 1 - POUPANÇA\n 2 - RENDA FIXA ")
tipo = int(input("Digite o tipo que vc vai escolher:"))
while tipo != 1 and  tipo != 2:
    print("TIPO INVÁLIDO! DIGITE NOVAMENTE")
    tipo = int(input("Digite o tipo que vc vai escolher:"))

vi = float(input("Agora digite o valor que vc vai investir: R$"))


if tipo == 1:
    vf = vi + (vi * 0.03)
    diferença = vf - vi
    print(f"O seu investimneto no tipo poupança durante 30 dias rendeu R${diferença}\n Gerando um saldo de R${vf}")

else :
    vf = vi + (vi * 0.05)
    diferença = (vf - vi)
    print(f"O seu investimneto no tipo renda fixa durante 30 dias rendeu R${diferença}\n Gerando um saldo de R${vf}")


 