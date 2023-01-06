def Liste():
    liste=[" SALUT ","Bonjour","aurevoir","goodby"]
    print(liste)
    idx1 = liste.index(" SALUT ")
    idx2 = liste.index("goodby")
    print(idx1)
    print(idx2)
    liste[idx1],liste[idx2] = liste [idx2],liste[idx1]
    print(liste)
Liste()
