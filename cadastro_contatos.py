def cadastrar_contatos():
    contato = {}
    contato['nome'] = input('Informe o nome: ')
    contato['telefone'] = input('Informe o telefone: ')
    contato['email'] = input('Informe o e-mail: ')
    return contato

def excluir_contatos():
    contato_para_excluir = input('Informe o nome do contato que você deseja excluir: ')
    for item in lista_contatos:
        if item['nome'] == contato_para_excluir:
            lista_contatos.remove(item)

def editar_contatos():
    contato_para_alterar = input('Informe o nome do contato que você deseja alterar: ')
    for contato_novo in lista_contatos:
        if contato_novo['nome'] == contato_para_alterar:
            contato_novo['nome'] = input('Informe o novo nome: ')
            contato_novo['telefone'] = input('Informe o novo telefone: ')
            contato_novo['email'] = input('Informe o novo e-mail: ')

def listar_contatos(lista_contatos):
    for contato in lista_contatos:
        print('='*30)
        print('Nome: ', contato['nome'])
        print('Telefone: ', contato['telefone'])
        print('E-mail: ', contato['email'])
        print('='*30)
       
continuar = True
lista_contatos = []

while continuar:
    print('Bem vindo ao sistema de contatos!\n')
    opcao = input('''
    ----------MENU----------
    Informe a opção que deseja efetuar:
    1 - Cadastrar  
    2 - Excluir  
    3 - Editar
    4 - Listar  
    5 - Sair     
    ''')

    if opcao == '1':
        contato = cadastrar_contatos()
        lista_contatos.append(contato)

    elif opcao == '2':
        excluir_contatos()
        listar_contatos(lista_contatos)

    elif opcao == '3':
        editar_contatos()
        listar_contatos(lista_contatos)

    elif opcao == '4':
        listar_contatos(lista_contatos)
    
    elif opcao == '5':
        continuar = False
        print('Sistema finalizado!')

    else:
        print('Opção inválida!')