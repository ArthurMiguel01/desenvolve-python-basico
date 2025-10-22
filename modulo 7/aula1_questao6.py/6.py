frase = input("Digite uma frase: ")
palavra_obj = input("Digite a palavra objetivo: ")
palavras = frase.split()
anagramas = [p for p in palavras if sorted(p.lower()) == sorted(palavra_obj.lower())]
print("Anagramas:", anagramas)
