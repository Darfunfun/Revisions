[Reprendre à Python #6 - boucles (12:00 min)

msg = "hello"
print(msg)

#Commentaire
a = 5
b = 0

if a > 0 :
    b += 1
    print("a est superieur à 0, a = ", a, "et b = ", b)


# parse de type
a_str = str(a)
print("Voici la variable \"a\" en str :", a_str)

# {} et .format
nomJoueur = "Diablo"
print ("Bienvenue {}. Vous etes le {}eme joueur".format(nomJoueur, a))


# input()
namePlayer = input("Choississez un nom de joueur : ")
print ("Bienvenue", namePlayer)


# in / not in
lettre_hasard = "b"

if lettre_hasard not in "aeiouy" : 
    print("C'est une consonne")


# Comparaison "fourchette"
age = 24
if 0 < age <= 100:
    print ("L'age est valide")
else:
    print ("L'age n'est pas valide")


# While
jeu_lance = True
print("")

while jeu_lance:
    choixMenu = input("> ")

    if choixMenu == "again":
        print("Ok, on recommence !")
        continue
    elif choixMenu == "quit":
        jeu_lance = False
    elif choixMenu == "new":
        print ("Alors... Le jeu est lancé, mais il est pas encore fini... Hehehe ")
    else:
        print("Commande introuvable...")
print("A bientot !")


