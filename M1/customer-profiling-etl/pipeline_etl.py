import pandas as pd

# =============================================================================
# 1 - Import all tables
# =============================================================================
df_client = pd.read_csv("data/table_client.csv")
df_commande_reprise = pd.read_csv("data/table_commande_reprise.csv")
df_vehicule = pd.read_csv("data/table_vehicule.csv")
df_financement = pd.read_csv("data/table_financement.csv")
df_nearest_agency = pd.read_csv("data/table_nearest_agency.csv")

# =============================================================================
# 2 - Deduplicate client on ID_LEAD
# =============================================================================
df_client = df_client.drop_duplicates(subset="ID_LEAD")

# =============================================================================
# 3 - Merge commande_reprise + client
# =============================================================================
df = pd.merge(df_commande_reprise, df_client, left_on="LEAD_ID", right_on="ID_LEAD", how="left")

# =============================================================================
# 4 - Calculate age = year of DATE_PANIER - YEAR_NAISSANCE
# =============================================================================
df["DATE_PANIER"] = pd.to_datetime(df["DATE_PANIER"])
df["AGE"] = df["DATE_PANIER"].dt.year - df["YEAR_NAISSANCE"]

# =============================================================================
# 5 - Split into table_reprise and table_commande
# =============================================================================
df_reprise = df[df["TYPE_PANIER"] == "Reprise"]
df_commande = df[df["TYPE_PANIER"] == "Commande"]

# =============================================================================
# 6 - Merge table_commande + vehicule (on VEHICULE_ID)
# =============================================================================
df_commande_vehicule = pd.merge(df_commande, df_vehicule
        , on="VEHICULE_ID", how="left")

# =============================================================================
# 7 - Merge + financement (on LEAD_ID and VEHICULE_ID)
# =============================================================================
df_commande_vehicule_financement = pd.merge(df_commande_vehicule, df_financement
        , on=["LEAD_ID", "VEHICULE_ID"], how="left")

# =============================================================================
# 8 - Merge + nearest_agency (on CODE_POSTAL = ZIP_CODE)
# =============================================================================
df_master = pd.merge(df_commande_vehicule_financement, df_nearest_agency
        , left_on="CODE_POSTAL", right_on="ZIP_CODE", how="left")

# =============================================================================
# Check final result
# =============================================================================
# print("table_commande_reprise :", df_commande_reprise.shape)
# print("table_commande + client:", df.shape)
# print("table_reprise          :", df_reprise.shape)
# print("table_commande         :", df_commande.shape)
# print("+ vehicule             :", df_commande_vehicule.shape)
# print("+ financement          :", df_commande_vehicule_financement.shape)
print("MASTER TABLE           :", df_master.shape)

df_master.columns

# list columns last table : 
    #'TYPE_PANIER', 'DATE_PANIER', 'LEAD_ID','VEHICULE_ID'
    #       , 'AGENCE_LIVRAISON_COM', 'PRIX_VENTE_TTC_COM', 'TYPE_LIVRAISON_COM'

    # 'ID_LEAD', 'DATE_CREATION', 'CODE_POSTAL', 'VILLE','YEAR_NAISSANCE', 'GENDER', 'AGE'

    # 'VEHICULE_TYPE', 'VEHICULE_MODELE', 'VEHICULE_MARQUE', 'VEHICULE_ENERGIE', 'VEHICULE_CATEGORIE', 'VEHICULE_BOITE_VITESSE'
    #   , 'VEHICULE_COULEUR', 'VEHICULE_KM','VEHICULE_MEC', 'OFFER_EQUIPMENTS_STANDARD_LABELS_LIST',
    #   ,  'OFFER_EQUIPMENTS_MAIN_LIST', 'OFFER_OFFER_TAGS_LIST', 
    # 
    # 'FI_TYPE', 

    # 'NEAREST_AGENCY_DISTANCE', 'NEAREST_AGENCY_DUREE','NEAREST_AGENCY_LABEL', 'ZIP_CODE'

