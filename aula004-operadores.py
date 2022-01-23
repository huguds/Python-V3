# Programador: Victor Hugo
# Data: 18/01/2022
# Algoritmo: Operadores Matemáticos | Revisão


"""
Operadores Matemáticos:
 +  <- Soma
 -  <- Subtração
 *  <- Multiplicação
 /  <- Divisão real
 // <- Divisão inteira
 %  <- Resto
 ** <- Potência
"""
# Variaveis e Valores
n1,n2 = 10,5

# Operações Matemáticas
print(f'A soma de {n1} + {n2} = {n1+n2}')
print(f'A subtração de {n1} - {n2} = {n1-n2}')
print(f'A multiplicação de {n1} x {n2} = {n1*n2}')
print(f'A divisão real de {n1} / {n2} = {n1/n2}')
print(f'A divisão inteira de {n1} / {n2} = {n1//n2}')
print(f'O resto da divisão de {n1} / {n2} = {n1%n2}')
print(f'A potencia de {n1} / {n2} = {n1**n2} \n')

# Expressão
x = 10 + 5 * 3 / 15 # Espera-se resultado = 3
print(x)

x = (10 + 5) * 3 / 15 # Expressão correta
print(x)