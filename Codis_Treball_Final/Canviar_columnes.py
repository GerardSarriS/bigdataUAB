"""import pandas as pd
from tqdm import tqdm

# Lee el archivo CSV
df = pd.read_csv('very_cleaned_data.csv', header=None)  # Leemos el archivo sin encabezados

# Define el diccionario de búsqueda y reemplazo
year_mapping = {
    f'{year}/{str(year+1)[-2:]}': str(year) for year in range(1990, 2024)
}

# Crea una barra de progreso
progress_bar = tqdm(total=df.size, desc="Procesando documento")

# Itera sobre cada celda en el DataFrame
for i, cell in df.stack().items():
    # Reemplaza los bloques de texto de la columna que coincidan con el diccionario de búsqueda y reemplazo
    for search_term, replace_term in year_mapping.items():
        if search_term in cell:
            df.at[i] = cell.replace(search_term, replace_term)

    # Actualiza la barra de progreso
    progress_bar.update()

# Guarda el archivo CSV actualizado
df.to_csv('tu_archivo_actualizado.csv', index=False, header=False)  # Guardamos sin encabezados

print("Se ha completado el cambio de los bloques de texto del documento.")
"""
import pandas as pd

# Lee el archivo CSV
df = pd.read_csv('very_cleaned_data.csv', header=None)  # Leemos el archivo sin encabezados

# Define el rango de temporadas de búsqueda y reemplazo
temporadas = [f'{str(year)[-2:]}/{str(year+1)[-2:]}' for year in range(1990, 2024)]
reemplazo = [str(year) for year in range(1990, 2024)]

# Realiza el reemplazo en todo el DataFrame
df.replace(temporadas, reemplazo, inplace=True, regex=True)

# Guarda el archivo CSV actualizado
df.to_csv('tu_archivo_actualizado1.csv', index=False, header=False)  # Guardamos sin encabezados

print("Se ha completado el cambio de los bloques de texto del documento.")


