#Programa que mostra o uso de listas 
nome1 = "Alessandro, Maria, Eduarda"
nome2 = ["Alessandro", "Maria", "Eduarda"]
print(nome1)
print(nome2)
print(nome2 [1])
print(len(nome2))
print("Listagem dos elementos do vector")
n = 1
for i in range(len(nome2)):     #len faz a leitura de quantas unidades tem dentro do vector
    print(f"{n}º - {nome2[i]}")
    n += 1
          