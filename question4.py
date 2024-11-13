print("Bem vindos a lista de contatos do Igor Sandro")

# inicialização com array vazio para armazenar os contatos e RU (id blobal)
lista_contatos = []
id_global = 5044993  # RU fictício para exemplo

# função para cadastro de contatos
def cadastrar_contato(id):
    print("\n------- MENU CADASTRAR CONTATO -------")
    print(f'Id do Contato: {id_global}')
    nome = input("Por favor entre com o nome do Contato: ")
    atividade = input("Por favor entre com a Atividade do contato: ")
    telefone = input("Por favor entre com o telefone do contato: ")
    
    contato = {
        "id": id,
        "nome": nome,
        "atividade": atividade,
        "telefone": telefone
    }
    
    #adiciona uma instancia ao array de contatos
    lista_contatos.append(contato.copy())
    print("Contato cadastrado com sucesso!")

# função para consultar os contatos existentes
def consultar_contatos():
    while True:
        print("\n------- MENU CONSULTAR CONTATO -------")
        print("Escolha a opção desejada:")
        print("1 - Consultar Todos os Contatos")
        print("2 - Consultar Contato por id")
        print("3 - Consultar Contato(s) por Atividade")
        print("4 - Retornar")
        
        opcao = input(">> ")
        
        if opcao == "1":
            for contato in lista_contatos:
                print(f"id: {contato['id']}")
                print(f"nome: {contato['nome']}")
                print(f"atividade: {contato['atividade']}")
                print(f"telefone: {contato['telefone']}")
                print("---------")
        
        elif opcao == "2":
            id_consulta = int(input("Digite o id do contato: "))
            encontrado = False
            for contato in lista_contatos:
                if contato["id"] == id_consulta:
                    print(f"id: {contato['id']}")
                    print(f"nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    encontrado = True
                    break
            if not encontrado:
                print("Contato não encontrado.")
        
        elif opcao == "3":
            atividade_consulta = input("Digite a Atividade do(s) Contato(s): ")
            encontrados = [contato for contato in lista_contatos if contato["atividade"] == atividade_consulta]
            if encontrados:
                for contato in encontrados:
                    print(f"id: {contato['id']}")
                    print(f"nome: {contato['nome']}")
                    print(f"atividade: {contato['atividade']}")
                    print(f"telefone: {contato['telefone']}")
                    print("---------")
            else:
                print("Nenhum contato encontrado com esta atividade.")
        
        elif opcao == "4":
            return
        
        else:
            print("Opção inválida")

# função para remoção dos contatos
def remover_contato():
    while True:
        print("\n------- MENU REMOÇÃO CONTATO -------")
        id_remover = int(input("Digite o id do contato a ser removido: "))
        for contato in lista_contatos:
            if contato["id"] == id_remover:
                lista_contatos.remove(contato)
                print("Contato removido com sucesso!")
                return
        print("Id inválido")

# menu principal, de onde são conjurada as demais funções através de um switch (while true)
while True:
    print("\n------- MENU PRINCIPAL -------")
    print("Escolha a opção desejada:")
    print("1 - Cadastrar Contato")
    print("2 - Consultar Contato(s)")
    print("3 - Remover Contato")
    print("4 - Sair")
    
    opcao = input(">> ")
    
    if opcao == "1":
        id_global += 1
        cadastrar_contato(id_global)
    
    elif opcao == "2":
        consultar_contatos()
    
    elif opcao == "3":
        remover_contato()
    
    elif opcao == "4":
        print("Encerrando o programa...")
        break
    
    else:
        print("Opção inválida")
