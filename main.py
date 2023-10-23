###VARIABILI (min 20)
#-cos'è una variabile? contenitore di un valore
x=5

#-nomenclatura = regole per definire una variabile 
    #snakecase:  nome_var
    #camelcase:  nomeVar
    #pascalcasa:  NomeVar

#-assegnare multipli valori
x,y,z=32,100,987
print(x)
print(y)
print(z)
print(x,y,z)

#unpacked di una collection
#lista = []:
citta = ["roma","milano","napoli"]
x,y,z= citta
print(x,y,z)

#-utilizzare una variabile
x=32
y=8
z=x+y+x+x
print(z)


###TIPI DI DATI(min 30)
#per capire il tipo di dato
x=5
print(type(x))
#str: x="ciao"   STRINGA
#int: x=20      INTERO
#float: x=20.5      CON VIRGOLA
#bool: x=True       BOLEANO= True False
#list: x=["roma","milano","napoli"]     LISTA: data collection
#tuple: x=()"roma","milano","napoli")    TUPLA
#range: x=range(6)      RANGE DA 0 A 5
#dict: x={"nome":"Luca", "eta":25}      DIZIONARIO: rapporto chiave-valore
#set: x={"roma","milano","napoli"}


###CASTING: prendere il valore di una variabile e convertire il suo type (min 40)
x="5"
y=5

#riportano due errori diversi
    #print(y+x) #unsopported
    #print(x+y) #can only concatenate

x="ciao sono"
y="luca"
    #print(x+y) #concatenazione delle due stringhe

x=float(5)
print(x) #5.0


###STRIGHE (min 46)
x="1234"
print(x[0])  #=1

for carattere in "computer":
    print(carattere)

x="ciao sono luca"
print(x[4])  #ritorna lo spazio
print(len(x)) #ci sono 15 caratteri ma va da 0 a 14
print(x[:3]) #cia ,la 3 posizione NON è compresa
print(x[2:]) #ao sono luca ,la 2 posizione è compresa 
print(x[-4]) #l , 4 posizione a partire dalla fine
print(x[-4:])  #luca ,dalla 4 posizione in avanti compresa
print(x.upper())  #CIAO SONO LUCA
print(x.lower())
x=" ciao sono luca "
print(x.strip())  #toglie lo spazio davanti e in fondo
print(x.replace("o","W")) #ciaW sWnW luca
print(x.split(","))     #["ciao","sono","luca"]

#si possono usare """  """ per identificare una stringa multiline


#combinare stringhe e numeri 
x=23
y=65
z=1.7
prova= "ciao sono luca e sono nato il {},peso {}, sono alto {}"
print(prova.format(x,y,z))

#backslash
prova= 'sono alla ricerca dell\'amore'
prova= "ciao sono luca e sono \"figo\""
print(prova)


#FORMATTAZIONE STRINGA
peso=65
altezza=176
eta=25
frase= "ciao sono luca, ho {} anni, peso {} e sono alto {} cm"
print(frase.format(eta,peso,altezza))

frase= "ciao sono luca, ho {0} anni, peso {1} e sono alto {2} cm, e faccio {0}"
print(frase.format(eta,peso,altezza))

frase= "ciao sono luca, ho {eta} anni, peso {peso} e sono alto {altezza} cm"
print(frase.format(eta=eta,peso=peso,altezza=altezza))



###BOOLEAN
#False:
    #bool(False)
    #bool(none)
    #bool(0) 
    #bool("")   #stringa vuota
    #bool(())
    #bool([])
    #bool({})   #list, tuple e set vuoi 

if 5<10:
    print("sono minore di 10")
else:
    print("sono maggiore di 10")

x=0
y=1
print(bool(x)) #False
print(bool(y)) #True

lista_spesa=["limone","pane","carote"]
if lista_spesa:
    print("andare al supermercato")
else:
    print("non andare al supermercato")



###OPERAZIONI
#operatori aritmetici
#+
#-
#*
#/
#% modulo, ci da il resto della division
#** potenza
#// floor division, risultato della divisione arrotondato per difetto

x=5
y=9
print(x%y)
print(x**3)
print(x//y)

#operatori di assegnamento
x+=2
x-=2
x*=2
x/=2
x%=2
x//=2
print(x)   #5+2

#metodi (min 1h24)
x=min(5,10,25)
x=max(5,10,25)
x=abs(-5)
x=pow(5,2)  #5^2
print(x)
