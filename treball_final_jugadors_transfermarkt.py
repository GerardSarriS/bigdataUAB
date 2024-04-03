import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
import os
import re

def extraer_y_juntar(numero_jugador, random_number):
    for jugador in numero_jugador:
        try:
            if not numero_jugador:  # Verificar si la llista està buida
                print("La llista de números de jugador està buida.")
                break

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 OPR/107.0.0.0"
            }

            resposta = requests.get(
                f"https://www.transfermarkt.com/lionel-messi/leistungsdatendetails/spieler/{jugador}",
                headers=headers,
            )

            resposta.raise_for_status()  # Llençar excepció en cas d'error HTTP

            soup = BeautifulSoup(resposta.text, "html.parser")
            final = soup.find("div", id="yw1")
            tabla = final.find_next("table")

            nom = soup.find("h1", class_="data-header__headline-wrapper").text
            nom = re.sub(r'[^a-zA-Z\s]', '', nom).strip()

            df = pd.read_html(tabla.prettify())[0]

            # Afegir columna de nom del jugador
            df["name"] = nom

            # Afegir columna de posició
            posicion = soup.find_all("li", class_="data-header__label")
            pos = posicion[4]
            a = pos.find_all("span")
            position_text = ""
            for span in a:
                position_text += span.text.strip() + " "
            df["position_text"] = position_text.strip()

            df.to_excel(f"final{jugador}.xlsx", index=False)
            time.sleep(random_number)
            print(f"Tot bé en {jugador}")

            # Llegir l'arxiu excel recent creat i canviar el nom de les columnes
            df = pd.read_excel(f"final{jugador}.xlsx")
            df.columns.values[0] = "Temporada"
            df.columns.values[2] = "Competicio"
            df.columns.values[3] = "Club"
            df.columns.values[4] = "Aparicions"
            df.columns.values[5] = "Gols"
            df.columns.values[6] = "Assistencies"
            df.columns.values[7] = "Targetes"
            df.columns.values[8] = "Min_Jugats"
            df = df.drop("Competition", axis=1)
            df = df.drop("Unnamed: 9", axis=1)
            df = df.iloc[:-1]  # Eliminar l'última fila

            # Guardar el DataFrame final en un nou arxiu Excel
            df.to_excel(f"final{jugador}.xlsx", index=False)

        except requests.exceptions.RequestException as e:
            print(f"Error en la sol·licitud HTTP per al jugador {jugador}: {e}")
            # Obtenir l'últim jugador processat amb èxit
            ultimo_jugador = jugador - 1 if jugador != numero_jugador[0] else numero_jugador[0]
            print(f"Reanudant des de l'últim jugador exitós ({ultimo_jugador})...")
            break
        except IndexError:
            print(f"Error: No s'ha pogut trobar la taula de dades per al jugador {jugador}.")
            continue
        except Exception as e:
            print(f"Error inesperat per al jugador {jugador}: {e}")

# Utilització de la funció
numero_jugador = range(28000, 28050, 1)
random_number = random.randint(1, 3)
extraer_y_juntar(numero_jugador, random_number)

