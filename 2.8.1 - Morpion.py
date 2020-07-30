import copy


def pions(tableau):
    for i, ligne in enumerate(tableau):
        for j, case in enumerate(tableau):
            if case[j] == 0:
                case[j] = '.'
            elif case[j] == 1:
                case[j] = 'x'
            elif case[j] == 2:
                case[j] = 'o'
    print(tableau) # A suppr à la fin du programme


def affichage(tableau):
    for i, ligne in enumerate(tableau):
        for j, case in enumerate(tableau):
            print(case[j], " ", end='')
        print("\n")


def verif_match_nul(tableau):
    for i, ligne in enumerate(tableau):
        for j, case in enumerate(tableau):
            if case[j] == 0:
                # print(f"case[j] = {case[j]}")
                return True
            else : 
                #print(f"case[pas normal] = {case[j]}")
                return False


tableau = [[0]*3]*3
tableau_print = copy.deepcopy(tableau)

print(tableau) # A suppr à la fin du programme
print(f"tableau-print -> {tableau_print}") # A suppr

verif_match_nul(tableau)

jeu = True


# Modification et verification à faire sur "tableau". Traduire ensuite les pions sur "tableau_print"
while jeu:
    pions(tableau_print)
    affichage(tableau_print)
    jeu = verif_match_nul(tableau)


