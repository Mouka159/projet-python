"""def afficher_plateau(plateau):
    for ligne in plateau:
        print(" | ".join(ligne))
        print("-" * 5)

def verifier_victoire(plateau, joueur):
    # Vérifie lignes
    for ligne in plateau:
        if all(case == joueur for case in ligne):
            return True
    # Vérifie colonnes
    for col in range(3):
        if all(plateau[ligne][col] == joueur for ligne in range(3)):
            return True
    # Vérifie diagonales
    if all(plateau[i][i] == joueur for i in range(3)):
        return True
    if all(plateau[i][2 - i] == joueur for i in range(3)):
        return True
    return False

def morpion():
    plateau = [[" " for _ in range(3)] for _ in range(3)]
    joueur = "X"
    coups = 0

    while coups < 9:
        afficher_plateau(plateau)
        print(f"Tour du joueur {joueur}")
        
        # Saisie des coordonnées
        ligne = int(input("Entrez la ligne (0-2) : "))
        col = int(input("Entrez la colonne (0-2) : "))

        # Vérifie si la case est libre
        if plateau[ligne][col] == " ":
            plateau[ligne][col] = joueur
            coups += 1

            # Vérifie victoire
            if verifier_victoire(plateau, joueur):
                afficher_plateau(plateau)
                print(f"Le joueur {joueur} a gagné !")
                return

            # Alterne joueur
            joueur = "O" if joueur == "X" else "X"
        else:
            print("Case déjà occupée, choisissez une autre.")

    afficher_plateau(plateau)
    print("Match nul !")

# Lancer le jeu
morpion()"""


# Saisie des dimensions
n = int(input("Entrez le nombre de lignes (n) : "))
m = int(input("Entrez le nombre de colonnes (m) : "))

# Création de la matrice vide
matrice = []

# Remplissage de la matrice par saisie utilisateur
for i in range(n):
    ligne = []
    for j in range(m):
        valeur = int(input(f"Entrez la valeur pour la case ({i},{j}) : "))
        ligne.append(valeur)
    matrice.append(ligne)

# Sommes des lignes
for i in range(n):
    somme_ligne = sum(matrice[i])
    print(f"Somme de la ligne {i} = {somme_ligne}")

# Sommes des colonnes
for j in range(m):
    somme_colonne = 0
    for i in range(n):
        somme_colonne += matrice[i][j]
    print(f"Somme de la colonne {j} = {somme_colonne}")
