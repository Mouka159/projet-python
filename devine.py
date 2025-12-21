print("Choisissez un nombre entier secret")
secret_number=int(input())
print("Deviner le nombre secret:")
devine=int(input())
if devine==secret_number:
    print("Félicitations! Vous avez deviné le nombre secret.")
elif devine<secret_number:
    print("Trop bas!.")
    devine=int(input())
elif devine> secret_number:
    print("Trop haut!")
else:
    print(" Entrer invalide")
    