import random

def randomize(ma_liste):
    i = 0
    while i < 5:
        ma_liste.append(random.randint(1, 10))
        i += 1

ma_liste = []
