# Transfermarkt Data Scraping Project

## Descripció

Aquest projecte té com a objectiu l'extracció de dades de la web Transfermarkt utilitzant tècniques de scraping amb Python. L'objectiu principal és obtenir informació detallada sobre els jugadors registrats a la web i analitzar diverses mètriques com:

- Quina posició fa més gols.
- Quina posició té més targetes grogues i vermelles.
- Màxims golejadors de tots els temps de les 5 millors lligues europees de futbol. (Comparació de la diferència entre lligues i jugadors.)
- Comparació del promig de gols marcats a les 5 millors lligues europees des de l'any 2000 fins ara.
- Quins jugadors tenen millor promig de gols per minut jugat.

## Requisits

Abans de començar, assegura't de tenir instal·lats els següents paquets de Python:

- `requests`
- `beautifulsoup4`
- `pandas`
- `os`
- `random`
- `time`
- `glob`

Pots instal·lar aquests paquets executant:

```bash
pip install requests beautifulsoup4 pandas os requests glob
```

## Ús

### 1. Scraping de Dades
Per obtenir les dades dels jugadors executa els següent script:

```bash
python Scraping_jugadors.py
```

### 2. Neteja de Dades
Mitjançant els scripts següents hem pogut netejar i compactar el milió i mitg de files que teniem de dades:

```bash
python Script_unir.py
python Canviar_columnes.py
python Script_Unnamed.py
python Extreure_Unnamed.py
```
### 3. Anàlisi
Mitjançant Tableau s'han crear gràfics per poder visualitzar les dades prèviament organitzades i netejades.

Alguns d'aquests gràfics han sigut els següents:

- Posició amb més gols.
  ![Posició amb més gols](imatges_gràfics/Freqüència%20de%20gols%20per%20posició.png) 

- Posició amb més targetes grogues i vermelles.
- Màxims golejadors de tots els temps de les 5 millors lligues europees.(Comparació de la diferència entre lligues i jugadors.)
- Comparació del promig de gols marcats des de l'any 2000 fins ara.
- Quins jugadors tenen millor promig de gols per minut jugat.



