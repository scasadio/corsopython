####
##EX.1
#scrivi un porgramma che legga il contenuto di un file di testo e lo stampi a schermo
with open("es_prova.txt","r") as file:
    contenuto=file.read()

print(contenuto)


##EX.2
#scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file
with open("es_prova.txt","r") as file_origine:
    contenuto=file_origine.read()
with open("es_copia.txt","w") as file_destinazione:
    file_destinazione.write(contenuto)


##EX.3
#scrivi un programma che chieda all'utente di inserire una stringa, quindi scriva la stringa in un file di testo
stringa=input("inserisci una stringa: ")
with open("es_copia.txt","w") as file:
    file.write(stringa)

##EX.4
#scrivi un porgramma che conti le righe di testo
with open("es_prova.txt","r") as file:
   num_righe=0
   for riga in file:
       num_righe+=1
print(f"il file ha {num_righe} righe")


##EX.5
#scrivi unporgramma che legga il contenuto di un file csv(valori separati da virgola) e lo stampi a schermo a forma di tabella
import csv
with open("es_prova.csv","r") as file:
    contenuto=csv.reader(file)
    for riga in contenuto:
        print("|".join(riga))


##EX.6
#scrivi un programma che chieda all'utente di inserire i valori di una tabella in formato csv(valori separati da virgola),
#quindi scriva i valori in un file csv
import csv
valori=[]
while True:
    valore=input("inserisci valore(digita fine per terminare): ")
    if valore == "fine":
        break
    valori.append(valore)
# with open("es_prova.csv","w") as file:
#     contenuto=csv.writer(file)
#     contenuto.writerow(valori)          #sovrascrive in es_prova.csv

##EX.7
#scrivi un programma che legga il contenuto di un file di testo e lo copi in un altro file, invertendo l'ordine delle righe
with open("es_prova.txt","r") as file_origine:
    righe=[]
    for riga in file_origine:
        righe.append(riga)

with open("es_copia.txt", "w") as file_destinazione:
    for riga in reversed(righe):
        file_destinazione.write(riga)