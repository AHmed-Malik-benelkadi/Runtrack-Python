def compt(L):

    compteur = 0


    for nombre in L:

        if nombre % 3 == 0:
            compteur += 1

    return compteur

# On teste la fonction
L = [8, 24, 48, 2, 16]
resultat = compt(L)
print(resultat)
