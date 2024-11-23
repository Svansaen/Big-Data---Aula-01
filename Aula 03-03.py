# Programa de cadastro do cliente com desvio e conectivo
nome = input("Informe o seu nome: ")
genero = input("Informe o seu genero (M ou F): ")
idade = int(input("Informe a sua idade: "))
if (idade >= 18) and (genero == "M" or genero == "m"):
    certificado = int(input("Informe o certificado de reservista: "))    
    print("Você é maior de idade")
elif idade >= 18:
    print("Você é maior de idade")    
else:
    print("Você é menor de idade")    