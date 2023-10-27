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

##
x='{"name":"luca","age":25,"citta":"bologna"}'
y=json.loads(x)

print(y["age"])

###CONVERT FROM PYTHON TO JSON
x={
    "name":"luca",
    "cognome":"rossi",
    "eta":25,
    "citta":"bologna"
}
y=json.dumps(x,indent=1) 
print(y)        #ritorna il dict in formato json con 1 indentazione



file="utente.json"
with open (file,"r") as json_file:
    data=json.load(json_file)
    for utente in data["utenti"]:
        if utente["id"]=="555":
            for numero in utente["recapiti"]["telefono"]:
                if numero["tipo"]=="ufficio":
                    telefono_uff=numero["numero"]
                    print(telefono_uff)

file="utente.json"
with open (file,"r") as json_file:
     data=json.load(json_file)
     utenti=data["utenti"]
     for i in utenti[0]["recapiti"]["telefono"]:
         if i["tipo"]=="ufficio":
             print(i["numero"])

  
# z=json.dumps(data,indent=3, separators=(". "," = "), sort_keys=True)    #sostiutiamo le , con i . e i : con =
# print(z)                                                                #e ordiniamo in ordine alfabetico

##aggiungo un nuovo utente al file

utente2={
    "id":"777",
    "nome":"anna",
    "cognome":"bianchi",
    "codiceFiscale":"BNCNNA93R43D199P",
    "sposato":True,
    "online":True,
    "eta":30,
    "indirizzo":{
        "via":"via maggiore 16",
        "citta":"bologna",
        "provincia":"BO",
        "codicePostale":48126
    },
    "recapiti":{
        "email":[{
            "tipo":"personale",
            "mail":"poiuyt@gmail.com"
        },
        {
            "tipo":"istituzionale",
            "mail":"anna.bianchi30@studio.unibo.it"
        }],
        "telefono":{
            "tipo_cell":"cellulare",
            "numero":"9987654321"
        }
    },
    "amici":[{
        "nome":"lucia",
        "cognome":"neri"
    },
    {   
        "nome":"matilde",
        "cognome":"fucsia"
    }]
}

with open (file,"r") as json_file:
     data=json.load(json_file)
     data["utenti"].append(utente2)



###############
with open(file,"w") as json_file:
    json.dump(data,json_file,indent=3)
import json
gen="generated.json"
with open (gen,"r") as json_file:
    file=json.load(json_file)

data=json.dumps(file,indent=4, sort_keys=True)    #sostiutiamo le , con i . e i : con =
print(data)   


import json
luca="lucaRossi.json"

with open (luca,"r") as json_file:
    data=json.load(json_file)

for key,value in data.items():
    # print(f'{key} : {value}')
    if key=="amici":
        print(value)


file="utente.json"
with open (file,"r") as json_file:
    data=json.load(json_file)
dati=data["utenti"]
data=dati[0]
print(data)


for key,value in data.items():
    # print(f'{key} : {value}')
    if key=="amici":
        print(value)




########esercizio
log='157.245.75.203 - - [24/Oct/2023:02:04:23 +0200] "GET /robots.txt HTTP/1.0" 404 4997 "-" "SafeDNSBot (https://www.safedns.com/searchbot)"'

ip=log[0:14]
Timestamp=log[20:46]
Verbo_Http=log[49:52]
risorsa=log[54:64]
versione=log[65:73]

print(ip)
print(Timestamp)
print(Verbo_Http)
print(risorsa)
print(versione)


substring=log[49:73]
parole=substring.split(" ")
print(parole)

Verbo_Http=parole[0]
risorsa=parole[1]
versione=parole[2]

