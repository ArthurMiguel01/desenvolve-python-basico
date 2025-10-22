# aula2_questao1.py
import random

# Gerar lista aleatória
valores = [random.randint(-100, 100) for _ in range(20)]

# Lista ordenada sem modificar a original
lista_ordenada = sorted(valores)

# Índices do maior e menor valor
indice_maior = valores.index(max(valores))
indice_menor = valores.index(min(valores))

# Impressão
print("Lista ordenada:", lista_ordenada)
print("Lista original:", valores)
print("Índice do maior valor:", indice_maior)
print("Índice do menor valor:", indice_menor)
