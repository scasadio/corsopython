#JAVASCRIPT OBJECT NOTATION
#formato leggero per salvare e trasportare dati
#usato per scambiare dati tra server e pagine web

#SINTASSI
#i dati sono mostrati come coppie chiave-valore
#tutti i nomi delle chiavi devono essere contenuti in " "
#i dati sono saparati da un avirgola
#[] rappresentano gli array
#{} rappresentano gli oggetti

#TIPI DI DATI
    #string
    #number
    #object
    #array
    #boolean
    #null

#trasforma json in oggetto javascript per poterci lavorare


#conversions to know
#dict                      |object
#list,tuple                |array
#str                       |string
#int,long,float            |number
#True                      |true
#False                     |false
#None                      |null

import json

file="utente.json"
with open (file,"r") as json_file:
    data=json.load(json_file)
    name_data=(data["info"])
    for i in name_data:
        name=(i["nome"])
        ident=(i["id"])
        print(f"{name} is {ident}")