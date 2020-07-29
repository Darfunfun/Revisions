import random


def commencer(allumettes):
    while (allumettes % 2) == 0 :
        allumettes = int(input("Saisissez un nombre impair d\'allumettes : "))
        return allumettes

def premier_tireur():
    premier_tireur = int(input("Voulez-vous commencer (1) ou que l\'ordinateur commence (2) : "))
    if premier_tireur == 1:
        return 1
    else:
        return 2

def afficher_allumettes(allumettes):
    print(f"Il reste {allumettes} allumettes : \n")
    print("| " * allumettes)
    print("\n")

def perdant(allumettes):
    if allumettes <= 0:
        print("Le joueur a perdu")


def jeu():

    allumettes = 0
    ordi = "AI"
    joueur = "Joueur"
    allumettes = commencer(allumettes)
    premier_tireur()
    print("\n")

    while allumettes > 0:
        
        afficher_allumettes(allumettes)
        
        tir = 0
        while tir < 1 or tir > 3:
            tir = int(input("Combien prenez-vous d\'allumettes ? "))
        allumettes -= tir
        
        afficher_allumettes(allumettes)

        tir = random.randint(1, 3)
        print(f"{ordi} a tiré {tir}")
        allumettes -= tir
        
        """
        if premier_tireur == 1 :
            while tir < 1 or tir > 3:
                tir = int(input("Combien prenez-vous d\'allumettes ? "))
        elif premier_tireur == 2:
            tir = random.randint(1, 3)
        """
        
        
        perdant(allumettes)




jeu()


