#demander combien de notes
nbre_notes=int(input("combien de note aimerais vous entrer ?"))
notes=[]
for i in range(nbre_notes):
 note=float(input(f"entrer la note {i+1}:"))
notes.append(note)
moyenne=sum(notes)/nbre_notes
print(f"la moyenne de vos notes est de: {moyenne}")

#calculer la moyenne de 10 notes