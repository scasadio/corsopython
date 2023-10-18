###PANDAS
#è costruito su numpy

import pandas as pd


###CREARE UNA SERIE
ds=[5,10,15,20,25]
serie=pd.Series(ds,index=["perUNO","perDUE","perTRE","perQUATTRO","perCINQUE"])  #devo inserire tutti gli indici
print(serie)

ds={"x":5,"y":10,"z":15,"w":20,"j":25}
serie=pd.Series(ds, index=["x","j"])    #considera solo quei due indici, si puo fare perche sono gia tutti specificati nella riga prima
print(serie)


###CREARE UN DATASET
ds={
    'mesi':["gennaio","febbraio","marzo","aprile","maggio"],
    "giorni":[31,28,31,30,31],
    "stagione":["inverno","inverno","primavera","primavera","primavera"],
    "festività":["befana","carnevale","festa donne","pesce","compleanno"]
}
df=pd.DataFrame(ds)
print(df.loc[[0,1]])            #loc = localisation, per catturare solo una riga o piu del dataset

df_i=pd.DataFrame(ds,index=["riga1","riga2","riga3","riga4","riga5"])       #rinomino gli indici delle righe
print(df_i.loc[["riga1","riga2"]]) 
