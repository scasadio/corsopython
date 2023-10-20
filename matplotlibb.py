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