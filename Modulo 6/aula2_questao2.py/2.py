# aula2_questao2.py
import random

# Número de elementos aleatório
num_elementos = random.randint(5, 20)

# Gerar lista com valores entre 1 e 10
elementos = [random.randint(1, 10) for _ in range(num_elementos)]

# Cálculos
soma = sum(elementos)
media = soma / len(elementos)

# Impressão
print("Lista de elementos:", elementos)
print("Soma:", soma)
print("Média:", media)
