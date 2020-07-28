chaine1 = "Pythons"
chaine2 = "Parions"



def hamming(chaine1, chaine2):
    compteur = 0
    for k in chaine1:
        compteur += chaine2.count(k)
    
    print(compteur)


hamming(chaine1, chaine2)