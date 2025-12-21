result=""
print(" le controle pour avoir acces a une salle de cinema")
age=int(input("Quel age avez vous?"))
bil=input("Avez vous le billet(oui/non)?")
if age>=18:
    if bil=="non":
        result=print("Acces refusé:manquant du billet")
    else:
        result=print("Acces complet autorisé")
else:
    if age<18:
        if bil=="non":
            result=print("Acces refusé")
        else:
            Accompagne=input("etes vous caccompagné(oui/non)?")
            if Accompagne=="oui":
                result=print("Acces Autorisé")
            else:
                result=print("Acces refusé")