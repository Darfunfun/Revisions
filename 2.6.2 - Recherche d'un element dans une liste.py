import random

def randomize(ma_liste):
    i = 0
    while i < 5:
        ma_liste.append(random.randint(1, 10))
        i += 1

def rechercher(chiffre, ma_liste):
    if chiffre in ma_liste:
        print(f"ma_liste.index(chiffre) = {ma_liste.index(chiffre)}")
        print(f"Le chiffre est présent à l'indice {ma_liste.index(chiffre)} de la liste")
    else :
        print("-1")


ma_liste = []
compteur = 0
chiffre = int(input("Entrez un chiffre à rechercher : "))
randomize(ma_liste)
print(ma_liste)
rechercher(chiffre, ma_liste)

