import pandas as pd
import isodate

df = pd.read_excel("KEXP.xlsx")
columnes = df.columns


#Quantes columnes i files té
num_files, num_columnes = df.shape

print(f'El dataset té {num_files} files i {num_columnes} columnes.')


#Quines columnes té:

print('Les columnes que composen el dataset son:')
for columna in columnes:
    print(f'- {columna}')


#Afegir columnes amb engagment, desviació absoluta, desviació percentual

df["engagment"]= df["likeCount"] + df["commentCount"]

promitg_espectadors = df['viewCount'].mean()
promitg_comentaris = df['commentCount'].mean()
promitg_likes = df['likeCount'].mean()

df['Desviació Absoluta Espectadors'] = df['viewCount'] - promitg_espectadors
df['Desviació Percentual Espectadors'] = round(((df['Desviació Absoluta Espectadors'] / promitg_espectadors) * 100),2)

df['Desviació Absoluta Comentaris'] = df['commentCount'] - promitg_comentaris
df['Desviació Percentual Comentaris'] = round(((df['Desviació Absoluta Comentaris'] / promitg_comentaris) * 100), 2)

df['Desviació Absoluta Likes'] = df['likeCount'] - promitg_likes
df['Desviació Percentual Likes'] = round(((df['Desviació Absoluta Likes'] / promitg_likes) * 100),2)



df = df.drop(["channelId","categoryId","channelTitle","tags","publishedAt","blocked_at"], axis= 1)


#Vídeo més vist i vídeo més comentat.

index_max_viwers = df["viewCount"].idxmax()
titol_del_video = df.loc[index_max_viwers,"title"]

index_max_comentado = df["commentCount"].idxmax()
titol_del_video_2 = df.loc[index_max_comentado,"title"]

print(f'El vídeo més vist és: {titol_del_video} ')
print(f'El vídeo més comentat és:  {titol_del_video_2} ')



df.to_excel("nou_dataset.xlsx", index= False)
