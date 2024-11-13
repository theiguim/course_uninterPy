print("Bem-vindo aosistema do Igor Oliveira")

# inicializando valores com input
valor_base = float(input("Informe o valor base do plano: R$ "))
num_idade = int(input("Informe a idade do cliente: "))

# realizando a lógica de comparação considerando os valores de entrada
if 0 <= num_idade < 19:
    valor_mensal = 100.00 *(100/valor_base)
    print(f'O valor mensal do plano é de: R$ {valor_mensal:.2f}')
elif 19 <= num_idade < 19:
    valor_mensal = 100.00*(150/valor_base)
    print(f'O valor mensal do plano é de: R$ {valor_mensal:.2f}')
elif 29<= num_idade <39:
    valor_mensal = 100*(225/valor_base)
    print(f'O valor mensal do plano é de {valor_mensal:.2f}')
elif 39 <= num_idade < 49:
    valor_mensal = 100.00*(240/valor_base)
    print(f'O valor mensal do plano é de: R$ {valor_mensal:.2f}')
elif 49 <= num_idade < 59:
    valor_mensal = 100.00*(350/valor_base)
    print(f'O valor mensal do plano é de: R$ {valor_mensal:.2f}')
elif num_idade >= 59:
    valor_mensal = 100.00*(600/valor_base)
    print(f'O valor mensal do plano é de: R$ {valor_mensal:.2f}')

