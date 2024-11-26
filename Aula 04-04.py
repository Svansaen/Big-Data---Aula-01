#Programa para calcular a soma e a media das idades de 10 pessoas
soma = 0
nummaior = 0
nomemaior = 0
for i in range(10):
    nome = (input("Informe seu nome: "))
    idade = int(input("Informe a sua idade: "))
    if idade > nummaior:
        nummaior = idade
        nomemaior = nome
    soma = soma + idade
media = soma /10 # ou media = soma / (i + 1)
print(f"A soma das idades é: {soma}")
print(f"A média das idades é: {media}")
print(f"A pessoa mais velha é: {nomemaior}")
