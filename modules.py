###MODULI
#è un file esterno contenente un insieme di funzioni o variabili che vogliamo includere nel nostro programma

import modulo
modulo.saluta("luca")

x=modulo.persona1["cognome"]
modulo.saluta(x)

#creare un alias
import modulo as mo
x=mo.persona1["nome"]
mo.saluta(x)

import platform #gia in python
x=platform.system()
print(x)


import math #gia in python
print(math.floor(2.9)) #arrotonda per difetto
#alcune funzioni aritmetiche non sono disponibile se non viene importato math

from modulo import persona1
print(persona1["nome"])


###MODULO MATH
#funzioni built-in mi maax abs pow #####vedi main
import math
#sqrt
#ceil : arrotronda per eccesso
#floor  #arriotonda per difetto
#pi #pi greco

print(dir(math)) #tutte le funzioni


###JSON
#dati convertibili in json
    #dict
    #list
    #tuple
    #string
    #int
    #float
    #True
    #False
    #None

import json
x='{"nome":"luca","cognome":"rossi","eta":25}'
y=json.loads(x)
print(y["nome"])

x={
    "nome":"luca",
    "cognome":"rossi",
    "eta":25,
    "isOnline":False,
    "interessi":["calcio","basket"],
    "monete":4.56,
    "fidanzata":None
}
y=json.dumps(x, indent=2, separators=(", ",": "),sort_keys=True)  #scaricare  #, tra le righe #tra riga e valore  #sort_keys= ordine alfabetico
print(y)