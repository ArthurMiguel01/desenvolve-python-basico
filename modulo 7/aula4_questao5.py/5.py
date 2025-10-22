livros = [
    ["O Caçador de Pipas","Khaled Hosseini",2003,368],
    ["Torto Arado","Itamar Vieira Junior",2019,264],
    ["1984","George Orwell",1949,328],
    ["Dom Casmurro","Machado de Assis",1899,256],
    ["Harry Potter e a Pedra Filosofal","J.K. Rowling",1997,223],
    ["O Senhor dos Anéis","J.R.R. Tolkien",1954,1216],
    ["A Menina que Roubava Livros","Markus Zusak",2005,480],
    ["Cem Anos de Solidão","Gabriel García Márquez",1967,417],
    ["O Pequeno Príncipe","Antoine de Saint-Exupéry",1943,96],
    ["A Culpa é das Estrelas","John Green",2012,313]
]

with open("meus_livros.csv","w", encoding="utf-8") as f:
    f.write("Título,Autor,Ano de publicação,Número de páginas\n")
    for livro in livros:
        f.write(",".join(str(c) for c in livro)+"\n")
