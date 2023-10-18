###PROGRAMMAZIONE AD OGGETTI
#CLASSI ED OGGETTI
#programazioni ad oggetti: prende oggetti ed entità del mondo reala e le trasforma nel programma
    #creare rappresentazioni programmate da cui possiamo ricavare degli oggetti

class Persona:
    nome="luca"
    cognome="rossi"
persona1=Persona() #dallo stesso stampo creiamo due persone
persona2=Persona()
#la classe è oggetto (non stringa), dell'istanza persona
#l'istanza persona è prodotta dallo stampo oggetto classe

print(persona1.nome)

#costruttore
class Persona:
    def __init__(self, nome, cognome):  #costruttore: prende i parametri assegnati 
        self.nome =nome     #self ci aiuta a capire di che istanza stiamo parlando(persona1 o persona2)
        self.cognome=cognome
    def saluta(self):
        print("ciao sono "+self.nome)
persona1= Persona("luca", "rossi")
persona2=Persona("marco","verdi") #due istanze diverse di persona

persona2.saluta()
persona2.nome="maria"
persona2.saluta()

del persona2.nome


##EREDITARIETA'
#riguarda tutto cio che le classi che vengono da altre classi ereditano

#una classe figlia eredita tutte le caratteristiche della classe mardre + estensioni delle sue proprietà
class Persona:
    def __init__(self,nome,cognome):
        self.nome =nome
        self.cognome =cognome
    def saluta(self):
        print("ciao sono "+self.nome) 
    
class Insegnante(Persona):
    pass  #da per buono, quindi insegnante deriva da persona

persona1= Persona("luca", "rossi")  
insegnante1= Insegnante("anna","neri")

insegnante1.saluta()


class Persona:
    def __init__(self,nome,cognome):
        self.nome =nome
        self.cognome =cognome
    def saluta(self):
        print("ciao sono "+self.nome) 
    
class Insegnante(Persona):
    def __init__(self,nome, cognome):
        Persona.__init__(nome,cognome)
#oppure
class Insegnante(Persona):
    def __init__(self, nome, cognome):
        super().__init__(nome, cognome)  #uso un costruttore che eredita
            #sopra a livello gerarchico c'è persona, quindi gli mando nome e cognome

#overriding:
#qualsiasi funzione con lo stesso nome verrà sovrascritta.

persona1=Persona("luca","rossi")
insegnante1=Insegnante("anna","neri")

insegnante1.saluta()

#proprietà esclusive della classe figlia
class Persona:
    def __init__(self,nome,cognome):
        self.nome =nome
        self.cognome =cognome
    def saluta(self):
        print("ciao sono "+self.nome) 
    
class Insegnante(Persona):
    def __init__(self, nome, cognome,materia):
        super().__init__(nome, cognome)  #il super, cioè persona, non ha materia
        self.materia=materia
    def saluta(self):
        print("buongiorno sono "+self.nome+" "+self.cognome)
    def dai_voto(self):
        print("bravo, 8")

persona1=Persona("luca","rossi")
insegnante1=Insegnante("anna","neri","matematica")

insegnante1.saluta()
insegnante1.dai_voto()


