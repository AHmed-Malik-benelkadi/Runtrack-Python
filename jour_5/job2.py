def rectangle(width, height):
    print("|" + "-" * width + "|")

    i = 1
    while i < (height -1):
        print("|" + " " * width + "|")
        i += 1

    print("|" + "-" * width + "|")
width = int(input("Entrez la largeur du rectangle : "))
height = int(input("Entrez la hauteur du rectangle : "))
# Si les dimensions sont valides on appelle la fonction
if width > 0 and height > 0:
    rectangle(width, height)
else:
    print("Les dimensions doivent être positives.")



