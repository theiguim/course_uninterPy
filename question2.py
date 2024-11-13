
#menu de interação inicial
print("-" * 10 + " Bem-vindo à Pizzaria do Igor Oliveira " + "-" * 11)
print("-" * 27 + " Menu " + "-" * 27)
print("-" * 60)
print("  Tamanho   | Pizza Salgada (PS) |  Pizza Doce (PD) ")
print("-" * 60)
print("     P      |     R$ 30.00       |    R$ 34.00    ")
print("     M      |     R$ 45.00       |    R$ 48.00    ")
print("     G      |     R$ 60.00       |    R$ 66.00    ")
print("-" * 60)

#var total acumulativa
total = 0

#condicoes comerciais | loop para satisfazê-las
while True:
    flavor = input("Entre com o sabor desejado (PS/PD): ").upper()
    if flavor != "PS" and flavor != "PD":
        print("Sabor inválido. Tente novamente")
        continue
    size = input("Entre com o tamanho desejado (P/M/G): ").upper()
    if size == "P" or size == "M" or size =="G":
        
        if size == "P":
            if flavor == "PS":
                total += 30
            else: 
                total += 34
        elif size == "M":
            if flavor == "PS":
                total += 45
            else: 
                total += 48
        elif size == "G":
            if flavor == "PS":
                total += 60
            else:
                total += 66
    else:  #returna ao inicio do while para refazer o pedido ou sai do menu apresentando o total.
        print("Tamanho inválido. Tente novamente")
        continue
   
    replay = input("Deseja algo mais? (S/N) ").upper()    
    if(replay == "S"):
        continue
    else: 
        print(f"O total é {total:.2f}")
        break
    

      
        
        
   
