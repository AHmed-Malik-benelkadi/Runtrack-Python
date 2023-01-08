def distance(nombre_marches, hauteur_marche):
  distance_totale = nombre_marches * hauteur_marche # distance parcourue en descendant aux toilettes
  distance_totale += nombre_marches * hauteur_marche # distance parcourue en remontant des toilette
  distance_totale *= 5 # distance parcourue chaque jour
  distance_totale *= 7 # distance parcourue chaque semaine
  distance_totale /= 100
  return distance_totale

distance_final = distance(10, 20) # 10 marches pour 20 cm de hauteur
print(f"Pour 10 marches de 20 cm, le gardien parcours {distance_final:.2f} m par semaine.") #le :.2f represente le nombre de poinnts apres la virgule
