def affiche_chiffres():
    i = 0
    while i <= 100:
        if i in [26, 37, 88]:
            i += 1
            continue
        print(i)
        i += 1

affiche_chiffres()
