import pandas as pd

# Lecture données
client = pd.read_csv("donnees/table_client.csv")
commande_reprise = pd.read_csv("donnees/table_commande_reprise.csv")
financement = pd.read_csv("donnees/table_financement.csv")
navigation_web = pd.read_csv("donnees/table_navigation_web.csv")
nearest_agency = pd.read_csv("donnees/table_nearest_agency.csv")
vehicule = pd.read_csv("donnees/table_vehicule.csv")

# Jointure et ajout de l'âge au moment de la transaction
jointure = commande_reprise.merge(client, how="left", left_on="LEAD_ID", right_on="ID_LEAD")
jointure["DATE_PANIER"] = pd.to_datetime(jointure["DATE_PANIER"], format="%Y-%m-%d %H:%M:%S.%f")
jointure["YEAR_NAISSANCE"] = pd.to_datetime(jointure["YEAR_NAISSANCE"], format="%Y")
jointure["AGE_TRANSAC"] = (jointure["DATE_PANIER"] - jointure["YEAR_NAISSANCE"]).dt.days / 365.25
mean(jointure["AGE_TRANSAC"])

# Pourcentage genre
Pourc_H = sum(client["GENDER"] == "H")/len(client["GENDER"]) * 100
print(f"Il y a {Pourc_H:.2f}% d'hommes et {(100-Pourc_H):.2f}% de femmes ici")

# 