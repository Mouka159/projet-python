#multiplication table en entrant le multiplicateur
nbre=int(input("Entrez un nombre : "))
for i in range(1,11):
    print(f"{nbre} x {i} = {nbre*i}")
#multiplication table for en entrant deux plage nombres
nbre1=int(input("Entrez le debut de la plage : "))
nbre2=int(input("Entrez la fin de la plage : "))
nbre=int(input("Entrer le multiplicateur : "))
for i in range (nbre1,nbre2+1):
     print(f"{i} x {nbre} = {nbre1*i}")
