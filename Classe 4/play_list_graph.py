
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import pandas as pd

#(clau no útil)
api_client_id = "2d24e72bccfc459d8c6eb1408f954097"
api_client_secret = "29126da8bfd742a39389cb3a03766b64" 

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

playlist_id = "3EPibIZjyrJDGTZpvI86HQ"

#info playlist
playlist_info = spotify.playlist_items(playlist_id)

#Ruta para conseguir el nombre del artista dentro de la lista de items de la playlist: playlist_info["items"][0]["track"]["artists"][0]["name"]

playlist_items = playlist_info["items"]

#Lista de listas con objetos dentro, cada objeto representa un artista que está presente como autor del track
playlist_artists_by_track_list = []

for i in range(len(playlist_items)):
    playlist_artists_by_track_list.append(playlist_items[i]["track"]["artists"])

total_artists = []

for i in range(len(playlist_artists_by_track_list)):
    for k in range(len(playlist_artists_by_track_list[i])):
        artist = {
            "name": playlist_artists_by_track_list[i][k]["name"],
            "id": playlist_artists_by_track_list[i][k]["id"]
        }
        total_artists.append(artist)

def delete_duplicates(list):
    new_list = []

    for item in list:
        if item not in new_list:
            new_list.append(item)

    return new_list

total_artists = delete_duplicates(total_artists)


list_related_artists = []

tuples = []

for artist in total_artists:
    related_artists = spotify.artist_related_artists(artist["id"])
    list_related_artists.append(artist)

    for related_artist in related_artists["artists"]:
        related_artist = {
            "name": related_artist["name"],
            "id": related_artist["id"]
        }

        source = artist["name"]
        target = related_artist["name"]
        tuple = (source, target)
        tuples.append(tuple)

        list_related_artists.append(related_artist)


df = pd.DataFrame(tuples, columns=["source", "target"])

df.to_csv("playlist.csv", sep=",", index= False)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(playlist_info, f, indent=4)

with open("playlist_artists_by_track_list.json", "w", encoding="utf-8") as f:
    json.dump(playlist_artists_by_track_list, f, indent=4)

with open("list_related_artists.json", "w", encoding="utf-8") as f:
    json.dump(list_related_artists,f,indent=4)
