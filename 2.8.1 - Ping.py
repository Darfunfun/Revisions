
def return_valeur():
    n = m = -1

    while n < 0 or m < 0:
        n = int(input("Veuillez entrer le nombre de colonne du plateau : "))
        m = int(input("Veuillez entrer le nombre de lignes du plateau : "))

        if n < 0 or m < 0:
            print("Les nombres ne sont pas positifs !")
    
    return n, m



def construction_du_plateau(n, m):
    return [[True]*n for i in range(m)]



def affichage(plateau):
    for ligne in plateau:
        for case in ligne:
            if case == True:
                case = 'O'
            elif case == False:
                case = 'X'
            print(case, ' ', end='')
        print("\n")



def coordonnees_pions(n, m):
    i = j = -1

    while not (1 <= i < n and 1 <= j < m):
        i = int(input("Sur quelle COLONNE voulez-vous placer le pion ? "))
        j = int(input("Sur quelle LIGNE voulez-vous placer le pion ? "))
    
    return i - 1, j - 1



def jeu_pion(plateau, i, j):
    """
    Deux erreurs persistent : 
    - Impossible de poser en [4][4] (out of range)
    - Les pions de l'autre côté du plateau change aussi (à cause des index negatifs), et je n'arrive pas à empecher ça (2.8.1 - Ping v2.py est une tentative mais rien à faire)
    """
    """
    for ligne in (j - 1, j, j + 1):
        for colonne in (i - 1, i, i + 1):
            if ligne == colonne == 0:
                continue
            if 0 <= ligne < len(plateau) and 0 <= colonne < len(plateau):
                plateau[j + ligne][i + colonne] = not plateau[j + ligne][i + colonne]
    """

    """
    plateau[i - 1][j - 1] = not plateau[i - 1][j - 1]
    plateau[i][j - 1] = not plateau[i][j - 1]
    plateau[i + 1][j - 1] = not plateau[i + 1][j - 1]

    plateau[i - 1][j] = not plateau[i - 1][j]
    plateau[i + 1][j] = not plateau[i + 1][j]

    plateau[i - 1][j + 1] = not plateau[i - 1][j + 1]
    plateau[i][j + 1] = not plateau[i][j + 1]
    plateau[i + 1][j + 1] = not plateau[i + 1][j + 1]
    """



# Fonction OK
def check_victoire(plateau):
    for ligne in plateau:
        for case in ligne:
            if case == False:
                print("Toutes les cases sont noires !")
                return True
                # victoire = True
                # break
            else:
                print("Il reste des cases blanches !")
                return False
                # victoire = False
                # break



# Fonction OK
def continuer_la_partie():
    vote_du_joueur = int(input("Voulez-vous continuer la partie ? \n1 = OUI, 0 = NON : "))
    vote_du_joueur = bool(vote_du_joueur)
    if vote_du_joueur == True:
        print("Aller, on continue, courage !")
        return True
    elif vote_du_joueur == False:
        print("Arret de la partie, rententez la prochaine fois !")
        return False
    else:
        print("GROSSE ERREUR")




n, m = return_valeur()
plateau = construction_du_plateau(n, m)
affichage(plateau)

while True:    
    i, j = coordonnees_pions(n, m)
    jeu_pion(plateau, i, j)
    affichage(plateau)
    check_victoire(plateau)
    #continuer = continuer_la_partie()