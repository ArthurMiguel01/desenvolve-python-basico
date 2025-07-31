# Lê o comprimento do terreno em metros (valor inteiro)
comprimento = int(input("Digite o comprimento do terreno (em metros): "))

# Lê a largura do terreno em metros (valor inteiro)
largura = int(input("Digite a largura do terreno (em metros): "))

# Lê o preço do metro quadrado na região (valor com ponto flutuante)
preco_m2 = float(input("Digite o preço do metro quadrado (em R$): "))

# Calcula a área total do terreno
area_m2 = comprimento * largura

# Calcula o preço total do terreno com base na área e no preço por metro quadrado
preco_total = preco_m2 * area_m2

# Imprime a área e o valor do terreno formatado com duas casas decimais
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")
