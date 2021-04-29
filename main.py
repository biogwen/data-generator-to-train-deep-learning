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
names = []
for prenoms in prenom:
    n = randint(1, 50)

    # ajout d'un nombre aléatoire de produit par personne
    for i in range(n):
        p = randint(0, 49)
        names.append(prenoms)
        stuff.append(produits[p])


data = {"noms": names, "objets": stuff}

data_frame = pd.DataFrame.from_dict(data)
#export en excel
data_frame.to_csv("sortie.csv", columns=("noms", "objets"), index=False)

