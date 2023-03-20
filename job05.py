def distance_toilettes(marches, hauteur):
    distance_totale = marches * hauteur * 2 
    # Distance totale en cm (aller-retour)
    distance_totale_m = distance_totale / 100 
    # Distance totale en mètres
    distance_semaine_m = distance_totale_m * 5 * 7 
    # Distance parcourue en une semaine
    distance_semaine_m_arrondie = round(distance_semaine_m, 2) 
    print(f"Pour {marches} marches de {hauteur} cm, le gardien parcours {distance_semaine_m_arrondie} m par semaine.")
distance_toilettes(50, 20)



