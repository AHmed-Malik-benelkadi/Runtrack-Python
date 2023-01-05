chaine = "abcdefghijklmnopqrstuvwxyz" * 10
longueur_de_chaine = len(chaine)

ligne = 1

i = 0

while i + ligne <= longueur_de_chaine:
  print(chaine[i:i+ligne])
  i += ligne
  ligne += 1