# Criando números inteiros
# 1. literais
# 2. Entradas de Usuário

import sys
inteiro = 29

numero = int(input("Escreva um número: "))

print(inteiro, numero)

print(f"O número 29 ocupa {inteiro.bit_length()} bits.")
print("\n")
print(f"O número DIGITADO, {numero}, ocupa {numero.bit_length()} bits.")
print("\n")
print(f"E o número DIGITADO, {numero}, ocupa {sys.getsizeof(numero)} bytes.")

binario = "111"

binario_a_base_decimal = int(binario, 2)

print(binario_a_base_decimal)