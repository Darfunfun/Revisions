ch1 = "items"
ch2 = "attention"
compteur = 0

for i, lettre in enumerate(ch1) :
    # print(i, "-> ", end='')
    # print(lettre, "-> ", end='')
    for j, lettre2 in enumerate(ch2):
        if lettre == lettre2:
            # print("True")
            compteur += 1
            # print(f"Compteur = {compteur}")
        else :
            pass
            # print("False")
            # print(f"Compteur = {compteur}")


if compteur == len(ch2):
    print("Ce sont des anagrammes")
else:
    print("Ce sont PAS des anagrammes")

