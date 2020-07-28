import random

compteur = 0
liste = []


while compteur < 5:
    liste.append(random.randint(1, 100))
    compteur += 1
    print(liste)


def pairs(liste):
    count = 0
    for i in liste:
        if (i % 2) == 0:
            count += 1
    print(f"Il y a {count} nombre pairs dans la liste !")

pairs(liste)




