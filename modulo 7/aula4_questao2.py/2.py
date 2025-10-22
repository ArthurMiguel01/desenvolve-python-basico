import re
with open("frase.txt", "r", encoding="utf-8") as f:
    texto = f.read()
palavras = re.findall(r"[A-Za-zÀ-ÿ]+", texto)
with open("palavras.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(palavras))
with open("palavras.txt", "r", encoding="utf-8") as f:
    print(f.read())
