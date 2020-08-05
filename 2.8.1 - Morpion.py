import copy


def pions(tableau):
    for l, ligne in enumerate(tableau):
        for b, bloc in enumerate(ligne):
            if tableau[l][b] == 0:
                tableau[l][b] = '.'
            elif tableau[l][b] == 1:
                tableau[l][b] = 'x'
            elif tableau[l][b] == 2:
                tableau[l][b] = 'o'
    print(tableau) # A suppr à la fin du programme


def affichage(tableau):
    for l, ligne in enumerate(tableau):
        for b, bloc in enumerate(ligne):
            print(tableau[l][b], " ", end='')
        print("\n")


def verif_match_nul(tableau):
    for l, ligne in enumerate(tableau):
        for b, bloc in enumerate(ligne):
            if tableau[l][b] == 0:
                # print(f"tableau[l][b] = {tableau[l][b]}")
                return True
            else : 
                #print(f"bloc[pas normal] = {tableau[l][b]}")
                return False


def poser_pion(tableau):

    pose = 1
    x = int(input("Veuillez entrer la LIGNE où vous souhaitez poser votre pion : "))
    y = int(input("Veuillez entrer la COLONNE où vous souhaitez poser votre pion : "))
    

    for l, ligne in enumerate(tableau):
        for c, case in enumerate(ligne):
            if tableau[l][c] == tableau[x][y]:          # Pose JUSQU'A l'emplacement choisi... Pourquoi ?
                #print(tableau)
                print("Pose en cours...")
                tableau[l][c] = pose
            else:
                print("Erreur")
                #print(f"Cas 2 : {tableau[l][c]}, avec l = {l}, ligne = {ligne}, c = {c} et case = {case} \n")



    """
    coordonnéesX = 0
    coordonnéesY = 0
    while tableau[l][b] != 0:
    
    coordonneesX = int(input("Veuillez entrer la LIGNE où vous souhaitez poser votre pion : "))
    coordonneesY = int(input("Veuillez entrer la COLONNE où vous souhaitez poser votre pion : "))

    print(f"Coordonnées X = {coordonneesX}")
    print(f"Coordonnées Y = {coordonneesY}")
    print(f"Tableau = {tableau}")
    
    tableau[coordonneesX][coordonneesY] = 2 # Ne ressort rien 

    for l, ligne in enumerate(tableau):
        for b, bloc in enumerate(ligne):
            #while tableau[l][b] != 0:
            tableau[coordonnéesX][coordonnéesY] = 1
            print(tableau[l][b], " ", end='')
            print("OK")
            print(f"Tableau = {tableau}")
        print("\n")
    """




tableau = [[0] * 3 for i in range(3)]
""" Equivaut à :
tableau = []
for i in range(3):
    tableau.append([0] * 3)
"""
tableau_print = copy.deepcopy(tableau)

print(tableau) # A suppr à la fin du programme
print(f"tableau_print -> {tableau_print}") # A suppr

verif_match_nul(tableau)

jeu = True


# Modification et verification à faire sur "tableau". Traduire ensuite les pions sur "tableau_print"
while jeu:
    poser_pion(tableau)
    jeu = verif_match_nul(tableau)
    pions(tableau_print)
    affichage(tableau_print)
    print(tableau)


