# Extracció de Dades d'Artistes de Spotify amb Python

Aquest repositori conté un script en Python que utilitza l'API de Spotify per extreure dades d'artistes i desar-les en un document Excel.

## Requisits

- Python 3.x
- pip (gestor de paquets de Python)

## Instal·lació

1. Clona aquest repositori a la teva màquina local:

```
git clone https://github.com/tu_usuari/nom_del_repositori.git
```

2. Instal·la les dependències necessàries:

```
pip install pandas
pip install json
pip install spotipy
pip install SpotifyClientCredentials
```

## Ús

1. Obtén les teves credencials de l'API de Spotify:
   - Vés a [Spotify for Developers](https://developer.spotify.com/dashboard/login) i crea una aplicació.
   - Copia el teu Client ID i Client Secret.

2. Configura les credencials al fitxer `config.py`:

```python
api_client_id = 'el_teu_client_id'
api_client_secret = 'el_teu_client_secret'
```

3. Executa l'script `main.py`:

```
py main.py
```

4. Es generarà un arxiu Excel anomenat `artist_data.xlsx` que conté les dades dels artistes.

## Estructura del Projecte

- `main.py`: Script principal per extreure dades d'artistes de Spotify.
- `README.md`: Documentació del projecte (aquest fitxer).

## Contribució

Les contribucions són benvingudes. Si desitges millorar el codi o afegir noves funcionalitats, si us plau, envia un pull request.


## Llicència

Aquest projecte està sota la llicència [MIT](https://opensource.org/licenses/MIT).
