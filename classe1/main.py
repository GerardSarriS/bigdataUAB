noms = ["lluc", "jan", "jana", "carles"]
notes = [1, 7, 5]

if "jan" in noms:
    index_jan = noms.index("jan")
    nota_jan = notes[index_jan]
    print("Jan ha estat a l'examen i la seva nota és:", nota_jan)
else:
    print("Jan no ha estat a l'examen.")
