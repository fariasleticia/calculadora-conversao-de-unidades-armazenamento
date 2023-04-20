from funcoes_de_conversao_da_calculadora import bit_para_byte, byte_para_bit, byte_para_kb, kb_para_byte, kb_para_mb, mb_para_kb, mb_para_gb, gb_para_mb, gb_para_tb, tb_para_gb, tb_para_pb, pb_para_tb

print ('- Insira 1 para converter de bit para Byte\n- Insira 2 para converter de Byte para bit\n- Insira 3 para converter de Byte para Kilobyte\n- Insira 4 para converter de Kilobyte para Byte\n- Insira 5 para converter de Kilobyte para Megabyte\n- Insira 6 para converter de Megabyte para Kilobyte\n- Insira 7 para converter de Megabyte para Gigabyte\n- Insira 8 para converter de Gigabyte para Megabyte\n- Insira 9 para converter de Gigabyte para Terabyte\n- Insira 10 para converter de Terabyte para Gigabyte\n- Insira 11 para converter de Terabyte para Petabyte\n- Insira 12 para converter de Petabyte para Terabyte')

escolha_conversao = input()

if escolha_conversao == '1':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = bit_para_byte(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '2':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = byte_para_bit(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '3':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = byte_para_kb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '4':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = kb_para_byte(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '5':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = kb_para_mb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '6':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = mb_para_kb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '7':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = mb_para_gb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '8':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = gb_para_mb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '9':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = gb_para_tb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '10':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = tb_para_gb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '11':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = tb_para_pb(numero_inserido)
    print('Valor convertido:', valor_convertido)

elif escolha_conversao == '12':
    numero_inserido = float(input('Insira o valor a ser convertido: '))
    valor_convertido = pb_para_tb(numero_inserido)
    print('Valor convertido:', valor_convertido)
