import random

with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = [linha.strip() for linha in f if linha.strip()]

with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
    estagios = f.read().split("\n\n")

palavra = random.choice(palavras)
progresso = ["_"] * len(palavra)
tentativas = 0
letras_erradas = []

def imprime_enforcado(erro):
    print(estagios[erro])

while tentativas < 6 and "_" in progresso:
    print("Palavra:", " ".join(progresso))
    letra = input("Digite uma letra: ").strip()
    if letra in palavra:
        for i, c in enumerate(palavra):
            if c == letra:
                progresso[i] = letra
    else:
        if letra not in letras_erradas:
            letras_erradas.append(letra)
            tentativas += 1
            imprime_enforcado(tentativas)
if "_" not in progresso:
    print("Parabéns! Você venceu:", palavra)
else:
    print("Fim de jogo. A palavra era:", palavra)
