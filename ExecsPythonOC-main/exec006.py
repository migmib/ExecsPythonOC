x: int = 0 
y: int = 0 
z: int = 0 

x = int(input("Digite seu valor x :"))
y = int(input("Digite seu valor y :")) 

print ("X =",x)
print ("y =",y)

z = x
x = y
y = z 

print("atualizando...")

print ("X =",x)
print ("y =",y)