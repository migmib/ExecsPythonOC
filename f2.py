import os

pasta = "."  # mesma pasta

for arquivo in os.listdir(pasta):
    if arquivo.startswith("exec") and arquivo.endswith(".py"):
        numero = arquivo[4:-3]

        if numero.isdigit():
            novo_nome = f"exec{int(numero):03d}.py"
            
            os.rename(arquivo, novo_nome)
            print(f"{arquivo} -> {novo_nome}")