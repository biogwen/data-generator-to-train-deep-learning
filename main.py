# import des bibliothèques
import pandas as pd
from random import randint


#import des prénoms
listing_prenoms = pd.read_csv('prenom.csv')
prenom = listing_prenoms.prenom

# création des codes produits à 9 chiffres

produits = []
for index_produit in range(50):
    reference_produit = ""
    for i in range(9):
        chiffre = randint(0, 9)
        reference_produit = reference_produit + str(chiffre)

    produits.append(reference_produit)

print (produits)

#création listings

stuff = []
for prenoms in prenom:
    stuff.append({"nom":prenoms, "objets": []})



#détermination aléatoire du nombre de contenu par personne

#génération des contenus par personne
def add_stuff(self, username, cust_name):
    num_things = randint(1, 60)
    i = 0

   # for i <= num_things:


#export en excel


