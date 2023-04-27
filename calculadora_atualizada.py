#valores e unidades pre-definidas
unidades_de_armazenamento = ['bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte']
VALOR_CONV_PRINCIPAL = 1024
VALOR_CONV_BIT = 8

#apresentacoes
print('Olá! Seja bem-vinda à minha humilde calculadora :)')
print('\nEstas são as unidades de armazenamento que você poderá usar aqui:', unidades_de_armazenamento)
print('\nPor favor, insira os valores pedidos abaixo.')

#coleta dos dados
unidade_inicial = input("\nUnidade inicial: ")
unidade_final = input("Unidade final: ")
numero_inserido = int(input("Valor a ser convertido: "))
