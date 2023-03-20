def arrondir_notes(notes):
    arrondies = []
    for note in notes:
        if note < 40:
            arrondies.append(note)
        else:
            if note % 5 >= 3:
                arrondies.append(note + 5 - (note % 5))
            else:
                arrondies.append(note)
    return arrondies
arrondir_notes(80)