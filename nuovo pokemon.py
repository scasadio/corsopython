import pandas as pd
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv')
sdf=df.sort_index()     #(ascending=False) parte dalla fine
print(sdf.head(3))
sdf=df.sort_values(by="Name")
print(sdf.head(5))

sdf=df.sort_values(by=["Total","HP"],ascending=[False,True]) #ordina total discendente e hp ascendente
print(sdf[["Name","Total","HP"]].head(5))
#ordina per totale, se ci sono dei doppioni in totale, ordina per hp

###MANIPOLARE COLONNE
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv')
df[["Wii","Switch","GameBoy"]]=["2nd","7th","1st"]  #valori da assegnare alle colonne
print(df[["Name","Total","Wii","Switch","GameBoy"]])      #aggiungiamo le colonne
#aggiungi commento