
class Cellule:


    def __init__(self, vivant = False):
        self.vivant = vivant
    
    def symboleAffichage(self):
        if self.vivant == False:
            self.vivant = '.'
            print(self.vivant)
        else:
            self.vivant = 'o'
            print(self.vivant)
    
    def prochainEtat(self, cellules_voisines_vivantes):
        if self.vivant == True:
            if cellules_voisines_vivantes <= 1 or cellules_voisines_vivantes > 3:
                self.vivant = False
            elif cellules_voisines_vivantes == 2 or cellules_voisines_vivantes == 3:
                self.vivant = True
        else:
            if cellules_voisines_vivantes == 3:
                self.vivant = True

c1 = Cellule()

c1.symboleAffichage()

c1.prochainEtat(3)

c1.symboleAffichage()