import random
import time


"""
Le programme est coder dans un ordre tel que chaque fonction appelle celle qui est au "dessus" d'elle
Cela me permet de lire facilement le code puisqu'il est bien "rangé"
"""


# Fonction OK
def affichage(plateau):
    for ligne in plateau:
        print("|", end='')
        for case in ligne:
            if case == 1:
                case = 'x'
            elif case == -1:
                case = 'o'
            else:
                case = ' '
            
            print(f"{case}|", end='')
        print("\n", end='')

    print(" -" * 7)
    for i in range(7):
        print(f" {i + 1}", end='')
    print("\n")



# Fonction OK -> Astuce : Enumerate pour choper l'indice qui sera incrementé pour chaque ligne
def pions_dans_la_colonne(plateau, numero_colonne):
    compteur = 0
    for l, ligne in enumerate(plateau):
        if plateau[l][numero_colonne] != 0:
            compteur += 1
    
    print(f"-> Il y a {compteur} pions dans la colonne {numero_colonne + 1}")
    return compteur



# Fonction OK -> Appel pions_dans_la_colonne
def check_colonne_pleine(plateau, numero_colonne):
    compteur = pions_dans_la_colonne(plateau, numero_colonne)
    
    if compteur >= 6:
        print(f"-> La colonne {numero_colonne + 1} est pleine !")
        return True
    else:
        print(f"-> Il reste {6 - compteur} cases vides dans la colonne {numero_colonne + 1} !")
        return False



# Fonction OK -> Appel check_colonne_pleine (Il reste juste à voir pourquoi le while veut pas prendre la condition > 7)
def selection_colonne_joueur(plateau):
    numero_colonne = int(input("Veuillez choisir une colonne : "))
    numero_colonne -= 1
    print(f"---> Le joueur a choisi la colonne {numero_colonne + 1}")
    
    while check_colonne_pleine(plateau, numero_colonne) or numero_colonne < 0 or numero_colonne == 7:
        numero_colonne = int(input("Veuillez choisir une colonne : "))
        numero_colonne -= 1
        print(f"---> Le joueur a choisi la colonne {numero_colonne + 1}")

    return numero_colonne



# Fonction OK -> Appel check_colonne_pleine
def selection_colonne_ordi(plateau):
    numero_colonne = random.randint(0, 6)
    numero_colonne -= 1
    print(f"---> L'ordi a choisi la colonne {numero_colonne + 1}")    

    while check_colonne_pleine(plateau, numero_colonne) or numero_colonne == -1:
        numero_colonne = random.randint(1, 7)
        numero_colonne -= 1
        print(f"---> L'ordi a choisi la colonne {numero_colonne + 1}")    

    return numero_colonne



# Fonction OK
def pose_pion(plateau, joueur):
    ligne = 5

    if joueur == 1:
        numero_colonne = selection_colonne_joueur(plateau)
        while plateau[ligne][numero_colonne] != 0 and ligne >= 0:
            ligne -= 1
        plateau[ligne][numero_colonne] = joueur

    elif joueur == -1:
        numero_colonne = selection_colonne_ordi(plateau)
        while plateau[ligne][numero_colonne] != 0 and ligne >= 0:
            ligne -= 1
        plateau[ligne][numero_colonne] = joueur
    else:
        print("BUGGGGGGGGG !!!!!!!!!")

    return numero_colonne # A suppr ?



# Fonction OK -> Est-ce que la variable "ligne" serait utilisable ? Si oui, comment ? Chercher si une fonction sur liste va check 4 meme valeur
def check_horizontal(plateau, numero_colonne, joueur):
    for l, ligne in enumerate(plateau):
        print(f"l = {l}")
        if plateau[l][numero_colonne] == joueur and plateau[l][numero_colonne + 1] == joueur and plateau[l][numero_colonne + 2] == joueur and plateau[l][numero_colonne + 3] == joueur:
            print("Alignement horizontal ! (Cas 1)")
            return True
        elif plateau[l][numero_colonne] == joueur and plateau[l][numero_colonne -1] == joueur and plateau[l][numero_colonne + 1] == joueur and plateau[l][numero_colonne + 2] == joueur:
            print("Alignement horizontal ! (Cas 2)")
            return True
        elif plateau[l][numero_colonne] == joueur and plateau[l][numero_colonne - 2] == joueur and plateau[l][numero_colonne - 1] == joueur and plateau[l][numero_colonne + 1] == joueur:
            print("Alignement horizontal ! (Cas 3)")
            return True
        elif plateau[l][numero_colonne] == joueur and plateau[l][numero_colonne - 3] == joueur and plateau[l][numero_colonne - 2] == joueur and plateau[l][numero_colonne - 1] == joueur:
            print("Alignement horizontal ! (Cas 4)")
            return True
        else:
            print("Pas d'alignement horizontal")
            







plateau = [[0]*7 for i in range(6)]
affichage(plateau)

joueur = 1
ordi = -1


while True:
    print("* Tour du joueur *")
    colonne_choisie = pose_pion(plateau, joueur)

    affichage(plateau)

    check_horizontal(plateau, colonne_choisie, joueur)

    time.sleep(1)
"""
    print("* Tour de l'ordi *")
    colonne_choisie = pose_pion(plateau, ordi)

    affichage(plateau)

    check_horizontal(plateau, colonne_choisie)
"""
# pions_dans_la_colonne(plateau, colonne)
# check_colonne_pleine(plateau, numero_colonne)