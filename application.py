from classBanque import *

continuer = True
connec = False
maBanque = Banque(10000)

while continuer:
    choix = input("Etes-vous déjà inscrit? \n\t1: OUI\n\t2: NON\n")

    # --------------- #
    # Creation compte #
    # --------------- #

    if choix == "2":
        creationCompte = input('Souhaitez-vous un compte Normal ou Premium? \n\t1: Normal\n\t2: Premium\n')

        # Compte normal
        if creationCompte == "1":
            nom = input("Saissiez votre nom:\n")
            mdp = input("Saissiez votre mdp:\n")
            newNormalUser = User(nom, mdp)
            newNormalUser.creaCompte(int(input("Combien souhaitez-vous créditer sur le compte?\n")))
            maBanque.banqueInscrits.append(newNormalUser)
            print("----------")
            newNormalUser.afficherInformations()

        # Compte premium
        elif creationCompte == "2":
            nom = input("Saissiez votre nom:\n")
            mdp = input("Saissiez votre mdp:\n")
            newPremiumUser = Premium(nom, mdp)
            newPremiumUser.creaCompte(int(input("Combien souhaitez-vous créditer sur le compte?\n")))
            maBanque.banqueInscrits.append(newPremiumUser)
            print("----------")
            newPremiumUser.afficherInformations()
        else:
            print("Saisie incorrect")

    # -------------- #
    # Gestion compte #
    # -------------- #

    elif choix == "1":
        if not maBanque.banqueInscrits:
            print("----------")
            print("Pas de compte inscrits actuellement")
        else:
            checkNom = input("Saissiez votre nom:\n")
            checkMDP = input("Saissiez votre mdp:\n")

            # Check dans la liste si nom et mdp présent dans un objet
            for i in maBanque.banqueInscrits:
                if i.nom == checkNom and i.mdp == checkMDP:

                    # Check si objet présent dans class User
                    if not isinstance(i, Premium):
                        connec = True
                        while connec:
                            choice = input(
                                "[NORMAL USER] Que souhaitez-vous faire: "
                                "\n\t1: Afficher le solde "
                                "\n\t2: Crediter du BITCOINS "
                                "\n\t3: Debiter du BITCOINS"
                                "\n\t4: Afficher les rentrées de BITCOINS "
                                "\n\t5: Afficher les sorties de BITCOINS "
                                "\n\t6: Quitter\n")
                            if choice == "1":
                                print("----------")
                                i.compteBanquaire.afficher()
                                input()
                            elif choice == "2":
                                i.compteBanquaire.crediter(int(input("Combien souhaitez-vous créditer sur le compte?\n")))
                                print("----------")
                                i.compteBanquaire.afficher()
                            elif choice == "3":
                                i.compteBanquaire.debiter(int(input("Combien souhaitez-vous créditer sur le compte?\n")))
                                print("----------")
                                i.compteBanquaire.afficher()
                            elif choice == "4":
                                print("----------")
                                i.compteBanquaire.afficherCredits()
                                input()
                            elif choice == "5":
                                print("----------")
                                i.compteBanquaire.afficherDebits()
                                input()
                            elif choice == "6":
                                connec = False
                            else:
                                print("Saisie incorrecte")

                    # Check si objet présent dans class Premium
                    else:
                        connec = True
                        while connec:
                            choice = input(
                                "[PREMIUM USER] Que souhaitez-vous faire: "
                                "\n\t1: Afficher le solde "
                                "\n\t2: Crediter du BITCOINS "
                                "\n\t3: Debiter du BITCOINS"
                                "\n\t4: Afficher les rentrées de BITCOINS "
                                "\n\t5: Afficher les sorties de BITCOINS "
                                "\n\t6: Emprunter "
                                "\n\t7: Rembourser "
                                "\n\t8: Etat de l'emprunt "
                                # "\n\t7: Rembourser "
                                "\n\t9: Quitter\n")
                            if choice == "1":
                                print("----------")
                                i.compteBanquaire.afficher()
                                input()
                            elif choice == "2":
                                i.compteBanquaire.crediter(int(input("Combien souhaitez-vous créditer sur le compte?\n")))
                                print("----------")
                                i.compteBanquaire.afficher()
                            elif choice == "3":
                                i.compteBanquaire.debiter(int(input("Combien souhaitez-vous créditer sur le compte?\n")))
                                print("----------")
                                i.compteBanquaire.afficher()
                            elif choice == "4":
                                print("----------")
                                i.compteBanquaire.afficherCredits()
                                input()
                            elif choice == "5":
                                print("----------")
                                i.compteBanquaire.afficherDebits()
                                input()
                            elif choice == "6":
                                somme = int(input("Combien souhaitez-vous emprunter à la banque?\n"))
                                i.emprunter(somme)
                                maBanque.pret(somme)
                            elif choice == "7":
                                somme = int(input("Combien souhaitez-vous emprunter à la banque?\n"))
                                i.remboursement(somme)
                                maBanque.reprise(somme)
                            elif choice == "7":
                                i.sommeEmprunt()
                            # elif choice == "7":
                            #     i.remboursement()
                            elif choice == "9":
                                connec = False
                            else:
                                print("----------")
                                print("Saisie incorrecte")
                else:
                    print("----------")
                    print("Identifiant et/ou mot de passe incorrect")
    else:
        print("----------")
        print("Saisie incorrecte")
