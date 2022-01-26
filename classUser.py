from classCompte import *


class User:

    def __init__(self, nom, mdp):
        self.nom = nom
        self.mdp = mdp
        self.compteBanquaire = Compte(self.nom)

    def afficherInformations(self):
        self.compteBanquaire.resume()
        print("----------")
        self.compteBanquaire.afficherCredits()
        print("----------")
        self.compteBanquaire.afficherDebits()

    def creaCompte(self, montant):

        self.compteBanquaire.solde += montant
        self.compteBanquaire.credit.append(montant)
