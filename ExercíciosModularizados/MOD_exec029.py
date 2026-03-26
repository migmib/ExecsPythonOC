

def rendimento(tipo, vi):
    if tipo == 1:
        vf = vi + (vi * 0.03)
        diferença = vf - vi
        print(f"O seu investimneto no tipo poupança durante 30 dias rendeu R${diferença}\n Gerando um saldo de R${vf}")

    else :
        vf = vi + (vi * 0.05)
        diferença = (vf - vi)
        print(f"O seu investimneto no tipo renda fixa durante 30 dias rendeu R${diferença}\n Gerando um saldo de R${vf}")


def Main_investimento():

    print ("TIPO DE INVESTIMNETO\n 1 - POUPANÇA\n 2 - RENDA FIXA ")
    tip = int(input("Digite o tipo que vc vai escolher:"))

    while tip != 1 and  tip != 2:
        print("TIPO INVÁLIDO! DIGITE NOVAMENTE")
        tip = int(input("Digite o tipo que vc vai escolher:"))

    valorInicial = float(input("Agora digite o valor que vc vai investir: R$"))

    rendimento(tip, valorInicial)


if __name__ == "__main__":
    Main_investimento()