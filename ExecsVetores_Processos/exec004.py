import platform
import subprocess


def system_name():
 
    system: str = " "
    system = platform.system()

    return system 

def abre_processo(processo):
    vetor_processo: str =[]
    vetor_processo = processo.split(" ")
    print(vetor_processo)
    resultado = subprocess.run(vetor_processo, capture_output=True, text=True, errors="ignore")
    return resultado.stdout 

def extrai_media(mensagem, nome):
    if nome == "Windows":
        pedaco = mensagem.split("dia =")
        med = pedaco[1]
        print(f"Média do ping do Win é {med}")

    elif nome == "Linux":
        pedaco = mensagem.split("/")
        med = pedaco[4]
        print(f"A média do ping do Linux é {med} ms")



def main():
    comando: str = ""
    name_os: str = " "
    name_os = system_name()
    print(name_os)

    if name_os == "Windows":

        comando = "ping -4 -n 10 www.google.com.br"

    elif name_os == "Linux":

        comando = "ping -4 -c 10 www.google.com.br"

    print("RODANDO PING...")
    
    texto = abre_processo(comando)

    print(texto)

    extrai_media(texto, name_os)





if __name__ == "__main__":
    main()
