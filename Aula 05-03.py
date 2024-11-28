#Programa que armazena e exibe os dados de um vetor
nomes = []
idades = []
for i in range(5): 
    nomes.append(input("Informe o nome:  "))   #append = comando que aramazena o dado dentro do vetor, dentro da lista
    idades.append(int(input("Informe a idade: ")))
print("Listagem dos usuários:")    
for i in range(len(nomes)):
    print(f"{nomes[i]} - {idades[i]}")