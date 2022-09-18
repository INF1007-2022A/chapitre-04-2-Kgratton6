mot = 'allo '
shift = 1
for i in range(len(mot)):
    if ( ord(mot[i]) + shift ) < 123:
        mot = (chr(ord(mot[i]) + shift)) + mot[i+1:]
