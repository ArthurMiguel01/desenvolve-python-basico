# Ler quantidade de respondentes
N = int(input("Digite o número de respondentes: "))

# Inicializar soma das idades
soma = 0

# Ler idades
for i in range(N):
    idade = int(input("Digite a idade: "))
    soma += idade

# Calcular média
media = soma / N

# Imprimir média
print(f"Média das idades: {media:.2f}")
