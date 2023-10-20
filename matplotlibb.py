from matplotlib import pyplot as plt
print(plt.style.available)
#plt.style.use("dark_background")
#plt.style.use("ggplot")
x=[25,26,27,28,29,30]
y1=[100,120,140,110,150,145]
y2=[80,90,120,150,170,140]
plt.plot(x,y1, label="italiani", color="red", linewidth=5, linestyle="--")
plt.plot(x,y2, label="francesi", color="#212121",linestyle="dotted",marker="o")
#titolo
plt.title("nome del grafico")
#etichette
plt.xlabel("eta")
plt.ylabel("valori")
plt.legend()
#plt.legend(["italiani","francesi"])
plt.grid()
plt.show()


###GRAFICI A BARRE
#barre affiancate
import numpy as np
indexs=np.arange(6)
width=0.3   #larghezza delle barre
print(indexs)
plt.bar(indexs,y1, label="italiani", width=width,color="red")
plt.bar(indexs+width,y2, label="francesi", width=width, color="#212121")    #indexs+width per affiancarle
plt.title("nome del grafico")
plt.xlabel("eta")
plt.ylabel("valori")
plt.legend()
plt.xticks(indexs+width/2,x)  #sposto il valore dell'indice in centro tra le due barre
plt.show()

#barre orizzontali
plt.barh(indexs,y1, label="italiani",color="red") 
plt.show()

#DIAGRAMMA A TORTA
slices=[60,40,50,30,10]
labels=["si","no","forse","non so","preferisco non dire"]
colors=["red","brown","orange","green","blue"]
explode=[0,0,0,0,0.1]   #per evidenziare preferisco non dire
plt.pie(slices,labels=labels, wedgeprops={"edgecolor":"#000000"}, startangle=180,explode=explode, autopct="%1.1f%%") #inserisco colori bordi e giro il grafico
plt.title("nome grafico")
plt.show()

import numpy as np
###GRAFICO A LINEE RIEMPITO
x=[25,26,27,28,29,30]
y=[80,150,170,130,140,190]
media=140   #per colorarele aree sopra o sotto la media
plt.plot(x,y)
plt.fill_between(x,y,media, color="blue",alpha=0.4)   #alpha riduce lintensita del colore di riempimento
plt.title("nome del grafico")
plt.show()

x=np.array([25,26,27,28,29,30]) #trasformo in array per aggiungere la condizione di y
y=np.array([80,150,170,130,140,190])
media=140   #per colorarele aree sopra o sotto la media
plt.plot(x,y)
plt.fill_between(x,y,media,where=(y > 150),color="blue",alpha=0.4, interpolate=True)    #alpha riduce lintensita del colore di riempimento
plt.title("nome del grafico")
plt.show()

from turtle import color
###HISTOGRAMS
x=[13,18,18,22,25,27,29,29,30,35,36,37,40,41,45,45,54,56,65]
bins=[10,20,30,40,50,60,70]    #creiamo fasce d'età
plt.hist(x,bins=bins, color="grey",edgecolor="black")  #bins=6 categorie:teen-20enni-30enni-40enni-50enni-60enni
plt.axvline(27, color="red",linewidth="3")
plt.title("nome del grafico")
plt.show()


###SCATTERPLOT (a dispersione)
plt.style.use("ggplot") #tiene la griglia allo sfondo del grafico

x=[1,5,6,8,3,2,2,7,9,1]
y=[8,8,4,6,2,7,1,3,1,7]
plt.scatter(x,y, s=200,c="green",edgecolor="purple", linewidths=30, alpha=0.5)     #s=size of punti,  marker="x"
plt.scatter(x,y, s=200,c="green",edgecolor="purple", linewidths=3)  
plt.title("nome grafico")
plt.show()

x=[1,5,6,8,3,2,2,7,9,1]
y=[8,8,4,6,2,7,1,3,1,7]
colors=[2,4,5,3,7,9,5,1,6,8]    #diversi colori
sizes=[20,400,60,600,100,90,45,60,300,75] #cambiare dimensione dei punti
plt.scatter(x,y, s=sizes,c=colors, cmap="Greens")   
cbar=plt.colorbar()
cbar.set_label("Intensita")  
plt.title("nome grafico")
plt.show()


###DATE
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates

plt.style.use("ggplot")
x=[
    datetime(2022,1,10),
    datetime(2022,1,15),
    datetime(2022,1,20),
    datetime(2022,1,25),
    datetime(2022,1,30)
]
y=[3,6,2,8,5]
plt.plot_date(x,y,linestyle="solid")
plt.gcf().autofmt_xdate()  #get current figure =tutta la finestra attuale, fai un format date
date_formattate=mpl_dates.DateFormatter("%d %B %Y") #day month year
plt.gca().xaxis.set_major_formatter(date_formattate)   #get current axis
plt.title("nome grafico")
plt.show()


###LAVORO CON I SUBSETS
plt.style.use("ggplot")
#pi grafici nella stessa finestra
fig, (ax1,ax2)=plt.subplots(nrows=2,ncols=1,sharex=True)      #figure è la finestra, axis è il grafico  #sharex true tiene gli indici solo sualla asse x del grafico 2
x=[1,2,3,4,5]
y=[3,6,7,2,5]

ax1.plot(x,y)
ax1.set_title("nome del grafico")   #ne basta uno per il tipo di visualizzazione
ax2.plot(x,y)
ax2.set_xlabel("prova")
plt.show()

#piu finestre
fig, (ax1a,ax1b)=plt.subplots(nrows=2,ncols=1,sharex=True)  
fig, (ax2a,ax2b)=plt.subplots(nrows=2,ncols=1,sharex=True) 
x=[1,2,3,4,5]
y=[3,6,7,2,5]

ax1a.plot(x,y)
ax1a.set_title("nome del grafico")  
ax1a.set_xlabel("prova")
ax1b.plot(x,y)
ax1b.set_xlabel("prova")

ax2a.plot(x,y)
ax2a.set_title("nome del grafico")  
ax2a.set_xlabel("prova")
ax2b.plot(x,y)
ax2b.set_xlabel("prova")

plt.show()