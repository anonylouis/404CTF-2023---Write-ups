import osmapi

# Initialiser le client de l'API OpenStreetMap
osm = osmapi.OsmApi()

# Trouver l'ID de la station de métro Anvers en utilisant son code d'arrêt RATP
nodes = osm.NodesGet({"ref:FR:RATP": "14107"})
if len(nodes) == 0:
    print("La station de métro Anvers n'a pas été trouvée.")
else:
    anvers_id = nodes[0]["id"]

    # Trouver l'ID du cinéma Les 7 Batignolles
    nodes = osm.NodesGet({"name": "Les 7 Batignolles", "amenity": "cinema"})
    if len(nodes) == 0:
        print("Le cinéma Les 7 Batignolles n'a pas été trouvé.")
    else:
        batignolles_id = nodes[0]["id"]

        # Récupérer le temps de trajet en transport en commun entre les deux adresses
        response = osm.TransportRoute(anvers_id, batignolles_id, "bus")
        if "route_summary" in response:
            transit_time = response["route_summary"]["total_time"]
            print("Le temps de trajet en transports en commun entre Anvers et Les 7 Batignolles est de", transit_time, "secondes.")
        else:
            print("Aucun résultat trouvé.")