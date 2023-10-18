### IF ELSE (min 1h26)
#operatori di comparazione
#== uguale
#!= diverso
#>=
#<=

#opertori logici
#_and
#_or
#_not

x=11
if x<10:
    print("minore")
elif x==10:
    print("uguale")
else:
    print("maggiore")

x=11
y=5
if x>10 and y>10:   #entrambe vere
    print("condizione veificata")
else:
    print("condizione non verificata")

if x>10 or y>10:      #almeno una delle due vera
    print('condizione verificata')
else:
    print("condizione non verificata")


if not(x< 10):  #not(false)
    print("condizione verificata")
else:
    print("condizione non verificata")

#versione short hand
if x>10: print("maggiore") #funziona solo con un singolo statement (quindi una sola riga di codice successiva a :)
print("maggiore") if x>10 and y<10  else print("minore")

#if nested
if x %2 == 0:
    print("numero pari")  #so che un numero pari diviso per due da resto 0 quindi %=0
else:
    print("numero dispari")

if x%2==0:
    if x>10:
        print("numero pari e maggiore")
else:
    print("numero dispari")


###WHILE LOOP (min 1h50)
x=["roma","milano","napoli"]
i=0
while i<6:  #il ciclo continua finchè la condizione è verificata
    print(i)
    i+=1

#break
i=0
while i<6:
    print(i)
    if i==3:
        break
    i+=1

#continue
i=0
while i<6:
    i+=1
    if i==3:
        continue  #passa alla prossima iterazione, salta i==3
    print(i)
else:
    print("finito")


###FOR LOOP
lista_citta=["roma","milano","napoli"]
for citta in lista_citta: #per ogni elemento in collezione di elementi
    print(citta)

stringa="anguria"
for lettera in stringa:
    print(lettera)

for x in range(6):
    if x==3:
        continue
    print(x)
else:
    print("finito")


for riga in range(6):
    for colonna in range(2):
        print("("+str(riga)+":"+str(colonna)+")")


###INTRODUZIONE ALLE COLLEZIONI DI DATI (min 2h13)
#una collezione di valori che fa riferimento ad una variabile
#spiegazione termini:
    #ordinato: la collezione ha un ordine ben definito e l'aggiunta di elementi incide
    #indicizzato: possiamo accedere agli elementi tramite indice
    #modificabile: possiamo aggiungere, cambiare e rimuovere elementi una volta creata la collezione
    #immutabile: non possiamo aggiungere, cambiare e rimuovere elementi
    #permete duplicazioni: possono esserci più elementi con lo stesso valore

citta=["udine","roma","milano","napoli","venezia"] #ordinato, se aggiungo elementi cambia l'indice della posizione 

#le liste sono collezioni ordinate (e quindi indicizzati), modificabili, permettono duplicati
#le tuple sono collezioni ordiate, immutabili, permettono duplicati
#i set sono collezioni non ordinate e percio non indicizzate, non permettono duplicati
#i dictionary sono collezioni ordinate e modificabili, non permettono duplicati.


