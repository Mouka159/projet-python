import re

contexte="nous somme entrain etudier  evoluer sur les reger et je ca ne serai pas facile 91970325" 
pattern=r"a"
resultat=re.findall(pattern,contexte)
print(resultat)
"""if resultat:
    print(resultat)
else:
    print("Numero non verifie")"""