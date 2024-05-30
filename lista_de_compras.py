# Objetivo: Desenvolver um programa em Python que simule uma lista de compras, 
# permitindo ao usuário realizar operações como inserir, alterar, excluir e visualizar itens da lista.
lista_compras = []

print('Bem vindo à sua lista de compras ')

while True:

    print('\nQual opção voce deseja realizar? ')
    print('1 - INSERIR')
    print('2 - ALTERAR')
    print('3 - EXCLUIR')
    print('4 - VISUALIZAR')
    print('Sair')
    operacao = input('\nDigite uma opção(números): ')

# Inserir

    if operacao == '1':
        lista_compras.append(input('Novo item: '))
        

# alterar
    elif operacao == '2':
        print(lista_compras)
        indice_alterar = int(input('Digite o índice que você deseja alterar! '))
        lista_compras[indice_alterar] = input('Digite o novo item: ')
        print(lista_compras)

# excluir
    elif operacao == '3':
        print(lista_compras)
        indice_excluir = (input('Digite o índice que você deseja excluir! '))
        lista_compras.remove(indice_excluir)
        # del(lista_compras[indice_excluir])
        print(lista_compras)

# # visualizar
    elif operacao == '4':
        for lista_compras in lista_compras:
            print(lista_compras)
        
# # Sair
    elif operacao == 'sair':
        quit()