###POKEMON
import pandas as pd
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')  #copia il percorso e GIRA GLI SLASH  
#, sep='\t',delimiter='\n'        
#\t sta per tab, indichiamo che il dataset è diviso dal tab (nel nostro caso c'è la virgola)
#il delimiter indica che deve andare a capo dopo ogni riga
print(df)

#df=pd.read_excel('excel.xlsx', index_col=0)
#print(df.loc["luca"])


##leggere i dati dal dataframe
print(df[0:10])
print(df.head(10))  #prende le prima 10  #df.tail(10) prende le ultime 10

print(df["Name"].head(3)) #se voglio solo il nome(prima colonna) delle prime 3 righe
print(df[["Name","HP","Generation"]][10:20])

print(df.loc[0,"Name"]) #colonna1
print(df.iloc[0,1]) #colonna1  


###LOC vs ILOC : localisation and index localisation
#loc: localizzare una serie di celle(righe,colonne, porzioni separate del dataset)
#iloc: localizza delle coordinate numeriche delle celle 

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv', index_col=1) #indice della colonna name
print(df.loc["Bulbasaur"])  #solo la riga di bulbasaur
print(df.iloc[9])   #riga di squirtle
print(df.iloc[9,3])     #print(df.loc["Squirtle","Total"])

print(df.loc["Bulbasaur":"Venusaur"])   #da_a_
print(df.loc["Bulbasaur",["Type 1","HP","Total"]])  #print(df.iloc[0,[1,4,3]])


####ITERARE DATAFRAME           #.iteritems NO in versione 2.0 --> use .items
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv').head(1)
for key,value in df.items():         
    print(key)  #chiavi di head

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv').head(4)
for key,value in df.items():         
    print(value)  #ritona tutti valori per le prime 4 righe del dataset

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv').head(1)
for row in df.itertuples():         
    print(row) #non legge gli spazi e i punti nei nomi delle colonne
    #crea una tupla con l'indice della riga e ci nomina tutte le colonne che abbiamo con il rispettivo risultato


df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv').head(1)
for index,row in df.iterrows():
    if(index==0):
        row['Name']="Bulbasaura"
    print(row)      #copia e cambia il nome di bulbasaur infatti
print(df.head(1))       #rimane bulbasaur


###ORDINARE UN DATAFRAME
import pandas as pd
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
sdf=df.sort_index()     #(ascending=False) parte dalla fine
print(sdf.head(3))
sdf=df.sort_values(by="Name")
print(sdf.head(5))

sdf=df.sort_values(by=["Total","HP"],ascending=[False,True]) #ordina total discendente e hp ascendente
print(sdf[["Name","Total","HP"]].head(5))
#ordina per totale, se ci sono dei doppioni in totale, ordina per hp

###MANIPOLARE COLONNE
from matplotlib.pyplot import axis
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
df[["Wii","Switch","GameBoy"]]=["2nd","7th","1st"]  #valori da assegnare alle colonne
print(df[["Name","Total","Wii","Switch","GameBoy"]])      #aggiungiamo le colonne

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
df.insert(1,"Nome","aaaa")
print(df)       #abbiamo aggiunto posizione, nome e valori 

df.loc[:,"Wii"]="aaaa"
print(df)       #abbiamo creato una colonna nuova e la mette in fondo

df=df.assign(Wii="qwerty")  #cambiato valore di wii
print(df)

df.drop("Legendary",inplace=True,axis=1)  #asse 1 è quella delle colonne
print(df)

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
colPop=df.pop("Name")   #permette di salvare la colonna rimossa
print(df.head(2))
print(colPop.head(2))

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
print(df.loc[:,["Type 1","Name","HP","Total"]]) #inverte le colonne
print(df.iloc[:,[1,3,5,2,4]]) #inverte le colonne

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
columns=list(df.columns)        #df.columns.tolist()
columns.reverse()
print(df[columns])

###SALVARE IN CSV E EXCEL
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
df2=df[["Name","#","Total"]]
#df2.to_csv("minipokemon",index false)
compressed_df2=dict(method="zip",archive_name="nuovi_pokemon.csv")      #chiamami nuovi_pokemnon.csv e salvalo in .zip
#df2.to_csv("nuovi_pokemon.zip",index=False,compression=compressed_df2)

