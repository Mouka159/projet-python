rep =""
vip=input("êtes vous VIP?")
if vip=="oui":
    rep="Autorisé :Bienvenue VIP"
else:
    cha=input("Quelle chaussure avez vous portez de sport?:")
    if cha=="non":
        carte=input("possedez vous une carte de membre?")
        if carte=="oui":
            rep="Autorisé:Bienvenue membre"
        else:
            age=int(input("Quel est votre âge?:"))
            if age>22:
                rep="autorisé:Bienvenue adulte"
            else:
                if age>=18 and age<=22:
                    acomp=input("êtes vous accompagné d'un adulte?")
                    if acomp=="oui":
                        rep="Autorisé:Bienvenue jeune accompagné"
                    else:
                        rep="Refusé:Non accompagné"
                else:
                    rep="Refusé:Mineur"
    else:
        rep="Refusé:Veuillez porter des chaussures de sport"
        
print(rep)