L: list[int] = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
sum = 0
i = 0

while i < len(L):

    if L[i] % 2 == 0:
        sum += L[i]
    i += 1

print(f'la valeur de la somme des chiffre pair est de : {sum}')
