#Programa doação de sangue
idade = int(input("Informe a sua idade: "))
peso = float(input("Informe o seu peso em kg: "))
sono = float(input("Informe quantas horas você dormiu na última noite: "))
if (idade >= 16 <= 69) and (peso >= 50) and (sono >= 6) :
    print("Você está apto a doar sangue.")
else:
    print("Você não está apto a doar sangue.")        