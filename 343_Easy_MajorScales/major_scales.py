notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
solfeges = {"Do": 0, "Re": 2, "Mi": 4, "Fa": 5, "So": 7, "La": 9, "Ti": 11}

def note(scale, solfege):
    number_of_solfege = solfeges[solfege]
    number_of_scale = notes.index(scale)
    print(notes[(number_of_scale+number_of_solfege)%12])
