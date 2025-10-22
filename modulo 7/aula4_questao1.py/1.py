import os
frase = input("Digite uma frase: ")
caminho = os.path.join(os.getcwd(), "frase.txt")
with open(caminho, "w", encoding="utf-8") as f:
    f.write(frase)
print("Frase salva em", caminho)
