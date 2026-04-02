import os

os.makedirs('/tmp/exercicios', exist_ok=True)
os.chmod('/tmp/exercicios', 0o744)

nome: str = ''
nota1: float = 0.0
nota2: float = 0.0
nota3: float = 0.0
nota4: float = 0.0
valor_media: float = 0.0
dir: str = ''
arq: str = ''


def med(n1, n2, n3, n4):
    media: float = (n1 + n2 + n3 + n4) / 4
    return media


def escreveArq(nome_dir, nome_arq, linha_cad):
    file: str = ''
    tipo: str = ''
    enc: str = ''
    
    if os.path.isdir(nome_dir):
        if os.path.exists(nome_dir + '/' + nome_arq):
            tipo = 'a' # Se já existe, anexa
        else:
            tipo = 'w' # Se não existe, cria do zero
            
        caminho_completo = nome_dir + '/' + nome_arq
        with open(caminho_completo, tipo) as f:
            f.write(linha_cad)


def cadastro(nm, nt1, nt2, nt3, nt4, vlr_med):
    global dir, arq
    dir = '/tmp/exercicios'
    arq = 'ex21.txt'
    
    linha: str = nm + ';' + str(nt1) + ';' + str(nt2) + ';' + str(nt3) + ';' + str(nt4) + ';' + str(vlr_med) + '\n'
    
    escreveArq(dir, arq, linha)


def entrada():
    global nome, nota1, nota2, nota3, nota4, valor_media
    
    nome = input("Nome do aluno: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    nota4 = float(input("Nota 4: "))
    
    valor_media = med(nota1, nota2, nota3, nota4)
    
    print(f"Média: {valor_media:.2f}")
    
    if valor_media >= 6.0:
        print("Status: APROVADO\n")
    elif valor_media >= 3.0:
        print("Status: EXAME\n")
    else:
        print("Status: RETIDO\n")
        
    cadastro(nome, nota1, nota2, nota3, nota4, valor_media)


def main():

    for contador in range(5):
        print(f"--- Cadastro do Aluno {contador + 1} de 5 ---")
        entrada()

if __name__ == '__main__':      

    main()
