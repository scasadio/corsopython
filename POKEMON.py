###POKEMON
import pandas as pd
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv')  #copia il percorso e GIRA GLI SLASH  
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

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv', index_col=1) #indice della colonna name
print(df.loc["Bulbasaur"])  #solo la riga di bulbasaur
print(df.iloc[9])   #riga di squirtle
print(df.iloc[9,3])     #print(df.loc["Squirtle","Total"])

print(df.loc["Bulbasaur":"Venusaur"])   #da_a_
print(df.loc["Bulbasaur",["Type 1","HP","Total"]])  #print(df.iloc[0,[1,4,3]])


####ITERARE DATAFRAME           #.iteritems NO in versione 2.0 --> use .items
df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv').head(1)
for key,value in df.items():         
    print(key)  #chiavi di head

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv').head(4)
for key,value in df.items():         
    print(value)  #ritona tutti valori per le prime 4 righe del dataset

df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv').head(1)
for row in df.itertuples():         
    print(row) #non legge gli spazi e i punti nei nomi delle colonne
    #crea una tupla con l'indice della riga e ci nomina tutte le colonne che abbiamo con il rispettivo risultato


df=pd.read_csv('C:/Users/Utente/OneDrive/Desktop/corsopython/pokemon.csv').head(1)
for index,row in df.iterrows():
    if(index==0):
        row['Name']="Bulbasaura"
    print(row)      #copia e cambia il nome di bulbasaur infatti
print(df.head(1))       #rimane bulbasaur


###ORDINARE UN DATAFRAME

