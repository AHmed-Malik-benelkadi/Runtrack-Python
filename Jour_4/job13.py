lst = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

uniq_lst = []

i = 0

length = 0
for c in lst:  # create boucle permet de remplacer la function len
    length += 1

while i < length:
    if lst[i] not in uniq_lst:
        temp_lst = [lst[i]]
        uniq_lst = uniq_lst + temp_lst
    # On passe à l'élément suivant
    i += 1

print(uniq_lst)
