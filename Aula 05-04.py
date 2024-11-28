# Programa conta quantos pares e quantos impares e ordena os numeros em ordem crescente e inversa
qntpar = 0 
qntimpar = 0
num = [17,15,12,13,11,21,22,50,30,45]
for i in range(len(num)):
    if num [i] % 2 == 0:
        qntpar += 1
    else:
        qntimpar += 1  
print(f"A quantidade de números pares é: {qntpar}")
print(f"A quantidade de números ímpares é: {qntimpar}")
print("Ordem de Criação")
print(num)
print("Ordem Reversa")
num.reverse()
print(num)
print("Ordem Crescente")
num.sort()
print(num)

