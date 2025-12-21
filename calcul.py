print(" les tarifs de la salle de cinéma  en fonction de votre age  ")
age=int(input("Entrer votre age:"))
if age<12:
    print(" Bienvenue! Votre ticket est gratuit")
elif age>=12 and age<=17:
    print(" Bienvenue! Votre ticket  est réduite de 50%")
elif age==18 and age<30:
    print(" Bienvenue! Votre ticket est au tarif normal")
elif age>=30 and age<65:
    print(" Bienvenue! votre ticket est au tarif senior")
else:
    print(" Veuillez direger vers la salle VIP")
    
    
    
 