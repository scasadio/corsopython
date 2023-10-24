########
### IF ELSE (min 1h26)
#operatori di comparazione
# Equals                    |a == b
# Not Equals                |a != b
# Less than                 |a < b
# Less than or equal to     |a <= b
# Greater than              |a > b
# Greater than or equal to  |a >= b

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

a = 10
b = 10
print("A") if a > b else print("=") if a == b else print("B")


#if nested
if x %2 == 0:
    print("numero pari")  #so che un numero pari diviso per due da resto 0 quindi %=0
else:
    print("numero dispari")

if x%2==0:
    if x>10:
        print("numero pari e maggiore")
    else:
        print("numero pari e minore")       #elif x<10:
else:
    print("numero dispari")


x=15
if x>10:
    print("maggiore 10"),
    if x>20:
        print("maggiore 20"),
    else:
        print("tra 10 e 20"),
else:
    print("minore 10")


x=23
if x>10:
    if x>20 and x%2==0:
        print("maggiore 20 e pari"),
    elif x>20 and x%2!=0:
        print("mggiore 20 dispari"),
    elif x%2!=0:
        print("tra 10 e 20 dispari"),
    else:
        print("tra 10 e 20 pari"),
elif x%2==0:
    print("minore 10 pari"),
else:
    print("minre di 10 dispari")


if x>10:
    if x>20:
        if x%2==0:
            print("maggiore 20 e pari")
        else:
            print("maggiore 20 dispari"),
    elif x%2==0:
        print("tra 10 e 20 pari"),
    else:
        print("tra 10 e 20 dispari"),
elif x%2==0:
    print("minore di 10 pari"),
else:
    print("minore 10 dispari")



######
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
    i+=1     #aumentando di uno in uno fino al 6 il ciclo si ferma al 3   

#continue
i=0
while i<6:
    i+=1
    if i==3:
        continue  #passa alla prossima iterazione, salta i==3
    print(i)
else:
    print("finito")



########
###FOR LOOP
lista_citta=["roma","milano","napoli"]
for citta in lista_citta: #per ogni elemento in collezione di elementi
    print(citta)

stringa="anguria"
for lettera in stringa:
    if lettera=="g":
        break
    print(lettera)

for x in range(6):
    if x==3:
        continue
    print(x)
else:
    print("finito")

for x in range(2,30,3):
    print(x)        #ritorna valori da 2 a 29 con salti di 3


for x in [0, 1, 2]:
    pass     #il pass evita che il ciclo vuoto ritorni un errore


#nested cicle
for riga in range(6):
    for colonna in range(2):
        print("("+str(riga)+":"+str(colonna)+")")
        #ritorna tutte le possibili combinazioni di riga:colonna 


