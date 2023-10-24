########
###FUNCTIONS
#blocco di codice riutilizzabile con all'interno delle istruzioni da eseguire ogni volta che la funzione verrà richiamata

def fai_la_pasta():
    print("metti l'acqua")
    print("fai bollire")
    print("metti la pasta")

fai_la_pasta() #ogni volta che la richiamo ritorna sempre le stesse funzioni

#definiamo dei parametri
#parametro=tipo_pasta

def fai_la_pasta(tipo_pasta, metti_sugo):
    print("metti l'acqua")
    print("fai bollire")
    print("metti "+ tipo_pasta)
    if metti_sugo:
        print("prepra sugo")

    #parametro= variabile generica che utilizzaimo nella difinizione della variabile (tipo pasta)
    #argomento= valore effittivo che usiamo quando richiamiamo la funzione (spaghetti)
fai_la_pasta("spaghetti",True) #true inserisce prepara sugo


#arbitrary arguments:
#argomenti da gestire quando non sappiamo quanti parametri vogliamo inserire
def fai_la_pasta(*opzioni):  #non so quanti sono 'opzioni' ma sono da gestire come segue
    print("metti l'acqua")
    print("fai bollire")
    print("metti "+ opzioni[0])
    if opzioni[1]:
        print("prepra sugo")

fai_la_pasta("spaghetti",True) #true inserisce prepara sugo


def fai_la_pasta(**opzioni):  #non so quanti sono 'opzioni' ma sono da gestire come segue
    print("metti l'acqua")
    print("fai bollire")
    print("metti "+ opzioni["tipo"])
    if opzioni["sugo"]:
        print("prepra sugo")

fai_la_pasta(tipo="spaghetti",sugo=True, posate="forchetta") #true inserisce prepara sugo


def fai_la_pasta(tipo_pasta, sugo):  #non so quanti sono 'opzioni' ma sono da gestire come segue
    print("metti l'acqua")
    print("fai bollire")
    print("metti "+ tipo_pasta)
    if sugo:
        print("prepara sugo")

fai_la_pasta(sugo=True, tipo_pasta="fusilli") #abbiamo inserito una combinazione chiave valore (tipo_pasta - fusilli, sugo - true)


#parametri di default
def fai_la_pasta(tipo_pasta="spaghetti", sugo=True): 
    #spaghetti sono il parametro di default
    #se viene definito un altro tipo pasta allora cambia, ma se non è specificato nulla: spaghetti
    print("metti l'acqua")
    print("fai bollire")
    print("metti "+ tipo_pasta)
    if sugo:
        print("prepara sugo")

fai_la_pasta()
fai_la_pasta("fusilli", False)
#è stato deciso per i fusilli in bianco anche se di default si sarebbero preparati spaghetti al sugo

#return dei valori
def fai_somma(num1, num2):
    somma= num1+num2
    return somma

x=fai_somma(2,2)
print(x)

#We use the k variable as the data, which decrements (-1) every time we recurse. 
#The recursion ends when the condition is not greater than 0 (i.e. when it is 0).
#A function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)
# 1     =1+0
# 3     =2+1
# 6     =3+2+1
# 10    =4+3+2+1
# 15
# 21    =6+5+4+3+2+1


#########
###LAMBDA FUNCTION
#esegue l'espressione e ritorna il risultato
x = lambda a : a + 10
print(x(5)) 

x = lambda a, b : a * b
print(x(5, 6))

def funzione(n):
  return lambda a : a * n

y=funzione(3)       #3 è n
z=funzione(5)
print(y(7))     #7 è a
print(z(7))



########
###SCOPE:
#è la disponibilà della variabile nel nostro codice
#scope locale: porzione del codice in cui la variabile è disponibile all'interno della funzione
def funzione():
    x=400
    #print(x)
    return x  #senza return la variabile è locale e non esce dalla funzione

x=funzione()
print(x)  #output= 400 della funzione e 400 del return


def funzione():
    x=400
    def sottofunzione():
        print(x)
    sottofunzione()

#x è disponibile anche nella sottofunzione perche è attiva in scope locale della funzione
funzione()

#scope globale: nel codice fuori funzione e valgono sia dentro sia fuori funzione
x=400
def funzione():
    print(x)
funzione()

#keyword globale
x=400
def funzione():
    x=100   
    print(x)
funzione()  #manda a schermo x=400
print(x)    #manda a schermo x=100

x=400
def funzione():
    global x    #questa fa riferimento alla x globale, non è una cosa diversa  
    x=100   #siccome ho inserito il global, viene cambiata la x fuori 
    print(x)
funzione()  #manda a schermo x=100
print(x)    #manda a schermo x=100






###DATE
#parametri formattzazione data
 #%a  giorno della settimana, abbreviato                                                                  |Mon
 #%A  giorno della settimana, intero                                                                      |Monday
 #%w numero del giorno della settimana da 0 a 6, dove 0 è Sunday                                          |1
 #%d numero del giorno del mese da 1 a 31                                                                 |16 
 #%b nome del mese abbreviato                                                                             |Oct
 #%B nome del mese intero                                                                                 |October
 #%m numero del mese da 1 a 12                                                                            |10
 #%y anno abbreviato                                                                                      |23
 #%Y anno intero                                                                                          |2023
 #%H ora da 00 a 23                                                                                       |12
 #%I  ora da 00 a 12                                                                                      |12
 #%p AM/PM                                                                                                |AM
 #%M minuti da 00 a 59                                                                                    |20
 #%S secondi da 00 a 59                                                                                   |45
 #%f microsecondi da 000000 a 999999                                                                      |882419
 #%z UTC offset                                                                                           |+0100
 #%Z Time zone                                                                                            |CST
 #%j numero del giorno nell'anno da 001 a 366                                                             |289
 #%U Numero della settimana dell'anno, domenica è il primo giorno della settimana, da 00 a 53             |42
 #%W Numero della settimana dell'anno, lunedì è il primo giorno della settimana, da 00 a 53               |42
 #%c versione locale di data e ora                                                                        |Mon Oct 16 12:20:45 2023
 #%x versione locale della data                                                                           |10/16/23
 #%X versione locale dell'ora                                                                             |12:20:45


import datetime
x=datetime.datetime.now()
x=datetime.datetime(2012,6,13) #esempio data a caso
print(x)

#strftime
x=datetime.datetime.now()   
print(x.strftime("%A %d-%B %Y"))  



