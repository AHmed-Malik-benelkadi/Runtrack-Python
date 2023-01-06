def list(L):
    i = 1
    length = 0
    for c in L:                             # cette boucle permet de remplacer la function len
        length += 1
    print(length)  # verifier si c'est bien comme len

    while i < length:  # length = .len
        element = L[i]
        j = i - 1
        # déplace les éléments qui sont plus grands que l'élément à insérer
        while j >= 0 and L[j] > element:
            L[j + 1] = L[j]
            j -= 1
        L[j + 1] = element
        i += 1

    return L


L = [753, 1122, 42, 39, 2]
print(list(L))

L = ['banane', 'pomme', 'orange', 'fraise']
print(list(L))
