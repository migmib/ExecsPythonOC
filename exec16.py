# h = horas
# vh = valor da hora
# pd = percentual de desconto
# nd = numero de dependentes 
# saliqui = salario liquido

h: float = 0        
vh: float = 0 
pd: float = 0 
nd: float = 0 
salario: float = 0 
saliqui: float = 0 
soma: float = 0 
desconto: float = 0 

h = float(input("Digite a quantidade de horas:\n"))
vh = float(input("Digite o valor da hora:\n"))
pd = float(input("Digite  o percentual de desconto:\n"))
nd = float(input("Digite a quantidade de depndentes:\n"))

salario = (h*vh)
desconto = (salario) * (pd/100)
saliqui  =  salario - desconto
soma = (nd *100)
saliqui = saliqui + soma 

print ("o seu salario final é de R$", saliqui)