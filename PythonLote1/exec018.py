a: int = 0 
b: int = 0 
diferença: int = 0

a = int(input("Digite o primeiro valor:\n"))
b = int(input("Digite o primeiro valor:\n"))

if (a>b): 
    diferença = ( a - b )
elif (b > a ):
    diferença = (b - a) 

print(f"A sua menor diferença é:{diferença}")