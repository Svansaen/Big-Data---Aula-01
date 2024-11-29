#
nome = []
nota1 = []
nota2 = []
for i in range(2):
    nome.append(input("Informe o nome do aluno: "))
    nota1.append(int(input("Informe a primeira nota do aluno: ")))
    nota2.append(int(input("Informe a segunda nota do aluno: ")))
media = (nota1 + nota2)/2
for i in range(len(nome) and (len(media))):
    if media >=7:
        print("O aluno está aprovado")
    else:
        print("aluno não está aprovado")
   