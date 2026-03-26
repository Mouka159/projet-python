"""print("Entrer un nombre pour vérifier s'il est pair ou impair:")
number=int(input())
if number%2==0:
    print("le nombre est pair")
else:
    print("le nombre est impaire")"""
    
#trie des note en affichant le max, min et la moyene et la difference entre le max et le min
def saisir_notes():
    notes=[]
    for i in range(n):
        note=float(input(f"entrer la note {i+1}:"))
        notes.append(note)
    return notes
def trouverMax(notes):
    return max(notes)
def trouverMin(notes):
    return min(notes)
def calculer_dif(max(notes),min(notes)):
    return 
def Calculermoyenne(notes):
    return sum(notes)/len(notes)
def trie_notes(notes):
    return sorted(notes)
def affichage(max_notes,min_notes,difference,moyenne,tries_notes):
    print("\n======Resultat=====")
    print("la meilleur note est :", max_notes)
    print("la faible note est :", min_notes)
    print("la difference entre le max et le min est  :", difference)
    print("la moyenne est  :", round(moyenne ,2))
    print("le trie dans l ordre croissant des notes :", tries_notes)
def main():
    notes=saisir_notes(10)
    max_notes=trouverMax(notes)
    min_notes=trouverMin(notes)
    differnce=calculer_dif(max_notes,min_notes)
    moyenne=Calculermoyenne(notes)
    tries_notes=trie_notes(notes)
affichage(trouverMax,trouverMin,calculer_dif,Calculermoyenne,trie_notes)
main()
          
                    
               