# Ler número de experimentos
N = int(input())

# Inicializar contadores
total = 0
coelhos = 0
ratos = 0
sapos = 0

# Ler experimentos
for i in range(N):
    entrada = input().split()
    quantia = int(entrada[0])
    tipo = entrada[1]

    total += quantia

    if tipo == 'C':
        coelhos += quantia
    elif tipo == 'R':
        ratos += quantia
    elif tipo == 'S':
        sapos += quantia

# Calcular percentuais
percent_coelhos = (coelhos / total) * 100
percent_ratos = (ratos / total) * 100
percent_sapos = (sapos / total) * 100

# Imprimir resultados
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {coelhos}")
print(f"Total de ratos: {ratos}")
print(f"Total de sapos: {sapos}")
print(f"Percentual de coelhos: {percent_coelhos:.2f} %")
print(f"Percentual de ratos: {percent_ratos:.2f} %")
print(f"Percentual de sapos: {percent_sapos:.2f} %")
