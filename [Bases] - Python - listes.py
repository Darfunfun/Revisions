import random


# Liste multidimentionelle

plateau = [[0]*4 for i in range (3)]
print(plateau)

"""
plateau[3][2] = 123
print(plateau)

"""

for ligne in plateau:
    for case in ligne:
        print(case, " ", end='')
    print("\n")


def randomize(plateau):
    for l, ligne in enumerate(plateau):
        for c, case in enumerate(plateau):
            plateau[l][c] = random.randint(0, 100)  # Ne remplit pas la derniere case de chaque lignes + comportement bizarre de "case"
            print((f"l = {l}"))
            print((f"ligne = {ligne}"))
            print((f"c = {c}"))
            print((f"case = {case}"))
            print(plateau)
            input()


randomize(plateau)

input("Nouveau plateau : ")

# boucle principale
for ligne in plateau:
    for case in ligne:
        print(case, " ", end='')
    print("\n")

