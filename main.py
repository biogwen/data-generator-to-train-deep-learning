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

#création listings

stuff = []
for prenoms in prenom:
    n = randint(1, 50)
    produit_client = []
    for i in range(n):
        p = randint(0, 49)
        produit_client.append(produits[p])


    stuff.append({"nom":prenoms, "objets": [produit_client]})



#détermination aléatoire du nombre de contenu par personne


#génération des contenus par personne



#export en excel


