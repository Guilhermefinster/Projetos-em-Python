# Jokenpo
print('='*30)
print('Bem vindo ao jogo jokenpo!')
print('='*30)

# solicitação de nome
usuario1 = input('Digite o seu nome: ')         
usuario2 = input('Digite o seu nome: ')         
                                                
# Jogadas do jogo
print('Jogadas disponíveis:')
print('- Pedra')
print('- Papel')
print('- Tesoura')

# solicitação para realizar a jogada
jogada1 = input(f'\n{usuario1} realize a sua jogada: ')
jogada2 = input(f'\n{usuario2} realize a sua jogada: ')

if jogada1 == 'Pedra' or jogada1 == 'pedra':
    if jogada2 == 'Pedra' or jogada2 == 'pedra':
        print(f'{jogada1} com {jogada2}: empate')

    elif jogada2 == 'Papel' or jogada2 == 'papel':
        print(f'Resultado de {jogada1} com {jogada2}: {usuario2} que jogou {jogada2} vencedor! ')

    elif jogada2 == 'Tesoura' or jogada2 == 'tesoura':
        print(f'Resultado de {jogada1} com {jogada2}: {usuario1} que jogou {jogada1} vencedor! ')

    
elif jogada1 == 'Papel' or jogada1 == 'papel':
    if jogada2 == 'Pedra' or jogada2 == 'pedra':
        print(f'Resultado de {jogada1} com {jogada2}: {usuario1} que jogou {jogada1} vencedor!')

    elif jogada2 == 'Papel' or jogada2 == 'papel':
        print(f'{jogada1} com {jogada2}: empate!')

    elif jogada2 == 'Tesoura' or jogada2 == 'tesoura':
        print(f'{jogada1} com {jogada2}: {usuario2} que jogou {jogada2} vencedor!')

elif jogada1 == 'Tesoura' or jogada1 == 'tesoura':
    if jogada2 == 'Pedra' or jogada2 == 'pedra':
        print(f'{jogada1} com {jogada2}: {usuario2} que jogou {jogada2} vencedor!')

    elif jogada2 == 'Papel' or jogada2 == 'papel': 
        print(f'{jogada1} com {jogada2}: {usuario1} que jogou {jogada1} vencedor!')

    elif jogada2 == 'Tesoura' or jogada2 == 'tesoura':
        print(f'{jogada1} com {jogada2}: empate')

else:
    print('Comando não reconhecido, por gentileza tentar novamente!')