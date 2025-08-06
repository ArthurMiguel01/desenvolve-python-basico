# Fluxograma 4
n = int(input("Quantos números você vai digitar? "))
maior = 0

while n > 0:
    x = float(input("Digite um número: "))
    if x > maior:
        maior = x
    n = n - 1

print("Maior número:", maior)
