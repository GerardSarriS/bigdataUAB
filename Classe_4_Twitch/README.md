# Extracció de Dades d'Streamers de Twitch amb Python

Aquest repositori conté un script en Python que utilitza l'API de Twitch per extreure dades d'streamers durant un temps determinat i guardar aquestes dades en arxius JSON.

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
pip install Twitch
pip install  json
pip install time
```

## Ús

1. Obtén les teves credencials de l'API de Twitch:
   - Vés a [Twitch Developer](https://dev.twitch.tv/console/apps) i crea una aplicació.
   - Copia el teu Client ID i Client Secret.

2. Configura les credencials al fitxer `config.py`:

```python
public = 'el_teu_client_id'
secret = 'el_teu_client_secret'
```

3. Executa l'script `twitch_streamers_data.py`:

```
python main.py
```

4. Es generaran arxius JSON amb les dades dels streamers.

## Estructura del Projecte

- `main.py`: Script principal per extreure dades d'streamers de Twitch.
- `README.md`: Documentació del projecte (aquest fitxer).

## Contribució

Les contribucions són benvingudes. Si desitges millorar el codi o afegir noves funcionalitats, si us plau, envia un pull request.

## Llicència

Aquest projecte està sota la llicència [MIT](https://opensource.org/licenses/MIT).
