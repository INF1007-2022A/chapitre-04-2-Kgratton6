mot = 'hellolalwlr'
ancien = 'l'
nouveau = 'w'
final = ''

for i in mot:
    if i == ancien:
        final += nouveau
    else:
        final += i

print(final)
