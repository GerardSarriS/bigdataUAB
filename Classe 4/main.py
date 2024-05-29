import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import glob
import pandas as pd

"""
api_client_id = "2d24e72bccfc459d8c6eb1408f954097"
api_client_secret = "29126da8bfd742a39389cb3a03766b64"

# Configurar el cliente de Spotify
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(api_client_id, api_client_secret))

# ID de la playlist que deseas obtener
playlist_list = ["3EPibIZjyrJDGTZpvI86HQ","4jQOYNbq4xQ94tRe5Y3g85","1yugX4RYk0Y9r27UC8U4xt"]
#serveix per agafar elements d'una playlist més enllà dels 100 items.
offset = 0

def get_playlist(playlist,offset):
    resposta = spotify.playlist_items(playlist,offset=offset)
    with open(f"{playlist}-{offset}.json", "w", encoding="utf-8") as f:
        json.dump(resposta, f, indent=4)


    if resposta["next"] == None:
        print("Final")
        pass
    else:
        offset = offset + 100
        print("nova petició")
        get_playlist(playlist, offset)




for playlist in playlist_list:
    offset = 0
    get_playlist(playlist,offset)
"""


files = glob.glob("*.json")
track_list = []
for file in files:
    with open(file) as f:
        d = json.load(f)
        tracks = d["items"]
        for track in tracks:
            track_dict = {}
            track_dict["name"] = track["track"]["name"]
            track_dict["duration_ms"] = track["track"]["duration_ms"]
            track_dict["duration_seg"] = round(track_dict["duration_ms"]/1000/60, 2)
            track_dict["track_id"] = track["track"]["id"]
            track_dict["popularity"] = track["track"]["popularity"]
            track_dict["artist_name"] = track["track"]["artists"][0]["name"]

            track_list.append(track_dict)

df = pd.DataFrame.from_dict(track_list)
df.to_csv("track_list.csv", sep=",", index= False)

print(df)










