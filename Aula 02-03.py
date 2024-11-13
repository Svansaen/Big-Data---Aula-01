# Programa valor da prestação
prestacao = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe o valor da taxa mensal: "))
tempo = float(input("Informe quantas prestações estão em atraso: "))
valorfinal = prestacao+(prestacao*(taxa/100)*tempo)
print (f"O valor da prestação é: R$ {valorfinal:.2f}")