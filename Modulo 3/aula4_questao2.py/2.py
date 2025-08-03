# Solicita a avaliação
nota = int(input("Digite a avaliação do filme (1 a 5): "))

# Verifica a nota e imprime a classificação
if nota == 5:
    print("Excelente!")
elif nota == 4:
    print("Muito Bom!")
elif nota == 3:
    print("Bom!")
elif nota == 2:
    print("Regular.")
elif nota == 1:
    print("Ruim.")
else:
    print("Nota inválida.")
