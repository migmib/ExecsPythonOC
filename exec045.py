soma: float = 0

print("Calculando a série...")

for i in range(1, 16):
    denominador = i * i
    
    if i % 2 == 0:
        soma = soma - (i / denominador)
        print(f" - {i}/{denominador}", end="")
        
    
    else:
        soma = soma + (i / denominador)
        if i == 1:
            print(f"{i}/{denominador}", end="")
        else:
            print(f" + {i}/{denominador}", end="")


print(f"\n\nO resultado final da série é = {soma:.2f}")