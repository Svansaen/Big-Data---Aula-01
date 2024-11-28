#Programa que calcula media de notas
for i in range(10):
    nome = input("Informe o nome do estudante: ")
    n1 = float(input("Informe a primeira nota: "))
    n2 = float(input("Informe a segunda nota: "))
    media = (n1 + n2)/2
    if media >= 7:
        print(f"{nome} você está atendido ")
    elif media >= 3:
        print(f"{nome} você está parcialmente atendido")
    else: 
        print(f"{nome} você não está atendido")        
