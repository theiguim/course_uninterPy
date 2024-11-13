print("Bem-vindo a Madeireira do Lenhador Igor Oliveira")

#função com switch interativo para tipo de madeira
def escolha_tipo():
    while True:
        tipo = input("Escolha o tipo de madeira desejado \nPIN - Tora de Pinho\nPER - Tora de Peroba\nMOG - Tora de Mogno\nIPE - Tora de Ipê\nIMB - Tora de Imbuia\n>>> ").upper()
        if tipo == "PIN":
            return 150.40
        elif tipo == "PER":
            return 170.20
        elif tipo == "MOG":
            return 190.90
        elif tipo == "IPE":
            return 210.10
        elif tipo == "IMB":
            return 220.70
        else:
            print("Escolha inváida, entre com modelo novamente.")

#função com switch interativo para quantidade por metro
def qtd_toras():
    while True:
        try:
            qtd = float(input("Entre com a quantidade de toras (m³): "))
            if qtd > 2000:
                print("Não aceitamos pedidos com essa quantidade de toras.\nPor favor, entre com a quantidade novamente.")
            else:
                if qtd < 100:
                    desconto = 0
                elif 100 <= qtd < 500:
                    desconto = 0.04
                elif 500 <= qtd < 1000:
                    desconto = 0.09
                elif 1000 <= qtd <= 2000:
                    desconto = 0.16
                return qtd, desconto
        except ValueError:
            print("Insira um número válido para a quantidade.")

#função com switch interativo para tipo de transporte
def transporte():
    while True:
        tipo_transporte = input("Escolha o tipo de transporte \n1- Rodoviário - R$ 1000.00 \n2- Ferroviário - 2000.00 \n3- Hidroviário - 2500.00 \n>>> ")
        if tipo_transporte == "1":
            return 1000
        elif tipo_transporte == "2":
            return 2000
        elif tipo_transporte == "3":
            return 2500
        else:
            print("Opção inválida! Tente novamente.")


#chamando as funções para obter os respectivos resultados e atribui-lo ao total.
tipo_madeira = escolha_tipo()
 
qtd, desconto = qtd_toras()
    
transporte_valor = transporte()
    
total = (tipo_madeira * qtd * (1 - desconto)) + transporte_valor
    
   
#implementando extrato interativo:
print(f"\nResumo da compra:")
print(f"Tipo de madeira: {tipo_madeira} R$")
print(f"Quantidade de toras: {qtd} m³")
print(f"Desconto: {desconto * 100}%")
print(f"Valor do transporte: R$ {transporte_valor}")
print(f"Total a pagar: R$ {total:.2f}")