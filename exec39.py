qntd: float = 1

# REGRA: pegar a quantidade de grãos que tinha na casa anterior e multiplicar por 2.
print("CÁLCULO DO TABULEIRO ")

for i in range (1,65):
    print(f" Casa: {i}, {qntd} grãos")
    qntd = qntd * 2
   

