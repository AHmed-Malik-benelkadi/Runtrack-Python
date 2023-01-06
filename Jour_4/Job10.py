L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

produit = 1
index = 0
while index < len(L):

    element = L[index]


    if 25 <= element <= 90:

        produit *= element


    index += 1

print(produit)
