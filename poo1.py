"""class animal:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
    def parler(self):
        print(self.nom,"viens ici",self.age,"ans")
    def manger(self):
        print(self.nom,"le mangé est prêt",self.age,"ans")
p=animal("Dog",5)
p.parler()
p.manger()"""

"""class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

class Bibliotheque:
    def __init__(self):
        self.livres = []   

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for livre in self.livres:
                print(f"{livre.titre} - {livre.auteur}")


livre1 = Livre("1984", "George Orwell")
livre2 = Livre("L'Étranger", "Albert Camus")

biblio = Bibliotheque()   # instanciation correcte

biblio.ajouter_livre(livre1)
biblio.ajouter_livre(livre2)

biblio.afficher_livres()"""

"""class etudiant:
    def __init__(self,nom,age,note):
        self.nom=nom
        self.age=age
        self.note=[]
    def ajouter_note(self,note):
        self.note.append(note)
    def afficher_note(self):
        print(self.nom,"a les notes suivantes:",self.note)
    def moyenne(self):
        if self.note:
            moyenne=sum(self.note)/len(self.note)
            print("La moyenne de",self.nom,"est:",moyenne)
        else:
            print(self.nom,"n'a aucune note.")
e=etudiant("Alice",20,[])
e.ajouter_note(15)
e.ajouter_note(18)
e.afficher_note()
e.moyenne()"""
"""class voiture:
    def __init__(self,marque,model,kilometrage=0):
        self.marque=marque
        self.model=model
        self.kilometrage=kilometrage
    def rouler(self,km):
        self.kilometrage+=km
        print("La voiture a roulé",km,"km. Kilométrage total:",self.kilometrage)
    def afficher_info(self):
        print("Marque:",self.marque)
        print("Modèle:",self.model)
        print("Kilométrage:",self.kilometrage)
v=voiture("Toyota","Corolla",150)
v.afficher_info()
v.rouler(150)
v.afficher_info()"""


class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self.titulaire = titulaire
        self.solde = solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"{montant} FCFA déposé. Nouveau solde: {self.solde} FCFA")
        else:
            print("Le montant doit être positif.")

    def retirer(self, montant):
        if montant > 0:
            if self.solde >= montant:
                self.solde -= montant
                print(f"{montant} FCFA retiré. Nouveau solde: {self.solde} FCFA")
            else:
                print("Fonds insuffisants.")
        else:
            print("Le montant doit être positif.")
    def afficher_solde(self):
        print(f"Titulaire: {self.titulaire}, Solde: {self.solde} FCFA")
compte = CompteBancaire("Jean Dupont", 1000)
compte.afficher_solde()
compte.deposer(500)
compte.retirer(200)
compte.afficher_solde()


    
    

 
        

        
        
        
        
        
    