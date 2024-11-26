#Programa que coleta 5 numeros e soma os mesmos e depois diz qual nº é maior
soma = 0
maior = 0
for i in range(5):
    #inicio do bloco de repetição
    num = int(input("Informe o valor: "))
    if num > maior:
        maior = num
    soma = soma + num #Acumulador
    #fim do bloco de repetição
print(f"O resultado da soma é: {soma}")    
print(f"O maior valor informado é: {maior} ")