def triangle(a, b, c):
  # Vérifiez si les longueurs sont positives
  if a <= 0 or b <= 0 or c <= 0:
    return "Les longueurs doivent être positives"

  if a >= b + c or b >= a + c or c >= a + b:
    return "Les longueurs ne satisfont pas les conditions pour construire un triangle"

  if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:

    if a == b or b == c or a == c:

      if a == b == c:
        return "Triangle équilatéral rectangle"
      else:
        return "Triangle rectangle isocèle"
    else:
      return "Triangle rectangle"

  # Vérifie si le triangle est isocèle
  if a == b or b == c or a == c:
    if a == b == c:
      return "Triangle équilatéral"
    else:
      return "Triangle isocèle"

  # Si aucune des conditions précédentes n'est remplie, alors le triangle est quelconque
  return "Triangle quelconque"
print(triangle(3, 4, 5)) # cela affichera "Triangle rectangle"
print(triangle(-3,-4, -5)) # cela affichera "Les longueurs doivent être positives
print(triangle(3,4, 50)) # cela affichera Les longueurs ne satisfont pas les conditions pour construire un triangle
print(triangle(5, 5, 7)) # cela affichera "Triangle isocèle"
print(triangle(6, 6, 6)) # cela affichera "Triangle équilatéral"
print(triangle(2, 3, 4)) # cela affichera "Triangle quelconque"
