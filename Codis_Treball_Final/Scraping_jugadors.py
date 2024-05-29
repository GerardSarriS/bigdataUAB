"""import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
import time
import glob
#llibreria os



numero_jugador = range(28003, 1)
random_number = random.randint(1, 3)

def extract_players(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}",
                headers=headers,
            )

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text.strip()

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()

            df.to_excel(f"{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

        except AttributeError:
            print(f"Problema en {jugador}")


numero_jugador = range(28003, 0, -1)  # Corregir el rango
random_number = random.randint(1, 3)

extract_players(numero_jugador, random_number)


def juntar():
    files = glob.glob("*.xlsx")
    llista_dfs = []

    for f in files:
        df = pd.read_excel(f)
        any = f.split("_")[1].split(".")[0]
        df["año"] = any

        df.columns.values[0] = "Temporada"
        df.columns.values[2] = "Competició"
        df.columns.values[3] = "Club"
        df.columns.values[4] = "Aparicions"
        df.columns.values[5] = "Gols"
        df.columns.values[6] = "Assistencies"
        df.columns.values[7] = "Targetes"
        df.columns.values[8] = "Min_Jugats"

        df = df.drop("Competition", axis=1)

        llista_dfs.append(df)

    final_df = pd.concat(llista_dfs)
    final_df.to_excel("final2.xlsx", index=False)


juntar()

df = pd.read_excel("final2.xlsx")
print(df) """

import pandas as pd
import requests
from bs4 import BeautifulSoup
import random
import time
import glob

"""numero_jugador = [28003]
random_number = random.randint(1, 3)

def extract_players(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}",
                headers=headers,
            )

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text.strip()

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()

            df.to_excel(f"{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

        except AttributeError:
            print(f"Problema en {jugador}")

# Solo el número 28003
extract_players(numero_jugador, random_number)

def juntar():
    files = glob.glob("*.xlsx")
    llista_dfs = []

    for f in files:
        df = pd.read_excel(f)

        df.columns.values[0] = "Temporada"
        df.columns.values[2] = "Competició"
        df.columns.values[3] = "Club"
        df.columns.values[4] = "Aparicions"
        df.columns.values[5] = "Gols"
        df.columns.values[6] = "Assistencies"
        df.columns.values[7] = "Targetes"
        df.columns.values[8] = "Min_Jugats"

        df = df.drop("Competition", axis=1)
        df = df.drop("Unnamed: 9", axis=1)

        df = df.iloc[:-1]  # Eliminar la última fila
        llista_dfs.append(df)


    final_df = pd.concat(llista_dfs)
    final_df.to_excel("final.xlsx", index=False)

juntar()

df = pd.read_excel("final.xlsx")
print(df)"""

"""import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import glob
import re

def extraer_y_juntar(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}",
                headers=headers,
            )

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text
            nom = re.sub(r'[^a-zA-Z\s]', '', nom).strip()

            #club = soup.find("img", class_="hauptlink no-border-rechts zentriert").get('title')

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            #Agregar columna de club

            #df["club"] = club

            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()

            df.to_excel(f"final{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

        except AttributeError:
            print(f"Problema en {jugador}")

    files = glob.glob(f"final*.xlsx")
    llista_dfs = []

    for f in files:
        df = pd.read_excel(f)

        df.columns.values[0] = "Temporada"
        df.columns.values[2] = "Competició"
        df.columns.values[3] = "Club"
        df.columns.values[4] = "Aparicions"
        df.columns.values[5] = "Gols"
        df.columns.values[6] = "Assistencies"
        df.columns.values[7] = "Targetes"
        df.columns.values[8] = "Min_Jugats"



        df = df.drop("Competition", axis=1)
        df = df.drop("Unnamed: 9", axis=1)

        df = df.iloc[:-1]  # Eliminar la última fila
        llista_dfs.append(df)

    final_df = pd.concat(llista_dfs)
    final_df.to_excel(f"final{numero_jugador[0]}.xlsx", index=False)

# Utilización de la función
numero_jugador = range(28003,28013,1)
random_number = random.randint(1, 3)
extraer_y_juntar(numero_jugador, random_number)

df = pd.read_excel(f"final{numero_jugador[0]}.xlsx")
print(df)"""

"""import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
import re

def extraer_y_juntar(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            # Comprobar si el archivo para el jugador ya existe
            if os.path.exists(f"final{jugador}.xlsx"):
                print(f"El archivo para el jugador {jugador} ya existe, saltando...")
                continue

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}",
                headers=headers,
            )

            resposta.raise_for_status()  # Lanzar excepción en caso de error HTTP

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text
            nom = re.sub(r'[^a-zA-Z\s]', '', nom).strip()

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()

            df.to_excel(f"final{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

            # Leer el archivo excel recién creado y renombrar las columnas
            df = pd.read_excel(f"final{jugador}.xlsx")
            df.columns.values[0] = "Temporada"
            df.columns.values[2] = "Competició"
            df.columns.values[3] = "Club"
            df.columns.values[4] = "Aparicions"
            df.columns.values[5] = "Gols"
            df.columns.values[6] = "Assistencies"
            df.columns.values[7] = "Targetes"
            df.columns.values[8] = "Min_Jugats"
            df = df.drop("Competition", axis=1)
            df = df.drop("Unnamed: 9", axis=1)
            df = df.iloc[:-1]  # Eliminar la última fila

            # Guardar el DataFrame final en un nuevo archivo Excel
            df.to_excel(f"final{jugador}.xlsx", index=False)

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP para el jugador {jugador}: {e}")
            # Obtener el último jugador procesado con éxito
            ultimo_jugador = jugador - 1 if jugador != numero_jugador[0] else numero_jugador[0]
            print(f"Reanudando desde el último jugador exitoso ({ultimo_jugador})...")
            break
        except Exception as e:
            print(f"Error inesperado para el jugador {jugador}: {e}")

# Utilización de la función
numero_jugador = range(28000, 28050, 1)
random_number = random.randint(1, 3)
extraer_y_juntar(numero_jugador, random_number)"""


