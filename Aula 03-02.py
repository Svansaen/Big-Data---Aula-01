#Programa de medias dos alunos com desvio
nome = input("Informe o seu nome: ")
n1 = float(input("Informe a nota da primeira prova: "))
n2 = float(input("Informe a nota da segunda prova: "))
media = (n1+n2) /2
if media >= 3 < 7:
    print(f"Sr(a) {nome}, sua média é {media}, portanto você está de Recuperação!! :( ")
elif media >= 7:
    print(f"Sr(a) {nome}, sua média é {media}, portanto você está Aprovado!! :) ")    
else:
    print(f"Sr(a) {nome}, sua média é {media}, portanto você está Reprovado! :( ") 

# ou if media >= 7
# ou elif media >= 3           

