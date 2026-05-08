import platform
import subprocess

def identificar_os():
    return platform.system()

def chama_processo(comando_string):
    vetor_comando = comando_string.split(" ")
    try:
        subprocess.run(vetor_comando, check=True)
    except Exception as e:
        print(f"Erro: {e}")

def main():
    so_atual = identificar_os()
    print(f"Sistema: {so_atual}")
    
    opcao = 0
    while opcao != 9:
        print("\n1 – Listar processos")
        print("2 – Matar por PID")
        print("3 – Matar por nome")
        print("9 – Encerrar aplicação")
        
        try:
            opcao = int(input("Escolha: "))
        except ValueError:
            continue

        if opcao == 1:
            if so_atual == "Windows":
                chama_processo("TASKLIST /FO TABLE")
            else:
                chama_processo("ps -ef")

        elif opcao == 2:
            pid = input("PID: ")
            if so_atual == "Windows":
                chama_processo(f"TASKKILL /PID {pid}")
            else:
                chama_processo(f"kill -9 {pid}")

        elif opcao == 3:
            nome = input("Nome: ")
            if so_atual == "Windows":
                chama_processo(f"TASKKILL /IM {nome}")
            else:
                chama_processo(f"pkill -f {nome}")

if __name__ == "__main__":
    main()
