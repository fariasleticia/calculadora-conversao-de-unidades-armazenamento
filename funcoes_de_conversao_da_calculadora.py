CONSTANTE_DE_CONVERSAO = 1024

#funções de conversão:

def bit_para_byte(numero_inserido):
    bytes_calculado = numero_inserido / 8
    return bytes_calculado

def byte_para_bit(numero_inserido):
    bits_calculado = numero_inserido * 8
    return bits_calculado

def byte_para_kb(numero_inserido):
    kb_calculado = numero_inserido / CONSTANTE_DE_CONVERSAO
    return kb_calculado

def kb_para_byte(numero_inserido):
    byte_calculado = numero_inserido * CONSTANTE_DE_CONVERSAO
    return byte_calculado

def kb_para_mb(numero_inserido):
    mb_calculado = numero_inserido / CONSTANTE_DE_CONVERSAO
    return mb_calculado

def mb_para_kb(numero_inserido):
    kb_calculado = numero_inserido * CONSTANTE_DE_CONVERSAO
    return kb_calculado

#prints das conversões acima:

print('Insira o valor a ser convertido de bit para Byte:')
numero_inserido = float(input())
valor_convertido = bit_para_byte(numero_inserido)
print('Valor convertido:', valor_convertido)

print('Insira o valor a ser convertido de Byte para bit:')
numero_inserido = float(input())
valor_convertido = byte_para_bit(numero_inserido)
print('Valor convertido:', valor_convertido)

print('Insira o valor a ser convertido de Byte para Kilobyte:')
numero_inserido = float(input())
valor_convertido = byte_para_kb(numero_inserido)
print('Valor convertido:', valor_convertido)

print('Insira o valor a ser convertido de Kilobyte para Byte:')
numero_inserido = float(input())
valor_convertido = kb_para_byte(numero_inserido)
print('Valor convertido:', valor_convertido)

print('Insira o valor a ser convertido de Kilobyte para Megabyte:')
numero_inserido = float(input())
valor_convertido = kb_para_mb(numero_inserido)
print('Valor convertido:', valor_convertido)

print('Insira o valor a ser convertido de Megabyte para Kilobyte:')
numero_inserido = float(input())
valor_convertido = mb_para_kb(numero_inserido)
print('Valor convertido:', valor_convertido)
