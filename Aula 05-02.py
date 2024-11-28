#Programa usando lista com operadores matematicos
num = [10,20,12,30,100,90,25,5,45,60]
num1 = []
print(f"A soma dos valores é: {sum(num)}")
print(f"O maior valor é: {max(num)}")
print(f"O menor valor é: {min(num)}")
print(f"A média dos valores é: {sum(num)/ len(num)}")
num1 = num.sort() #comando para ordernar a lista em ordem crescente
num1 = num.sort(reverse=True) # comando para ordernar a lista inversamente