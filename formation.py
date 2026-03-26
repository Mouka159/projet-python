"""def dire_bonjour(name):
    print('bonjour:',name)
dire_bonjour('abalo')
dire_bonjour('gana')
dire_bonjour('nadege')"""

"""age=int(input('entrer votre age:'))
def dire_bonjour():
    if age>=18:
        print('vous etes majeur')
    else:
        print('vous etes mineur')
dire_bonjour()"""
"""
def calcul_moyenne(note1,note2):
    moyenne=(note1+note2)/2
    return moyenne
moyenne=calcul_moyenne(15,16)
if moyenne>=10:
        print("Admis")
else:
        print('Ajournée')"""
        
"""fruit=["banane","tomate","orange"]
print(fruit[0])
print(fruit[1])
print(fruit[2]) """

"""liste=[]
liste.append(10) 
liste.append(20)
liste.append("python")
liste.append("Moukaila")
print(liste)
liste.remove(10)
print(liste)
liste.pop(1)      
print(liste)"""

'''personne={
   "nom":"gana",
    "age":15,   
}
print(personne.get("nom"))'''


"""personne={"nom":"afi","age":14,"ville":"paris"}
for cle in personne.keys():
    #pacourir les cles
     print('clé',cle)
     
     
     #parcourir les valeurs
for valeur in personne.values():
        print('valeur',valeur)
        
        
        #parcourir les cles et les valeurs
for cle,valeur in personne.items():
    print(f"{cle}=>{valeur}") """
    
"""ensemble=set()
ensemble.add(2)
ensemble.add(3)
ensemble.add(4)
print(ensemble) 
ensemble.remove(2)
print(ensemble)
ensemble.discard(5)
print(ensemble)
ensemble.remove(7)
print(ensemble)"""

#verfier si un nombre est positif,negatif ou null
"""nbre=int(input('entrer un nombre:'))
if nbre>0:
    print('le nombre est positif')
elif nbre<0:
    print('le nombre est negatif')
else:
    print(' le nombre est null')"""
    
#trouver le maximum entrer deux nombre en utiisant la fonction max
"""nbre1=int(input('entrer le premier nombre:'))
nbre2=int(input('entrer la deuxieme nombre:'))
if nbre1>nbre2:
    print(f'{nbre1} est superieur a {nbre2}')
else:
    print(f'{nbre2} est superieur a {nbre1}')"""
    
 #somme des nombre de 1 a 100
"""somme=0
for i in range (1,100):
   somme=somme+i
   result=print(somme)"""
 
 #demander le nombre d etudiant et calculer la moyenne de chacun d'eux
"""nbre_etudiant=int(input("Combien d'étudiants voulez-vous enregistrer?"))
etudiants={}
for i in range(nbre_etudiant):
  nom=str(input(f"Entrer le nom de l'étudiant {i+1}:"))
  notes=[]
  for j in range(4):
      note=float(input(f"Entrer la note {j+1}:"))
      notes.append(note)
      etudiants[nom]=notes
print("\n-------Resultats---------")
for nom,notes in etudiants.items():
   moyenne=sum(notes)/len(notes)
   print(f"{nom} a une moyenne de:{moyenne:.2f}")"""
   
#
"""nbre=int(input("combien d'étudiant voulez-vous enregistrer?"))
etudiant={}
for i in range(nbre):
    nom=str(input(f"Entrer le nom de l'étudiant {i+1}:"))
    #etudiant.values(nom)
    notes=[]
    for j in range(4):
       note=int(input(f"Entrer la note {j+1}:"))
       notes.keys()
       for nom,notes in etudiant.items():
           print(f" {nom}=>{notes}")"""
           
#on presente les menu lorsque les repas existe il affiche le nom             
"""("----Menu deu restaurant----")
print("***les repas***")
print("pizza:8.5$")
print("bugger:10$")
print("salade:5$")
print("fruit de mer:15$")
print("ayimolou cuit a la vapeur:10$")
print("riz mouillé au jarbon:15$")
print("***les jus***")
print("jus aromatisé a sodabi:8.5$")
print("jus au larve de poisson:10$")
print("jus de raisin:5$")
print("jus de chias:8.5$")
print("jus de miel apanaché au vin de palme:10$")
print("jus vinsmatique:5$")

Menu={ 
    "pizza":8.5,
    "bugger":10,
   " salade":5,
    "fruit de mer":15, 
    "ayimolou cuit a la vapeur":10, 
    "riz mouillé au jarbon":15,
    "jus aromatisé a sodabi":8.5, 
    "jus au larve de poisson":10, 
    "jus de raisin":5, 
    "jus de chias":8.5,
    "jus de miel apanaché au vin de palme":10,
    "jus vinsmatique":5,
} 
food=str(input("quel plat voulez-vous choisir?:"))
juice=str(input("quel jus voulez-vous choisir?:"))
juice.value()
food1=food.values()
print(Menu.get(food))
print(Menu.get(juice)) """
#calcul
"""def operation(n1,n2,signe):
    result=""
    if signe=="+":
        result=n1+n2
    elif signe=="-":
        result=n1-n2
    elif signe=="*":
        result=n1*n2
    elif signe=="/":
        if n2==0:
            print("Erreur:division par zero")
            return None
        result=n1/n2
    elif signe=="%":
        if n2==0:
            print("Erreur:modulopar zero")
            return None
        result=n1%n2
    elif signe=="**":
        result=n1**n2
    else:
        print("signe invalide")
        return None
    return result
while True:
    print("----calculatrice----")
    print("les operateurs disponibles:+,-,*,/,%,**")
    print("Taper 'q' pour quiter le programme:")
    n1=int(input("Entrer le premier nombre:"))
    signe=input("Entrer une operateur:")
    n2=int(input("Entrer le deuxieme nombre:"))
    if n1 or n2 or signe=="q":
        break
result=operation(n1,n2,signe)
print("Result:",result)"""

"""try:
    x=int(input("Entrer un nombre:"))
    print("vous avez saisi",x)
except:
    print("Erreur:vous devez entrer un nombre valide.")
   """
class chien:
    def int(self,nom):
        self.nom=nom
        def aboyer(self):
            print(self.nom,"aboie! woof woof")
chien1=chien("gana")
chien2=chien("gueye") 
chien1.aboyer()
chien2.aboyer()


