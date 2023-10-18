###TRY EXCEPT
#try: permette di testare un blocco di codice
#excep: raccoglie l'errore generato in try
#finally: permette di eseguire un altrotipo di codice una volta fatti try e except

try:
    print(x)
except:
    print("c'è stato un errore")

try:
    print(x)
except:
    pass
#cosi lo schippa e non ritorna nulla


x=5
try:
    print(x+"ciao")     #l'errore è che non si possono concatenare numero e stringa in questo modo
except NameError:
    print("x non definita")
except:
    print("non è un name error")
else:
    print("nessun porblema")

x=5
try:
    print(x)    
except NameError:
    print("x non definita")
except:
    print("non è un name error")
else:
    print("nessun porblema")  #manda a schermo se va tutto bene
finally:
    print("finally")  #manda a schermo a prescindere da se va tutto bene o no

x=-1
#if x<0:
    #raise Exception("numero minore di 0")
#ritorna un errore che lanciamo noi, creiamo un errore se x è minore di 0



###USER INPUT
x=input("cosa vuoi fare")
print(x)


#creare una tupla operazioni
persona={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25
}

operazioni=("aggiungere","modificare","eliminare")

def start():
    operazione=input("cosa vuoi fare? ")
    if operazione==operazioni[0]:
        x=input("aggiungi chiave:valore separati da una virgola: ")
        aggiungi(x.split(","))
    elif operazione==operazioni[1]:
        pass
    elif operazione==operazioni[2]:
        pass

def aggiungi(param):
    chiave=param[0]
    valore=param[1]
    persona[chiave]=valore
    print(persona)

while True:
    start()




###LAVORARE CON I FILE
#introduzione al file handling
    #r-Read: apre il file per leggerlo, errore se non esiste
    #a-Append:apre il file per appendere in fondo, crea il file se non esiste
    #w-Write:apre il file per scrivere, crea il file se non esiste
    #x-Create:crea il file, errore se esiste

f=open("testo.txt","r")
print(f.read())

print(f.read(5))   #mostra primi 5 caratteri
print(f.readline())   #mostra la prima righa

f=open("testo.txt","a")
f.write("dentro scriviamo quello che vogliamo")
f.close()
f=open("testo.txt")
print(f.read())

testo = f.read()

f=open("prova.txt","w")

import os
os.remove("testo.txt")

if os.path.exists("prova.txt"):
    os.remove("prova.txt")
else:
    print("non eisste un file con questo nome")

os.rmdir("prova")  #elimina una cartella