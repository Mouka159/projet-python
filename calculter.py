def operation(n1,n2,signe):
    result=''
    if signe=='+':
        result=n1+n2
    elif signe=='-':
        result=n1-n2
    elif signe=='*':
        result=n1*n2
    elif signe=='/':
        if n2==0:
            print("division par zero")
            return None
        result=n1/n2
    elif signe=='**':
         result=n1**n2
    elif signe=='%':
        if n2==0:
            print('modulo par zero')
            return None
        result=n1%n2
    else:
        print('operation invalide')
        return None
    return result
while True:
    print("------Calculatrice----")
    print("les operations disponibles: +, -, *, /, **, %")
    n1=int(input("entrer le premier nombre:"))
    n2=int(input("entrer le deuxieme nombre:"))
    signe=input("entrer l'operation:")
    result=operation(n1,n2,signe)
    if result is not None:
        print(f"le resultat de {n1} {signe} {n2} est: {result}")
    continuer=input("voulez vous continuer? (oui/non):")
    if continuer.lower() != 'oui':
        break