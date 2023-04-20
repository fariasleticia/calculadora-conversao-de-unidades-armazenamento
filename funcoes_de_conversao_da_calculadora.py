#funções de conversão:

def bit_para_byte(numero_inserido):
    bytes_calculado = numero_inserido / 8
    return bytes_calculado

def byte_para_bit(numero_inserido):
    bits_calculado = numero_inserido * 8
    return bits_calculado

#prints das conversões acima:

print('Insira o valor a ser convertido de bit para Byte:')
numero_inserido = float(input())
valor_convertido = bit_para_byte(numero_inserido)
print('Valor convertido:', valor_convertido)

print('Insira o valor a ser convertido de Byte para bit:')
numero_inserido = float(input())
valor_convertido = byte_para_bit(numero_inserido)
print('Valor convertido:', valor_convertido)
