# aula2_questao3.py
import random

# Gerar listas
lista1 = [random.randint(0, 50) for _ in range(20)]
lista2 = [random.randint(0, 50) for _ in range(20)]

# Interseção sem duplicatas
intersecao = sorted(list(set(lista1) & set(lista2)))

# Impressão das listas
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Interseção ordenada:", intersecao)

# Contagem de cada elemento na interseção
for elem in intersecao:
    print(f"{elem}: (lista1={lista1.count(elem)}, lista2={lista2.count(elem)})")
