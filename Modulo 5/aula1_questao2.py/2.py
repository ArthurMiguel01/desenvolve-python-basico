# aula1_questao2.py

import random
import math

n = int(input("Digite a quantidade de números: "))
soma = 0

for _ in range(n):
    valor = random.randint(0, 100)
    soma += valor

raiz = math.sqrt(soma)
print(f"A raiz quadrada da soma ({soma}) é: {raiz:.2f}")
