frase = input("Digite uma frase: ")
vogais = "aeiouAEIOU"
modificada = "".join("*" if c in vogais else c for c in frase)
print("Frase modificada:", modificada)
