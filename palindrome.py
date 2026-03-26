mot=input("Entrez un mot : ")
def est_palindrome(mot): 
    mot=mot.lower().remplace()
    return mot==mot[::-1]
if mot==mot[::-1]:
    print(f"{mot} egal à {mot[::-1]} est un palindrome.")
else:
    print(f"{mot} egal a {mot[::-1]} n'est pas un palindrome.")