#df2.to_excel("nuovi_pokemon.xlsx", index=False, sheet_name="Pokemon Totali")

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
from typing import Dict

df2=df[["Name","#","Total"]]
df3=df[["Name","HP","Sp. Atk"]]
df4=df[["Name","Attack","Sp. Atk","Speed","Generation"]]
with pd.ExcelWriter("nuovi_pokemon.xlsx") as writer:
    df2.to_excel(writer,sheet_name="Totali", index=False)
    df3.to_excel(writer,sheet_name="Stats", index=False)
    df4.to_excel(writer,sheet_name="Quarti", index=False)
#scrivere su piu fogli interni al foglio di lavoro

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
df2=df.iloc[0:10,0:4]  #prendo una porzione del dataset
print(df2)

with pd.ExcelWriter("nuovi_pokemon.xlsx",mode="a") as writer:
    df2.to_excel(writer, sheet_name="foglio appeso")        #appendere un foglio in piu nel doc exce

import pandas as pd
###FILTRARE I DATI
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
print(df[df.Name=="Bulbasaur"])     #inserisco la condizione del print che voglio
print(df[df["Name"].str.contains("saur")])  #vogliamo quelli che contengono saur nel nome
print(df)

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
filtro=["Bulbasaur","Charmander","Squirtle"]
print(df["Name"].isin(filtro))      #ritorna solo quelli che sono nel filtro

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
filtro=["Bulbasaur","Charmander","Squirtle"]
print(df[(df["Total"]>700) & (df["Sp. Atk"]>160)])
print(df.loc[(df['Name'].str.contains("Bulbasaur")),["Name","HP","Generation"]])
print(df.query("Total>750 and Speed>100"))




###COME MODIFICARE I DATI
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
df.loc[df['Name']=='Bulbasaur',"Name"]="Babasaur"#cambiato nome
df.loc[df['Name']=='Bulbasaur',["Type 1","Type 2"]]=["Grass","Poison"]
print(df.head)

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
df.loc[(df["Name"].str.contains("saur"))&(df['Total']>500),["Type 1","Type 2"]]=["qwerty", "cvdte"]
print(df.head)      #multiple colonna e multipli valori


###COME RAGGRUPPARE CON GROUPBY
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
types=df.groupby("Type 1")
print(types.groups)

for name, group in types:
    print(name)
    print(group)

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/python/pokemon.csv')
#types=df.groupby(["Type 1"]).mean()[["HP","Attack","Sp. Atk", "Defense","Sp. Def","Speed"]]
#print(types.sort_values(by="Defense", ascending=False))

df["count"]=1       #creo una colonna count
types=df.groupby(["Type 1"]).count()["count"]
print(types)



###DATASET CALORIES
import pandas as pd
df=pd.read_csv("C:/Users/Utente/OneDrive/Desktop/python/clear.csv")
print(df)
#possiamo notare missing values, duplicati e valori difettati

#puliamo celle vuote
df.dropna(inplace=True)  #inplace per non avere un nuovo dataframe
print(df) #oppuure
df=pd.read_csv("C:/Users/Utente/OneDrive/Desktop/python/clear.csv")
df.fillna(9999,inplace=True)
print(df)
#su una specifica colonna
df=pd.read_csv("C:/Users/Utente/OneDrive/Desktop/python/clear.csv")
df["Calories"].fillna(df["Calories"].mean(),inplace=True)   #sostituisco con la media delle calorie
df["Date"].fillna("2020/12/22",inplace=True)
#dobbiamo sistemare il formato della data che abbiamo inserito
###df["Date"]=pd.to_datetime(df["Date"],)   #format="%Y/%m/%d"  non va
df.loc[7,"Duration"]=45
print(df) 

for index in df.index:
    if df.loc[index,"Duration"]>60:         #siccome c'era una sessione di allenamento sbagliata, tutto cio che è superiore a 60 lo portiamo a 60
        df.loc[index,"Duration"]=60
print(df)

df.drop_duplicates(inplace=True)
print(df)