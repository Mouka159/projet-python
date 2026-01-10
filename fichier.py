print("Entrer votre nom ,prenom,age et de verifier s'il est admissible")
name=input("Entrer votre nom:")
user_name=input("Entrer votre prenom:")
age=input("Entrer votre age:")
if  int(age)> 18:
    print("vous etes autoriser a vous inscrire Monsieur " +name ," " +user_name)
else:
    print("vous n' etes pas autoriser a vous inscrire Monsieur " +name ," " +user_name)
