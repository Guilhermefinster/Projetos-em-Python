# Calculadora

n1 = int(input('Informe o número um: '))
n2 = int(input('Informe o número dois: '))
print('''
      OPÇÕES:
      1 - soma
      2 - subtração
      3 - multiplicação
      4- divisão           
      ''')
operacao = input('Digite a operação a ser realizada: ')

if operacao == '1' or operacao == 'soma' or operacao == 'Soma':
    soma = n1 + n2
    print(f'A soma entre {n1} e {n2} é: {soma}')

elif operacao == '2' or operacao == 'subtração' or operacao == 'Subtração':
    subtracao = n1 - n2
    print(f'A subtração entre {n1} e {n2} é: {subtracao}')

elif operacao == '3' or operacao == 'multiplicação' or operacao == 'Multiplicação':
    multiplicacao = n1 * n2
    print(f'A multiplicação entre {n1} e {n2} é: {multiplicacao}')

elif operacao == '4' or operacao == 'divisão' or operacao == 'Divisão':
    divisao = n1 / n2
    print(f'A divisão entre {n1} e {n2} é: {divisao}')

else: 
    print('Operação não reconhecida!')













