import random

def encrypt(nomes):
    chave = random.randint(1, 10)
    cript = []
    for nome in nomes:
        nova = ""
        for c in nome:
            cod = ord(c) + chave
            if cod > 126:
                cod = 33 + (cod - 127)
            nova += chr(cod)
        cript.append(nova)
    return cript, chave

nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)
print("Chave:", chave_aleatoria)
print("Nomes criptografados:", nomes_cript)
