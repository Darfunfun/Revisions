import random

allumettes = 0

while (allumettes % 2) == 0 :
    allumettes = int(input("Saisissez un nombre impair d\'allumettes : "))

premier_tireur = int(input("Voulez-vous commencer (1) ou que l\'ordinateur commence (2) : "))



print("\n")


while allumettes > 0:
    print("Il reste {} allumettes : \n".format(allumettes))
    # print(f"Il reste {allumettes} allumettes : \n")
    print("| " * allumettes)
    print("\n")
    
    tir = 0
    
    if premier_tireur == 1 :
        while tir < 1 or tir > 3:
            tir = int(input("Combien prenez-vous d\'allumettes ? "))
    elif premier_tireur == 2:
        tir = random.randint(1, 3)


    print("\n")
    allumettes -= tir



