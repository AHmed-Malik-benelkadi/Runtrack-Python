L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
# je met le max et le min en index 0
max = L[0]
min = L[0]

index = 0

while index < len(L):
    x = L[index]
    if x > max:  # si x est plus grande que
        max = x
    if x < min:
        min = x
    index += 1

print("L a valeur  maximum de cette liste  est de : ", max)
print("La valeur minume de cette liste  minimum est de :", min)
