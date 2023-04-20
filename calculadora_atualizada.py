unidades_de_armazenamento = ["bit", "byte", "kilobyte", "megabyte", "gigabyte", "terabyte", "petabyte"]
valor_conversao = 1024

def inserir_dados():
    print("Para realizar os cálculos, insira os dados a seguir.")
    unidade_inicial = input("Unidade a ser convertida: ")
    while unidade_inicial not in unidades_de_armazenamento:
        unidade_inicial = input("Unidade inválida. Insira novamente: ")
    unidade_final = input("Unidade final: ")
    while unidade_final not in unidades_de_armazenamento:
        unidade_final = input("Unidade inválida. Insira novamente: ")
    numero_inserido = int(input("Valor a ser calculado: "))
    return unidade_inicial, unidade_final, numero_inserido

inserir_dados()
