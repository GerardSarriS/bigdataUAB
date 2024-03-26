# Creació de Relacions entre Artistes de Spotify amb Python

Aquest repositori conté un script en Python que analitza una llista de cançons de Spotify per crear relacions entre els artistes i guardar aquestes dades en un fitxer CSV per generar posteriorment un gràfic.

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
pip install spotipy
pip install SpotifyClientCredentials
pip install json
pip install pandas
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

3. Executa l'script `playlist.py`:

```
py playlist.py
```

4. Es generarà un arxiu CSV anomenat `graf_generes.csv` que conté les relacions entre artistes.

5. Utilitza aquest arxiu CSV per generar un gràfic amb l'eina de visualització de la teva elecció.

## Estructura del Projecte

- `playlist.py`: Script principal per crear relacions entre artistes a partir d'una llista de cançons de Spotify.
- `README.md`: Documentació del projecte (aquest fitxer).

## Contribució

Les contribucions són benvingudes. Si desitges millorar el codi o afegir noves funcionalitats, si us plau, envia un pull request.

## Llicència

Aquest projecte està sota la llicència [MIT](https://opensource.org/licenses/MIT).
