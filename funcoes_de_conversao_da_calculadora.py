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

def mb_para_gb(numero_inserido):
    gb_calculado = numero_inserido / CONSTANTE_DE_CONVERSAO
    return gb_calculado

def gb_para_mb(numero_inserido):
    mb_calculado = numero_inserido * CONSTANTE_DE_CONVERSAO
    return mb_calculado

def gb_para_tb(numero_inserido):
    tb_calculado = numero_inserido / CONSTANTE_DE_CONVERSAO
    return tb_calculado

def tb_para_gb(numero_inserido):
    gb_calculado = numero_inserido * CONSTANTE_DE_CONVERSAO
    return gb_calculado

def tb_para_pb(numero_inserido):
    pb_calculado = numero_inserido / CONSTANTE_DE_CONVERSAO
    return pb_calculado

def pb_para_tb(numero_inserido):
    tb_calculado = numero_inserido * CONSTANTE_DE_CONVERSAO
    return tb_calculado
