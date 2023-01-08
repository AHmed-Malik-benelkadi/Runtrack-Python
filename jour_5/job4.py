def decale_message(message, decalage):
    message_decale = "" # vide
    i = 0
    while i < len(message):
        lettre = message[i]
        # On récupère son code ASCII
        code = ord(lettre)
        if code >= 65 and code <= 90:
            code += decalage
            if code > 90:
                code -= 26
            elif code < 65:
                code += 26
        elif code >= 97 and code <= 122:
            code += decalage
            # Si elle dépasse 'z' on revient au début de l'alphabet
            if code > 122:
                code -= 26
            # Si elle dépasse 'a  on avance jusqu'à 'z'
            elif code < 97:
                code += 26
        else:
            pass
        message_decale += chr(code)
        i += 1
    return message_decale
message = input("Entrez votre message : ")
decalage = int(input("Entrez le décalage souhaité : "))
message_decale = decale_message(message, decalage)
print("Voici votre message décalé :", message_decale)
