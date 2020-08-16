
def affichage(plateau):
    print("   ", "0 ", "1 ", "2")
    print("  ", " _", " _", " _")
    for l, ligne in enumerate(plateau):
        print(l, '| ', end='')
        for case in ligne:
            if case == 1:
                case = 'x'
            elif case == 2:
                case = 'o'
            else:
                case = '.'
            print(case, ' ', end='')
        print("\n")


def au_moins_une_case_est_vide(plateau):
    continuer = False
    for ligne in plateau:
        for case in ligne:
            if case == 0:
                continuer = True
                break
    return continuer


def poser_pion(plateau, joueur):

    pion_ligne = int(input("Selectionnez une LIGNE : "))
    pion_colonne = int(input("Selectionnez une COLONNE : "))
    

    #while (pion_ligne < 0 or pion_ligne > 2) or (pion_colonne < 0 or pion_colonne > 2):  
    while not ((0 >= pion_ligne >= 2) and (0 >= pion_colonne >= 2)) and plateau[pion_ligne][pion_colonne] != 0:
        print("Veuillez entrer des coordonnées valides ! \n")
        pion_ligne = int(input("Selectionnez une LIGNE : "))
        pion_colonne = int(input("Selectionnez une COLONNE : "))


    plateau[pion_ligne][pion_colonne] = joueur


def check_victoire(plateau, joueur):
    
    for ligne in range(len(plateau)):
        if plateau[ligne][0] == joueur and plateau[ligne][1] == joueur and plateau[ligne][2] == joueur:
            print("Alignement Horizontal !!")
            return True

    for colonne in range(len(plateau)):
        if plateau[0][colonne] == joueur and plateau[1][colonne] == joueur and plateau[2][colonne] == joueur:
            print("Alignment Vertical !!")
            return True

    if plateau[0][0] == joueur and plateau[1][1] == joueur and plateau[2][2] == joueur:
        print("Alignement diagonale !")
        return True

    if plateau[2][0] == joueur and plateau[1][1] == joueur and plateau[0][2] == joueur:
        print("Alignement diagonale !")
        return True
        
    print("Pas d'alignement \n")
    return False



plateau = [[0]*3 for i in range(3)]
affichage(plateau)
joueur1 = 1
joueur2 = 2

def main():
        
    while True:

        print("Au tour de X")
        poser_pion(plateau, joueur1)
        affichage(plateau)
        if check_victoire(plateau, joueur1):
            print("Victoire du Joueur 1 !")
            break
        
        continuer = au_moins_une_case_est_vide(plateau)
        if continuer == False:
            print("Match nul !")
            break

        print("Au tour de O")
        poser_pion(plateau, joueur2)
        affichage(plateau)
        if check_victoire(plateau, joueur2):
            print("Victoire du Joueur 2 !")
            break
        
        continuer = au_moins_une_case_est_vide(plateau)
        if continuer == False:
            print("Match nul !")
            break
    
main()