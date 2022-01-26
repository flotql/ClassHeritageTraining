from classPremium import *

class Banque:

    nom = "laF"

    def __init__(self,pecule):
        self.banqueInscrits = []
        self.empruntBanque = 0
        self.pecule = pecule

    def pret(self,montant):
        self.pecule -= montant
        self.empruntBanque += montant

    def reprise(self,montant):
        self.pecule += montant
        self.empruntBanque -= montant