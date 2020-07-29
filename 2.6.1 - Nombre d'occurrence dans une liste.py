import random

def randomize(ma_liste):
    i = 0
    while i < 5:
        ma_liste.append(random.randint(1, 3))
        i += 1

def nb_occurence(ma_liste, chiffre):
    compteur = 0
    for i in ma_liste:
        if chiffre == i:
            compteur += 1
    print(f"Il y a {compteur} occurence du chiffre {chiffre}")


ma_liste = []
chiffre = 2
randomize(ma_liste)
print(ma_liste)
nb_occurence(ma_liste, chiffre)

