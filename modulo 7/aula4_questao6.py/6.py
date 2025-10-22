top_musicas = []
anos = range(2012,2023)

with open("spotify-2023.csv","r",encoding="latin-1") as f:
    linhas = f.readlines()[1:]

for ano in anos:
    mais_streams = 0
    top = None
    for l in linhas:
        if '"' in l.split(",")[0]:
            continue
        campos = l.strip().split(",")
        try:
            ano_l = int(campos[3])
            streams = int(campos[8])
        except:
            continue
        if ano_l == ano and streams > mais_streams:
            mais_streams = streams
            top = [campos[0], campos[1], ano_l, streams]
    if top:
        top_musicas.append(top)
print(top_musicas)
