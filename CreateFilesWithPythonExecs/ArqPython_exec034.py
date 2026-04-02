import os 
os.makedirs('/tmp/ExecsPython', exist_ok = True)
os.chmod('/tmp/ExecsPython', 0o744)

valor: int = 0 
dir: str = ''
arq: str = ''

def mult(vlr, tab):
    res = vlr * tab
    return res

def grava(c, rslt):
    global dir, arq
    dir = '/tmp/ExecsPython/'
    arq = 'exec034.txt'

    file:str = ''
    tipo:str = ''
    enc:str = ''
    linha:str = ''

    linha = str(rslt) +'\n'

    if os.path.isdir(dir):
        tipo = 'w' 

        if os.path.exists(dir + '/' + arq):
            if c > 0:
                tipo = 'a'

        caminhoFinal = dir  + arq
        with open (caminhoFinal, tipo) as f:
            f.write(linha)


def main():
    global valor
    valor = int(input('Digite um valor:'))
    for i in range (11):
        resultado = mult(valor, i)
        print(f'{valor} X {i} = {resultado}')
        grava(i, resultado)


if __name__ == '__main__':      

    main()
