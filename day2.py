print("Bienvenue sur le calculatuer de pourboire")
facture = input("quelle est le montant de la facture? $")
prctg = input("Quel pourcentage voulez-vous donner? 10,12 ou 15?: ")
nbrP = input("Combien de personnes vont partager la facture?: ")

pay = (float(facture) / int(nbrP)) * (1 + (float(prctg) / 100))

print("Chaque personne devra donner: $" + str(round(pay, 2)))
