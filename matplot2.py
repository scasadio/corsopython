from matplotlib import pyplot as plt
###GRAFICO A LINEE RIEMPITO
x=[25,26,27,28,29,30]
y=[80,150,170,130,140,190]
plt.plot(x,y)
plt.fill_between(x,y, color="blue")
plt.title=("nome del grafico")
plt.show()