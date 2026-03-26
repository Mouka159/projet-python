""" def reverse():
    tab=[1,2,3,4,5,6,7,8,9,10]
    tab.reverse()
    print(tab)
reverse()"""
 
def moyenne():
    notes=[]
    for i in range(10):
        note=float(input(f"entrer la note {i+1}:"))
        notes.append(note)
    moyenne=sum(notes)/len(notes)
    print(f"la moyenne de vos notes est de: {moyenne}")
    
moyenne()



    

