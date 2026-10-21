# 22210908 Thomas De Laubier

# Section 1 les imports
import requests
import sys

API_URL_AMIS = "https://my-json-server.typicode.com/rtavenar/fake_api/adresses_amis"
API_URL_HOTELS = "https://tabular-api.data.gouv.fr/api/resources/3ce290bf-07ec-4d63-b12b-d0496193a535/data/"

def recuperer_villes_amis(url_amis):
    """
    Récupère la liste des adresses des amis depuis l'API 
    et retourne un ensemble (set) de villes uniques.
    """
    try:
        response = requests.get(url_amis)
        # Lève une exception si la requête a échoué (ex: 404, 500)
        response.raise_for_status() 
        
        adresses_amis = response.json()
        villes = set()
        
        for ami in adresses_amis:
            try:
                # Sépare l'adresse en parties (ex: "2 Rue de la Liberté, 35000 Rennes")
                adresse_complete = ami.get('adresse', '')
                # Prend la partie après la virgule (ex: " 35000 Rennes")
                partie_ville = adresse_complete.split(',')[-1].strip()
                # Sépare le code postal et la ville, en ne coupant qu'au premier espace
                # (ex: ["35000", "Rennes"])
                ville = partie_ville.split(' ', 1)[1]
                villes.add(ville)
            except IndexError:
                print(f"Attention: Impossible d'analyser l'adresse suivante : {adresse_complete}", file=sys.stderr)
            except AttributeError:
                 print(f"Attention: Donnée d'ami mal formée : {ami}", file=sys.stderr)

        return villes
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des adresses des amis : {e}", file=sys.stderr)
        return None
    except requests.exceptions.JSONDecodeError:
        print("Erreur: Impossible de décoder la réponse JSON des amis.", file=sys.stderr)
        return None

def recuperer_hotels(url_hotels):
    """
    Récupère la liste complète des hôtels depuis l'API data.gouv.fr.
    Retourne la liste des hôtels (contenue dans la clé 'data' du JSON).
    """
    try:
        response = requests.get(url_hotels)
        response.raise_for_status()
        
        # Les données des hôtels sont nichées sous la clé 'data'
        return response.json().get('data', [])
        
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors de la récupération des hôtels : {e}", file=sys.stderr)
        return None
    except requests.exceptions.JSONDecodeError:
        print("Erreur: Impossible de décoder la réponse JSON des hôtels.", file=sys.stderr)
        return None

def main():
    """
    Fonction principale du programme.
    """
    print("Récupération des villes des amis...")
    villes = recuperer_villes_amis(API_URL_AMIS)
    
    if not villes:
        print("Impossible de récupérer les villes des amis. Arrêt du programme.")
        return

    print("Récupération de la liste des hôtels...")
    tous_les_hotels = recuperer_hotels(API_URL_HOTELS)
    
    if tous_les_hotels is None:
        print("Impossible de récupérer la liste des hôtels. Arrêt du programme.")
        return

    print("\n--- Recherche des hôtels par ville ---\n")

    # Pour chaque ville où habite un ami...
    for ville in villes:
        print(f"==========================================")
        print(f"🏨 Hôtels disponibles à {ville}")
        print(f"==========================================")
        
        hotels_trouves = []
        
        # ... on parcourt la liste complète des hôtels
        for hotel in tous_les_hotels:
            # On compare la ville de l'hôtel (champ 'commune') avec la ville de l'ami
            if hotel.get('commune') and hotel.get('commune').lower() == ville.lower():
                hotels_trouves.append(hotel)
        
        if hotels_trouves:
            # Affichage des hôtels trouvés, comme demandé 
            for hotel in hotels_trouves:
                nom = hotel.get('nom_commercial', 'Nom non disponible')
                adresse = hotel.get('adresse', 'Adresse non disponible')
                etoiles = hotel.get('classement', 'Classement non disponible')
                
                print(f"  • {nom}")
                print(f"    Adresse : {adresse}")
                print(f"    Étoiles : {etoiles}\n")
        else:
            print(f"  -> Aucun hôtel trouvé dans la base de données pour {ville}.\n")

# Point d'entrée du script
if __name__ == "__main__":
    main()