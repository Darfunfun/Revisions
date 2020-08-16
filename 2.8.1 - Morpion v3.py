
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
            print(case, end=' ')
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
    while True:
        pion_ligne = int(input("Selectionnez une LIGNE : "))
        pion_colonne = int(input("Selectionnez une COLONNE : "))
        if ((0 <= pion_ligne <= 2) and (0 <= pion_colonne <= 2)) and plateau[pion_ligne][pion_colonne] == 0:
            plateau[pion_ligne][pion_colonne] = joueur
            break
        print("Veuillez entrer des coordonnées valides ! \n")



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
    au_tour_de_x = True

    while True:
        if au_tour_de_x:
            joueur = joueur1
            print("Au tour de X")
        else:
            joueur = joueur2
            print("Au tour de O")

        poser_pion(plateau, joueur)
        affichage(plateau)
        if check_victoire(plateau, joueur):
            print("Victoire du Joueur", int(not au_tour_de_x) + 1) # Bool -> int -> Ajout de 1 pour donner 1 ou 2 (joueur)
            break
        
        if not au_moins_une_case_est_vide(plateau):
            print("Match nul !")
            break
    
main()