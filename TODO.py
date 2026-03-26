#Gestion de to do list 
class Gestion:
    #initialisation
    def __init__(self):
     self.tache=[]
    #predefinition des fonctions
    def ajouter(self,nom):
        self.tache.append(nom)
        print("Ajouter avec succes")
    def supprimer(self,nom):
        if nom in self.tache:
          self.tache.remove(nom)
          print(f"{nom} Supprimer avec succes")
        else:
            print(f"{nom} n'exit pas dans la liste")
    def afficher(self):
        if self.tache:
            print("\n la liste des tâches : ")
            for i,tache in enumerate(self.tache,start=1):
                print(f"{i}.{tache}")
        else:
                print("Aucun element n'existe dans la liste.")
                #programme Menu
def Menu():
     todolist=Gestion()
     while True:
         print("\n====MENU DES TACHES ======")
         print("1.Ajouter ")
         print("2.supprimer ")
         print("3.Afficher ")
         print("4.Quiter")
         
         choix=(input("Choisissez une option : "))
         if choix=="1":
             nom=input("Entrer votre tâche : ")
             todolist.ajouter(nom)
         elif choix=="2":
             nom=input("Entrer la tache a supprimer : ")
             todolist.supprimer(nom)
         elif choix=="3":
             todolist.afficher()
         elif choix=="4":
             confirm=input("Voulez vous vraiment quiter(oui/non) : ")
             if confirm.lower()=="oui":
                  print("Merci a bientôt")
                  break
             else:
                   print("Ok!")
         else:
             print("Choix invalide,Veuillez ressayer.")
Menu()            
       
             
