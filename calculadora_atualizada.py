#valores e unidades pre-definidas
unidades_de_armazenamento = ['bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte']
VALOR_CONV_PRINCIPAL = 1024
VALOR_CONV_BIT = 8

#apresentacoes
print('Olá! Seja bem-vinda à minha humilde calculadora :)')
print('\nEstas são as unidades de armazenamento que você poderá usar aqui:', unidades_de_armazenamento)
print('\nPor favor, insira os valores pedidos abaixo.')

#coleta dos dados e calculo das distancias
unidade_inicial = input("\nUnidade inicial: ")
while unidade_inicial not in unidades_de_armazenamento:
    unidade_inicial = input("Unidade inválida. Insira alguma presente na lista: ")
else:
    posicao_inc = unidades_de_armazenamento.index(unidade_inicial)

unidade_final = input("Unidade final: ")
while unidade_final not in unidades_de_armazenamento:
    unidade_final = input("Unidade inválida. Insira alguma presente na lista: ")
else:
    posicao_fnl = unidades_de_armazenamento.index(unidade_final)

numero_inserido = int(input("Valor a ser convertido: "))
