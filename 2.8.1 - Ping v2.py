
# Fonction OK
def return_valeur():
    n = m = -1

    while n < 0 or m < 0:
        if n < 0 or m < 0:
            print("Les nombres ne sont pas positifs !")
        n = int(input("Veuillez entrer le nombre de colonne du plateau : "))
        m = int(input("Veuillez entrer le nombre de lignes du plateau : "))
    
    return n, m


# Fonction OK
def construction_du_plateau(n, m):
    return [[True]*(n) for i in range(m)]


# Fonction OK
def affichage(plateau):
    
    for ligne in plateau:
        for case in ligne:
            if case == True:
                case = 'O'
            elif case == False:
                case = 'X'
            print(case, ' ', end='')
        print("\n")


# Fonction OK
def coordonnees_pions(n, m):
    i = j = -1
    

    while not (1 <= i < n and 1 <= j < m):
        i = int(input("Sur quelle COLONNE voulez-vous placer le pion ? "))
        j = int(input("Sur quelle LIGNE voulez-vous placer le pion ? "))
    
    return i, j


# Fonction PAS OK DU TOUT
def jeu_pion(plateau, i, j):
    
    """
    for ligne in (j - 1, j, j + 1):
        for colonne in (i - 1, i, i + 1):
            if ligne == colonne == 0:
                continue
            if 0 <= ligne < len(plateau) and 0 <= colonne < len(plateau):
                plateau[j + ligne][i + colonne] = not plateau[j + ligne][i + colonne]
    """

    """
    for l, ligne in enumerate(plateau):
        # for c, case in enumerate(plateau):
        if l < 0 or l > len(plateau):
            continue
        else:
            # Full code


    if plateau[i][j] == plateau[0][0]:
        plateau[i + 1][j] = not plateau[i + 1]
        plateau[i][j + 1] = not plateau[i][j + 1]
        plateau[i + 1][j + 1] = not plateau[i + 1][j + 1] # Erreur ici : TypeError: 'bool' object is not subscriptable

    if plateau[i][j] == plateau[1][0]:
        plateau[i - 1][j] = not plateau[i - 1]
        plateau[i][j + 1] = not plateau[i][j + 1]
        plateau[i - 1][j + 1] = not plateau[i - 1][j + 1]

    if plateau[i][j] == plateau[1][1]:
        plateau[i - 1][j] = not plateau[i - 1]
        plateau[i][j - 1] = not plateau[i][j - 1]
        plateau[i - 1][j - 1] = not plateau[i - 1][j - 1]

    if plateau[i][j] == plateau[0][1]:
        plateau[i + 1][j] = not plateau[i + 1]
        plateau[i][j - 1] = not plateau[i][j - 1]
        plateau[i + 1][j - 1] = not plateau[i + 1][j - 1]

        
    
    plateau[i - 1][j - 1] = not plateau[i - 1][j - 1]
    plateau[i][j - 1] = not plateau[i][j - 1]
    plateau[i + 1][j - 1] = not plateau[i + 1][j - 1]

    plateau[i - 1][j] = not plateau[i - 1][j]
    plateau[i + 1][j] = not plateau[i + 1][j]

    plateau[i - 1][j + 1] = not plateau[i - 1][j + 1]
    plateau[i][j + 1] = not plateau[i][j + 1]
    plateau[i + 1][j + 1] = not plateau[i + 1][j + 1]
    """
    
    """
    3eme tentative 

    l = i
    c = j

    while (l < 0 and c < 0) and (i in range(plateau) and j in range(plateau)):
        print("Sortie du tableau")
        pass
    else:
        plateau[i - 1][j - 1] = not plateau[i - 1][j - 1]
        plateau[i][j - 1] = not plateau[i][j - 1]
        plateau[i + 1][j - 1] = not plateau[i + 1][j - 1]

        plateau[i - 1][j] = not plateau[i - 1][j]
        plateau[i + 1][j] = not plateau[i + 1][j]

        plateau[i - 1][j + 1] = not plateau[i - 1][j + 1]
        plateau[i][j + 1] = not plateau[i][j + 1]
        plateau[i + 1][j + 1] = not plateau[i + 1][j + 1]
    """

    """
    2eme tentative

    for ligne, j in enumerate(plateau):
        for colonne, i in enumerate(plateau):
            print(f"Ligne = {ligne}, Colonne = {colonne}")
            if ligne < 0 or colonne < 0:
                print("Passage dans les negatifs !!!")
                continue
            else:
                print("Premier ligne")
                plateau[colonne - 1][ligne - 1] = not plateau[colonne - 1][ligne - 1]
                print("Deuxieme ligne")
                plateau[colonne][ligne - 1] = not plateau[colonne][ligne - 1]
                print("Troisieme ligne")
                plateau[colonne + 1][ligne - 1] = not plateau[colonne + 1][ligne - 1]

                print("Quatrieme ligne")
                plateau[colonne - 1][ligne] = not plateau[colonne - 1][ligne]
                print("Cinquieme ligne")
                plateau[colonne + 1][ligne] = not plateau[colonne + 1][ligne]

                print("Sixieme ligne")
                plateau[colonne - 1][ligne + 1] = not plateau[colonne - 1][ligne + 1]
                print("Septieme ligne")
                plateau[colonne][ligne + 1] = not plateau[colonne][ligne + 1]
                print("Huitieme ligne")
                plateau[colonne + 1][ligne + 1] = not plateau[colonne + 1][ligne + 1]
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