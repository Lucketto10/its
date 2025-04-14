def charDuplicator(string):
    if not string:
        return ""
    else:
        return string[0] * 2 + charDuplicator(string[1:])

stringa = "libro"
risultato = charDuplicator(stringa)
print(f"La stringa con i caratteri duplicati è: '{risultato}'")
