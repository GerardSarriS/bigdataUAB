import os
import pandas as pd
import shutil

def move_and_remove_files_with_unnamed_columns(directory, destination_folder):
    count = 0
    # Recorrer todos los archivos en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith('.xlsx'):
            # Construir el path completo al archivo
            filepath = os.path.join(directory, filename)
            try:
                # Cargar el archivo Excel
                df = pd.read_excel(filepath)
                # Comprobar si alguna columna contiene 'Unnamed'
                if any('Unnamed' in col for col in df.columns):
                    count += 1
                    # Mover el archivo a la nueva carpeta
                    shutil.move(filepath, os.path.join(destination_folder, filename))
                    # Eliminar el archivo del directorio original
                    os.remove(filepath)
            except Exception as e:
                print(f"No se pudo procesar el archivo {filename}: {e}")
    return count

# Ruta al directorio donde están los archivos Excel
directory_path = '.'  # Directorio actual
# Ruta a la nueva carpeta donde se moverán los archivos
new_folder_path = './unnamed_files'  # Puedes cambiar este nombre o la ruta según tu preferencia
# Crear la nueva carpeta si no existe
os.makedirs(new_folder_path, exist_ok=True)
# Llamar a la función y mostrar el resultado
unnamed_count = move_and_remove_files_with_unnamed_columns(directory_path, new_folder_path)
print(f"Número de archivos con columnas 'Unnamed': {unnamed_count}")
