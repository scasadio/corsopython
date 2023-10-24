
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


#########
###LISTE (min 2h23)
#collezioni di dati ordinate e indicizzate, modificabili e permettono duplicati
#creare una una lista con tipi uguali o mischiati

x=["milano","roma","napoli","venezia"]

print(len(x))

x[0]="brescia" #cambio elemento 0
x[1:3]=["brescia","udine"]
x[1:3]=["brescia"] #accorpa i due valori in un unico brescia, non la duplica

#inserire elementi
x=["milano","roma","napoli","venezia"]
x.append("brescia") #inserisce sul fondo della lista
x.insert(1,"brescia") #inserisce brescia alla posizione 1, le altre slittano
y=["ciao",909, False]
x.extend(y)
print(x)

#rimuovere degli elementi
x.remove("milano") #rimuove il valore che assegno
x.pop() #rimuove dl fondo
x.pop(1) #rimuove la posizione 1
x.clear() #la lista c'è ma è vuota

print(x) 
del x #cacello tutta la lista

x=["milano","roma","napoli","venezia"]
for i in range(len(x)):
    print(x[i])

i=0
while i<len(x):
    print(x[i])
    i+=1

#shortcut
lista_citta=["milano","roma","napoli","venezia"]
[print(citta) for citta in lista_citta if citta!="roma"]

citta2 =["milano" for citta in lista_citta if citta!="roma"]
print(citta2) #per tutti i valori diversi da roma nella lista1, sostituisco milano

lista_citta.sort() #ordine alfabetico
lista_citta.sort(reverse=True)
print(lista_citta)

x=["milano","roma","napoli","venezia"]
y=x
y[0]="new york" #cambia anche x
print(x)

y=x.copy() #posso modificare solo y , oppure
y=list(x)

x=["milano","roma","napoli","venezia"]
y=["udine","bari"]
for citta in y:
    x.append(citta)

x.extend(y)
print(x)


######
###TUPLE (min 2h50)
#collezioni di dati ordinate, indicizzate, non modificabili, permettono duplicati

x=("milano","roma","napoli")
j=("milano",) #tupla con un solo valore devea vere la virgola

if "milano" in x:
    print(x) #verifica se l'elemento esiste

#costruttori list(), tuple()
y=list(x)
y[0]="venezia"
x=tuple(y)  #trasformzaione per modificare una tupla, non modificabile
print(x)

#unpack di una tupla
citta=("milano","roma","napoli","venezia")
(x,y,*z)=citta
print(x)
print(y)
print(z) #è una lista, considera gli elementi rimanenti che non vegono assegnati alle altre variabili

lista_citta=("milano","roma","napoli","venezia")
i=0
while i<len(lista_citta):
    print(lista_citta[i])
    i+=1

lista_citta=("milano","roma","napoli","venezia")
lista_citta2=("udine", "londra")
y=lista_citta + lista_citta2 #è una nuova tupla
print(y)

x=lista_citta.count("milano") #quante volte un elemento si ripete nella tupla
x=lista_citta.index("roma") #ritorna l'indice corrispondente al valore che voglio, se questo si ripete piu volte ritorna solo l'indice del primo
print(x)


#######
###SET
#collezioni di dati non ordinate, non indicizzate, non modificabili, non permettono duplicati
#possiamo pero aggiungere e rimuovere elementi

#operazioni su due set
# add(" ")	                        |Adds an element to the set
# union()	                        |Return a set containing the union of sets
# update()	                        |Update the set with the union of this set and others
# copy()	                        |Returns a copy of the set
# clear()	                        |Removes all the elements from the set
# pop(" ")	                        |Removes an element from the set
# discard(" ")	                    |Remove the specified item
# remove(" ")	                    |Removes the specified element
# difference()         	            |Returns a set containing the difference between two or more sets
# difference_update()	            |Removes the items in this set that are also included in another, specified set
# intersection()	                |Returns a set, that is the intersection of two other sets
# intersection_update()	            |Removes the items in this set that are not present in other, specified set(s)
# symmetric_difference()	        |Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	    |inserts the symmetric differences from this set and another
# isdisjoint()	                    |Returns whether two sets have a intersection or not
# issubset()	                    |Returns whether another set contains this set or not
# issuperset()	                    |Returns whether this set contains another set or not


x={"milano","roma","napoli"}
y=set(("milano","roma","napoli"))  #costruzione del set usando il costruttore
print(x) #continuando a fare print(), vengono visualizzati gli elementi in ordine diverso, in quanto non ordinati
#si puo accedere agli elementi del set solo tramite loop

print(len(x))
x.add("venezia") #aggiuge un elemento
y={"venezia","udine"}   
x.update(y) #aggiorna il set aggiungendo elementi
list=["kiwi","pesca"]
x.update(list) #gli elementi della lista diventano parte del set
x={"milano","roma","napoli"}
x.discard("udine")  #se l'elemento non esiste non ritorna nulla
x.remove("roma")  #funziona solo se l'elemento esiste, altrimenti da un errore
x.pop()  #ogni volta che lo rimandiamo cambia l'elemento che esclude
print(x)

del x

x={"milano","roma","napoli"}
y={"venezia","roma"} 

z=x.union(y)  #come update(), esclude gli elementi duplicati

z=x.intersection(y)  #nuovo set
x.intersection_update(y)  #aggiorna un set gia esistente

z=x.symmetric_difference(y) #nuovo set con tutto tranne quello che hanno in comune
x.symmetric_difference_update(y)  #set gia esistente con tutto tranne uno di quello che hanno in comune 

x = {"apple", "banana", "cherry", True}
y = {"google", 1, "apple", 2}
z = x.symmetric_difference(y)   #1 e true sono lo stesso valore quindi vengono esclusi

print(z)
print(x)

set={"milano","roma","napoli",True, 1, 2} #true e 1 sono considerati valori uguali, cosi come false e 0



######
###DICTIONARY (min 3h15)
#collezioni di dati ordinate, modificabili ma non perettono duplicati

persona ={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25
}

print(persona) #le chiavi non possono essere duplicate
print(persona["cognome"])
print(persona.get("nome"))      #due modi per richiamare il valore di una chiave

x=persona.keys()  #crea una lista con le chiavi del soggetto
x=persona.values() #per i valori
x=persona.items()  #crea una tupla con le coppie chiave-valore della persona

print(x)

print("yoyoyo" in persona) #per vedere se un chiave esiste nel dizionario

persona["nome"]="marco" #persona.update({"nome":"marco"})
print(persona)

#aggiungere una nuova chiave
persona["colore"]="blu"
persona.update({"colore":"nero"})   #siccome ho gia creato la chiave "colore"
print(persona)

persona.popitem()  #rimuove l'ultimo item
persona.clear()

persona ={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25
}
del persona["nome"]  #elimina solo il nome, se non specifico rimuove tutto il dic

#cicli
persona ={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25
}
for x in persona:
    print(x)    #ritorna le chiavi
for x in persona.keys():
    print(x)  

for x in persona:
    print(persona[x]) #ritorna i valori 
for x in persona.values():
    print(x)

for x,y in persona.items():
    print(x,y)      #ritora le coppie chiave-valore

x=persona.copy() #copia su cui possiamo lavorare
x=dict(persona)  #nuovo dict che prede i valori da persona

print(x)

#dict nested
persona ={
    "nome":"luca",
    "cognome":"rossi",
    "età":23,
    "eta":25,       #sovrascrive la precedente
    "indirizzo":{
        "città": "milano",
        "cap":"00000",
        "civico":45
    },
    "hobbies":["sport","leggere","musica"]
}
print(persona)