# Programa de calcular idade
import datetime # Importa a biblioteca datetime
data_atual = datetime.date.today() # Armazena na variavel a data completa
ano_atual = data_atual.year # Armazena na variavel o ano atual
nascimento = int(input("Informe o ano em que você nasceu: "))
idade = (ano_atual- nascimento )
print(f"A sua idade é: {idade} anos.")
