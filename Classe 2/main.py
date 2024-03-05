#Spotify 2024
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd


api_client_id = "917bba0c50b0444c80906935168daa01"
api_client_secret = "eeb564ee21734c94ab49af9d8d1df394"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id,api_client_secret))

artista_inicial="4gzpq5DPGxSnKTe4SA8HAU"

related = spotify.artist_related_artists(artista_inicial)

artistes = related["artists"]

#creem llista sempre abans del FOR

llista_artistes = []
i=0
for a in artistes:
    i += 1

    name = a["name"]
    seguidors = a["followers"]["total"]
    link = a["external_urls"]["spotify"]
    id = a["id"]
    popularidad = a["popularity"]


    frame = pd.DataFrame({
        "semilla": artista_inicial,
        "name": name,
        "seguidors": seguidors,
        "link": link,
        "id": id,
        "popularidad": popularidad,


    }, index=[i])
    llista_artistes.append(frame)

    related_2 = spotify.artist_related_artists(id)
    artistes_2 = related_2["artists"]

    for a_2 in artistes_2:
        i +=1
        name = a_2["name"]
        seguidors = a_2["followers"]["total"]
        link = a_2["external_urls"]["spotify"]
        id_2 = a_2["id"]
        popularidad = a_2["popularity"]


        frame = pd.DataFrame({
            "semilla": id,
            "name": name,
            "seguidors": seguidors,
            "link": link,
            "id": id_2,
            "popularidad": popularidad,


        }, index=[i])
        llista_artistes.append(frame)

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(related, f, indent=4)

final = pd.concat(llista_artistes)
print(final)

final.to_excel("dataset.xlsx")

"""import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd

api_client_id = "917bba0c50b0444c80906935168daa01"
api_client_secret = "eeb564ee21734c94ab49af9d8d1df394"

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

artista_inicial = "4gzpq5DPGxSnKTe4SA8HAU"

related = spotify.artist_related_artists(artista_inicial)

artistes = related["artists"]

# Inicializamos la lista de artistas
llista_artistes = []


# Función para obtener los artistas relacionados y construir el DataFrame
def obtener_artistas_relacionados(id_artista, semilla):
    related_artists = spotify.artist_related_artists(id_artista)
    artistes_relacionats = related_artists["artists"]
    return artistes_relacionats


# Función para construir el DataFrame con la información del artista
def construir_dataframe(artista, semilla):
    name = artista["name"]
    seguidors = artista["followers"]["total"]
    link = artista["external_urls"]["spotify"]
    id = artista["id"]

    frame = pd.DataFrame({
        "semilla": semilla,
        "name": name,
        "seguidors": seguidors,
        "link": link,
        "id": id,
    }, index=[0])  # Usamos index=[0] porque solo estamos agregando un artista a la vez

    return frame


# Bucle para iterar sobre los artistas relacionados
for artista in artistes:
    # Construimos el DataFrame para el artista actual
    frame_artista = construir_dataframe(artista, artista_inicial)

    # Agregamos el DataFrame a la lista
    llista_artistes.append(frame_artista)

    # Obtenemos los artistas relacionados del artista actual
    artistas_relacionados_2 = obtener_artistas_relacionados(artista["id"], artista_inicial)

    # Bucle para iterar sobre los artistas relacionados del artista actual
    for artista_relacionado_2 in artistas_relacionados_2:
        # Construimos el DataFrame para el artista relacionado
        frame_artista_relacionado_2 = construir_dataframe(artista_relacionado_2, artista_inicial)

        # Agregamos el DataFrame a la lista
        llista_artistes.append(frame_artista_relacionado_2)

# Concatenamos todos los DataFrames en uno final
final = pd.concat(llista_artistes)

# Imprimimos el DataFrame final
print(final)

# Guardamos el DataFrame en un archivo Excel
final.to_excel("dataset2.xlsx")

"""






