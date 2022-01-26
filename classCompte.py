import datetime


class Compte:

    banque = "laF"

    def __init__(self, proprio):
        self.dateCreation = str(datetime.date.today())
        self.solde = 0
        self.proprio = proprio
        self.debit = []
        self.credit = []

    def crediter(self, montant):
        self.solde += montant
        self.credit.append(montant)
        self.afficher()

    def debiter(self, montant):
        self.solde -= montant
        self.debit.append(montant)
        print(f"votre solde est maintenant de {self.solde} bitcoins")

    def afficher(self):
        print(f"votre solde est maintenant de {self.solde} bitcoins")

    def resume(self):
        print("Le proprietaire du compte est {}. "
              "Le compte a été créé le {}. "
              "Il dispose de {} bitcoins. "
              "Il est hébergé à la banque {} ".format(self.proprio,
                                                      self.dateCreation,
                                                      self.solde,
                                                      self.banque))

    def afficherCredits(self):
        for i in self.credit:
            print(i)

    def afficherDebits(self):
        for i in self.debit:
            print(i)