"""import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
import re

def extraer_y_juntar(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            if not numero_jugador:  # Verificar si la lista está vacía
                print("La lista de números de jugador está vacía.")
                break

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}",
                headers=headers,
            )

            resposta.raise_for_status()  # Lanzar excepción en caso de error HTTP

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text
            nom = re.sub(r'[^a-zA-Z\s]', '', nom).strip()

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()

            df.to_excel(f"final{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

            # Leer el archivo excel recién creado y renombrar las columnas
            df = pd.read_excel(f"final{jugador}.xlsx")
            df.columns.values[0] = "Temporada"
            df.columns.values[2] = "Competició"
            df.columns.values[3] = "Club"
            df.columns.values[4] = "Aparicions"
            df.columns.values[5] = "Gols"
            df.columns.values[6] = "Assistencies"
            df.columns.values[7] = "Targetes"
            df.columns.values[8] = "Min_Jugats"
            df = df.drop("Competition", axis=1)
            df = df.drop("Unnamed: 9", axis=1)

            df = df.iloc[:-1]  # Eliminar la última fila

            # Guardar el DataFrame final en un nuevo archivo Excel
            df.to_excel(f"final{jugador}.xlsx", index=False)

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP para el jugador {jugador}: {e}")
            # Obtener el último jugador procesado con éxito
            ultimo_jugador = jugador - 1 if jugador != numero_jugador[0] else numero_jugador[0]
            print(f"Reanudando desde el último jugador exitoso ({ultimo_jugador})...")
            break
        except IndexError:
            print(f"Error: No se pudo encontrar la tabla de datos para el jugador {jugador}.")
            continue
        except Exception as e:
            print(f"Error inesperado para el jugador {jugador}: {e}")

# Utilización de la función
numero_jugador = range(28133, 50000, 1)
random_number = random.randint(1, 3)
extraer_y_juntar(numero_jugador, random_number)"""


import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import re

def extraer_y_juntar(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            if not numero_jugador:  # Verificar si la lista está vacía
                print("La lista de números de jugador está vacía.")
                break

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}/saison//verein/0/liga/0/wettbewerb//pos/0/trainer_id/0/plus/1",
                headers=headers,
            )

            resposta.raise_for_status()  # Lanzar excepción en caso de error HTTP

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text
            nom = re.sub(r'[^a-zA-Z\s]', '', nom).strip()

            df = pd.read_html(tabla.prettify())[0]

            # Agregar columna de nombre del jugador
            df["name"] = nom

            #Afegir la columna ID
            df["id_jugador"] = jugador


            # Agregar columna de posición
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()


            df.to_excel(f"player_{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Todo bien en {jugador}")

            # Leer el archivo excel recién creado y renombrar las columnas
            df = pd.read_excel(f"player_{jugador}.xlsx")
            df.columns.values[0] = "Season"
            df.columns.values[2] = "Competitició"
            df.columns.values[3] = "Club"
            df.columns.values[4] = "Squad"
            df.columns.values[5] = "Appearances"
            df.columns.values[6] = "Points per match"
            df.columns.values[7] = "Goals"
            df.columns.values[8] = "Assists"
            df.columns.values[9] = "Own goals"
            df.columns.values[10] = "Subtitutions on"
            df.columns.values[11] = "Subtitutions off"
            df.columns.values[12] = "Yellow cards"
            df.columns.values[13] = "Second yellow cards"
            df.columns.values[14] = "Red cards"
            df.columns.values[15] = "Penalty goals"
            df.columns.values[16] = "Minutes per goal"
            df.columns.values[17] = "Minutes played"

            df = df.drop("Competition", axis=1)
            df = df.drop("Unnamed: 18", axis=1)

            imagenes = soup.find_all("img", class_="tiny_wappen")

            list_club_names = []

            for img in imagenes:
                club_name = img.get("alt")
                list_club_names.append(club_name)

            df2 = pd.DataFrame(list_club_names)
            df["clubs_ok"] = df2[0]
            df = df.iloc[:-1]  # Eliminar la última fila

            # Guardar el DataFrame final en un nuevo archivo Excel
            df.to_excel(f"player_{jugador}.xlsx", index=False)

        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP para el jugador {jugador}: {e}")
            # Obtener el último jugador procesado con éxito
            ultimo_jugador = jugador - 1 if jugador != numero_jugador[0] else numero_jugador[0]
            print(f"Reanudando desde el último jugador exitoso ({ultimo_jugador})...")
            break
        except IndexError:
            print(f"Error: No se pudo encontrar la tabla de datos para el jugador {jugador}.")
            continue
        except Exception as e:
            print(f"Error inesperado para el jugador {jugador}: {e}")

# Utilización de la función
numero_jugador = range(32062, 33333, 1)
random_number = random.randint(1, 3)
extraer_y_juntar(numero_jugador, random_number)












