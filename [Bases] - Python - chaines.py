
"""
Une méthode de chaïne travaille sur une copie, et non sur la chaîne elle-meme

Quelques méthodes : 
str.upper(), str.lower(), str.capitalize(), str.title(), str.strip()
str.center(<largeur>, [caractere_remplissage])

str.find(<chaine>, [debut], [fin])
str.index(<chaine, [debut], [fin]) # Meme chose que find mais retourne une erreur au lieu de -1 si le terme n'est pas trouvé
str.replace(<ancienne>, <nouvelle>, [occurence])

str.split(<separateur>) # Transforme la chaine en liste
str.join()


Autres methodes de test :
str.isalpha(), str.isdigit(), str.isdecimal(), str.isnumeric(), str.isalphanum()
str.islower(), str.isupper()
str.isidentifier(), str.iskeyword()

"""

# Classe str : string (chaînes de caractères)
ma_chaine = "Salut tout le monde !"

ma_chaine = ma_chaine.upper()               # SALUT TOUT LE MONDE !
ma_chaine = ma_chaine.lower()               # salut tout le monde !
ma_chaine = ma_chaine.capitalize()          # Salut tout le monde !
ma_chaine = ma_chaine.title()               # Salut Tout Le Monde !
ma_chaine = ma_chaine.strip()               # Supprime les espaces avant et après (si aucun sympbole entre les espaces)

ma_chaine = "Mon Super Programme"
ma_chaine = ma_chaine.center(50, "-")       # ---------------Mon Super Programme----------------    -> Ne fait pas de copie ! Modifie directement la chaine !
print(ma_chaine)


# Recherche et test dans la chaine
print(ma_chaine[2])                         # -

if "Super" in ma_chaine:
    print("Trouvé")                         # Trouvé

ma_chaine = "Mon Super Programme"

print(ma_chaine[2])                         # n
print(ma_chaine.find("super"))              # -1 -> ne trouve pas (car sensible à la casse)
print(ma_chaine.find("Super"))              # 4 -> Position / indice où le terme est trouvé



# Remplacement 
ma_chaine = ma_chaine.replace("P", "B")     # Mon Super Brogramme
print(ma_chaine)


# Transformation en liste

print(ma_chaine.split(" "))                 # ['Mon', 'Super', 'Brogramme']

nouvelle_chaine = "Magicien|10|5"
print(nouvelle_chaine.split("|"))           # ['Magicien', '10', '5']



















