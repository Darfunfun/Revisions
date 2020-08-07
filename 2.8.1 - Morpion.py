import copy


def convert_pions(tableau):
    for ligne in tableau:
        for bloc in ligne:
            if ligne[bloc] == 1:
                case = 'x'
            elif ligne[bloc] == 2:
                case = 'o'
            else:
                case = '.'


# Fonction OK
def affichage(tableau):
    for ligne in tableau:
        for bloc in ligne:
            print(ligne[bloc], " ", end='')
        print("\n")


# Fonction OK
def verif_match_nul(tableau):
    for ligne in tableau:
        for bloc in ligne:
            if ligne[bloc] == 0:
                print("True")
                return True
            else : 
                print("False")
                return False


def poser_pion(tableau):

    pose = 1
    ligne = int(input("Veuillez entrer la LIGNE où vous souhaitez poser votre pion : "))
    colonne = int(input("Veuillez entrer la COLONNE où vous souhaitez poser votre pion : "))

    print(ligne)
    print(colonne)
    
    for l in tableau:
        for bloc in l:
            tableau[ligne][colonne] = pose




tableau = [[0] * 3 for i in range(3)]
""" Equivaut à :
tableau = []
for i in range(3):
    tableau.append([0] * 3)
"""

print(f"Tableau de base : {tableau}") # A suppr à la fin du programme

jeu = True


# Modification et verification à faire sur "tableau". Traduire ensuite les pions avec convert_pions 
while jeu:
    poser_pion(tableau)
    jeu = verif_match_nul(tableau)
    convert_pions(tableau)
    affichage(tableau)
    print(tableau)
