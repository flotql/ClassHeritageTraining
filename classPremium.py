from classUser import *
# import time

timer = False


class Premium(User):

    def __init__(self, nomPremium, mdpPremium):
        super().__init__(nomPremium, mdpPremium)
        self.emprunt = 0

    def emprunter(self, montant):
        self.emprunt += montant
        self.compteBanquaire.crediter(montant)
        print(f"Votre emprunt s'élève à {self.emprunt} BITCOINS")

    def remboursement(self, montant):
        self.emprunt -= montant
        self.compteBanquaire.debiter(montant)
        if self.emprunt == 0:
            print(f"Votre emprunt est maintenant complètement remboursé, merci !")
        else:
            print(f"Votre emprunt s'élève à {self.emprunt} BITCOINS")

    def sommeEmprunt(self):
        print(f"Votre emprunt s'élève à {self.emprunt} BITCOINS")

    # def remboursement(self):
    #     global timer
    #     debut = time.time()
    #     while self.emprunt != 0:
    #         while timer:
    #             time.sleep(2.0 - ((time.time() - debut) % 1.0))
    #             self.emprunt -= self.emprunt*5/100
    #             if self.emprunt == 0:
    #                 timer = True
