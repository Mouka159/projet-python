import random

# L'ordinateur choisit un nombre au hasard
nombre_mystere = random.randint(1, 20)
trouve = False

while not trouve:
    # Demander une tentative
    essai = int(input("Devine le nombre (entre 1 et 20) : "))
    
    # Vérifier la condition
    if essai < nombre_mystere:
        print("Trop petit !")
    elif essai > nombre_mystere:
        print("Trop grand !")
    else:
        print("Bravo, tu as trouvé !")
        trouve = True
 