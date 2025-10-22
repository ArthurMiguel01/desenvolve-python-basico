import random

lista = [random.randint(-10, 10) for _ in range(20)]

def intervalo_mais_negativos(lst):
    max_neg = 0
    inicio = 0
    fim = 0
    i = 0
    while i < len(lst):
        if lst[i] < 0:
            j = i
            while j < len(lst) and lst[j] < 0:
                j += 1
            if j - i > max_neg:
                max_neg = j - i
                inicio, fim = i, j
            i = j
        else:
            i += 1
    return inicio, fim

inicio, fim = intervalo_mais_negativos(lista)
print("Original:", lista)
if inicio != fim:
    del lista[inicio:fim]
print("Editada:", lista)
