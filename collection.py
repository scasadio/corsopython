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


###SET
#collezioni di dati non ordinate, non indicizzate, non modificabili, non permettono duplicati
#possiamo pero aggiungere e rimuovere elementi

x={"milano","roma","napoli"}
y=set(("milano","roma","napoli"))  #costruzione del set usando il costruttore
print(x) #continuando a fare print(), vengono visualizzati gli elementi in ordine diverso, in quanto non ordinati
#si puo accedere agli elementi del set solo tramite loop

x.add("venezia") #aggiuge un elemento
y={"venezia","udine"}   
x.update(y) #aggiorna il set aggiungendo elementi
x={"milano","roma","napoli"}
x.discard("udine")  #se l'elemento non esiste non ritorna nulla
x.remove("roma")  #funziona solo se l'elemento esiste, altrimenti da un errore
x.pop()  #ogni volta che lo rimandiamo cambia l'elemento che esclude
print(x)

del x

#unire o aggiungere elementi
#union()
#update()
#intersection_update()
#intersection()
#symmetric_difference_update()
#symmetric_difference()

x={"milano","roma","napoli"}
y={"venezia","roma"} 

z=x.union(y)  #come update(), esclude gli elementi duplicati
x.intersection_update(y)  #aggiorna un set gia esistente
z=x.intersection(y)  #nuovo set
z=x.symmetric_difference(y) #nuovo set con tutto tranne quello che hanno in comune
x.symmetric_difference_update(y)  #set gia esistente con tutto tranne uno di quello che hanno in comune 
print(z)
print(x)



###DICTIONARY (min 3h15)
#collezioni di dati ordinate, modificabili ma non perettono duplicati

persona ={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25
}

print(persona) #le chiavi non possono essere duplicate
print(persona["cognome"])
print(persona.get("nome"))  
x=persona.keys()  #crea una lista con le chiavi del soggetto
x=persona.items()  #crea una tupla con le coppie chiave-valore della persona
x=persona.values() #per i valori
print(x)

print("yoyoyo" in persona) #per vedere se un chiave esiste nel dizionario

persona["nome"]="marco" #persona.update({"nome":"marco"})
print(persona)

persona ={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25
}

#aggiungere una nova chiave
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
    print(persona[x]) #ritorna i valori 
#oppure

for x in persona.values():
    print(x)

for x in persona.keys():
    print(x)  

x=persona.copy() #copia su cui possiamo lavorare
x=dict(persona)  #nuovo dict che prede i valori da persona

print(x)

#dict nested
persona ={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25,
    "indirizzo":{
        "città": "milano",
        "cap":"00000",
        "civico":45
    }
}
print(persona)