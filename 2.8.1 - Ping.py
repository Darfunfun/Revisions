
def return_valeur():
    n = m = -1

    while n < 0 or m < 0:
        if n < 0 or m < 0:
            print("Les nombres ne sont pas positifs !")
        n = int(input("Veuillez entrer le nombre de colonne du plateau : "))
        m = int(input("Veuillez entrer le nombre de lignes du plateau : "))
    
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
    """if plateau[i][j] == plateau[0][0] or plateau[i][j] == plateau[3][0] or plateau[i][j] == plateau[0][3] or plateau[i][j] == plateau[3][3]:
        

    elif plateau[i][j] == plateau[1][0] or plateau[i][j] == plateau[2][0] or plateau[i][j] == plateau[0][1] or plateau[i][j] == plateau[3][1] or plateau[i][j] == plateau[0][2] or plateau[i][j] == plateau[3][2] or plateau[i][j] == plateau[1][3] or plateau[i][j] == plateau[2][3]:
        pass

    else:"""

    plateau[i - 1][j - 1] = not plateau[i - 1][j - 1]
    plateau[i][j - 1] = not plateau[i][j - 1]
    plateau[i + 1][j - 1] = not plateau[i + 1][j - 1]

    plateau[i - 1][j] = not plateau[i - 1][j]
    plateau[i + 1][j] = not plateau[i + 1][j]

    plateau[i - 1][j + 1] = not plateau[i - 1][j + 1]
    plateau[i][j + 1] = not plateau[i][j + 1]
    plateau[i + 1][j + 1] = not plateau[i + 1][j + 1]



plateau = [[True]*n for i in range(m)]







n, m = return_valeur()
plateau = construction_du_plateau(n, m)
affichage(plateau)

while range(4):    
    i, j = coordonnees_pions(n, m)
    jeu_pion(plateau, i, j)
    affichage(plateau)


print(plateau)