# Solicita distância e peso
distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

# Define o valor base por kg
if distancia <= 100:
    preco_kg = 1.0
elif distancia <= 300:
    preco_kg = 1.5
else:
    preco_kg = 2.0

# Calcula valor inicial
frete = peso * preco_kg

# Aplica taxa extra para pacotes acima de 10 kg
if peso > 10:
    frete += 10

# Exibe valor do frete
print(f"Valor do frete: R${frete:.2f}")
