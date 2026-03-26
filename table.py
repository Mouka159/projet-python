"""for i in range(1,11):
    for j in range(1,11):
        print(f'{i}  *  {j}= {i*j}',end='\n')
    print()
    
    #afficher les mutiple de 3 entre 1  et 50
for i in range(1,50):
         if i%3==0:
             print(i)
            
#la somme des nombre paire entre 1 et 100
        somme=0
        for i in range(1,100):
            if i%2==0:
            somme+=i
            print(somme)"""
"""notes=[10,15,12,16]
def calcul_moyenne(notes):
    moyenne=sum(notes)/len(notes)
    return moyenne
print(calcul_moyenne(notes))"""
#calcul d'aire e et le perimetre d un rectangle
"""def rectangle(longueur,largeur):
    perimetre=2*(longueur+largeur)
    aire=longueur*largeur
    return perimetre,aire
a,p=rectangle(5,3)
print("perimetre:",a,"Aire:",p)"""
#niveau expert
def calcul(Longueur,Largeur):
    perimetre=(Longueur+Largeur)*2
    Aire=Longueur*Largeur
    return perimetre,Aire

nbre=int(input(f"Combien de rectangle voulez vous analyser:"))
print("\nRectangle| Longeur | Largeur | Perimetre | Aire |")
print("----------------------------------------------------")
for i in range(1,nbre):
    nom=print(f"le rectangle{i}")
    L=str(input("la longueur:"))
    l=str(input("la largeur:")) 

Aire,perimetre=calcul(Longueur=int(L),Largeur=int(l))
print(f"{i:<9} | {L:<8} | {l:<7} | {Aire:<4} | {perimetre:<9} |")


    
    
    
            
    
         
        
