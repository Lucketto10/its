def vowelRemover(string):
    if not string:
        return ""
    else:
        if string[0].lower() in 'aeiou':
            return vowelRemover(string[1:])
        else:
            return string[0] + vowelRemover(string[1:])

stringa = "Ciao Mondo"
risultato = vowelRemover(stringa)
print(f"La stringa senza vocali è: '{risultato}'")
