#valores e unidades pre-definidas
unidades_de_armazenamento = ['bit', 'byte', 'kilobyte', 'megabyte', 'gigabyte', 'terabyte', 'petabyte']
VALOR_CONV_PRINCIPAL = 1024
VALOR_CONV_BIT = 8

#apresentacoes
print('Olá! Seja bem-vinda à minha humilde calculadora :)')
print('\nEstas são as unidades de armazenamento que você poderá usar aqui:', unidades_de_armazenamento)
print('\nPor favor, insira os valores pedidos abaixo.')

def calculadora_dados_e_conversao():
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

    #conversao do valor inserido
    def calculo_conversao():
        if unidade_inicial == 'bit' and unidade_final != 'bit':
            conversao_primaria = numero_inserido / VALOR_CONV_BIT
            distancia = posicao_fnl - unidades_de_armazenamento.index('byte')
            resultado = conversao_primaria / (VALOR_CONV_PRINCIPAL**distancia)
        elif unidade_final == 'bit' and unidade_inicial != 'bit':
            distancia = posicao_inc - unidades_de_armazenamento.index('byte')
            conversao_primaria = numero_inserido * (VALOR_CONV_PRINCIPAL**distancia)
            resultado = conversao_primaria * VALOR_CONV_BIT
        elif unidade_final == 'bit' and unidade_inicial == 'bit':
            resultado = numero_inserido

        else:
            if posicao_inc >= posicao_fnl:
                distancia = posicao_inc - posicao_fnl
                resultado = numero_inserido * (VALOR_CONV_PRINCIPAL**distancia)
            elif posicao_inc < posicao_fnl:
                distancia = posicao_fnl - posicao_inc
                resultado = numero_inserido / (VALOR_CONV_PRINCIPAL**distancia)
        print('\nOkay. Seu resultado é:', resultado, str(unidade_final) + '(s)')
    calculo_conversao()

calculadora_dados_e_conversao()

#looping de repeticao da calculadora
parar_programa = False

while parar_programa == False:
    print("\nQuer calcular mais alguma coisa? Insira 'sim' ou 'nao'.")
    repetir_programa = input()
    if repetir_programa == 'sim':
        print('\njoinha!\nInsira os valores pedidos abaixo:')
        calculadora_dados_e_conversao()
    elif repetir_programa == 'nao':
        print('\nbelezinha <3')
        parar_programa = True
