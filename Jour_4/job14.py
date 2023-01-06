def monmot(n, string):
    mots = []
    i = 0
    le_mot = ""

    length = 0
    for j in string:  # cette boucle permet de remplacer la function len
        length += 1

    while i < length:
        if string[i] != " ":
            le_mot += string[i]
        else:
            if len(le_mot) > n:
                mots += [le_mot]
            current_word = ""
        i += 1

    if len(le_mot) > n:
        mots += [le_mot]
    return mots


long_words = monmot(3, "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène "
                       "à la haine la haine mène à la souffrance")

print(long_words)
