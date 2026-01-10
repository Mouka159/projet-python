#demander combien de notes
nbre_notes=int(input("combien de note aimerais vous entrer?"))

somme=0
compteur=0
for i in range(nbre_notes):
    notes=float(input(f"entrer la note {i+1}:"))
    #resolution des condition
    if 0<=notes<=20:
       somme+=notes 
       compteur+=1
    else:
        print("entrer invalide :les notes doivent etre comprise entre 0 et 20")
        #calcul de la moyenne
        if compteur>0:
            moyenne=somme/compteur
            print(f'la moyenne des{compteur} notes valides est : {moyenne:.2f}')
        else:
            print("Aucune notes valide entrée")