def affiche_nombres_premiers():
    i = 2
    while i <= 1000:
        premier = True
        j = 2
        while j < i:
            if i % j == 0:
                premier = False
                break
            j += 1
        if premier:
            print(i)
        i += 1

affiche_nombres_premiers()
