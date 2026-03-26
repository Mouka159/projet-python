
#n = int(input("Enter a number: "))
for i in range(0,13):
   # print( f"{n} x {i} = {n*i}" )
#
#for i in range(1,21):
   # print(i)
    
  fruits=["banane","pomme","orange"]
for index,  fruit in enumerate (fruits, start =1  ):
    #print(index, fruit)
   
   somme=0
for i in range(1,100):
    somme=somme+i 
    #result=print( somme)
 #la table de multiplication en entrant le debut ,la fin et le mutilpliant de la table    
#nd=int(input("entrer le debut de la table:"))
#nf=int(input("entrer la fin de la table:"))
#mlt=int(input("entrer le multiplicateur de la table:"))
#for i in range(nd,nf):
   #result=print(f'{i}*{mlt}={i*mlt}')
   
   
 #Calcule la somme des nombres pairs entre 1 et 100.     
somme=0
for i in range(1,102):
   if i%2==0:
      somme=i+somme
     # result=print(somme)