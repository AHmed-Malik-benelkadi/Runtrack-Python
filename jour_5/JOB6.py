def arrondir_notes(notes):
  arrondies = []
  i = 0
  while True:
    if i >= len(notes):
      break
    note = notes[i]
    if note < 40:
      arrondies += [note]
    elif note % 5 >= 3:
      arrondies += [note + (5 - note % 5)]
    else:
      arrondies += [note]
    i += 1
  return arrondies


notes = [78, 82,83, 45, 33, 67, 95, 53,10,6,3]
arrondies = arrondir_notes(notes)
print(arrondies)
