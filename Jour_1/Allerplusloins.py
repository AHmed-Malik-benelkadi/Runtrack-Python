# Initialisation de la variable qui indique si le programme doit continuer à s'exécuter
running = True

while running:
# Début de la boucle infinie qui s'exécutera tant que "running" est vrai
    phrase = input("Veillez rentrer une phrase pour verifier si la lettre 'e' est presente : ")
    # Je demande a l'utilisateur d'inserer une phrase
    print("vous avez ecrit", phrase)

    if "e" in phrase or "E" in phrase:)))
        print("la lettre 'E' est bien presente dans la  phrase")
    else:
        print("la lettre 'E' n'est pas presente dans la phrase ")

    if phrase == "stop":  # condition pour dire  si l'utilisateur Ecrit "stop" le programme s'arrette
            running = False
            print("Votre programme s'arrette")
    continue


