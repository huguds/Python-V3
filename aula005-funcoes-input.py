# Programador: Victor Hugo
# Data: 18/01/2022
# Algoritmo: Funcoes input | Revisão

"""
Input: 
É uma maneira de receber 
a entrada de dados do usuário
"""

"""
Comandos:
input("")        <- String
int(input(""))   <- Int
float(input("")) <- Float
"""

num = input("Digite um número inteiro:")
print(type(num)) # String

# Função para converter uma String para Inteiro
num = int(num)
print(type(num)) # Int

# Função para converter uma String para Float
num = float(num)
print(type(num)) # Float

# Função para converter uma String para boolean
num = bool(num)
print(type(num))
print(num)