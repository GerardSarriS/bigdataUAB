#Ejercicio 1: Introducción a Pandas

"""Objetivo: Crea un documento .CSV con 5 columnas:

Columna 1: Nombre y apellidos (en una única cadena de texto) de cada alumno
Columna 2: Nota de cada alumno
Columna 3: Nota "en texto" para cada alumno:
Si la nota final es inferior a 5, añadir el texto "suspendido".
Si la nota se encuentra entre 5 y 6 (ambos incluídos), añadir el texto "aprobado".
Si la nota es superior a 6, e inferior a 7, añadir el texto "bien".
Si la nota es igual o superior a 7, añadir el texto "notable".
Si la nota supera el 9, añadir el texto "Excelente".
Si la nota equivale a un 10, añadir el texto "matrícula de honor".
Columna 4: Diferencia de nota respecto a la mediana del grupo
Columna 4: Diferencia de nota (expreseda en porcentaje) respecto a la mediana del grupo
Condiciones especiales
Antes de hacer los cálculos, debes sumar UN punto a cada alumno, pero la nota máxima nunca puede superar el 10."""

import pandas as pd


notes = [1, 6, 8, 9, 10, 6, 5]
alumnes = ["Jaume", "Carles", "Cristina", "Josep", "Rafael", "Agnès", "Marta"]
cognoms = ["Tort", "Soldevila", "Luna", "Muñoz", "Fernandez", "Hernandez", "Llopart"]

# Afegir un punt més a la nota final i ajuntar noms i cognoms
notes_arreglades = []
noms_complets = []

for nota in notes:
    if nota <10:
        nota = nota + 1
        notes_arreglades.append(nota)
    else:
        nota
        notes_arreglades.append(nota)



for nom,cognom in zip(alumnes,cognoms):
    nom_complet = nom+" "+cognom
    noms_complets.append(nom_complet)

# Crear un DataFrame amb les primeres dades
df = pd.DataFrame({
    'Nom i cognoms': noms_complets,
    'Nota': notes_arreglades
})

# Calcular la nota "amb format text"
def nota_amb_text(nota):
    if nota < 5:
        return 'Suspès'
    elif 5 <= nota <= 6:
        return 'Aprobat'
    elif 6 < nota < 7:
        return 'Bé'
    elif nota >= 7 and nota < 9:
        return 'Notable'
    elif nota >= 9 and nota < 10:
        return 'Excelent'
    elif nota == 10:
        return 'Matrícula d Honor'

# Aplicar la funció para obtenir la nota "amb format Text"
df['Nota amb text'] = df['Nota'].apply(nota_amb_text)

# Calcular la diferència de la nota respecte a la mitjana del grup
mitjana_grup = df['Nota'].median()
df['Diferencia respecte a la mitjana'] = df['Nota'] - mitjana_grup

# Calcular la diferència de la nota en percentatge respecte a la mitjana del grup
df['Diferencia en porcentaje respecto a mediana'] = ((df['Nota'] - mitjana_grup) / mitjana_grup) * 100

# Guardar el DataFrame en un arxiu CSV
df.to_csv('notes_alumnes.csv', index=False)

# Mostrar el DataFrame
print(df)


