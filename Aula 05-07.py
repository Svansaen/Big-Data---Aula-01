#
nome = []
idade = []
sexo = []
for i in range(2):
    nome.append(input("Informe o nome: "))
    idade.append(int(input("Informe a idade: ")))
    sexo.append(input("Informe o sexo: "))
print(f"{nome}é a pessoa mais velha com {max(idade)}anos") 
print(f"{nome}é a pessoa mais nova com {min(idade)}anos")   