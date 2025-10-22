# aula2_questao4.py

# Função para ler uma lista do usuário
def ler_lista(n):
    lista = []
    for i in range(n):
        valor = int(input())
        lista.append(valor)
    return lista

# Lista 1
qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os {qtd1} elementos da lista 1:")
lista1 = ler_lista(qtd1)

# Lista 2
qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite os {qtd2} elementos da lista 2:")
lista2 = ler_lista(qtd2)

# Intercalando listas
lista_intercalada = []
menor_tamanho = min(len(lista1), len(lista2))

for i in range(menor_tamanho):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])

# Adicionando elementos remanescentes
lista_intercalada.extend(lista1[menor_tamanho:])
lista_intercalada.extend(lista2[menor_tamanho:])

# Impressão do resultado
print("Lista intercalada:", ' '.join(map(str, lista_intercalada)))
