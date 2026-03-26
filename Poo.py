#structure try/except
"""try:
    x=int(input("Entrer un nombre:"))
    print("le carre de",x,"est",x**2)
except ValueError:
    print("Erreur:vous  devez  entrer un nombre entier")"""
"""try:
    f=open("data.txt")
    contenu=f.read()
except FileNotFoundError:
    print("fichier non trouvé")
else:
    print("la lecture réussie:",contenu)
finally:
    print("fichier fermé")"""
"""class personne:
    def __init__(self,nom,age):
        self.nom=nom
        self.age=age
p=personne("Alice",25)
print(p.nom)
print(p.age)"""
class voiture:
    def __init__(self,couleur):
        self.voiture=couleur
    def demarrer(self):
        print("la voiture",self.voiture,"démarre!")
    def arreter(self):
        print("la voiture",self.voiture,"s'arrête!")
    def freiner(self):
        print("la voiture",self.voiture,"freiner!")
v=voiture("rouge")
v.demarrer()
v.arreter()
v.freiner()
print(".........................")
class moto:
    def __init__(self,marque):
        self.moto=marque
    def demarrer(self):
        print("la moto",self.moto,"démarre!")
    def arreter(self):
        print("la moto",self.moto,"s'arrête!")
    def freiner(self):
        print("la moto",self.moto,"freiner!")
v=moto("TOYOTA")
v.demarrer()
v.arreter()
v.freiner()
    
        
    
